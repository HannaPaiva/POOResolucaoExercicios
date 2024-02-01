from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox

class BoxI(BoxLayout):
    def __init__(self, **kwargs):
        super(BoxI, self).__init__(orientation='vertical', **kwargs)

        self.label_i = Label(text='Se a checkbox estiver checada, conta reverso. Se não estiver, conta normal')
        self.text_input_i = TextInput(hint_text='0', readonly=True)
        self.checkbox_i = CheckBox(active=False)
        self.button_i = Button(text='Incrementar')

        self.add_widget(self.label_i)
        self.add_widget(self.text_input_i)
        self.add_widget(self.checkbox_i)
        self.add_widget(self.button_i)

        self.button_i.bind(on_press=self.increment_counter)

    def increment_counter(self, instance):
        if self.checkbox_i.active:
            current_value = int(self.text_input_i.text) if self.text_input_i.text else 0
            self.text_input_i.text = str(current_value - 1)
        else:
            current_value = int(self.text_input_i.text) if self.text_input_i.text else 0
            self.text_input_i.text = str(current_value + 1)


class BoxIApp(App):
    def build(self):
        return BoxI()


if __name__ == '__main__':
    BoxIApp().run()
