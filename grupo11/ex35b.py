
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


class BoxB(BoxLayout):
    def __init__(self, **kwargs):
        super(BoxB, self).__init__(orientation='horizontal', **kwargs)
        
        self.text_input1 = TextInput(hint_text='Texto 1')
        self.text_input2 = TextInput(hint_text='Texto 2')
        
        self.add_widget(self.text_input1)
        self.add_widget(self.text_input2)

        self.text_input1.bind(text=self.on_text_invert)

    def on_text_invert(self, instance, value):
        self.text_input2.text = value[::-1]


class TextApp(App):
    def build(self):
        # Criando a interface principal
        box_b = BoxB()

        # Criação da interface final
        root = box_b

        return root


if __name__ == '__main__':
    TextApp().run()
