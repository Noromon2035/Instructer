from tokenizers import pos_tokenizer


non_clause_seperators=("and","or",",",".")
clause_seperators=(".",",",";","!")
temp_clauses=[]
result={}

def conj_index_processor(conj_index, pos):

    resulting_clauses=[]

    for i in list(range(0, len(conj_index))):
        temp_next_clause=[]
        temp_prev_clause=[]
        temp_indexes=[]
        temp_pos=pos[conj_index[i]]
        temp_center_index=0

        #remove all and/or/,/./
        for j in list(range(0,len(conj_index))):
            is_seperator=True
            if j == i or (pos[conj_index[j]][0] not in non_clause_seperators):
                temp_indexes.append(conj_index[j])

        temp_center_index=temp_indexes.index(conj_index[i])  
        if temp_center_index-1 >=0:
            for j in list(range(temp_indexes[temp_center_index-1], temp_indexes[temp_center_index])):
                temp_prev_clause.append(pos[j])
        else:
            for j in list(range(0, temp_indexes[temp_center_index])):
                temp_prev_clause.append(pos[j])
        if temp_center_index+1 < len(temp_indexes):
            temp_pos=pos[temp_indexes[temp_center_index+1]]
            if temp_pos[2]=="RB" or temp_pos[0] in clause_seperators:
                for j in list(range(temp_indexes[temp_center_index], len(pos))):
                    temp_next_clause.append(pos[j])
            else:
                for j in list(range(temp_indexes[temp_center_index], temp_indexes[temp_center_index+1])):
                    temp_next_clause.append(pos[j])
        else:
            for j in list(range(temp_indexes[temp_center_index], len(pos))):
                temp_next_clause.append(pos[j])

        #check if there's a verb before and after clauses
        vb_in_prev=False
        vb_in_next=False
        for token in temp_prev_clause:
            if token[1]=="VERB" or token[1]=="AUX":
                vb_in_prev=True
                break
        if vb_in_prev==True:
            for token in temp_next_clause:
                if token[1]=="VERB" or token[1]=="AUX":
                    vb_in_next=True
                    if temp_prev_clause not in resulting_clauses:
                        resulting_clauses.append(temp_prev_clause)
                    if temp_next_clause not in resulting_clauses:
                        resulting_clauses.append(temp_next_clause)
                    print("Index: " + str(conj_index[i]))
                    break

    print("\nClauses were found: ")
    for clause in resulting_clauses:
        print(clause)
    if resulting_clauses ==[]:
        return [pos]
    else:
        return resulting_clauses
                
def process_clause(conj_index,conj_index_consecutive, pos):

    resulting_clauses=[]
    legit_prep_indices=[]

    for i in list(range(0, len(conj_index))):
        temp_next_clause=[]
        temp_prev_clause=[]
        temp_indexes=[]
        temp_pos=pos[conj_index[i]]
        temp_center_index=0

        #remove all and/or/,/./
        for j in list(range(0,len(conj_index))):
            if len(conj_index_consecutive[j][1])>1:
                    temp_indexes.append(conj_index[j])
            elif j == i or pos[conj_index[j]][0] not in non_clause_seperators:
                temp_indexes.append(conj_index[j])
        
        temp_center_index=temp_indexes.index(conj_index[i])  

        if temp_center_index-1 >=0:
            for j in list(range(temp_indexes[temp_center_index-1], temp_indexes[temp_center_index])):
                temp_prev_clause.append(pos[j])
        else:
            for j in list(range(0, temp_indexes[temp_center_index])):
                temp_prev_clause.append(pos[j])
        if temp_center_index+1 < len(temp_indexes):
            temp_pos=pos[temp_indexes[temp_center_index+1]]
            if temp_pos[2]=="RB" or temp_pos[0] in clause_seperators:
                for j in list(range(temp_indexes[temp_center_index], len(pos))):
                    temp_next_clause.append(pos[j])
            else:
                for j in list(range(temp_indexes[temp_center_index], temp_indexes[temp_center_index+1])):
                    temp_next_clause.append(pos[j])
        else:
            for j in list(range(temp_indexes[temp_center_index], len(pos))):
                temp_next_clause.append(pos[j])

        #check if there's a verb before and after clauses
        vb_in_prev=False
        for token in temp_prev_clause:
            if token[1]=="VERB" or token[1]=="AUX":
                vb_in_prev=True
                break
        if vb_in_prev==True:
            for token in temp_next_clause:
                if token[1]=="VERB" or token[1]=="AUX":
                    legit_prep_indices.append(conj_index[i])
                    print("Index: " + str(conj_index[i]))
                    break
    
    next_index=0
    for i in list(range(0,len(legit_prep_indices))):
        index=legit_prep_indices[i]
        if i+1<len(legit_prep_indices):
            next_index=legit_prep_indices[i+1]
        else:
            next_index=len(pos)-1
        if i==0:
            resulting_clauses.append(pos[0:index])
            resulting_clauses.append(pos[index:next_index])    
        else:
            resulting_clauses.append(pos[index:next_index])
    print("\nClauses were found: ")
    if resulting_clauses ==[]:
        return [pos]
    else:
        return resulting_clauses

def tokenize(text, pos):
    __pos=pos
    __clauses=[]
    __conj_index=[]

    #First find all clause seperators
    for i in list(range(0, len(__pos))):
        if __pos[i][1]=="CCONJ" or __pos[i][1]=="SCONJ" or __pos[i][0] in clause_seperators or __pos[i][2]=="RB":
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
        if count>1:
            while count >1:
                consecutive_indeces.add(index+count-1)
                consecutive.append(index+count-1)
                count-=1
        if index not in consecutive_indeces:
            result_indeces_w_consecutive.append([index,consecutive])
        current+=1
    result_indices=[x for x in __conj_index if x not in consecutive_indeces]
    __clauses=process_clause(result_indices,result_indeces_w_consecutive, __pos)
    print(__clauses)
    return __clauses

