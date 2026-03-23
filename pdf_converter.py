#pdf converter.py


import pypdf
import os
import json

path = os.getcwd()
file  = os.path.join(path, 'samplepdef.pdf')

pdf = pypdf.PdfReader(file)
mylist = []
for page in pdf.pages:
    print(page.extract_text())
    
    mylist.append(page.extract_text())
    
with open('output.txt', 'w') as f:  
    for item in mylist:
        f.write("%s\n" % item)
        
#save as json
mydict = {}
for x, y in enumerate(mylist):
    mydict[x] = {"page": x+1, "text": y}
    
with open('output.json', 'w') as f:
    json.dump(mydict, f, indent=4)
    

