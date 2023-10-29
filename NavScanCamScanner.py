import cv2
import numpy
from mss.windows import MSS as mss

# Initialize a QR code detector
qcd = cv2.QRCodeDetector()

# Define the screen capture region
monitor = {'top': 100, 'left': 100, 'width': 1500, 'height': 700}

# Initialize a screen capture object
with mss() as sct:
    while True:
        # Capture the screen region defined in 'monitor'
        im = numpy.array(sct.grab(monitor))
        
        # Flip the image horizontally (1)
        im = numpy.flip(im[:, :, :3], 2)
        
        # Convert the image from BGR to RGB color space (2)
        im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

        # Try to detect QR codes in the captured image
        retval, decoded_info, points, straight_qrcode = qcd.detectAndDecodeMulti(im)

        # If a QR code is detected and decoded successfully
        if (retval == True and decoded_info[0] != ''):
            print("Found QR Code!")
            print(decoded_info)
            
            # Draw a green border around the detected QR code
            cv2.polylines(im, [points.astype(int)], True, (0, 255, 0), 3)
            break

# Calculate the width of the detected QR code
print(int(points[0][2][0] - points[0][1][0]))

# Calculate the x-coordinate for placing text
x_coord = (int((points[0][2][0] - points[0][0][0]) / 2) + int(points[0][0][0])) - 50

# Add the decoded QR code information as text on the image
cv2.putText(im, decoded_info[0], (x_coord, int(points[0][0][1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA, False)

# Display the image with the detected QR code and text
cv2.imshow("Screenshot", im)
cv2.waitKey(0) 
cv2.destroyAllWindows()
