import spacy
import re

nlp = spacy.load("en_core_web_sm")

def check(text, tokens):

  __turning_index=[]
  __object=[]
  __verb=''
  __predicates=[]
  __final_instruction=''

  #Passive let-mode detection
  if tokens[0][0].lower() =='let':
    print("The instruction is in passive \"let\" mode!")
    __turning_index=[tokens.index(x) for x in tokens if x[0].lower()=="be" or x[0].lower()=="not"]
    
    #find both object and verb base form
    for i in list(range(1, __turning_index[0])):
      __object.append(tokens[i][0])
    __doc=nlp(tokens[__turning_index[-1]+1][0])
    __verb=__doc[0].lemma_
    print("The object *{}*, and verb *{}*  in base form were found.".format(__object,__verb))

    #find predicates
    for i in list(range(__turning_index[-1]+2, len(tokens))):
      __predicates.append(tokens[i][0])
    print("The predicate *{}* was found.".format(__predicates))

    #determine if positive or negative
    if "not" in [x[0] for x in tokens]:
      __verb = "Don't " + __verb 

    #construct the active mode
    __final_instruction += __verb.capitalize()
    for x in __object:
      if x=="'s":
        __final_instruction += x
      else:
        __final_instruction += " " + x

    for x in __predicates:
      if x=="'s" or x=="." or x=="?" or x=="!" or x==",":
        __final_instruction += x
      else:
        __final_instruction += " " + x
    print(__final_instruction)
    return __final_instruction
  
  #Passive polite mode detection
  elif tokens[0][0].lower() == "you" and tokens[1][1] == "AUX" and tokens[2][2] == "VBN":
    print("The instruction is in a polite passive mode.")
    return text

  #Active mode detection
  elif tokens[0][1] == "VERB":
    print("The instruction is in active mode.")
    return text
  
  #Non-imperative text detection
  else:
    print ("The instruction is declarative.")
    return "The instruction is declarative."