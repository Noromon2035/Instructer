print("Importing " + __file__)
import sentence_tokenizer
print("Finished importing " + __file__)

def convert(text):
    __sentences=[]
    __sentences=sentence_tokenizer.convert(text)

convert("The big bad talking wolf's brother is tasked to bring the little dogs and pigs while he and she is eating, but it failed.")