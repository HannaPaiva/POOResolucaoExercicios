from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class BoxE(BoxLayout):
    def __init__(self, **kwargs):
        super(BoxE, self).__init__(orientation='horizontal', **kwargs)

        self.text_input_left = TextInput(hint_text='Esquerda')
        self.text_input_right = TextInput(hint_text='Direita')
        self.button_swap = Button(text='Trocar Texto')

        self.add_widget(self.text_input_left)
        self.add_widget(self.text_input_right)
        self.add_widget(self.button_swap)

        self.button_swap.bind(on_press=self.swap_text_inputs)

    def swap_text_inputs(self, instance):
        text_left = self.text_input_left.text
        text_right = self.text_input_right.text
        self.text_input_left.text = text_right
        self.text_input_right.text = text_left


class BoxEApp(App):
    def build(self):
        return BoxE()


if __name__ == '__main__':
    BoxEApp().run()
