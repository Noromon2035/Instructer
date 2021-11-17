import spacy
import re
from spacy import displacy
nlp = spacy.load("en_core_web_sm")

def check(text):

  __pos_tokens=[]
  __turning_index=[]
  __object=[]
  __verb=''
  __predicates=[]
  __final_instruction=''

  #tokenizer
  __doc = nlp(text)
  for token in __doc:
    __pos_tokens.append([token.text, token.pos_])
  print("The instruction was tokenized.")

  #Passive let-mode detection
  if __pos_tokens[0][0].lower() =='let':
    print("The instruction is in passive \"let\" mode!")
    __turning_index=[__pos_tokens.index(x) for x in __pos_tokens if x[0].lower()=="be" or x[0].lower()=="not"]
    
    #find both object and verb base form
    for i in list(range(1, __turning_index[0])):
      __object.append(__pos_tokens[i][0])
    __doc=nlp(__pos_tokens[__turning_index[-1]+1][0])
    __verb=__doc[0].lemma_
    print("The object *{}*, and verb *{}*  in base form were found.".format(__object,__verb))

    #find predicates
    for i in list(range(__turning_index[-1]+2, len(__pos_tokens))):
      __predicates.append(__pos_tokens[i][0])
    print("The predicate *{}* was found.".format(__predicates))

    #determine if positive or negative
    if "not" in [x[0] for x in __pos_tokens]:
      __verb = "Don't " + __verb 

    #construct the active mode
    __final_instruction += __verb
    for x in __object:
      if x=="'s":
        __final_instruction += x
      else:
        __final_instruction += " " + x

    for x in __predicates:
      if x=="'s":
        __final_instruction += x
      else:
        __final_instruction += " " + x
    print(__final_instruction)
  
  #Active mode detection
  else:
    print("The instruction is in active mode.")
    return
  

check("Let the cabin's wood not be burnt by fire.")