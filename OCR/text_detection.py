import cv2 as cv
import pytesseract

#tesseract exe speichort
pytesseract.pytesseract.tesseract_cmd = "D:\\Tesseract\\tesseract.exe"

#bekomme daten aus bild ausgelesen als string (nicht 100% -> denkt z.b. r = 1)
def image_to_string(img):
    print(pytesseract.image_to_string(img))

#bekomme bounding box um die charakters
def image_to_boxes(img):
    hImg, wImg, _ = img.shape

    boxes = pytesseract.image_to_boxes(img)

    #bekomme werte (x, y, width, height) als liste für jeden charakter
    for i in boxes.splitlines():
        i = i.split(' ')
        print(i)
        x, y, w, h = int(i[1]), int(i[2]), int(i[3]), int(i[4])

        #baue rechteck um charaktere
        cv.rectangle(img, (x, hImg - y), (w, hImg - h), (0,0,255), 1)
        cv.putText(img, i[0], (x, hImg - y + 25), cv.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)

#bekomme wörter
def image_to_data(img):
    hImg, wImg, _ = img.shape

    boxes = pytesseract.image_to_data(img)

    for x, i in enumerate(boxes.splitlines()):
        if x != 0:
            i = i.split()
            print(i)
            #wenn länge = 12 -> wort
            if len(i) == 12:
                x, y, w, h = int(i[6]), int(i[7]), int(i[8]), int(i[9])
                cv.rectangle(img, (x, y), (w + x, h + y), (0, 0, 255), 2)
                cv.putText(img, i[11], (x, y - 10), cv.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)

#bekomme nur zahlen
def number_from_image(img):
    hImg, wImg, _ = img.shape

    #congif um nur numbers zu erkennen -> siehe dokumentation (engine modes)
    conf = r'--oem 3 --psm 6 outputbase digits'

    boxes = pytesseract.image_to_data(img, config=conf)

    for x, i in enumerate(boxes.splitlines()):
        if x != 0:
            i = i.split()
            print(i)
            #wenn länge = 12 -> wort
            if len(i) == 12:
                x, y, w, h = int(i[6]), int(i[7]), int(i[8]), int(i[9])
                cv.rectangle(img, (x, y), (w + x, h + y), (0, 0, 255), 2)
                cv.putText(img, i[11], (x, y - 10), cv.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)


if __name__ == "__main__":
    #test um 1 wegzubekommen


    # bild zum einlesen
    img = cv.imread('1.png')

    # pytesseract akzeptiert nur rgb-werte, opencv ist aber in bgr-werte -> müssen konvertieren
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    #image_to_string(img)
    #image_to_boxes(img)
    #image_to_data(img)
    number_from_image(img)

    # zeige unser fenster/bild
    cv.imshow('Result', img)
    cv.waitKey(0)