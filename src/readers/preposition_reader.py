import re

file=open("complex_prepositions_lists.txt","r")
preps=file.readlines()
prepositions=[]
for prep in preps:
    prep=prep.strip("\n")
    prepositions.append(re.split(",",prep))
file.close()
print(prepositions)