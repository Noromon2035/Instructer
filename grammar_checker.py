#Grammarly lite
from gingerit.gingerit import GingerIt

def check(sentence):
    parser = GingerIt()
    result = parser.parse(sentence)
    return result['result']