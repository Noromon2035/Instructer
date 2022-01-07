unspaced=("\'s","n't","-")

def convert(pos):
  if pos==[]:
    return ""
    
  __sentence=""
  __count=0

  for x in pos:
    if x[0] in unspaced or x[1]=="PUNCT" or __count==0:
      __sentence += x[0]
    else:
      __sentence += " " + x[0]
    __count+=1
  return __sentence