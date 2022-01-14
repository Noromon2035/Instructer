#region Single Prepositions

single_prepositions=[['from', 'whose'], ['from', 'whom'], ['from', 'who'], ['from', 'what'], 
['alongside', 'who'], ['except', 'who'], ['about', 'who'], ['against', 'who'], 
['alongside', 'who'], ['besides', 'who'], ['concerning', 'who'], ['concerning', 'who'], 
['counting', 'who'], ['except', 'who'], ['excepting', 'who'], ['excluding', 'who'], 
['including', 'who'], ['of', 'who'], ['regarding', 'who'], ['respecting', 'who'], 
['versus', 'who'], ['with', 'who'], ['without', 'who'], ['worth', 'who'], 
['alongside', 'what'], ['except', 'what'], ['about', 'what'], ['against', 'what'], 
['alongside', 'what'], ['besides', 'what'], ['concerning', 'what'], ['concerning', 'what'], 
['counting', 'what'], ['except', 'what'], ['excepting', 'what'], ['excluding', 'what'], 
['including', 'what'], ['of', 'what'], ['regarding', 'what'], ['respecting', 'what'], 
['versus', 'what'], ['with', 'what'], ['without', 'what'], ['worth', 'what'], 
['aboard', 'where'], ['above', 'where'], ['across', 'where'], ['along', 'where'], 
['among', 'where'], ['around', 'where'], ['astride', 'where'], ['at', 'where'], 
['atop', 'where'], ['behind', 'where'], ['below', 'where'], ['beneath', 'where'], 
['beside', 'where'], ['between', 'where'], ['beyond', 'where'], ['by', 'where'], 
['down', 'where'], ['in', 'where'], ['inside', 'where'], ['into', 'where'], 
['near', 'where'], ['of', 'where'], ['off', 'where'], ['onto', 'where'], 
['opposite', 'where'], ['outside', 'where'], ['over', 'where'], ['past', 'where'], 
['round', 'where'], ['through', 'where'], ['thru', 'where'], ['throughout', 'where'], 
['to', 'where'], ['toward', 'where'], ['towards', 'where'], ['under', 'where'], 
['underneath', 'where'], ['up', 'where'], ['upon', 'where'], ['within', 'where'], 
['after', 'when'], ['amidst', 'when'], ['amid', 'when'], ['around', 'when'], 
['at', 'when'], ['before', 'when'], ['between', 'when'], ['beyond', 'when'], ['by', 'when'], 
['circa', 'when'], ['during', 'when'], ['following', 'when'], ['gone', 'when'], 
['in', 'when'], ['over', 'when'], ['past', 'when'], ['pending', 'when'], ['re', 'when'], 
['since', 'when'], ['throughout', 'when'], ['till', 'when'], ['to', 'when'], 
['under', 'when'], ['until', 'when'], ['upon', 'when'], ['within', 'when'], 
['concerning', 'why'], ['considering', 'why'], ['following', 'why'], ['for', 'why'], 
['regarding', 'why'], ['respecting', 'why'], ['since', 'why'], ['touching', 'why'], 
['as', 'how'], ['by', 'how'], ['excepting', 'how'], ['excluding', 'how'], ['less', 'how'], 
['like', 'how'], ['minus', 'how'], ['notwithstanding', 'how'], ['per', 'how'], 
['plus', 'how'], ['than', 'how'], ['through', 'how'], ['thru', 'how'], ['touching', 'how'], 
['unlike', 'how'], ['upon', 'how'], ['via', 'how'], ['with', 'how'], ['without', 'how'], 
['bar', 'what'], ['despite', 'how'], ['given', 'how'], ['given', 'what'], 
['pro', 'what'], ['pro', 'how'], ['save', 'how'], ['save', 'what'], ['saving', 'how'], 
['saving', 'what'], ['of', 'when']]
#endregion

