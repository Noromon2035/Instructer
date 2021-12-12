print("Importing " + __file__)
import pos_tokenizer
import clause_tokenizer
import pos_to_sent_converter
print("Finished importing " + __file__)

def convert(text):

    __tokens={}
    __nouns=[]
    __pos=[]
    __clauses=[]

    __tokens["pos"]=pos_tokenizer.tokenize(text)
    print(__tokens["pos"])
    print("The instruction was tagged.\n")

    __tokens["clauses"]=clause_tokenizer.tokenize(text, __tokens["pos"])
    print("Clauses were detected.\n")

    for token in __tokens["clauses"]:
        temp_clause=pos_to_sent_converter.convert(token)
        __clauses.append(temp_clause)
    print(__clauses)
    return __tokens

convert("The big bad talking wolf's brother is tasked to bring the little dogs and pigs while he and she is eating by failing it.")