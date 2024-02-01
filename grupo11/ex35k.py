from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
import random

class BoxK(BoxLayout):
    def __init__(self, **kwargs):
        super(BoxK, self).__init__(orientation='vertical', **kwargs)

        self.label_k = Label(text='Número aleatório entre 1 e 100')
        self.number_to_guess = random.randint(1, 100)
        self.masked_number = '*' * len(str(self.number_to_guess))
        self.text_input_guess = TextInput(hint_text='Tenta adivinhar...', password=True)
        self.text_input_guess_result = TextInput(hint_text='Resultado', readonly=True)
        self.button_guess = Button(text='Verificar')

        self.add_widget(self.label_k)
        self.add_widget(self.text_input_guess)
        self.add_widget(self.text_input_guess_result)
        self.add_widget(self.button_guess)

        self.button_guess.bind(on_press=self.check_guess)

    def check_guess(self, instance):
        guess = self.text_input_guess.text
        if guess.isdigit():
            guess = int(guess)
            if guess < self.number_to_guess:
                result = 'Tenta um valor maior'
            elif guess > self.number_to_guess:
                result = 'Tenta um valor menor'
            else:
                result = 'Acertaste'
                self.text_input_guess_result.password = False  # Revelar número
        else:
            result = 'Entrada inválida. Insere um número.'

        self.text_input_guess_result.text = result


class BoxKApp(App):
    def build(self):
        return BoxK()


if __name__ == '__main__':
    BoxKApp().run()
