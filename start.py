import os

from gan import generate_gans
from psnr import generate_psnr
import cv2

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
            print(i[-2:])
        # /00037-3574770352.jpg
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
            print(v[-2:])

            # /00037-3574770352.jpg
            if v[-2:] == "md":
                print("Pass Not Image file: {}".format(i[-2:]))
                pass

            if v[-2:]:
                if weights == "gans":
                    generate_gans(weights, i)
                
                else:
                    generate_psnr(weights, i)
            
            else:
                print("Pass")
start()