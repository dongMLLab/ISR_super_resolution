import os

from gan import generate_gans
from psnr import generate_psnr

def run_main(weights: str, fileName: str, versionId: str, client):
    try:
        print("Run Main")
        usable_weights = ['psnr-large', 'psnr-small', 'noise-cancel', 'gans']

        if weights not in usable_weights:
            print("Please select usable weights.: {}".format(*usable_weights))

            return fileName, "No Weight Usable"

        if weights == "gans":
            new_fileName, new_version_id= generate_gans(weights, fileName, versionId,client)

            return new_fileName, new_version_id
        
        else:
            new_fileName, new_version_id = generate_psnr(weights, fileName, client)

            return new_fileName, new_version_id
    except Exception as e:
            print(e)

            return e
