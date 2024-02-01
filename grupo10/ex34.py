from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button


class TextApp(App):
    def build(self):
        # (a) Uma caixa de texto
        box_a = BoxLayout(orientation='vertical')
        text_input_a = TextInput(hint_text='Digite algo')
        label_a = Label(text='Texto na consola:')
        box_a.add_widget(text_input_a)
        box_a.add_widget(label_a)

        # (b) Duas caixas de texto
        box_b = BoxLayout(orientation='horizontal')
        text_input_b1 = TextInput(hint_text='Texto 1')
        text_input_b2 = TextInput(hint_text='Texto 2')
        box_b.add_widget(text_input_b1)
        box_b.add_widget(text_input_b2)

        # (c) Duas caixas de texto e um label
        box_c = BoxLayout(orientation='vertical')
        text_input_c1 = TextInput(hint_text='Texto 1')
        text_input_c2 = TextInput(hint_text='Texto 2')
        label_c = Label(text='Resultado:')

        box_c.add_widget(text_input_c1)
        box_c.add_widget(text_input_c2)
        box_c.add_widget(label_c)

        # (d) Uma caixa de texto e um botão
        box_d = BoxLayout(orientation='vertical')
        text_input_d = TextInput(hint_text='Digite algo')
        button_d = Button(text='Copiar para Consola')

        box_d.add_widget(text_input_d)
        box_d.add_widget(button_d)

        # (e) Duas caixas de texto e um botão
        box_e = BoxLayout(orientation='horizontal')
        text_input_e1 = TextInput(hint_text='Esquerda')
        text_input_e2 = TextInput(hint_text='Direita')
        button_e = Button(text='Trocar Texto')

        box_e.add_widget(text_input_e1)
        box_e.add_widget(text_input_e2)
        box_e.add_widget(button_e)

        # (f) Uma caixa de texto e 2 botões
        box_f = BoxLayout(orientation='vertical')
        text_input_f = TextInput(hint_text='Digite algo')
        button_left_f = Button(text='Copiar até Cursor')
        button_right_f = Button(text='Copiar após Cursor')

        box_f.add_widget(text_input_f)
        box_f.add_widget(button_left_f)
        box_f.add_widget(button_right_f)

        # (g) Um label, uma caixa de texto e um botão
        box_g = BoxLayout(orientation='vertical')
        label_g = Label(text='Contador:')
        text_input_g = TextInput(hint_text='0', readonly=True)
        button_g = Button(text='Incrementar')

        box_g.add_widget(label_g)
        box_g.add_widget(text_input_g)
        box_g.add_widget(button_g)

        # Adicionando comportamentos
        self.bind_text_change(text_input_a, label_a)
        self.bind_text_invert(text_input_b1, text_input_b2)
        self.bind_text_compare(text_input_c1, text_input_c2, label_c)
        button_d.bind(on_press=lambda instance: self.copy_to_console(text_input_d.text))
        button_e.bind(on_press=lambda instance: self.swap_text_inputs(text_input_e1, text_input_e2))
        button_left_f.bind(on_press=lambda instance: self.copy_selection(text_input_f, 'left'))
        button_right_f.bind(on_press=lambda instance: self.copy_selection(text_input_f, 'right'))
        button_g.bind(on_press=lambda instance: self.increment_counter(text_input_g))

        # Criação da interface final
        root = BoxLayout(orientation='vertical')
        root.add_widget(box_a)
        root.add_widget(box_b)
        root.add_widget(box_c)
        root.add_widget(box_d)
        root.add_widget(box_e)
        root.add_widget(box_f)
        root.add_widget(box_g)

        return root

    def bind_text_change(self, text_input, label):
        text_input.bind(text=self.on_text_change)
        self.label_console = label

    def on_text_change(self, instance, value):
        self.label_console.text = f'Texto na consola: {value}'

    def bind_text_invert(self, text_input1, text_input2):
        text_input1.bind(text=self.on_text_invert)
        self.text_input2 = text_input2

    def on_text_invert(self, instance, value):
        self.text_input2.text = value[::-1]

    def bind_text_compare(self, text_input1, text_input2, label):
        text_input1.bind(text=self.on_text_compare)
        text_input2.bind(text=self.on_text_compare)
        self.label_compare = label

    def on_text_compare(self, instance, value):
        if value == self.text_input2.text[::-1]:
            self.label_compare.text = 'Textos inversos'
            self.label_compare.color = (0, 1, 0, 1)  # Cor verde
        else:
            self.label_compare.text = 'Textos não inversos'
            self.label_compare.color = (1, 0, 0, 1)  # Cor vermelha

    def copy_to_console(self, text):
        print(f'Texto copiado para a consola: {text}')
        self.root.children[0].children[1].text = ''

    def swap_text_inputs(self, text_input1, text_input2):
        text1 = text_input1.text
        text2 = text_input2.text
        text_input1.text = text2
        text_input2.text = text1

    def copy_selection(self, text_input, direction):
        selection_from, selection_to = text_input.selection_from, text_input.selection_to
        if selection_from is not None and selection_to is not None:
            text = text_input.text[selection_from:selection_to]
            print(f'Texto copiado ({direction}): {text}')

    def increment_counter(self, text_input):
        current_value = int(text_input.text) if text_input.text else 0
        text_input.text = str(current_value + 1)


if __name__ == '__main__':
    TextApp().run()
