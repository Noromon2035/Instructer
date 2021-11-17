#main program
import grammar_checker
import voice_checker_spaCy

if __name__ == "__main__":
    text = 'Let the gmes be plays my with sister.'
    grammatically_checked = grammar_checker.check(text)
    voice_checked = voice_checker_spaCy.check(grammatically_checked)
    print(voice_checked) 