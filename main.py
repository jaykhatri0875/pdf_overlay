from pytesseract import pytesseract
from parser_1 import HocrParser
import io
import utils
import os
from ino.reader import DocumentFile
import glob, sys, fitz
# setting tesseract dependency manually
pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

input_path = None
output_path = None

"""
# not used as of now
def preprocess(raw_image):
    # pre process image
    # save it in inputs format
    ## use fitz for reshaping images
    pass
"""

def pdf_to_image(pdf_path):
    zoom_x = 2.0  # horizontal zoom
    zoom_y = 2.0  # vertical zoom
    mat = fitz.Matrix(zoom_x, zoom_y)  # zoom factor 2 in each dimension
    try:
        path = '.././inputs/test_text.pdf'
        name = os.path.splitext(os.path.basename(path))[0]
        doc = fitz.open(path)
        return 1
    except:
        return "error converting pdf to image"


for page in doc:  # iterate through the pages
    pix = page.get_pixmap(matrix=mat)  # render page to an image
    pix.save(name + "_" + "%i.png" % page.number)
def get_name(path):
    return os.path.splitext(os.path.basename(path))[0]

def get_hocr(input_image_path):
    hocr_file_name = get_name(input_image_path) + "_hocr"
    hocr_file_path = "./outputs/" + hocr_file_name + ".hocr"
    try:
        pytesseract.run_tesseract(input_image_path, hocr_file_path, lang=None, config="hocr", extension='hocr')
        return 1, hocr_file_path
    except:
        return 0, None


def export(hocr_file_path, input_path, output_path):
    file = open(hocr_file_path, 'r', encoding="utf8")
    xmls = file.read()
    print(xmls)
    
    """
    parser = HocrParser()
    docs = DocumentFile.from_images(input_path)
    for i, img in enumerate(docs):
        xml_element_tree = xmls
        parser.export_pdfa('test_img.pdf', hocr=xml_element_tree, image = img, invisible_text = False)
    """

if __name__ == "__main__":
    # TODO: read input_path and output_path from user
    input_path = "./inputs/test_image2.jpg"
    flag, path = get_hocr(input_path)
    print(path)
    if(flag == 1):
        output_path = "./outputs/" + get_name(input_path) + "_out.pdf"
        print(output_path)
        export(input_path, input_path, output_path)
    else:
        # raise error
        print("error in ocr processing")