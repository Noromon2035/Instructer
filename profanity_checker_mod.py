print("Importing " + __file__)
from profanity_filter import ProfanityFilter
print("Finished importing " + __file__)

pf = ProfanityFilter()


def check(text):
    if pf.is_clean(text) == True:
        print("No profanity detected.")
        return True
    else:
        print("Please remove any profanity detected.\n" + pf.censor(text))
        return False

