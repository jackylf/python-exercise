import PyPDF2

pdf_writer = PyPDF2.PdfWriter()
with open('meetingminutes.pdf','rb') as my_file:
    my_pdf = PyPDF2.PdfReader(my_file)
    for page_num in range(len(my_pdf.pages)):
        page_obj = my_pdf.pages[page_num]
        pdf_writer.add_page(page_obj)

with open('meetingminutes2.pdf','rb') as my_file:
    my_pdf = PyPDF2.PdfReader(my_file)
    for page_num in range(len(my_pdf.pages)):
        page_obj = my_pdf.pages[page_num]
        pdf_writer.add_page(page_obj)

with open('combinedminutes.pdf','wb') as my_file:
    pdf_writer.write(my_file)
