import re
from string import punctuation
from spellchecker import SpellChecker
spell=SpellChecker()

def check(text):
    words=re.split("[\s{}]+".format(punctuation),text)
    common_words=set()
    count=0
    result=text

    for word in words:
        if len(word)==1:
            count+=1
            continue
        elif word.lower() == "dont":
            result=re.sub(r"\b[Dd]ont\b","don't",result)
        else:
            has_punct=False
            for char in word:
                if char in punctuation:
                    has_punct==True
                    break
            if word.islower()==True and word.isalpha()==True and has_punct==False:
                common_words.add(word)
        count+=1

    misspelled=spell.unknown(common_words)
    print(misspelled)
    for word in misspelled:
        correction=spell.correction(word)
        if word.capitalize() in common_words:
            word=word.capitalize()
            correction=correction.capitalize()
        result=re.sub(r"\b{}\b".format(word),correction,result)
    return result

if __name__=="__main__":
    result=check("riote not eat bnana Chariote.")
    print(result)