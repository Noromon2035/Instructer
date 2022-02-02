unspaced=("\'s","n't","-")
brackets=("{","(","[")

def convert(pos):
  if pos==[]:
    return ""
    
  __sentence=""
  __count=0

  try:
    for x in pos:
      if __count>0:
        if pos[__count-1][0] in brackets:
          __sentence += x[0]
          __count+=1
          continue
      if x[0] in unspaced or (x[1]=="PUNCT" and  x[0] not in brackets) or __count==0:
        __sentence += x[0]
      else:
        __sentence += " " + x[0]
      __count+=1
  except:
    return ""
  return __sentence