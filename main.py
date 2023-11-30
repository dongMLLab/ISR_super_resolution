import warnings
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request
from minio import S3Error

warnings.filterwarnings(action='ignore')

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.router.post("/resolution")
def super_resolution(request):
    try:
        print()
    except Exception as e:
        print(e)