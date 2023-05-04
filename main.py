import kivy
from kivy.app import App
from kivy.core.audio import SoundLoader
import random
from playsound import playsound
from kivy.uix.textinput import TextInput

number = 0
times = 0

class Paadas(App):
    def pose_a_problem(self):
        number = random.randint(1,10)
        times = random.randint(1,10)
        sound = SoundLoader.load("numbers/" + str(number) + ".wav")
        if sound:
            sound.play()
        sound = SoundLoader.load("times/" + str(times) + ".wav")
        if sound:
            sound.play()

    def on_enter(self, value):
        print('instance: ', self, 'value.text: ', value.text)

        # check answer

        product = number * times

        if value.text == str(product):
            sound = SoundLoader.load("prompt/correct.wav")
            if sound:
                sound.play()
        else:
            sound = SoundLoader.load("prompt/incorrect.wav")
            if sound:
                sound.play()
            print(value.text)
            sound = SoundLoader.load("numbers/" + value.text + ".wav")
            if sound:
                sound.play()
            sound = SoundLoader.load("prompt/incorrect.wav")
            if sound:
                sound.play()
        self.pose_a_problem()

    def build(self):
        self.pose_a_problem()
 
        # listen to the answer
        answer = TextInput(text='', multiline=False)
        answer.bind(on_text_validate=self.on_enter)
        return answer    

if __name__ == '__main__':
    Paadas().run()
