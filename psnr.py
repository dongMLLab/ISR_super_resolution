from ISR.models import RDN
import numpy as np
from PIL import Image
import os

<<<<<<< HEAD
def generate_psnr(weights: str, fileName: str):
    img = Image.open('./img/'+fileName)
=======
def generate_psnr(weights: str, fileName: str, versionId: str, client):
    try :
        print("Start Generating PSNR Method: {}".format(weights))
>>>>>>> 39b4f0fb7038c2a070615acf696ec5251082fa31

        data = client.get_image_file("raw", fileName, versionId)

        img = Image.open(data)

        lr_img = np.array(img)

        # psnr-large, psnr-small, noise-cancel

        # weights = "psnr-large"
        rdn = RDN(weights=weights)

<<<<<<< HEAD
    # new_version_id = client.upload_visualize_file(
    #     "resolution", 
    #     weights +"_" + fileName,
    #     "results/isr/" + weights +"_" + fileName
    # )
    

    return weights +"_" + fileName
=======
        sr_img = rdn.predict(lr_img)
        image = Image.fromarray(sr_img)

        image.save("/app/results/isr/" + weights +"_" + fileName)

        new_version_id = client.upload_visualize_file(
            "resolution", 
            weights +"_" + fileName,
            "/app/results/isr/" + weights +"_" + fileName
        )
        
        print("Resolution Finished: {}".format(new_version_id))

        return weights +"_" + fileName, new_version_id
    except Exception as e:
        print(e)

        return e
>>>>>>> 39b4f0fb7038c2a070615acf696ec5251082fa31
