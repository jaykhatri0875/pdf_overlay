import cv2
import pytesseract
from pytesseract import Output
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('test_image.jpg')

# use tesseract , try rescaling with fitz, check tesserocr
# https://github.com/mindee/notebooks/blob/main/doctr/export_as_pdfa.ipynb
# TODO: check this tutorial : https://mlichtenberg.wordpress.com/2014/12/23/hocrimagemapper-a-tool-for-visualizing-hocr-files/

data = pytesseract.image_to_data(img, output_type=Output.DICT)
print(data.keys())
print(data)
n_boxes = len(data['text'])
for i in range(n_boxes):
    if int(data['conf'][i]) > 60:
        (x, y, w, h) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)