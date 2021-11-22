#main program
import grammar_checker
import voice_checker_spaCy
import tokenizer

def main():
    text = 'I mommy see Santa Clause kissing.'
    grammatically_checked = grammar_checker.check(text)
    tokens = tokenizer.convert(grammatically_checked)
    voice_checked = voice_checker_spaCy.check(grammatically_checked, tokens["pos"])
    print(voice_checked) 

if __name__ == "__main__":
    main()