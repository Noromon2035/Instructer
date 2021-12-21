print("Importing " + __file__)
import pos_tokenizer
import pos_to_string_converter
print("Finished importing " + __file__)

def tokenize(text):
    __pos=pos_tokenizer.tokenize(text)
    __prep_indexes=[]
    for i in list(range(0,len(__pos))):
        if __pos[i][1] == "ADP":
            __prep_indexes.append(i)

    __prep_phrases=[]
    for i in list(range(0,len(__prep_indexes))):
        __temp_pos_phrase=[]
        first_index=__prep_indexes[i]
        try:
            last_index=__prep_indexes[i+1]
        except:
            last_index=len(__pos)
        for j in list(range(first_index,last_index)):
            __temp_pos_phrase.append(__pos[j])
        __temp_phrase=pos_to_string_converter.convert(__temp_pos_phrase)
        __prep_phrases.append(__temp_phrase)
    
    print("Prepositional phrases were found.")
    return __prep_phrases