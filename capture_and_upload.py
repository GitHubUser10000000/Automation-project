import cv2
import dropbox
import time
import random
start_time=time.time()
def take_snapshot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time
        result=False
    print("snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()
    return img_name
def upload_file(image_name):
    access_token='sl.A_i7FLn8BJF_iTTo5k8WAYr4LnwFVo5mntiJykPoO-VzlmSgbhewBu33KkJYGDAr-jmgTwTRMiUX9bqsHOewRm0QOVodfApINj8V5gdGm4CIxVtqV5GWVdl_V6_QxwTr8-MqtD83rtSu'
    file=image_name
    file_from=file
    file_to="/testFolder/"+(image_name)
    dbx=dropbox.Dropbox(access_token)
    print("the file has been moved")
    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
    
def main():
    while(True):
        if((time.time() - start_time)>=5):
            name=take_snapshot()
            upload_file(name)
main()
            