print("Importing " + __file__)
import pos_tokenizer
import clause_tokenizer
import pos_to_string_converter
print("Finished importing " + __file__)

def convert(text):

    __tokens={}
    __nouns=[]
    __pos=[]
    __clauses=[]

    __tokens["pos"]=pos_tokenizer.tokenize(text)

    __tokens["clauses"]=clause_tokenizer.tokenize(text, __tokens["pos"])

    for token in __tokens["clauses"]:
        temp_clause=pos_to_string_converter.convert(token)
        __clauses.append(temp_clause)
    
    print("\nSentence structures were found.")
    print(__clauses)
    return __clauses

convert("The big bad talking wolf's brother is tasked to bring the little dogs and pigs while he and she is eating by failing it.")