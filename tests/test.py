from gensim.models import KeyedVectors
wordvec = KeyedVectors.load("instruct_vector.wordvectors", mmap='r')

results=wordvec.most_similar("eating",topn=20)
for result in results:
    print(result)