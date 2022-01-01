from gensim.models import Word2Vec

sentences = [["cat", "say", ""], ["dog", "say", "woof"]]

model = Word2Vec(sentences, min_count=1)
sentences=[["hello","world"]]
model.build_vocab(sentences,update=True)
sentences2=[["academic","integrity"],["cat","food"]]
model.build_vocab(sentences2,update=True)
model.train(sentences,total_examples=model.corpus_count,epochs=model.epochs)


print(len(model.wv))