import os
# from client import MinioClient

from gan import generate_gans, generate_video_gans
from psnr import generate_psnr, generate_video_psnr
import cv2

# minio_endpoint = os.environ.get("MINIO_ENDPOINT")
# minio_access = os.environ.get("MINIO_ACCESSKEY")
# minio_secret = os.environ.get("MINIO_SECRET")

# print("minio_scret: {}".format(minio_secret))
# print("Endpoint: {}".format(minio_endpoint))

# client = MinioClient(
#     minio_endpoint,
#     minio_access,
#     minio_secret
# )

def start():
    usable_weights = ['psnr-large', 'psnr-small', 'noise-cancel', 'gans']

    weights = input("Please select weights: 'psnr-large', 'psnr-small', 'noise-cancel', 'gans': ")
    mode = input("video / image: ")

    if weights not in usable_weights:
        print("Please select usable weights.: {}".format(*usable_weights))
        return False
    
    if mode == "image":
        image_dir = os.listdir("./img")

        for i in image_dir:
            print("Image Mode Selected. Proceed File: {}".format(i[-2:]))

            if i[-2:] == "md":
                print("Pass Not Image file: {}".format(i[-2:]))
                pass

            if i[-2:]:
                if weights == "gans":
                    generate_gans(weights, i)
                
                else:
                    generate_psnr(weights, i)
            
            else:
                print("Pass")

    if mode == "video":
        video_dir = os.listdir("./video")

        for v in video_dir:
            print("Video Mode Selected. Proceed File: {}".format(v[-2:]))

            if v[-2:] == "md":
                print("Pass Not Image file: {}".format(i[-2:]))
                pass

            if v[-2:]:
                if weights == "gans":
                    generate_video_gans(weights, i)
                
                else:
                    generate_video_psnr(weights, i)
            
            else:
                print("Pass")
start()