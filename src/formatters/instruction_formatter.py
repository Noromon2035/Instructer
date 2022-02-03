import re
from formatters import notes_constructor

def get_predicate(coded_sentence):
    #add re.sub
    matched_vb=re.search(r"\w+\^",coded_sentence)
    if matched_vb!=None:
        vb=matched_vb.group()
        if re.search(r"[nN][oO][tT]\s+\w+\^|n't\s+\w+\^",coded_sentence)!=None:
            vb="not {}".format(vb)
        return vb[:-1].lower()
    else:
        return "do"
def construct(coded_sentences,receiver):
    all_question_words=set()
    questions=[]
    q_count=0
    instructions=[]

    scount=0
    for i in list(range(0,len(coded_sentences))):
        question_words=set()
        sentence=coded_sentences[i]
        sentence_str=sentence[0]
        for question_word in sentence[1]:
            question_words.add(question_word)
            all_question_words.add(question_word)

        if "what" not in sentence[1]:
            predicate=get_predicate(sentence[0])
            questions.append("Who/what should {} {}?".format(receiver,predicate))
            sentence_str=sentence[0].replace("^","^{}^".format(q_count))
            q_count+=1
        else:
            sentence_str=sentence[0].replace("^","")
        sentence_str=str(scount+1) + ". " + sentence_str.replace("`","").capitalize()
        instructions.append(sentence_str)
        scount+=1
    notes=notes_constructor.construct(all_question_words,receiver)

    if len(instructions)==1:
        instructions[0]=instructions[0][3:]
    
    return questions, instructions, notes