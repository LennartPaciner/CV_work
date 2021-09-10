import cv2
import numpy as np
from pyzbar.pyzbar import decode

# img = cv2.imread('1.png')
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

with open('myDataFile.text') as f:
    myDataList = f.read().splitlines()

print(myDataList)


while True:

    success, img = cap.read()
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')   # Barcode ID -> need to save
        print(myData)

        if myData in myDataList:
            myOutput = 'Authorized'
            myColor = (0, 255, 0)
        else:
            myOutput = 'not Authorized'
            myColor = (0, 0, 255)

        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        # Lines that surround the Barcode/QRCode
        cv2.polylines(img, [pts], True, myColor, 5)
        pts2 = barcode.rect
        # Text for Barcode/QRCode visible in Camera
        cv2.putText(img, myOutput, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, myColor, 2)

    cv2.imshow('Result', img)
    cv2.waitKey(1)
