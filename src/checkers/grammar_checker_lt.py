try:
    import language_tool_python
except Exception as e:
    print(e)
tool = language_tool_python.LanguageTool('en-US')

def check(sentence):
    matches = tool.correct(sentence)
    print("The instructions was grammatically checked.\nResult = " + matches)
    return matches

