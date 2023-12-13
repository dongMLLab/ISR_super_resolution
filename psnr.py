from ISR.models import RDN
import numpy as np
from PIL import Image
from pqdm.processes import pqdm


def generate_psnr(weights: str, fileName: str, versionId: str, client):
    try :
        print("Start Generating PSNR Method: {}".format(weights))
        data = client.get_image_file("raw", fileName, versionId)

        img = Image.open(data)

        lr_img = np.array(img)

        # psnr-large, psnr-small, noise-cancel

        # weights = "psnr-large"
        rdn = RDN(weights=weights)



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
    
def generate_video_psnr(fileName: str, weights: str):
    try:
        import cv2
        rdn = RDN(weights=weights)  
        print(fileName)
        cap = cv2.VideoCapture(fileName)

        fps = int(cap.get(cv2.CAP_PROP_FPS))
        fourcc = int(cap.get(cv2.CAP_PROP_FOURCC))
        w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        writer = cv2.VideoWriter("video_results/"+weights+"_"+fileName+"_sred.mp4", fourcc=fourcc, fps=fps, frameSize=(w, h))
     

        while cap.isOpened():
            with pqdm(total=100) as bar:
                success, frame = cap.read()
    
                print("Start Generating Gans Method")
                
                if not success:
                    print("Capture not opened")

                lr_frame = np.array(frame)

                sr_img = rdn.predict(lr_frame)
                # resized = cv2.resize(sr_img, frame_size)
                # image = Image.fromarray(sr_img)
                
                # image.save("/app/results/gan/"+"gans_"+fileName)

                print("Resolution Finished: {}".format(fileName))
                bar.update(fps*5)

                writer.write(sr_img.astype(np.uint8))
                cv2.imshow('Frame', sr_img.astype(np.uint8))
            
                # Press Q on keyboard to  exit
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break

        cap.release()

        return weights+"_"+fileName
    except Exception as e:
        print(e)

        return e

generate_video_psnr("video/video.mp4", "psnr-large")