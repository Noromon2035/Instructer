#main program
import profanity_checker_mod
import grammar_checker_lt
import voice_checker_spaCy
import tokenizer

__is_clean=False

def main():
    text = 'You closes the door motherfucker'
    grammatically_checked = grammar_checker_lt.check(text)
    __is_clean= profanity_checker_mod.check(grammatically_checked)
    if __is_clean==False:
        return
    tokens = tokenizer.convert(grammatically_checked)
    voice_checked = voice_checker_spaCy.check(grammatically_checked, tokens["pos"])
    print(voice_checked) 

if __name__ == "__main__":
    main()