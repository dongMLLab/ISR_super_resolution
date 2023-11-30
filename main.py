from ISR.models import RDN
import numpy as np
from PIL import Image
import os

image_dir = os.listdir("./img")

for i in image_dir:
# /00037-3574770352.jpg
    if i[:-2] == "md":
        print("Pass Not Image file: {}".format(i[:-2]))
        pass
    img = Image.open('./img/'+i)

    lr_img = np.array(img)

    # psnr-large, psnr-small, noise-cancel

    weights = "psnr-large"
    rdn = RDN(weights=weights)

    sr_img = rdn.predict(lr_img)
    image = Image.fromarray(sr_img)

    image.save("results/isr/" + weights +"_" + i)
    print("Resolution Finished: {}".format(i))