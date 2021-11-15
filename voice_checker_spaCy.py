import spacy
nlp = spacy.load("en_core_web_sm")
text = '''Washing your hands is easy, and it’s one of the most effective ways to prevent the spread of germs. Clean hands can stop germs from spreading from one person to another and throughout an entire community—from your home and workplace to childcare facilities and hospitals.
Follow these five steps every time.
Wet your hands with clean, running water (warm or cold), turn off the tap, and apply soap.
Lather your hands by rubbing them together with the soap. Lather the backs of your hands, between your fingers, and under your nails.
Scrub your hands for at least 20 seconds. Need a timer? Hum the “Happy Birthday” song from beginning to end twice.
Rinse your hands well under clean, running water.
Dry your hands using a clean towel or air dry them.'''

doc = nlp(text)
for token in doc:
    print (token.text, token.pos_, token.tag_)