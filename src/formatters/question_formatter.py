
def construct_question(result_sentences, receiver):
    for i in list(range(0,len(result_sentences))):
        result=result_sentences[i]
        if "what" not in result["questions"]:
            predicate=result["predicate"]
            if predicate[-1] in (".",",",";","!"):
                predicate=predicate[0:len(predicate)-1]+"?"
            result_sentences[i]["questions"]= "Who/What should {} {}\n".format(receiver,predicate)
        else:
            result_sentences[i]["questions"]=""
    return result_sentences
        