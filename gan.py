from ISR.models import RRDN
import numpy as np
from PIL import Image
import os

def generate_gans(weights: str, fileName: str):

# /00037-3574770352.jpg
    img = Image.open('./img/'+fileName)

    lr_img = np.array(img)

    rrdn = RRDN(weights=weights)

    sr_img = rrdn.predict(lr_img)
    image = Image.fromarray(sr_img)

    image.save("results/gan/"+"gans_"+fileName)
    print("Resolution Finished: {}".format(fileName))
    
    return fileName