import re

lines=[]
with open("corpus-vocab.txt", 'r') as f:
    lines=f.readlines()
print("Lines were read.")


with open("model-vocab-1.txt", 'w') as w:
    for line in lines:
        sentences=re.split("  ",line)
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

print("\n\nFinish!\n\n")