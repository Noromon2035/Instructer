print("Importing " + __file__)
import pos_tokenizer
import pos_to_string_converter
import verb_finder
print("Finished importing " + __file__)

verb_tags=("VERB","AUX")
def tokenize(text):
    __subj=[]
    __pred=[]
    __final_vb_indexes=[]
    __result={}
    __pos=pos_tokenizer.tokenize(text)

    __final_vb_indexes=verb_finder.find(text, __pos)
    
    for i in list(range(0,__final_vb_indexes[0])):
        __subj.append(__pos[i])

    if __pos[__final_vb_indexes[-1]][2] == "VBG":
        for i in list(range(__final_vb_indexes[-2],len(__pos))):
            __pred.append(__pos[i])
    else:
        for i in list(range(__final_vb_indexes[-1],len(__pos))):
            __pred.append(__pos[i])

    __result["subject"]=pos_to_string_converter.convert(__subj)
    __result["predicate"]=pos_to_string_converter.convert(__pred)
    print(__pos)
    return __result

tokenize("The eating boy will be eating foods of the east by chewing it.")