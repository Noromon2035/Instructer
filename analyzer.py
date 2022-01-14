print("Importing " + __file__)
from checkers import grammar_checker_lt
print("Importing grammar checker")
from checkers import voice_checker
print("Importing voice checker")
from converters import simplifier
print("Importing simplifier")
from tokenizers import preposition_tokenizer as prt
print("Importing preposition tokenizer")
from tokenizers import pos_tokenizer
print("Importing pos tokenizer")
from tokenizers import sentence_tokenizer as st
print("Importing sentence tokenizer")
from tokenizers import subject_predicate_tokenizer as spt
print("Importing sp tokenizer")
from formatters import instruction_formatter
print("Importing instruction formatter")
from formatters import question_formatter
print("Importing question formatter")
print("Finished importing " + __file__)

def read_text_file(file_paths):
    print("Reading text file...")
    doc=""
    for path in file_paths:
        with open(path, 'r') as f:
            doc+=f.read()
    return doc

def analyze(instruction,receiver):
    doc=read_text_file(["model-vocab-1.txt","model-vocab-2.txt","model-vocab-3.txt"])
    text=grammar_checker_lt.check(instruction)
    __sentences=[]
    __result_sentences=[]
    __pos=pos_tokenizer.pos_tokenize(text)
    print(__pos)
    print()
    __sentences=st.convert(text, __pos)    
    #main.change_max((len(__sentences)*4)+2)
    #main.update_progress(1)
    print("\n\n\n\n\n")
    for sentence_token in __sentences:
        __answered_questions=set()
        sentence=sentence_token[1]
        __sent_pos=pos_tokenizer.pos_tokenize(sentence)
        __simplfied=simplifier.simplify(__sent_pos,doc)
        #main.update_progress(1)

        __simplfied_pos=pos_tokenizer.pos_tokenize(__simplfied)
        print(__simplfied)
        subj_pred=spt.tokenize(__simplfied,__simplfied_pos)
        #main.update_progress(1)

        subj_prep=prt.tokenize(subj_pred["subject"],is_predicate=False)
        #main.update_progress(1)

        if subj_prep != None:
            for prep in subj_prep:
                if prep[2]!="":
                    __answered_questions.add(prep[2])

        pred_prep=prt.tokenize(subj_pred["predicate"])
        if pred_prep !=None:
            for prep in pred_prep:
                if prep[2]!="":
                    __answered_questions.add(prep[2])
        #main.update_progress(1)

        __imperatived=voice_checker.check(__simplfied)
        __result_sentences.append([__imperatived["active"],__answered_questions,subj_pred["predicate"]])
        print("\n")

    #main.max_progress()
    result_instruction=instruction_formatter.format(__result_sentences)
    result_instruction=question_formatter.construct_question(result_instruction,receiver)
    for result in result_instruction:
        print(result)
    return result_instruction

#text1="Ok, so push your arm towards the bread, now squeeze the bread. Rip a bit of it off and put that in your mouth. Now move your jaw up and down repeatedly. Now swallow."
#text1="Do not eat"
#convert(text1,"Jomar")