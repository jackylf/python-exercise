import PyPDF2
import os

file_folder = os.path.join(os.getcwd(),'chap 13')
file_path1 = os.path.join(file_folder,'meetingminutes.pdf')
file_path2 = os.path.join(file_folder,'encrypt_minutes.pdf')

pdf_writer = PyPDF2.PdfWriter()
with open(file_path1,'rb') as my_file:
    my_pdf = PyPDF2.PdfReader(my_file)
    for page in my_pdf.pages:
        pdf_writer.add_page(page)

pdf_writer.encrypt('123456')
with open(file_path2,'wb') as my_file:
    pdf_writer.write(my_file)

