try:
    import spacy
except Exception as e:
    print(e)

def match(nlp, text, pattern):
    matcher = spacy.matcher.Matcher(nlp.vocab)
    #pattern [[{:},{:}]]
    matcher.add("matcher", pattern)
    doc = nlp(text)
    matches = matcher(doc, as_spans=True)
    for span in matches:
        print(span.text)
    return matches

if __name__ == "__main__":
    nlp = spacy.load("en_core_web_sm")
    match(nlp,"I am me",[[{"POS":"PRON"}]])