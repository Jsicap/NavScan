import cv2
import numpy
from mss.windows import MSS as mss

qcd = cv2.QRCodeDetector()
monitor = {'top': 100, 'left': 100, 'width': 1500, 'height': 700}

with mss() as sct:
    while True:
        im = numpy.array(sct.grab(monitor))
        im = numpy.flip(im[:, :, :3], 2)  # 1
        im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)  # 2

        retval, decoded_info, points, straight_qrcode = qcd.detectAndDecodeMulti(im)
        if (retval == True and decoded_info[0] != ''):
            print("Found QR Code!")
            print(decoded_info)
            
            cv2.polylines(im, [points.astype(int)], True, (0, 255, 0), 3)
            break

print(int(points[0][2][0]-points[0][1][0]))

x_coord = (int((points[0][2][0]-points[0][0][0])/2) + int(points[0][0][0])) - 50

cv2.putText(im, decoded_info[0], (x_coord, int(points[0][0][1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA, False)
cv2.imshow("Screenshot", im)
cv2.waitKey(0) 
cv2.destroyAllWindows()
  
# # initialize the camera 
# # If you have multiple camera connected with  
# # current device, assign a value in cam_port  
# # variable according to that 
# cam_port = 0
# cam = cv2.VideoCapture(cam_port) 
  
# # reading the input using the camera 
# result, image = cam.read() 
  
# # If image will detected without any error,  
# # show result 
# if result: 
  
#     # showing result, it take frame name and image  
#     # output 
#     cv2.imshow("GeeksForGeeks", image) 
  
#     # saving image in local storage 
#     cv2.imwrite("GeeksForGeeks.png", image) 
  
#     # If keyboard interrupt occurs, destroy image  
#     # window 
#     cv2.waitKey(0) 
#     cv2.destroyWindow("GeeksForGeeks") 
  
# # If captured image is corrupted, moving to else part 
# else: 
#     print("No image detected. Please! try again") 