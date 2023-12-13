from ISR.models import RRDN
import numpy as np
from PIL import Image

<<<<<<< HEAD
def generate_gans(weights: str, fileName: str):
=======
def generate_gans(weights: str, fileName: str, versionId: str, client):
    try :
        print("Start Generating Gans Method")
>>>>>>> 39b4f0fb7038c2a070615acf696ec5251082fa31

        data = client.get_image_file("raw", fileName, versionId)

    # /00037-3574770352.jpg
        img = Image.open(data)

        lr_img = np.array(img)

        rrdn = RRDN(weights=weights)

<<<<<<< HEAD
    image.save("results/gan/"+"gans_"+fileName)
    print("Resolution Finished: {}".format(fileName))
    
    # new_version_id = client.upload_visualize_file(
    #     "resolution",
    #     "gans_"+fileName,
    #     "results/gan/"+"gans_"+fileName,
    # )

    return "gans_"+fileName
=======
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

def generate_video_gans(fileName: str, weights: str):
    try :
        import cv2

        cap = cv2.VideoCapture(fileName)

        while cap.isOpened():
            fps = int(cap.get(cv2.CAP_PROP_FPS))
            fourcc = int(cap.get(cv2.CAP_PROP_FOURCC))
            w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

            writer = cv2.VideoWriter("video_results/"+fileName+"_sred", fourcc=fourcc, fps=fps, frameSize=(w, h))
            success, frame = cap.read()
            print("Start Generating Gans Method")
            
            if not success:
                print("Capture not opened")

            lr_frame = np.array(frame)

            rrdn = RRDN(weights=weights)

            sr_img = rrdn.predict(lr_frame)
            image = Image.fromarray(sr_img)
            
            # image.save("/app/results/gan/"+"gans_"+fileName)

            print("Resolution Finished: {}".format(fileName))
            
            writer.write(image)
            cv2.imshow('Frame', image)

            # Press Q on keyboard to  exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        cap.release()

        return "gans_"+fileName
    except Exception as e:
        print(e)

        return e

generate_video_gans("video/video.mp4", "gans")
>>>>>>> 39b4f0fb7038c2a070615acf696ec5251082fa31
