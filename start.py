import os

from gan import generate_gans
from psnr import generate_psnr


def start():
    usable_weights = ['psnr-large', 'psnr-small', 'noise-cancel', 'gans']

    weights = input("Please select weights: 'psnr-large', 'psnr-small', 'noise-cancel', 'gans': ")

    if weights not in usable_weights:
        print("Please select usable weights.: {}".format(*usable_weights))
        return False
    
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

start()