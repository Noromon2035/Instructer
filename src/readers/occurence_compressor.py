import re
import json

def read_text_file(file_paths):
        print("Reading text file...")
        doc=""
        for path in file_paths:
            with open(path, 'r') as f:
                doc+=f.read()
        return doc

def read_sentences(file_paths):
        print("Reading sentences...")
        sentences=[]
        for path in file_paths:
            with open(path, 'r') as f:
                sentences=f.readlines()
        return sentences

def compress_corpus():
    doc=read_text_file(["model-vocab-1.txt","model-vocab-2.txt","model-vocab-3.txt"])
    sentences=read_sentences(["solowords.txt"])

    sentences=read_sentences(["solowords1.txt"])
    print("Find occurences")
    with open("occurences.txt", 'a') as w:
        for i in list(range(166397,len(sentences))):
            word=sentences[i]
            occurences=doc.count("{} ".format(word[0:-1]))
            w.write("{} {}".format(word[0:-1],occurences))  
            w.write("\n")
            print("{}/{} {}".format(i,len(sentences),word[0:-1]))

def save_occurences():
    tokens=read_sentences(["occurences.txt"])
    occurences={}
    count=0
    for token in tokens:
        words=re.split(" ",token)
        words[1]=int(words[1][0:-1])
        occurences[words[0]]=words[1]
        print("{}/{}".format(count,len(tokens)))
        count+=1
    print("Saving as dictionary...")
    with open('occurences.json', 'w') as f:
        json.dump(occurences,f)
    print("Finished")

save_occurences()