print("Importing spacy")
import spacy
from spacy.tokenizer import Tokenizer
from spacy.lang.char_classes import ALPHA, ALPHA_LOWER, ALPHA_UPPER, CONCAT_QUOTES, LIST_ELLIPSES, LIST_ICONS
from spacy.util import compile_infix_regex

print("Importing preposition tokenizer")
from tokenizers import preposition_tokenizer as prt
print("Importing sentence tokenizer")
from tokenizers import sentence_tokenizer as st
print("Importing sp tokenizer")
from tokenizers import subject_predicate_tokenizer as spt
print("Importing instruction formatter")
from formatters import instruction_formatter
from tokenizers import pos_tokenizer



class Analyzer():
    def __init__(self):
        pass

    def read_text_file(self,file_paths):
        print("Reading text file...")
        doc=""
        for path in file_paths:
            with open(path, 'r') as f:
                doc+=f.read()
        return doc
    
    def custom_tokenizer(self,nlp):
        infixes = (
            LIST_ELLIPSES
            + LIST_ICONS
            + [
                r"(?<=[0-9])[+\-\*^](?=[0-9-'])",
                r"(?<=[{al}{q}])\.(?=[{au}{q}])".format(
                    al=ALPHA_LOWER, au=ALPHA_UPPER, q=CONCAT_QUOTES
                ),
                r"(?<=[{a}]),(?=[{a}])".format(a=ALPHA),
                #r"(?<=[{a}])(?:{h})(?=[{a}])".format(a=ALPHA, h=HYPHENS),
                r"(?<=[{a}0-9])[:<>=/](?=[{a}])".format(a=ALPHA),
            ]
        )

        infix_re = compile_infix_regex(infixes)
        exceptions=nlp.Defaults.tokenizer_exceptions
        filtered_exceptions = {k:v for k,v in exceptions.items() if "'" not in k}

        return Tokenizer(nlp.vocab, prefix_search=nlp.tokenizer.prefix_search,
                                    suffix_search=nlp.tokenizer.suffix_search,
                                    infix_finditer=infix_re.finditer,
                                    token_match=nlp.tokenizer.token_match,
                                    rules=filtered_exceptions)

    def analyze(self,nlp, instruction,receiver):
        __sentences=[]
        __result_sentences=[]
        __pos=pos_tokenizer.pos_tokenize(nlp,instruction)
        
        print("Dividing into sentences")
        __sentences=st.convert(nlp,instruction, __pos)    
        print("\n\n\n\n\n")

        try:
            for sentence_coded in __sentences:
                __answered_questions=set()

                imp_index=sentence_coded.find("`")
                imperative_sent=""
                if imp_index+1 < len(sentence_coded) and imp_index!=-1:
                    imperative_sent=sentence_coded[imp_index+1:]
                else:
                    imperative_sent=sentence_coded
                imperative_coded=imperative_sent
                imperative_sent= imperative_sent.replace("^","")

                imp_prep=prt.tokenize(nlp,imperative_coded)
                if imp_prep !=None:
                    for prep in imp_prep:
                        if prep[2]!="":
                            __answered_questions.add(prep[2])

                if imp_index!=0:
                    non_imperative_sent=sentence_coded[:imp_index]
                    non_imp_prep=prt.tokenize(nlp,non_imperative_sent)
                    for prep in non_imp_prep:
                        if prep[2]!="":
                            __answered_questions.add(prep[2])

                __result_sentences.append([sentence_coded,__answered_questions])
                print(sentence_coded,__answered_questions)
                print("\n\n")
            questions, instructions, notes=instruction_formatter.construct(__result_sentences,receiver)
            print(questions, instructions, notes)
        except:
            return [],[instruction],[]
        
        return questions,instructions, notes

if __name__ == "__main__":
    text1="Ok, so push Mr. Antolin's arm(hand) towards the bread A.S.A.P, now squeeze the bread. Rip a bit of it off and put that in your mouth. Now move your jaw up and down repeatedly. Now swallow."
    text2="Once it can be safely assumed that the base of the flour-based cake has reached a satisfactory level of cook, firmly grasp handle of your flipping leverage tool with flip-side up and thrust forward using shoulder, engaging glenohumeral joint for smooth motion. Then swallow."
    analyzer=Analyzer()
    print("Loading spacy nlp")
    nlp = spacy.load("en_core_web_sm")
    nlp.tokenizer = analyzer.custom_tokenizer(nlp)
    result=analyzer.analyze(nlp,text2,"Jomar")
    print("Result:")
    print(result)