import re

def print_inst(questions,answers,instructions):
    result=""
    for inst in instructions:
        result+=inst+"\n"
    result=result[0:-1]

    for i in list(range(0,len(questions))):
        answer=answers[i]
        if answer !="":
            answer=" "+answer
        result=re.sub(r"\^{}\^\w*".format(i),"^{}^{}".format(i,answer),result)

    return result


if __name__=="__main__":
    questions=['Who/what should Jomar swallow?',""]
    answers=["banana","fish"]
    instructions=["0. Don't eat^0^. Swallow.",'1. Once it can be safely assumed^1^ that the base of the flour-based cake has reached an acceptable level of cook, firmly grasp handle of your flipping leverage tool with flip-side up.', '2. Throw forward using shoulder, engaging glenohumeral joint (shoulder joint) for smooth motion.', '3. Then swallow^0^.']
    result=print_inst(questions,answers,instructions)
    result=re.sub(r"\^.+\^","",result)
    print(result)