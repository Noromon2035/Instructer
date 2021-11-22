#main program
from numpy import rint
import grammar_checker
import voice_checker_spaCy
import tokenizer

def main():
    text = 'Let the gmes be plays my with sister.'
    grammatically_checked = grammar_checker.check(text)
    tokens = tokenizer.convert(grammatically_checked)
    voice_checked = voice_checker_spaCy.check(grammatically_checked, tokens)
    print(voice_checked) 

if __name__ == "__main__":
    main()