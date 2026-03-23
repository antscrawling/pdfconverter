#pdf converter.py

import pypdf
import os

path = os.getcwd()
file  = os.path.join(path, 'Letterofoffer.pdf')

pdf = pypdf.PdfReader(file)
mylist = []
for page in pdf.pages:
    print(page.extract_text())
    mylist.append(page.extract_text())
    
with open('output.txt', 'w') as f:  
    for item in mylist:
        f.write("%s\n" % item)