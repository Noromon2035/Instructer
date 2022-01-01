import os
import platform

def read_text_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def combine_corpora():
    path=os.getcwd()
    for file in os.listdir():
        if file=="corpora-2":
            if platform.system=="Windows":
                file_path = f"{path}\{file}"
            else:
                file_path = f"{path}/{file}"
            path=file_path
            break
    os.chdir(path)

    doc=""
    for file in os.listdir():
        if platform.system=="Windows":
            file_path = f"{path}\{file}"
        else:
            file_path = f"{path}/{file}"
        doc+=read_text_file(file_path)

    with open("corpus-2.txt", 'w') as f:
        f.write(doc)
    print("File was created.\n\n\n")

import re

lines=[]
with open("corpus-2.txt", 'r') as f:
    lines=f.readlines()
print("Lines were read.")


with open("model-vocab-2.txt", 'w') as w:
    for line in lines:
        sentences=re.split(r"[,.]|<p>|<h>",line)
        for sentence in sentences:
            raw_sentence=""
            words=re.split(" ",sentence)
            for word in words:
                if bool(re.search("[^a-zA-Z0-9_-]", word))==False and word!="" and word!="-":
                    raw_sentence+= word + " "
            if raw_sentence!="" and raw_sentence!=" ":
                w.write(raw_sentence)  
                w.write("\n")
                print(raw_sentence)
