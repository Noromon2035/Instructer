import wikipedia
import re

def find_meaning(word=""):
    meaning=word
    searched_words=wikipedia.search(word)
    print(searched_words)
    if word.isupper()==True:
        pattern=r""
        for char in word:
            pattern+="{}\w+\s".format(char)
        pattern=pattern[:-2]
        print(pattern)

        for search_word in searched_words:
            word_match=re.search(r"{}".format(pattern),search_word)
            if word_match !=None:
                meaning=word_match.group()
                print(meaning)
                return meaning
        return meaning
            
    try:
        print(wikipedia.summary(searched_words[0],1))
    except Exception as e:
        new_words=e.options
        print(new_words)
        try:
            print(wikipedia.summary(new_words[0],1))
        except:
            print(None)


find_meaning("ICC")
"""
['it', 'the base', 'the flour-based cake', 'a satisfactory level', 
'cook', 'handle', 'your flipping leverage tool', 'shoulder', 'glenohumeral joint', 
'smooth motion']
"""