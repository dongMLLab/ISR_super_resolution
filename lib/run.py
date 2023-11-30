import os

from gan import generate_gans
from psnr import generate_psnr

def run_main(weights: str, fileName: str, client):
    usable_weights = ['psnr-large', 'psnr-small', 'noise-cancel', 'gans']

    if weights not in usable_weights:
        print("Please select usable weights.: {}".format(*usable_weights))

        return False

    if weights == "gans":
        generate_gans(weights, fileName, client)
    
    else:
        generate_psnr(weights, fileName, client)
    
