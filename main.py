#import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.clock import Clock
import analyzer
 
Config.set('graphics', 'resizable', True)
Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '707')

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
    resulting_dict=[]
    progress_bar=ObjectProperty(None)

    def on_enter(self, *args):
        inst=sm.get_screen("main").instruction_input.text
        receiver=sm.get_screen("main").receiver_input.text
        print(inst,receiver)
        self.resulting_dict=analyzer.analyze(inst,receiver)
        self.max_progress()
        sm.current="result"


    def change_max(self,max):
        self.progress_bar.max=max
    
    def update_progress(self):
        self.progress_bar.value+=3

    def max_progress(self):
        self.progress_bar.value=self.progress_bar.max

class ResultWindow(Screen):
    result_output=ObjectProperty(None)
    notes_output=ObjectProperty(None)
    
    def on_pre_enter(self, *args):
        try:
            res_dict=sm.get_screen("loading").resulting_dict
            for res in res_dict:
                self.result_output.text+=res["text"]
                if res["questions"]!="":
                    self.notes_output.text+=res["questions"]
            self.result_output.copy(data=self.result_output.text)
        except:
            pass

class WindowManager(ScreenManager):
    pass

sm=WindowManager()
kv=Builder.load_file("instructer_kivy.kv")
screens=[MainWindow(name="main"),LoadingWindow(name="loading"),ResultWindow(name="result")]
for screen in screens:
    sm.add_widget(screen)

class Instructer(App):
    def build(self):
        return sm
    def on_start(self, *args):
        #Clock.schedule_once(self.import_analyzer,5)
        pass

    def import_analyzer(self,*args):
        import analyzer
        sm.current="main"
    
if __name__ == "__main__":
    Instructer().run()


#outside functions
def change_max(max):
    sm.get_screen("loading").change_max(max) 
def update_progress(increment):
    sm.get_screen("loading").update_progress(increment)
def max_progress(increment):
    sm.get_screen("loading").max_progress()