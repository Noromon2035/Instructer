try:
    import spacy
    from spacy.matcher import Matcher
except Exception as e:
    print(e)
    
nlp = spacy.load("en_core_web_sm")

def match(text, pattern):
    matcher = Matcher(nlp.vocab)
    #pattern [{:},{:}]
    matcher.add("matcher", pattern)
    doc = nlp(text)
    matches = matcher(doc, as_spans=True)
    for span in matches:
        print(span.text)
    return matches