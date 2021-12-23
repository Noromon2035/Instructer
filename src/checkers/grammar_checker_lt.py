print("Importing " + __file__)
import language_tool_python
print("Finished importing " + __file__)

def check(sentence):
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.correct(sentence)
    print("The instructions was grammatically checked.\nResult = " + matches)
    return matches

