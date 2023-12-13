from ISR.models import RDN
import numpy as np
from PIL import Image
import os

def generate_psnr(weights: str, fileName: str):
    img = Image.open('./img/'+fileName)

    lr_img = np.array(img)

    # psnr-large, psnr-small, noise-cancel

    # weights = "psnr-large"
    rdn = RDN(weights=weights)

    sr_img = rdn.predict(lr_img)
    image = Image.fromarray(sr_img)

    image.save("results/isr/" + weights +"_" + fileName)

    # new_version_id = client.upload_visualize_file(
    #     "resolution", 
    #     weights +"_" + fileName,
    #     "results/isr/" + weights +"_" + fileName
    # )
    

    return weights +"_" + fileName