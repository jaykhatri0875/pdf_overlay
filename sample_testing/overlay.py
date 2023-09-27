import fpdf
from PyPDF2 import PdfWriter, PdfReader

overlay_pdf_file_name = 'overlay_PDF.pdf'
pdf_template_file_name = 'jay_pancard.pdf'
result_pdf_file_name = 'final_PDF.pdf'

# This section creates a PDF containing the information you want to enter in the fields
# on your base PDF.
pdf = fpdf.FPDF(format='letter', unit='pt')
pdf.add_page()
pdf_style = 'B'
pdf.set_font("Arial", style=pdf_style, size=10)
pdf.set_xy(100, 100)
pdf.cell(0, 10, txt='THIS IS THE TEXT THAT IS GOING IN YOUR FIELD', ln=0)
pdf.output(overlay_pdf_file_name)
pdf.close()

# Take the PDF you created above and overlay it on your template PDF
# Open your template PDF
pdf_template = PdfReader(pdf_template_file_name, 'rb')
# Get the first page from the template
template_page = pdf_template.pages[0]
# Open your overlay PDF that was created earlier
overlay_pdf = PdfReader(overlay_pdf_file_name, 'rb')
# Merge the overlay page onto the template page
# print(overlay_pdf.pages)
template_page.merge_page(overlay_pdf.pages[0])
# Write the result to a new PDF file
output_pdf = PdfWriter()
output_pdf.add_page(template_page)
output_pdf.write(result_pdf_file_name)


def overlay(source_pdf, text_pdf, merge_pdf):
    pdf_template = PdfReader(source_pdf, 'rb')
    template_page = pdf_template.pages[0] # needs to act for all pages, 
    # source and text should be both pdf of same pages, impose each pdf on each other 
    overlay_pdf = PdfReader(text_pdf, 'rb')
    template_page.merge_page(overlay_pdf.pages[0])
    output_pdf = PdfWriter()
    output_pdf.add_page(template_page)
    output_pdf.write(merge_pdf)