
non_clause_seperators=("and","or",",",".")
clause_seperators=(".",",",";","!")
temp_clauses=[]
result={}

def process_clause(conj_index,conj_index_consecutive, pos):

    resulting_clauses=[]
    legit_prep_indices=[]
    consecutives=[]

    for i in list(range(0, len(conj_index))):
        temp_next_clause=[]
        temp_prev_clause=[]
        temp_indexes=[]
        temp_pos=pos[conj_index[i]]
        temp_center_index=0

        #remove all and/or/,/./
        for j in list(range(0,len(conj_index))):
            try:
                if len(conj_index_consecutive[j][1])>1:
                        temp_indexes.append(conj_index[j])
                elif j == i or pos[conj_index[j]][0] not in non_clause_seperators:
                    temp_indexes.append(conj_index[j])
                elif (pos[conj_index[j]][0] == "." and pos[conj_index[j]+1][2] == "RB"):
                    temp_indexes.append(conj_index[j])
            except:
                continue
        
        temp_center_index=temp_indexes.index(conj_index[i])  

        #appending previous clause
        if temp_center_index-1 >=0:
            for j in list(range(temp_indexes[temp_center_index-1], temp_indexes[temp_center_index])):
                temp_prev_clause.append(pos[j])
        else:
            for j in list(range(0, temp_indexes[temp_center_index])):
                temp_prev_clause.append(pos[j])

        #appending next clause
        if temp_center_index+1 < len(temp_indexes):
            for j in list(range(temp_indexes[temp_center_index], temp_indexes[temp_center_index+1])):
                temp_next_clause.append(pos[j])
        else:
            for j in list(range(temp_indexes[temp_center_index], len(pos))):
                temp_next_clause.append(pos[j])

        #check if there's a verb before and after clauses
        vb_in_prev=False
        for token in temp_prev_clause:
            if (token[1]=="VERB" and token[0][-3:]!="ing") or token[1]=="AUX":
                vb_in_prev=True
                break
        if vb_in_prev==True:
            count=0
            for token in temp_next_clause:
                if (token[1]=="VERB" and token[0][-3:]!="ing") or token[1]=="AUX":
                    legit_prep_indices.append(conj_index[i])
                    consecutives.append(conj_index_consecutive[i])
                    print("Index: " + str(conj_index[i]))
                    print(temp_indexes)
                    break
                elif count+1<len(temp_next_clause):
                    if token[2]=="RB" and temp_next_clause[count+1][2]=="JJ":
                        legit_prep_indices.append(conj_index[i])
                        consecutives.append(conj_index_consecutive[i])
                        print("Index: " + str(conj_index[i]))
                        print(temp_indexes)
                        break
                count+=1

    #getting all phrases including prepositions seperarted
    next_index=0
    for i in list(range(0,len(legit_prep_indices))):
        index=legit_prep_indices[i]
        if i+1<len(legit_prep_indices):
            next_index=legit_prep_indices[i+1]
        else:
            next_index=len(pos)
        if i==0:
            resulting_clauses.append([[],pos[0:index]])
            try:
                prep_phrase=pos[index:consecutives[i][-1][-1]+1]
                resulting_clauses.append([prep_phrase, pos[consecutives[i][-1][-1]+1:next_index]])
            except:
                prep_phrase=pos[index:index+1]
                resulting_clauses.append([prep_phrase, pos[index+1:next_index]]) 
                
        else:
            try:
                prep_phrase=pos[index:consecutives[i][-1][-1]+1]
                resulting_clauses.append([prep_phrase, pos[consecutives[i][-1][-1]+1:next_index]]) 
            except:
                prep_phrase=pos[index:index+1]
                resulting_clauses.append([prep_phrase, pos[index+1:next_index]]) 
            

    if resulting_clauses ==[]:
        return [["",pos]]
    else:
        return resulting_clauses

def tokenize(text, pos):
    __pos=pos
    __clauses=[]
    __conj_index=[]    

    #First find all clause seperators
    for i in list(range(0, len(__pos))):
        if __pos[i][1]=="CCONJ" or __pos[i][1]=="SCONJ" or __pos[i][0] in clause_seperators:
            __conj_index.append(i)
        elif i==0:
            if (__pos[i][2]=="RB"):
                __conj_index.append(i)
        elif (__pos[i-1][1]=="PUNCT" and __pos[i][2]=="RB"):
            __conj_index.append(i)

    current=0
    consecutive_indeces=set()
    result_indeces_w_consecutive=[]
    for index in __conj_index:
        consecutive=[]
        count=1
        if current+count>=len(__conj_index):
            result_indeces_w_consecutive.append([index,[]])
            continue
        while index+count == __conj_index[current+count]:
            count+=1
            if current+count >= len(__conj_index):
                break
        if count>1:
            while count >1:
                consecutive_indeces.add(index+count-1)
                consecutive.append(index+count-1)
                count-=1
        if index not in consecutive_indeces:
            result_indeces_w_consecutive.append([index,consecutive[::-1]])
        current+=1

    result_indices=[x for x in __conj_index if x not in consecutive_indeces]
    __clauses=process_clause(result_indices,result_indeces_w_consecutive, __pos)

    print("\nClauses were found: ")
    for clause in __clauses:
        print()
        print(clause)
    return __clauses