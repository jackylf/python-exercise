import PyPDF2
import os

file_folder = os.path.join(os.getcwd(),'chap 13')
file_path1 = os.path.join(file_folder,'meetingminutes.pdf')
file_path2 = os.path.join(file_folder,'rotate_page.pdf')

pdf_writer = PyPDF2.PdfWriter()
with open(file_path1,'rb') as my_file:
    my_pdf = PyPDF2.PdfReader(my_file)
    my_page = my_pdf.pages[0].rotate(90)
    pdf_writer.add_page(my_page)

with open(file_path2,'wb') as my_file:
    pdf_writer.write(my_file)