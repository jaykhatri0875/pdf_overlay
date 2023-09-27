import glob, sys, fitz
import os

# To get better resolution
zoom_x = 2.0  # horizontal zoom
zoom_y = 2.0  # vertical zoom
mat = fitz.Matrix(zoom_x, zoom_y)  # zoom factor 2 in each dimension

path = '.././inputs/test_text.pdf'
# all_files = glob.glob(path + "*.pdf")

name = os.path.splitext(os.path.basename(path))[0]
doc = fitz.open(path)
for page in doc:  # iterate through the pages
    pix = page.get_pixmap(matrix=mat)  # render page to an image
    pix.save(name + "_" + "%i.png" % page.number)

"""
for filename in all_files:
    doc = fitz.open(filename)  # open document
    for page in doc:  # iterate through the pages
        pix = page.get_pixmap(matrix=mat)  # render page to an image
        pix.save("../data/out/page-%i.png" % page.number)  # store image as a PNG

"""