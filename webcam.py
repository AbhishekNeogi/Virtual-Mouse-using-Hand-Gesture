# from cgi import print_form
import cv2
cam = cv2.VideoCapture(0)
img_count = 0
if not cam.isOpened:
    print("camera not opening")
else:
    print("camera opening")

while True:
    ret,frame = cam.read()

    # if not ret:
    #     print("Filed to grab frame")
    #     break
    mirror_frame = cv2.flip(frame,1)
    cv2.imshow('Webcam Feed',mirror_frame)

    k = cv2.waitKey(1)
    if k %256 == 113:
        print("esc hit, app closed ")
        break
    elif k %256 == 32:
        img_name = "opencv_frame_{}.png".format(img_count)
        cv2.imwrite(img_name,frame)
        print("screenshot")
        img_count+=1
    

cam.release()
cv2.destroyAllWindows()