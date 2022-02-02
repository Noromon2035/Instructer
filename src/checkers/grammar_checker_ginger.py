#Grammarly lite
from gingerit.gingerit import GingerIt

def check(sentence):
    parser = GingerIt()
    result = parser.parse(sentence)
    print("The instructions was grammatically checked.\nResult = " + result['result'])
    return result['result']