import docx

def get_text(word_file):
    doc = docx.Document(word_file)
    texts = []
    for para in doc.paragraphs:
        texts.append(para.text)
    return '\n'.join(texts)

text = get_text('demo.docx')
print(text)
