print("Importing spacy")
import spacy
from spacy.tokenizer import Tokenizer
from spacy.lang.char_classes import ALPHA, ALPHA_LOWER, ALPHA_UPPER, CONCAT_QUOTES, LIST_ELLIPSES, LIST_ICONS
from spacy.util import compile_infix_regex

print("Importing kivy")
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.clipboard import Clipboard
from printers import instruction_printer
import re
 
Config.set('graphics', 'resizable', True)
Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '707')

class StartUpWindow(Screen):
    
    def on_enter(self, *args):
        Clock.schedule_once(self.change,2)
    
    def on_pre_leave(self, *args):
        pass    
    def change(self,dt):
        sm.current="main"

    """ def load(self):
        from analyzer import Analyzer
        from checkers import spell_checker
        from tokenizers import pos_tokenizer
        from converters import phrase_simplifier
        from converters import simplifier
        from checkers import grammar_checker_lt"""


class MainWindow(Screen):
    instruction_input=ObjectProperty(None)
    receiver_input = ObjectProperty(None)
    enter_instruction=ObjectProperty(None)

    def check_input(self):
        popup = Popup(title='Missing instruction', content=Label(text='Please type an instruction in the textbox.'),size_hint=(None, None), size=(350, 100), auto_dismiss=True)
        if self.instruction_input.text=="":
            popup.open()
        else:
            popup.dismiss()
            sm.current="loading"
        

class LoadingWindow(Screen):
    status=ObjectProperty(None)
    
    instructions=[]
    questions=[]
    notes=[]
    analyzer=None
    nlp=None
    inst=""
    count=0

    def custom_tokenizer(self,nlp):
        infixes = (
            LIST_ELLIPSES
            + LIST_ICONS
            + [
                r"(?<=[0-9])[+\-\*^](?=[0-9-'])",
                r"(?<=[{al}{q}])\.(?=[{au}{q}])".format(
                    al=ALPHA_LOWER, au=ALPHA_UPPER, q=CONCAT_QUOTES
                ),
                r"(?<=[{a}]),(?=[{a}])".format(a=ALPHA),
                #r"(?<=[{a}])(?:{h})(?=[{a}])".format(a=ALPHA, h=HYPHENS),
                r"(?<=[{a}0-9])[:<>=/](?=[{a}])".format(a=ALPHA),
            ]
        )

        infix_re = compile_infix_regex(infixes)
        exceptions=nlp.Defaults.tokenizer_exceptions
        filtered_exceptions = {k:v for k,v in exceptions.items() if "'" not in k}

        return Tokenizer(nlp.vocab, prefix_search=nlp.tokenizer.prefix_search,
                                    suffix_search=nlp.tokenizer.suffix_search,
                                    infix_finditer=infix_re.finditer,
                                    token_match=nlp.tokenizer.token_match,
                                    rules=filtered_exceptions)

    def print_status(self,text):
        self.status.text=text

    def fix_brackets(self,inst):
        bracket_matches=re.finditer(r"\w[\(\{\[]",inst)
        for match in bracket_matches:
            match_str=match.group()
            replacer="{} {}".format(match_str[0],match_str[1])
            inst=inst.replace(match_str,replacer)
        self.inst=inst

    def load_nlp(self):
        from analyzer import Analyzer
        print("Loading spacy")
        self.analyzer=Analyzer()        
        self.nlp = spacy.load("en_core_web_sm")
        self.nlp.tokenizer = self.custom_tokenizer(self.nlp)

    def check_spelling(self):
        from checkers import spell_checker
        print("checking spelling")
        self.inst=spell_checker.check(self.inst)

    def simplify_phrases(self):
        from tokenizers import pos_tokenizer
        from converters import phrase_simplifier
        from converters import simplifier
        print("Simplifying phrases")
        phrases_simplified=phrase_simplifier.simplify(self.nlp,self.inst)
        __pos=pos_tokenizer.pos_tokenize(self.nlp,phrases_simplified)
        self.inst=simplifier.simplify(self.nlp,__pos)

    def check_grammar(self):
        from checkers import grammar_checker_lt
        print("Checking grammar")
        self.inst=grammar_checker_lt.check(self.inst)

    def analyze(self):
        print("Analyzing")
        if self.receiver=="":
            self.receiver="they"
        try:
            self.questions,self.instructions, self.notes=self.analyzer.analyze(self.nlp,self.inst,self.receiver)
            sm.current="result"
        except:
            self.questions,self.instructions, self.notes=self.analyzer.analyze(self.nlp,"Try again",self.receiver)
            sm.current="error"
    
    def scheduled_analysis(self,dt):
        try:
            if self.count==0:
                self.print_status("Loading spaCy nlp")
            elif self.count==1:
                self.load_nlp()
            elif self.count==2:
                self.print_status("Checking spelling")
            elif self.count==3:
                self.check_spelling()
            elif self.count==4:
                self.print_status("Simplifying phrases")
            elif self.count==5:
                self.simplify_phrases()
            elif self.count==6:
                self.print_status("Checking grammar")
            elif self.count==7:
                self.check_grammar()
            elif self.count==8:
                self.print_status("Finalizing analysis")
            elif self.count==9:
                self.analyze()
            self.count+=1
        except:
            sm.current="error"

    def on_enter(self, *args):
        self.inst=sm.get_screen("main").instruction_input.text
        self.receiver=sm.get_screen("main").receiver_input.text
        self.count=0
        self.fix_brackets(self.inst)
        Clock.schedule_interval(self.scheduled_analysis,0.1)
        


