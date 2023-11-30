from ISR.models import RRDN
import numpy as np
from PIL import Image
import os

image_dir = os.listdir("./img")

for i in image_dir:
    if i[:-2] == "md":
        print("Pass Not Image file: {}".format(i[:-2]))
        pass
# /00037-3574770352.jpg
    img = Image.open('./img/'+i)

    lr_img = np.array(img)

    rrdn = RRDN(weights='gans')

    sr_img = rrdn.predict(lr_img)
    image = Image.fromarray(sr_img)

    image.save("results/gan/"+"gans_"+i)
    print("Resolution Finished: {}".format(i))