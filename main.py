import kivy
from kivy.app import App
from kivy.core.audio import SoundLoader
import random
from playsound import playsound
from kivy.uix.textinput import TextInput
import time

class Paadas(App):
    def pose_a_problem(self):
        self.number = random.randint(1,10)
        self.times = random.randint(1,10)
        sound = SoundLoader.load("numbers/" + str(self.number) + ".wav")
        if sound:
            sound.play()
        else:
            print("Could not load audio for ", self.number)
        time.sleep(1)
        sound = SoundLoader.load("times/" + str(self.times) + ".wav")
        if sound:
            sound.play()
        else:
            print("Could not load audio for ", self.times)
        time.sleep(1)

    def on_enter(self, value):
        print('instance: ', self, 'value.text: ', value.text)

        # check answer

        product = self.number * self.times
        print("product: ", product)

        if value.text == str(product):
            sound = SoundLoader.load("prompt/correct.wav")
            if sound:
                sound.play()
            time.sleep(1)
        else:
            sound = SoundLoader.load("prompt/incorrect.wav")
            if sound:
                sound.play()
            time.sleep(1)
            print(value.text)
            sound = SoundLoader.load("numbers/" + value.text + ".wav")
            if sound:
                sound.play()
            time.sleep(1)
            sound = SoundLoader.load("prompt/incorrect.wav")
            if sound:
                sound.play()
            time.sleep(1)

        # revise the problem

        sound = SoundLoader.load("numbers/" + str(self.number) + ".wav")
        if sound:
            sound.play()
        time.sleep(1)
        sound = SoundLoader.load("times/" + str(self.times) + ".wav")
        if sound:
            sound.play()
        time.sleep(1)
        sound = SoundLoader.load("numbers/" + str(product) + ".wav")
        if sound:
            sound.play()
        time.sleep(2)

        # clear answer
        self.answer.text = ''
        self.pose_a_problem()

    def build(self):
        self.pose_a_problem()
 
        # listen to the answer
        self.answer = TextInput(text='', multiline=False)
        self.answer.bind(on_text_validate=self.on_enter)
        return self.answer    

if __name__ == '__main__':
    Paadas().run()