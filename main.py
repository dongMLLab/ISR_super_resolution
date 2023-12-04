import warnings
from client import MinioClient
from dto.upload import UploadRequestDto
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import os
from lib.run import run_main
from dotenv import load_dotenv

warnings.filterwarnings(action='ignore')

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv( verbose=True)

minio_endpoint = os.getenv("MINIO_ENDPOINT")
minio_access = os.getenv("MINIO_ACCESSKEY")
minio_secret = os.getenv("MINIO_SECRET")

print("Endpoint: {}".format(minio_endpoint))

client = MinioClient(
    endpoint=minio_endpoint,
    access_key=minio_access,
    secret_key=minio_secret,
)

@app.router.post("/resolution")
def super_resolution(request: UploadRequestDto):
    try:
        weights, fileName, versionId = request

        print("weights: {}, fileName: {}, version_id: {}".format(weights, fileName, versionId))

        client.get_image_file("raw", request.fileName, request.versionId)

        new_fileName, new_version_id = run_main(request.weights, request.fileName, client)

        print("Result File Name: {}".format(new_version_id))

        return {
            "newFileName": new_fileName,
            "newVersionId": new_version_id
        }
    
    except Exception as e:
        return e