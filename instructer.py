#main program
import grammar_checker

if __name__ == "__main__":
    text = 'The smelt of fliwers bring back momories.'
    result = grammar_checker.check(text)
    print(result) 