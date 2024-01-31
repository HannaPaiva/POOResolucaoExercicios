from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
import requests
import json



# COMANDO Scripts\activate 
class PizzariaApp(App):
    base_url = 'http://127.0.0.1:5000'

    def build(self):
        layout = BoxLayout(orientation='vertical')

        layout.add_widget(Button(text='Cliente', on_press=self.show_cliente_options))
        layout.add_widget(Button(text='Encomenda', on_press=self.show_encomenda_options))
        layout.add_widget(Button(text='Pizza', on_press=self.show_pizza_options))

        return layout

    def show_cliente_options(self, instance):
        content = BoxLayout(orientation='vertical')
        content.add_widget(Button(text='Adicionar Cliente', on_press=self.show_add_cliente_form))
        content.add_widget(Button(text='Listar Clientes', on_press=self.listar_clientes))
        content.add_widget(Button(text='Pesquisar Clientes', on_press=self.pesquisar_clientes))

        popup = Popup(title='Opções de Cliente', content=content, size_hint=(None, None), size=(600, 600))
        popup.open()

    def show_encomenda_options(self, instance):
        content = BoxLayout(orientation='vertical')
        content.add_widget(Button(text='Adicionar Encomenda', on_press=self.show_add_encomenda_form))
        content.add_widget(Button(text='Listar Encomendas', on_press=self.listar_encomendas))
        content.add_widget(Button(text='Pesquisar Encomendas', on_press=self.pesquisar_encomendas))

        popup = Popup(title='Opções de Encomenda', content=content, size_hint=(None, None), size=(600, 600))
        popup.open()

    def show_pizza_options(self, instance):
        content = BoxLayout(orientation='vertical')
        content.add_widget(Button(text='Adicionar Pizza', on_press=self.show_add_pizza_form))
        content.add_widget(Button(text='Listar Pizzas', on_press=self.listar_pizzas))
        content.add_widget(Button(text='Pesquisar Pizzas', on_press=self.pesquisar_pizzas))

        popup = Popup(title='Opções de Pizza', content=content, size_hint=(None, None), size=(600, 600))
        popup.open()

    def show_add_cliente_form(self, instance):
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text='Nome do Cliente:'))
        nome_input = TextInput(multiline=False)
        content.add_widget(nome_input)
        content.add_widget(Label(text='Morada do Cliente:'))
        morada_input = TextInput(multiline=False)
        content.add_widget(morada_input)
        content.add_widget(Label(text='Telefone do Cliente:'))
        telefone_input = TextInput(multiline=False)
        content.add_widget(telefone_input)

        content.add_widget(Button(text='Adicionar Cliente', on_press=lambda x: self.adicionar_cliente(nome_input.text, morada_input.text, telefone_input.text)))

        popup = Popup(title='Adicionar Cliente', content=content, size_hint=(None, None), size=(600, 600))
        popup.open()

    def adicionar_cliente(self, nome, morada, telefone):
        payload = {'nome': nome, 'morada': morada, 'telefone': telefone}
        response = requests.post(f'{self.base_url}/clientes', json=payload)

        if response.status_code == 201:
            print(f'Cliente adicionado: Nome: {nome}, Morada: {morada}, Telefone: {telefone}')
        else:
            print(f'Erro ao adicionar cliente. Código de status: {response.status_code}')

    def listar_clientes(self, instance):
        response = requests.get(f'{self.base_url}/clientes')

        if response.status_code == 200:
            clientes = response.json()
            content = Label(text='\n'.join([f"{cliente['id_cliente']} - {cliente['nome']}" for cliente in clientes]))
            popup = Popup(title='Lista de Clientes', content=content, size_hint=(None, None), size=(600, 600))
            popup.open()
        else:
            print(f'Erro ao obter lista de clientes. Código de status: {response.status_code}')

    def pesquisar_clientes(self, instance):
        pass

    def show_add_encomenda_form(self, instance):
        content = BoxLayout(orientation='vertical')

        # Dropdown para selecionar cliente existente
        content.add_widget(Label(text='Escolha o Cliente:'))
        cliente_dropdown = Spinner(text='Selecione o Cliente', values=self.get_clientes_names(), size_hint=(None, None), size=(200, 44))
        content.add_widget(cliente_dropdown)

        # Dropdown para selecionar pizza existente
        content.add_widget(Label(text='Escolha a Pizza:'))
        pizza_dropdown = Spinner(text='Selecione a Pizza', values=self.get_pizzas_names(), size_hint=(None, None), size=(200, 44))
        content.add_widget(pizza_dropdown)

        content.add_widget(Label(text='Quantidade:'))
        quantidade_input = TextInput(multiline=False)
        content.add_widget(quantidade_input)

        content.add_widget(Label(text='Tamanho:'))
        tamanho_input = TextInput(multiline=False)
        content.add_widget(tamanho_input)

        content.add_widget(Button(text='Adicionar Encomenda', on_press=lambda x: self.adicionar_encomenda(cliente_dropdown.text, pizza_dropdown.text, quantidade_input.text, tamanho_input.text)))

        popup = Popup(title='Adicionar Encomenda', content=content, size_hint=(None, None), size=(600, 600))
        popup.open()

    def adicionar_encomenda(self, cliente, pizza, quantidade, tamanho):
        cliente_id = self.get_cliente_id(cliente)
        pizza_id = self.get_pizza_id(pizza)

        payload = {'id_cliente': cliente_id, 'id_pizza': pizza_id, 'quantidade': quantidade, 'tamanho': tamanho}
        response = requests.post(f'{self.base_url}/encomendas', json=payload)

        if response.status_code == 201:
            print(f'Encomenda adicionada: Cliente ID: {cliente_id}, Pizza ID: {pizza_id}, Quantidade: {quantidade}, Tamanho: {tamanho}')
        else:
            print(f'Erro ao adicionar encomenda. Código de status: {response.status_code}')

    def listar_encomendas(self, instance):
        response = requests.get(f'{self.base_url}/encomendas')

        if response.status_code == 200:
            encomendas = response.json()
            content = Label(text='\n'.join([f"{encomenda['id_encomenda']} - Cliente: {encomenda['cliente_nome']}, Pizza: {encomenda['pizza_nome']}, Quantidade: {encomenda['quantidade']}, Tamanho: {encomenda['tamanho']}, Data/Hora: {encomenda['data_hora']}" for encomenda in encomendas]))
            popup = Popup(title='Lista de Encomendas', content=content, size_hint=(None, None), size=(1000, 1000))
            popup.open()
        else:
            print(f'Erro ao obter lista de encomendas. Código de status: {response.status_code}')

    def pesquisar_encomendas(self, instance):
        pass

    def show_add_pizza_form(self, instance):
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text='Nome da Pizza:'))
        nome_input = TextInput(multiline=False)
        content.add_widget(nome_input)
        content.add_widget(Label(text='Ingredientes da Pizza:'))
        ingredientes_input = TextInput(multiline=False)
        content.add_widget(ingredientes_input)

        content.add_widget(Button(text='Adicionar Pizza', on_press=lambda x: self.adicionar_pizza(nome_input.text, ingredientes_input.text)))

        popup = Popup(title='Adicionar Pizza', content=content, size_hint=(None, None), size=(600, 600))
        popup.open()

    def adicionar_pizza(self, nome, ingredientes):
        payload = {'nome': nome, 'ingredientes': ingredientes}
        response = requests.post(f'{self.base_url}/pizzas', json=payload)

        if response.status_code == 201:
            print(f'Pizza adicionada: Nome: {nome}, Ingredientes: {ingredientes}')
        else:
            print(f'Erro ao adicionar pizza. Código de status: {response.status_code}')

    def listar_pizzas(self, instance):
        response = requests.get(f'{self.base_url}/pizzas')

        if response.status_code == 200:
            pizzas = response.json()
            content = Label(text='\n'.join([f"{pizza['id_pizza']} - {pizza['nome']}" for pizza in pizzas]))
            popup = Popup(title='Lista de Pizzas', content=content, size_hint=(None, None), size=(600, 600))
            popup.open()
        else:
            print(f'Erro ao obter lista de pizzas. Código de status: {response.status_code}')

    def pesquisar_pizzas(self, instance):
        pass

    def get_clientes_names(self):
        response = requests.get(f'{self.base_url}/clientes')

        if response.status_code == 200:
            clientes = response.json()
            return [cliente['nome'] for cliente in clientes]
        else:
            print(f'Erro ao obter lista de clientes. Código de status: {response.status_code}')
            return []

    def get_pizzas_names(self):
        response = requests.get(f'{self.base_url}/pizzas')

        if response.status_code == 200:
            pizzas = response.json()
            return [pizza['nome'] for pizza in pizzas]
        else:
            print(f'Erro ao obter lista de pizzas. Código de status: {response.status_code}')
            return []

    def get_cliente_id(self, nome_cliente):
        response = requests.get(f'{self.base_url}/clientes')

        if response.status_code == 200:
            clientes = response.json()
            for cliente in clientes:
                if cliente['nome'] == nome_cliente:
                    return cliente['id_cliente']
        else:
            print(f'Erro ao obter ID do cliente. Código de status: {response.status_code}')

    def get_pizza_id(self, nome_pizza):
        response = requests.get(f'{self.base_url}/pizzas')

        if response.status_code == 200:
            pizzas = response.json()
            for pizza in pizzas:
                if pizza['nome'] == nome_pizza:
                    return pizza['id_pizza']
        else:
            print(f'Erro ao obter ID da pizza. Código de status: {response.status_code}')

if __name__ == '__main__':
    PizzariaApp().run()
