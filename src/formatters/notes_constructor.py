
def construct(all_questions,receiver):
    notes=[]
    
    if "where" not in all_questions:
        notes_dict={}
        notes_dict["question"]="Where should {} do this?".format(receiver)
        notes_dict["first"]="{} must do this ^where^".format(receiver.capitalize())
        notes_dict["later"]=notes_dict["first"]
        notes.append(notes_dict)

    if "when" not in all_questions:
        notes_dict={}
        notes_dict["question"]="When should {} do this?".format(receiver)
        notes_dict["first"]="{} must do this ^start^".format(receiver.capitalize())
        notes_dict["later"]=" ^start^"
        notes.append(notes_dict)

    if "when" not in all_questions:
        notes_dict={}
        notes_dict["question"]="When is the deadline?".format(receiver)
        notes_dict["first"]="This has to be done ^end^"
        notes_dict["later"]=", and it has to be done ^end^."
        notes.append(notes_dict)

    return notes

if __name__=="__main__":
    print(construct({"what","how"},"Jomar"))  
