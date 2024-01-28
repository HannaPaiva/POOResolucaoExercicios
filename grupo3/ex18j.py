from ex18b import Pessoa
from ex18d import Empregado
from ex18f import Operario
from ex18i import Vendedor
from ex18c import Fornecedor

def criar_pessoa():
    nome = input("Nome: ")
    endereco = input("Endereço: ")
    telefone = input("Telefone: ")
    return Pessoa(nome, endereco, telefone)

def criar_empregado():
    pessoa = criar_pessoa()
    codigo_setor = input("Código Setor: ")
    salario_base = float(input("Salário Base: "))
    imposto = float(input("Imposto (%): "))
    return Empregado(pessoa.get_nome(), pessoa.get_endereco(), pessoa.get_telefone(), codigo_setor, salario_base, imposto)

def criar_operario():
    empregado = criar_empregado()
    valor_producao = float(input("Valor Produção: "))
    comissao = float(input("Comissão (%): "))
    return Operario(empregado.get_nome(), empregado.get_endereco(), empregado.get_telefone(), empregado.get_codigo_setor(),
                    empregado.get_salario_base(), empregado.get_imposto(), valor_producao, comissao)

def criar_vendedor():
    empregado = criar_empregado()
    valor_vendas = float(input("Valor Vendas: "))
    comissao = float(input("Comissão (%): "))
    return Vendedor(empregado.get_nome(), empregado.get_endereco(), empregado.get_telefone(), empregado.get_codigo_setor(),
                    empregado.get_salario_base(), empregado.get_imposto(), valor_vendas, comissao)

def criar_fornecedor():
    pessoa = criar_pessoa()
    valor_credito = float(input("Valor Crédito: "))
    valor_divida = float(input("Valor Dívida: "))
    return Fornecedor(pessoa.get_nome(), pessoa.get_endereco(), pessoa.get_telefone(), valor_credito, valor_divida)

def menu():
    while True:
        print("\n1. Criar Operário")
        print("2. Criar Vendedor")
        print("3. Criar Fornecedor")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            operario = criar_operario()
            print("Operário criado:", operario)
        elif opcao == '2':
            vendedor = criar_vendedor()
            print("Vendedor criado:", vendedor)
        elif opcao == '3':
            fornecedor = criar_fornecedor()
            print("Fornecedor criado:", fornecedor)
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
