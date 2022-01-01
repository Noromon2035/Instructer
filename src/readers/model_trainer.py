from gensim.models import Word2Vec
from nltk.corpus import brown
from nltk.corpus import stopwords
from string import punctuation
import pprint as pp
import re

sw = stopwords.words('english')

def train(corpus,model_name):
    vec=Word2Vec([["academic","integrity"]],min_count=1)
    count=0
    max=0
    with open(corpus, 'r') as mv1:
        lines=mv1.readlines()
        max=len(lines)
        print(max)

   
    #divide vocab
    for i in list(range(0,len(lines),100000)):
        after=0
        sents=[]
        after=i+100000
        if after>len(lines):
            after=len(lines)
        print("\n\nExtracting sentences from text file...")
        for line in lines[i:after]:
            temp_sent=re.split(" ",line)
            sents.append(temp_sent)
            print(str(count) + "/" + str(max))
            count+=1
        print("\n\nFinished extracting sentences from text\n\n")
        vocab = [[w.lower() for w in s if w not in punctuation and w not in sw and w!="\n"] for s in sents]
        print("Finished reading brown vocabulary")
        
        print("Training {} chunck...".format(after))

        print("Training model...")
        print(len(vec.wv))
        vec.min_count=1
        vec.build_vocab(vocab,update=True)
        vec.train(vocab,total_examples=vec.corpus_count,epochs=vec.epochs)

    vec.save(model_name)
    print("Saved!")

def train_brown():
    print("Extracting sentences from brown...")
    brown_sents = brown.sents()
    print("Finished extracting sentences from brown")
    sw = stopwords.words('english')
    brown_vocab = [[w.lower() for w in s if w not in punctuation and w not in sw] for s in brown_sents]
    print("Finished reading brown vocabulary")
    print("Training model...")
    brown_vec=Word2Vec.load("instruct_vec.model")
    brown_vec.train(brown_vocab,total_examples=len(brown_vocab),epochs=5)
    print("Finished....")
    brown_vec.save("instruct_vec.model")
    print("Saved!")

def find_similarity(word1,word2):
    model=Word2Vec.load("instruct_model.model")
    vector=model.wv
    vector.save("instruct_vector.wordvectors")
    try:
        sims = model.wv.similarity(word1,word2)
    except:
        sims=-1
    print("\n\nSimilarity between {} and {}:".format(word1,word2))
    print(sims)

#train("model-vocab-1.txt","instruct_model.model")
find_similarity("light","white")
find_similarity("eat","food")