import docx


def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
        # fullText.append('\n')
    return '\n'.join(fullText)
