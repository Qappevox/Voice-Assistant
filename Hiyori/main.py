#using python 3.6.8
#created by Qappevox
#date: 16.02.2022

try:
    #kivy imports
    from kivy.uix.boxlayout import BoxLayout
    import kivy
    from kivymd.app import MDApp

    #Hiyori imports
    import datetime
    from datetime import datetime
    import gtts
    from gtts import langs
    import speech_recognition as sr 
    from gtts import gTTS
    from playsound import playsound, PlaysoundException
    import random
    import os
except ModuleNotFoundError:
    print("Modules are not installed")




kivy.require('1.9.0')
r = sr.Recognizer()
langswitch = "en"
htext = "a"


class Hiyori(BoxLayout):

    def __init__(self,mysentence, hsentence):
        super(Hiyori, self).__init__()
       
        self.mysentence = mysentence


        self.hsentence = hsentence




    def listenning(self):

        with sr.Microphone() as source:
            print("Hiyori now listennig")
            audio = r.listen(source)
            print("checkpoint")
            voice = ""
 
            try:
                voice = r.recognize_google(audio, language= "EN-en")

            except sr.UnknownValueError:
                print("system unknown value error--> sentence is not understanding")


            except sr.RequestError:
                print("system request error")
            
            voice = voice.lower()

            self.mysentence = voice

            print(voice)
            
            
            
        return voice






    def condition(self):
        global htext

        if '' in self.mysentence:

            self.hsentence = "i don't understand, could you repeat"   


        if 'hi' in self.mysentence:
            self.hsentence = "hi" 


        if 'how old are you' in self.mysentence:
            self.hsentence = "I'm 20"

        if 'what time is it' in self.mysentence:
        
            self.hsentence = (str(datetime.now().strftime('%H:%M:%S')))


        #You can change dialogs like that:
        """
        if '#keyword' in self.mysentence:

            self.sentence = "#answer"


        """

            
        htext = str(self.hsentence)
        
        self.speaking()
            
        return htext
        






    def speaking(self):
        global htext
        
        print(htext)
  
       
        rand = random.randint(1,10000)
        try:
            tts = gTTS(text = htext, lang = langswitch, slow= False)
            
            file = 'audio-'+str(rand)+'.mp3'

            tts.save(file)

        except AssertionError:
            return False

        try:
            playsound(file)
            os.remove(file)

        except PlaysoundException:
            playsound(file)
            os.remove(file)

        

        return self.hsentence





class HiyoriVoiceAssistant(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Light"  

        self.theme_cls.primary_palette = "Purple"

        return Hiyori("", "")


hiyori= Hiyori("","")

p = HiyoriVoiceAssistant()
p.run()
