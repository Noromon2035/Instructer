print("Importing " + __file__)
from tokenizers import clause_tokenizer
from converters import pos_to_string_converter
print("Finished importing " + __file__)

def convert(text,pos):

    __tokens={}
    __clauses=[]

    __tokens["clauses"]=clause_tokenizer.tokenize(text, pos)

    for clause in __tokens["clauses"]:
        temp_clause=[]
        for token in clause:
            text_token=pos_to_string_converter.convert(token)
            temp_clause.append(text_token)
        __clauses.append(temp_clause)
    
    print("\nSentence structures were found.")
    print(__clauses)
    return __clauses