#region Complex Prepositions
complex_prepositions=[['along with', 'who'], ['along with', 'what'], ['along with', 'how'], 
['apart from', 'who'], ['apart from', 'what'], ['apart from', 'how'], ['as for', 'who'], 
['as for', 'what'], ['as for', 'why'], ['aside from', 'who'], ['aside from', 'what'], 
['aside from', 'how'], ['as well as', 'who'], ['as well as', 'what'], ['as well as', 'how'], 
['except for', 'what'], ['except for', 'who'], ['in addition to', 'who'], 
['in addition to', 'what'], ['other than', 'what'], ['other than', 'who'], 
['regardless of', 'what'], ['regardless of', 'who'], ['save for', 'what'], 
['save for', 'who'], ['together with', 'who'], ['together with', 'what'], 
['together with', 'how'], ['up against', 'who'], ['up against', 'what'], 
['up against', 'where'], ['vis-a-vis', 'who'], ['vis-a-vis', 'what'], ['vis-a-vis', 'why'], 
['with regard to', 'who'], ['with regard to', 'what'], ['with regard to', 'why'], 
['ahead of', 'where'], ['ahead of', 'when'], ['away from', 'where'], ['close to', 'where'], 
['forward of', 'where'], ['in between', 'where'], ['in favour of', 'where'], 
['in front of', 'where'], ['near to', 'where'], ['next to', 'where'], ['onboard', 'where'], 
['onto', 'where'], ['on top of', 'where'], ['opposite to', 'where'], ['out of', 'where'], 
['outside of', 'where'], ['further to', 'when'], ['in case of', 'when'], 
['in face of', 'when'], ['prior to', 'when'], ['up to', 'when'], ['up until', 'when'], 
['according to', 'why'], ['as per', 'why'], ['as to', 'why'], ['because of', 'why'], 
['but for', 'why'], ['due to', 'why'], ['in spite of', 'why'], ['instead of', 'why'], 
['in view of', 'why'], ['irrespective of', 'why'], ['on account of', 'why'], 
['on behalf of', 'why'], ['owing to', 'why'], ['preperatory to', 'why'], 
['thanks to', 'why'], ['with reference to', 'who'], ['with reference to', 'what'], 
['with reference to', 'why'], ['a la', 'how'], ['by means of', 'how'], 
['contrary to', 'how'], ['depending on', 'how'], ['in lieu of', 'how'], 
['other than', 'how'], ['with reference to', 'how']]
#endregion

question_words=("person","what","place","when","why","how","whose","whom")

try:
    import re
    from finders import noun_phrase_finder
    from tokenizers import pos_tokenizer
    from gensim.models import KeyedVectors
    from tokenizers import pos_tokenizer
except Exception as e:
    print(e)
    
wordvec = KeyedVectors.load("instruct_vector.wordvectors", mmap='r')

def partition(arr,low,high):
    i = (low-1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j][1] <= pivot[1]:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quicksort_prep(prepositions,low,high):
    if len(prepositions) == 1:
        return prepositions
    if low < high:
        pi = partition(prepositions, low, high)
        quicksort_prep(prepositions, low, pi-1)
        quicksort_prep(prepositions, pi+1, high)

def convert_token(tokens,first,last):
    phrase=""
    for j in list(range(first,last)):
        if j!=last-1:
            phrase+=tokens[j]+" "
        else:
            phrase+=tokens[j]
    return phrase

def search_prep_func(phrase):
    result=phrase
    for prep in single_prepositions:
        if prep[0]==phrase[0].lower():
            result.append(prep[1])
    if len(result)<=3:
        for prep in complex_prepositions:
            if prep[0]==phrase[0].lower():
                result.append(prep[1])
    return result

def search_prep_func(phrase):
    result=phrase
    for prep in single_prepositions:
        if prep[0]==phrase[0].lower():
            result.append(prep[1])
    if len(result)<=3:
        for prep in complex_prepositions:
            if prep[0]==phrase[0].lower():
                result.append(prep[1])
    return result

def check_prep_role(prep):
    if len(prep[2])<=1:
        print("\n"+prep[1])
        prep[2]=prep[2][0]
        return prep
    else:
        time_regex=r"\d+:\d+"
        date_regex=r"\d+[/-]\d+[/-]\d+"
        gerund_regex=r"by \w+ing"
        if re.findall(time_regex,prep[1])!=[] or re.findall(date_regex,prep[1])!=[]:
            prep[2]="when"
            return prep
        if re.findall(gerund_regex,prep[1])!=[]:
            prep[2]="how"
            return prep
        else:
            pos=pos_tokenizer.pos_tokenize(prep[1])
            similarities=[]
            for quest_word in question_words:
                highest_similarity=-1
                for token in pos:
                    similarity=0
                    try:
                        similarity=wordvec.similarity(quest_word,token[0].lower())
                    except:
                        if token[0] not in (".",","):
                            similarity=-1
                    if similarity> highest_similarity:
                        highest_similarity=similarity
                converted_q_word=quest_word
                if quest_word=="person":
                    converted_q_word="who"
                elif quest_word=="place":
                    converted_q_word="where"
                similarities.append([converted_q_word,highest_similarity])
            
            highest=similarities[0]
            for similarity in similarities:
                if similarity[1]>highest[1] and similarity[0] in prep[2]:
                    highest=similarity
            print("\n"+prep[1])
            print(highest)
            prep[2]=highest[0]
            return prep

