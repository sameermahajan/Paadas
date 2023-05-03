import kivy
from kivy.app import App
from kivy.core.audio import SoundLoader
import random
from playsound import playsound
from kivy.uix.textinput import TextInput

class Paadas(App):
    def build(self):
        while True:
            number = random.randint(1,10)
            times = random.randint(1,10)
            sound = SoundLoader.load("numbers/" + str(number) + ".wav")
            if sound:
                sound.play()
            sound = SoundLoader.load("times/" + str(times) + ".wav")
            if sound:
                sound.play()

            # listen to the answer
            answer = TextInput(focus=True)

            # check answer
            product = number * times

            if answer == str(product):
                sound = SoundLoader.load("prompt/correct.wav")
                if sound:
                    sound.play()
            else:
                sound = SoundLoader.load("prompt/incorrect.wav")
                if sound:
                    sound.play()
                print(answer)
                sound = SoundLoader.load("numbers/" + answer + ".wav"
                if sound:
                    sound.play()
                sound = SoundLoader.load("prompt/incorrect.wav")
                if sound:
                    sound.play()

if __name__ == '__main__':
    Paadas().run()
