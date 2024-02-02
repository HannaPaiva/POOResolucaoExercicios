from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label


class BoxC(BoxLayout):
    def __init__(self, **kwargs):
        super(BoxC, self).__init__(orientation='vertical', **kwargs)

        self.text_input1 = TextInput(hint_text='Texto 1')
        self.text_input2 = TextInput(hint_text='Texto 2')
        self.label_result = Label(text='Resultado:', color=(1, 0, 0, 1))  

        self.add_widget(self.text_input1)
        self.add_widget(self.text_input2)
        self.add_widget(self.label_result)

        self.text_input1.bind(text=self.update_label)
        self.text_input2.bind(text=self.update_label)

    def update_label(self, instance, value):
        text1 = self.text_input1.text
        text2 = self.text_input2.text

        if text1 == text2[::-1]:
            self.label_result.text = 'Textos inversos'
            self.label_result.color = (0, 1, 0, 1)  # Cor verde
        else:
            self.label_result.text = 'Textos não inversos'
            self.label_result.color = (1, 0, 0, 1)  # Cor vermelha


class TextApp(App):
    def build(self):
        # Criando a interface principal
        box_c = BoxC()

    
        root = box_c

        return root


if __name__ == '__main__':
    TextApp().run()
