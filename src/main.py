#main program
from checkers import profanity_checker_mod as profanity_checker_mod
from checkers import grammar_checker_lt  as gcl
from tokenizers import tokenizer as tokenizer
from checkers import voice_checker as vc

__is_clean=False

def main():
    text = 'You closes the door motherfucker'
    grammatically_checked = gcl.check(text)
    __is_clean= profanity_checker_mod.check(grammatically_checked)
    if __is_clean==False:
        return
    tokens = tokenizer.convert(grammatically_checked)
    voice_checked = vc.check(grammatically_checked, tokens["pos"])
    print(voice_checked) 

if __name__ == "__main__":
    main()