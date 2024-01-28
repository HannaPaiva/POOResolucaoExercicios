# Para criar essa aplicação de encomenda de pizzas, vamos dividir o processo em três partes: a base de dados, o web service e o interface GUI.

# Base de Dados:
# A base de dados deve conter três tabelas: Clientes, Pizzas, e Encomendas. Aqui está a estrutura básica para cada tabela:

# Tabela Clientes:

# idCliente (chave primária)
# nome
# morada
# telefone
# Tabela Pizzas:

# nome (chave primária)
# ingredientes
# imagem (caminho para a imagem ilustrativa)
# Tabela Encomendas:

# idCliente (chave estrangeira referenciando a tabela Clientes)
# Nome (da pizza) (chave estrangeira referenciando a tabela Pizzas)
# quantidade
# tamanho (pequena, média, familiar)
# data/hora
# Web Service:
# O web service irá fornecer endpoints para acessar e manipular os dados da base de dados. Alguns endpoints necessários podem ser:

# GET /clientes: Retorna a lista de clientes.
# GET /pizzas: Retorna a lista de pizzas.
# POST /encomendas: Cria uma nova encomenda.
# GET /encomendas/{idCliente}: Retorna as encomendas de um cliente específico.
# Interface GUI:
# O interface GUI será implementado usando Kivy. Você pode esboçar o interface de acordo com as necessidades do sistema. Aqui estão algumas ideias:

# Uma barra de pesquisa para encontrar clientes por nome facilmente.
# Opções de filtragem para a lista de pizzas, como por ingredientes ou tamanho.
# As pizzas devem ser exibidas com uma imagem ilustrativa, nome e lista de ingredientes.
# Campos para selecionar a quantidade e tamanho da pizza a ser encomendada.
# Um botão para enviar a encomenda.
# Você pode começar desenhando o esboço do interface em papel e lápis, e depois implementá-lo utilizando Kivy, usando Python para interagir com o web service e manipular os dados da base de dados conforme necessário.
# python -m pip install --upgrade pip setuptools virtualenv --user
# python -m venv kivy_venv
# kivy_venv\Scripts\activate
# python -m pip install "kivy[base]" kivy_examples

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class EncomendaPizzaApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        # Campo para inserir o ID do cliente
        layout.add_widget(Label(text='ID do Cliente:'))
        self.id_cliente_input = TextInput(multiline=False)
        layout.add_widget(self.id_cliente_input)
        
        # Campo para inserir o nome da pizza
        layout.add_widget(Label(text='Nome da Pizza:'))
        self.nome_pizza_input = TextInput(multiline=False)
        layout.add_widget(self.nome_pizza_input)
        
        # Campo para inserir a quantidade
        layout.add_widget(Label(text='Quantidade:'))
        self.quantidade_input = TextInput(multiline=False)
        layout.add_widget(self.quantidade_input)
        
        # Campo para inserir o tamanho
        layout.add_widget(Label(text='Tamanho:'))
        self.tamanho_input = TextInput(multiline=False)
        layout.add_widget(self.tamanho_input)
        
        # Campo para inserir a data/hora
        layout.add_widget(Label(text='Data/Hora:'))
        self.data_hora_input = TextInput(multiline=False)
        layout.add_widget(self.data_hora_input)
        
        # Botão para enviar a encomenda
        enviar_button = Button(text='Enviar Encomenda')
        enviar_button.bind(on_press=self.enviar_encomenda)
        layout.add_widget(enviar_button)
        
        return layout
    
    def enviar_encomenda(self, instance):
        id_cliente = self.id_cliente_input.text
        nome_pizza = self.nome_pizza_input.text
        quantidade = self.quantidade_input.text
        tamanho = self.tamanho_input.text
        data_hora = self.data_hora_input.text
        
        # Aqui você pode adicionar a lógica para enviar a encomenda para o web service
        
        # Exibir mensagem de confirmação
        print(f'Encomenda enviada: ID Cliente: {id_cliente}, Pizza: {nome_pizza}, Quantidade: {quantidade}, Tamanho: {tamanho}, Data/Hora: {data_hora}')

if __name__ == '__main__':
    EncomendaPizzaApp().run()
