import warnings
from client import MinioClient
from dto.upload import UploadRequestDto
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request
from minio import S3Error
import os
from lib.run import run_main

warnings.filterwarnings(action='ignore')

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

minio_endpoint = os.getenv("MINIO_ENDPOINT")
minio_access = os.getenv("MINIO_ACCESSKEY")
minio_secret = os.getenv("MINIO_SECRET")

client = MinioClient(
    minio_endpoint,
    minio_access,
    minio_secret
)

@app.router.post("/resolution")
def super_resolution(request: UploadRequestDto):
    try:
        weights, fileName, versionId = request

        print("Request: {}".format(request.fileName))

        client.get_image_file("raw", fileName, versionId)

        new_fileName, new_version_id = run_main(weights, fileName, client)

        print("Result File Name: {}".format(new_version_id))

        return {
            "newFileName": new_fileName,
            "newVersionId": new_version_id
        }
    
    except Exception as e:
        print(e)