class ResultWindow(Screen):
    result_output=ObjectProperty(None)
    notes_output=ObjectProperty(None)
    answers_input=ObjectProperty(None)
    question_title=ObjectProperty(None)

    index=0
    q_length=0
    notes_index=0
    res_inst=[]
    res_insts_quest=[]
    res_insts_answers=[]
    res_notes=[]
    res_notes_answers=[]

    def print_instruction(self,questions,answers,instruction):
        result=instruction_printer.print_inst(questions,answers,instruction)
        result=re.sub(r"\^.+\^","",result)
        return result
    
    def print_notes(self,notes,answers):
        result="\nNote: "
        ans_count=0
        for i in list(range(0,len(notes))):
            answer_raw=answers[i+self.notes_index]
            if answer_raw!="":
                if ans_count==0:
                    note=notes[i]["first"]
                    question=re.search(r"\^.+\^",note).group()
                    answer="^{}^{}".format(question[1:-1],answer_raw)
                    note=re.sub(r"\^.+\^\w*",answer,note)
                    result+=note
                    ans_count+=1
                else:
                    note=notes[i]["later"]
                    question=re.search(r"\^.+\^",note).group()
                    answer="^{}^{}".format(question[1:-1],answer_raw)
                    note=re.sub(r"\^.+\^\w*",answer,note)
                    result+=note
                    ans_count+=1 
                result=re.sub(r"\^.+\^","",result)    
        if result=="\nNote: ":
            return ""
        else:
            return result
        
    
    def on_pre_enter(self, *args):
        try:
            self.answers_input.text=""
            self.result_output.text=""
            self.notes_output.text=""

            self.res_insts=sm.get_screen("loading").instructions
            self.res_insts_quests=sm.get_screen("loading").questions
            self.res_notes=sm.get_screen("loading").notes

            self.notes_index=len(self.res_insts_quests)
            self.res_insts_quests.extend([x["question"] for x in self.res_notes])

            self.q_length=len(self.res_insts_quests)
            self.index=0 if self.q_length>0 else -1
            self.res_insts_answers=["" for i in list(range(0,self.q_length))]

            self.question_title.text="QUESTION 1/{}".format(self.q_length) if self.index >-1 else "NO QUESTIONS NEEDED"
            Clock.schedule_interval(self.input_update,0.5)
            Clipboard.copy(self.result_output.text)
        except Exception as e:
            print(e)
            sm.current="error"
            pass

    def input_update(self,dt):
        try:
            if len(self.res_insts_answers)>0:
                answer=self.answers_input.text
                self.res_insts_answers[self.index]=re.sub("\\\\","",answer)
                self.notes_output.text=self.res_insts_quests[self.index]
            instruction=self.print_instruction(self.res_insts_quests,self.res_insts_answers,self.res_insts) + self.print_notes(self.res_notes,self.res_insts_answers)
            self.result_output.text=instruction 
        except:
            sm.current="error"

    def copy(self):
        Clipboard.copy(self.result_output.text)

    def next_inst(self):
        if self.q_length<=0:
            return

        self.index+=1
        if self.index >= self.q_length:
            self.index=0
        self.notes_output.text=self.res_insts_quests[self.index]
        self.answers_input.text=self.res_insts_answers[self.index]
        self.question_title.text="QUESTION {}/{}".format(self.index+1,self.q_length)

    def previous_inst(self):
        if self.q_length<=0:
            return

        self.index-=1
        if self.index < 0:
            self.index=self.q_length-1
        self.notes_output.text=self.res_insts_quests[self.index]
        self.answers_input.text=self.res_insts_answers[self.index]
        self.question_title.text="QUESTION {}/{}".format(self.index+1,self.q_length)


class ErrorWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv=Builder.load_file("instructer_kivy_v2.kv")
sm=WindowManager()
screens=[StartUpWindow(name="startup"),MainWindow(name="main"),LoadingWindow(name="loading"),ResultWindow(name="result"),ErrorWindow(name="error")]
for screen in screens:
    sm.add_widget(screen)


class Instructer(App):
    def build(self):
        return sm
    
if __name__ == "__main__":
    Instructer().run()


#outside functions
def change_max(max):
    sm.get_screen("loading").change_max(max) 
def update_progress(increment):
    sm.get_screen("loading").update_progress(increment)
def max_progress(increment):
    sm.get_screen("loading").max_progress()