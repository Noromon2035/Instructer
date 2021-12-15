print("Importing " + __file__)
import sentence_tokenizer
import pos_tokenizer
print("Finished importing " + __file__)

def convert(text):
    __sentences=[]
    __sentences=sentence_tokenizer.convert(text)
    print("\n\n\n\n\n")
    for sentence in __sentences:
        print(pos_tokenizer.tokenize(sentence))



convert("First, the big bad talking wolf's brother is tasked to bring the little dogs and pigs then he and she is eating, but it failed.")