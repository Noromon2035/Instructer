print("Importing " + __file__)
import clause_tokenizer
from converters import pos_to_string_converter as pos_to_string_converter
print("Finished importing " + __file__)

def convert(text,pos):

    __tokens={}
    __clauses=[]

    __tokens["clauses"]=clause_tokenizer.tokenize(text, pos)

    for token in __tokens["clauses"]:
        temp_clause=pos_to_string_converter.convert(token)
        __clauses.append(temp_clause)
    
    print("\nSentence structures were found.")
    print(__clauses)
    return __clauses