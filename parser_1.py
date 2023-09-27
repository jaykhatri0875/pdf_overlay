# Imports
import base64
import re
from tempfile import TemporaryDirectory
from math import atan, cos, sin
from typing import Dict, Optional, Tuple
from xml.etree import ElementTree as ET
from xml.etree.ElementTree import Element,XML, fromstring
import numpy as np


from ino.reader import DocumentFile
from PIL import Image
from reportlab.lib.colors import black
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen.canvas import Canvas


class HocrParser():
    def __init__(self):
        self.box_pattern = re.compile(r'bbox((\s+\d+){4})')
        self.baseline_pattern = re.compile(r'baseline((\s+[\d\.\-]+){2})')

    def _element_coordinates(self, element: Element) -> Dict:
        """
        Returns a tuple containing the coordinates of the bounding box around
        an element
        """
        out = out = {'x1': 0, 'y1': 0, 'x2': 0, 'y2': 0}
        if 'title' in element.attrib:
            matches = self.box_pattern.search(element.attrib['title'])
            print(matches)
            if matches:
                coords = matches.group(1).split()
                out = {'x1': int(coords[0]), 'y1': int(
                    coords[1]), 'x2': int(coords[2]), 'y2': int(coords[3])}
        return out

    def _get_baseline(self, element: Element) -> Tuple[float, float]:
        """
        Returns a tuple containing the baseline slope and intercept.
        """
        if 'title' in element.attrib:
            matches = self.baseline_pattern.search(
                element.attrib['title']).group(1).split()
            if matches:
                return float(matches[0]), float(matches[1])
        return (0.0, 0.0)

    def _pt_from_pixel(self, pxl: Dict, dpi: int) -> Dict:
        """
        Returns the quantity in PDF units (pt) given quantity in pixels
        TODO : add transparency layer
        """
        pt = [(c / dpi * inch) for c in pxl.values()]
        return {'x1': pt[0], 'y1': pt[1], 'x2': pt[2], 'y2': pt[3]}

    def _get_element_text(self, element: Element) -> str:
        """
        Return the textual content of the element and its children
        """
        text = ''
        if element.text is not None:
            text += element.text
        for child in element:
            text += self._get_element_text(child)
        if element.tail is not None:
            text += element.tail
        return text

    def export_pdfa(self,
                    out_filename: str,
                    hocr: ET.ElementTree,
                    image: Optional[np.ndarray] = None,
                    fontname: str = "Times-Roman",
                    fontsize: int = 1,
                    invisible_text: bool = True,
                    add_spaces: bool = True,
                    dpi: int = 100):
        """
        Generates a PDF/A document from a hOCR document.
        """
        # hardcoding for now
        width, height = 285.84,404.16
        # Get the image dimensions
        print("@findall",hocr.findall(".//div[@class='ocr_page']"))
        for div in hocr.findall(".//div[@class='ocr_page']"):
            coords = self._element_coordinates(div)
            #print("@coords",coords)
            pt_coords = self._pt_from_pixel(coords, dpi)
            #print("@point coordinates==",pt_coords)
            width, height = pt_coords['x2'] - \
                pt_coords['x1'], pt_coords['y2'] - pt_coords['y1']
            # after catch break loop
            break
        if width is None or height is None:
            raise ValueError("Could not determine page size")

        pdf = Canvas(out_filename, pagesize=(width, height), pageCompression=1)

        span_elements = [element for element in hocr.iterfind(".//span")]
        print("@span elements", span_elements)
        for line in span_elements:
            print("line", line)
            if 'class' in line.attrib and line.attrib['class'] == 'ocr_line' and line is not None:
                # get information from xml
                pxl_line_coords = self._element_coordinates(line)
                line_box = self._pt_from_pixel(pxl_line_coords, dpi)

                # compute baseline
                slope, pxl_intercept = self._get_baseline(line)
                if abs(slope) < 0.005:
                    slope = 0.0
                angle = atan(slope)
                cos_a, sin_a = cos(angle), sin(angle)
                intercept = pxl_intercept / dpi * inch
                baseline_y2 = height - (line_box['y2'] + intercept)

                # configure options
                text = pdf.beginText()
                text.setFont(fontname, fontsize)
                pdf.setFillColor(black)
                if invisible_text:
                    text.setTextRenderMode(3)  # invisible text

                # transform overlayed text
                text.setTextTransform(
                    cos_a, -sin_a, sin_a, cos_a, line_box['x1'], baseline_y2)

                elements = line.findall(".//span[@class='ocrx_word']")
                print("@elements", elements)
                for elem in elements:
                    elemtxt = self._get_element_text(elem).strip()
                    # replace unsupported characters
                    elemtxt = elemtxt.translate(str.maketrans(
                        {'ﬀ': 'ff', 'ﬃ': 'f‌f‌i', 'ﬄ': 'f‌f‌l', 'ﬁ': 'fi', 'ﬂ': 'fl'}))
                    if not elemtxt:
                        continue

                    # compute string width
                    pxl_coords = self._element_coordinates(elem)
                    box = self._pt_from_pixel(pxl_coords, dpi)
                    if add_spaces:
                        elemtxt += ' '
                        box_width = box['x2'] + pdf.stringWidth(elemtxt, fontname, fontsize) - box['x1']
                    else:
                        box_width = box['x2'] - box['x1']
                    font_width = pdf.stringWidth(elemtxt, fontname, fontsize)

                    # Adjust relative position of cursor
                    cursor = text.getStartOfLine()
                    dx = box['x1'] - cursor[0]
                    dy = baseline_y2 - cursor[1]
                    text.moveCursor(dx, dy)

                    # suppress text if it is 0 units wide
                    if font_width > 0:
                        text.setHorizScale(100 * box_width / font_width)
                        text.textOut(elemtxt)
                pdf.drawText(text)

        # overlay image if provided
        if image is not None:
            pdf.drawImage(ImageReader(Image.fromarray(image)),
                          0, 0, width=width, height=height)
        pdf.save()



# model = ocr_predictor(det_arch='db_resnet50', reco_arch='crnn_vgg16_bn', pretrained=True)
# we will grab only the first two pages from the pdf for demonstration
# result = model(docs[:2])

# xml_outputs = result.export_as_xml()

# init the above parser

#docs = DocumentFile.from_pdf("./inputs/test_text.pdf")
docs = DocumentFile.from_images("./inputs/test_image_9.jpg")
parser = HocrParser()
file = open("./hocr_outputs/test_img_9.hocr", 'r', encoding="utf8")
test_xml3 = file.read()

xmls = ET.ElementTree(fromstring(test_xml3))

def print_tree(root):
    for child in root:
        print(" 0 ",child.tag,child.attrib)
        for c in child:
            print("   1 ",c.tag,c.attrib)
            for ck in c:
                print("      2 ",ck.tag,ck.attrib)
                for ckg in c:
                    print("          3 ",ckg.tag,ckg.attrib)
print_tree(fromstring(test_xml3))
# old impl: #parser.export_pdfa('output.pdf', hocr=xml, invisible_text=False)
# iterate through the xml outputs and images and export to pdf/a
# the image is optional else you can set invisible_text=False and the text will be printed on a blank page
for i, img in enumerate(docs):
    xml_element_tree = xmls
    parser.export_pdfa('test_img_9.pdf', hocr=xml_element_tree, image = img, invisible_text = False)
