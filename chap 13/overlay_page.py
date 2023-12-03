import PyPDF2
import os

file_folder = os.path.join(os.getcwd(),'chap 13')
file_path1 = os.path.join(file_folder,'meetingminutes.pdf')
file_path2 = os.path.join(file_folder,'watermark.pdf')
file_path3 = os.path.join(file_folder,'overlay.pdf')

pdf_writer = PyPDF2.PdfWriter()
with open(file_path1,'rb') as myfile:
    my_pdf = PyPDF2.PdfReader(myfile)
    first_page = my_pdf.pages[0]
    watermark_page = PyPDF2.PdfReader(open(file_path2,'rb')).pages[0]
    first_page.merge_page(watermark_page)
    for page in my_pdf.pages:
        pdf_writer.add_page(page)

with open(file_path3,'wb') as myfile:
    pdf_writer.write(myfile)