def check_non_prep_role(prep,is_pred):
    if is_pred==False:
        if len(re.split(r"[^a-zA-Z0-9_'-:/]",prep[1]))>1:
            prep[2]="what"
        else:
            prep[2]=""
    else:
        poss=pos_tokenizer.pos_tokenize(prep[1])
        count=0
        vb_index=0
        for pos in poss:
            if pos[1]=="VERB":
                vb_index=count
                break
            count+=1
        if len(poss[vb_index:])<2:
            prep[2]=""
        elif poss[vb_index:][1][1]=="PUNCT":
            prep[2]=""
        else:
            prep[2]="what"

    return prep

def tokenize(text,is_predicate=True):
    found_indexes=set()
    found_prepositions=[]
    tokens=re.split(r"[^a-zA-Z0-9_'-:/]",text)
    try:
        tokens.remove(' ')
    except:
        pass
    max_word_count=4    #highest word count of preposition
    while max_word_count>len(tokens):
        max_word_count-=1
    
    #get all combinations from max to low word count
    for h in list(reversed(range(0,max_word_count))):
        phrases=[]
        for i in list(range(h,len(tokens))):
            phrase=convert_token(tokens,i-h,i+1)
            phrases.append([phrase,i-h,i])
        if h==0:
            for phrase in phrases:
                is_appendable=True
                for i in list(range(phrase[1],phrase[2]+1)):
                    if i in found_indexes:
                        is_appendable=False
                        break
                if is_appendable==True:
                    for prep in single_prepositions:
                        if phrase[0].lower()==prep[0] and phrase not in  found_prepositions:
                            phrase=search_prep_func(phrase)
                            found_prepositions.append(phrase)
                            for i in list(range(phrase[1],phrase[2]+1)):
                                found_indexes.add(i)
        else:
            for phrase in phrases:
                is_appendable=True
                for i in list(range(phrase[1],phrase[2]+1)):
                    if i in found_indexes:
                        is_appendable=False
                        break
                if is_appendable==True:
                    for prep in complex_prepositions:
                        if phrase[0].lower()==prep[0] and phrase not in found_prepositions:
                            phrase=search_prep_func(phrase)
                            found_prepositions.append(phrase)
                            for i in list(range(phrase[1],phrase[2]+1)):
                                found_indexes.add(i)
    
    #arrange set in numerical order of indexes
    if len(found_prepositions)<=0:
        result=check_non_prep_role(["",text,[""]],is_predicate)
        return [result]
    quicksort_prep(found_prepositions,0,len(found_prepositions)-1)

    #get prepositional phrases and before it
    prep_phrases=[]
    for i in list(range(0,len(found_prepositions))):
        prep_phrase_tokens=[]
        before_prep_tokens=[]
        try:
            for j in list(range(found_prepositions[i][1],found_prepositions[i+1][1])):
                prep_phrase_tokens.append(tokens[j])
        except:
            for j in list(range(found_prepositions[i][1],len(tokens))):
                prep_phrase_tokens.append(tokens[j])
        if i!=0:
            for j in list(range(found_prepositions[i-1][1],found_prepositions[i][1])):
                before_prep_tokens.append(tokens[j])
        else:
            for j in list(range(0,found_prepositions[i][1])):
                before_prep_tokens.append(tokens[j])
            before_prep_phrase=convert_token(before_prep_tokens,0,len(before_prep_tokens))
            prep_phrases.append(["",before_prep_phrase,[""]])
        prep_phrase=convert_token(prep_phrase_tokens,0,len(prep_phrase_tokens))
        before_prep_phrase=convert_token(before_prep_tokens,0,len(before_prep_tokens))
        prep_phrases.append([before_prep_phrase,prep_phrase,found_prepositions[i][3:]])

    count=0
    for phrase in prep_phrases:
        if count==0:
            check_non_prep_role(phrase,is_predicate)
        else:
            check_prep_role(phrase)
        count+=1
    print(prep_phrases)
    return prep_phrases

#tokenize("Are you contacting teacher of the class after eating in cafe at 1:20 pm along with him?")
