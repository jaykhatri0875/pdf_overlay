from pytesseract import pytesseract

pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

file = "./inputs/test_image_9.jpg"

pytesseract.run_tesseract(file,'./hocr_outputs/test_img_9', lang=None, config="hocr", extension='hocr')