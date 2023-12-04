from ISR.models import RRDN
import numpy as np
from PIL import Image
import os

def generate_gans(weights: str, fileName: str, client):
    try :
        print("Start Generating Gans Method")
    # /00037-3574770352.jpg
        img = Image.open('/app/img/'+fileName)

        lr_img = np.array(img)

        rrdn = RRDN(weights=weights)

        sr_img = rrdn.predict(lr_img)
        image = Image.fromarray(sr_img)

        image.save("/app/results/gan/"+"gans_"+fileName)

        print("Resolution Finished: {}".format(fileName))
        
        new_version_id = client.upload_visualize_file(
            "resolution",
            "gans_"+fileName,
            "/app/results/gan/"+"gans_"+fileName,
        )

        return "gans_"+fileName, new_version_id
    except Exception as e:
        print(e)

        return e