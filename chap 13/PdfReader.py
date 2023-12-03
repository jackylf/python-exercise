import PyPDF2

with open('正面管教.pdf','rb') as myfile:
    mypdf = PyPDF2.PdfReader(myfile)
    mypage = mypdf.pages[1]
    text = mypage.extract_text()
    print(mypdf.is_encrypted)
    
print(text)
