import re
from string import punctuation
from spellchecker import SpellChecker
spell=SpellChecker()

units_of_measurement=('km', 'hm', 'dam', 'dm', 'cm', 'mm', 'nm', 'pm', 'fm', 'am', 
'zm', 'kkg', 'hkg', 'dakg', 'dkg', 'ckg', 'mkg', 'nkg', 'pkg', 'fkg', 'akg', 'zkg', 
'ks', 'hs', 'das', 'ds', 'cs', 'ms', 'ns', 'ps', 'fs', 'as', 'zs', 'kA', 'hA', 'daA',
'dA', 'cA', 'mA', 'nA', 'pA', 'fA', 'aA', 'zA', 'kK', 'hK', 'daK', 'dK', 'cK', 'mK', 
'nK', 'pK', 'fK', 'aK', 'zK', 'kmol', 'hmol', 'damol', 'dmol', 'cmol', 'mmol', 'nmol', 
'pmol', 'fmol', 'amol', 'zmol', 'kcd', 'hcd', 'dacd', 'dcd', 'ccd', 'mcd', 'ncd', 'pcd', 
'fcd', 'acd', 'zcd')

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
            if word.islower()==True and word.isalpha()==True and has_punct==False and word not in units_of_measurement:
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