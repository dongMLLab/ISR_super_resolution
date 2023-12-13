from ISR.models import RRDN
import numpy as np
from PIL import Image
import cv2

def generate_gans(weights: str, fileName: str, versionId: str, client):
    try :
        print("Start Generating Gans Method")

        data = client.get_image_file("raw", fileName, versionId)

    # /00037-3574770352.jpg
        img = Image.open(data)

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

def generate_video_gans(fileName: str, weights: str):
    try :
        rrdn = RRDN(weights=weights)
        print(fileName)
        cap = cv2.VideoCapture(fileName)

        fps = int(cap.get(cv2.CAP_PROP_FPS))
        fourcc = cv2.VideoWriter_fourcc(*'MP4V')
        # w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        # h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        writer = cv2.VideoWriter("video_results/"+"gans_"+fileName+"_sred", fourcc=fourcc, fps=fps, frameSize=(1024, 1024))

        while cap.isOpened():
            success, frame = cap.read()
            print("Start Generating Gans Method")
            
            if not success:
                print("Capture not opened")

            lr_frame = np.array(frame)

            sr_img = rrdn.predict(lr_frame)
            # resized = cv2.resize(sr_img, frame_size)
            # image = Image.fromarray(sr_img)
            
            # image.save("/app/results/gan/"+"gans_"+fileName)
            
            writer.write(sr_img.astype(np.uint8))
            cv2.imshow('Frame', sr_img.astype(np.uint8))
        
            # Press Q on keyboard to  exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        print("Resolution Finished: {}".format(fileName))
        cap.release()

        return "gans_"+fileName
    except Exception as e:
        print(e)

        return e

generate_video_gans("video/video.mp4", "gans")

