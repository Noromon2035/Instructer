#Grammarly lite
from gingerit.gingerit import GingerIt

def check_grammar(sentence):
    parser = GingerIt()
    result = parser.parse(sentence)
    print(result['result'])

text = 'The smelt of fliwers bring back momories.'
check_grammar(text)