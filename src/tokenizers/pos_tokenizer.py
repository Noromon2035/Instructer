try:
    import spacy
    from spacy.tokenizer import Tokenizer
    from spacy.lang.char_classes import ALPHA, ALPHA_LOWER, ALPHA_UPPER, CONCAT_QUOTES, LIST_ELLIPSES, LIST_ICONS
    from spacy.util import compile_infix_regex
except Exception as e:
    print(e)

def custom_tokenizer(nlp):
    infixes = (
        LIST_ELLIPSES
        + LIST_ICONS
        + [
            r"(?<=[0-9])[+\-\*^](?=[0-9-'])",
            r"(?<=[{al}{q}])\.(?=[{au}{q}])".format(
                al=ALPHA_LOWER, au=ALPHA_UPPER, q=CONCAT_QUOTES
            ),
            r"(?<=[{a}]),(?=[{a}])".format(a=ALPHA),
            #r"(?<=[{a}])(?:{h})(?=[{a}])".format(a=ALPHA, h=HYPHENS),
            r"(?<=[{a}0-9])[:<>=/](?=[{a}])".format(a=ALPHA),
        ]
    )

    infix_re = compile_infix_regex(infixes)
    exceptions=nlp.Defaults.tokenizer_exceptions
    filtered_exceptions = {k:v for k,v in exceptions.items() if "'" not in k}

    return Tokenizer(nlp.vocab, prefix_search=nlp.tokenizer.prefix_search,
                                suffix_search=nlp.tokenizer.suffix_search,
                                infix_finditer=infix_re.finditer,
                                token_match=nlp.tokenizer.token_match,
                                rules=filtered_exceptions)

nlp = spacy.load("en_core_web_sm")
nlp.tokenizer = custom_tokenizer(nlp)

def tokenize(text):
    __doc = nlp(text)
    return __doc

def pos_tokenize(text):
    __pos=[]
    __doc = nlp(text)
    for token in __doc:
        __pos.append([token.text, token.pos_, token.tag_,token.lemma_])
    return __pos