def convert(pos):
    __sentence=""
    __count=0

    for x in pos:
      if x[0] == "\'s" or x[1]=="PUNCT" or __count==0 :
        __sentence += x[0]
      else:
        __sentence += " " + x[0]
      __count+=1
    print("POS tags were converted into \"" + __sentence + "\"")
    return __sentence