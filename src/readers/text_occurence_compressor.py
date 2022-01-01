import re

with open("model-vocab-1.txt", 'r') as f:
    lines=f.readlines()
print("Lines were read.")

current=0
max=len(lines)
all_words=set()

for line in lines:
    words=re.split(" ",line)
    for word in words:
        if bool(re.search("[0-9]", word))==False:
            all_words.add(word.lower())
            
    print("{}/{}".format(current,max))
    current+=1
print(len(all_words))
"""
with open("occurences.txt", 'w') as w:
    file=open("model-vocab-1.txt", 'r')
    doc=file.read()
    for word in all_words:
        word_line="{},{},\n".format(word,doc.count("{} ".format(word.lower())))
        w.write(word_line)
        print(word_line)
"""