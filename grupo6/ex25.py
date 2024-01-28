import math

def calcular_raiz_quadrada():
    while True:
        try:
            numero = float(input("Digite um número para calcular a sua raiz quadrada: "))
            if numero < 0:
                raise ValueError("Não é possível calcular a raiz quadrada de um número negativo.")
            resultado = math.sqrt(numero)

            print(f"A raiz quadrada de {numero} é {resultado}.")
            break
        except ValueError as ve:
            print(f"Erro: {ve}")

        except Exception as e:
            print(f"Erro inesperado: {e}")

def calcular_divisao():
    while True:
        try:
            numerador = int(input("Digite o numerador (número inteiro): "))
            denominador = int(input("Digite o denominador (número inteiro diferente de zero): "))
            if denominador == 0:
                raise ValueError("O denominador não pode ser zero.")
            resultado = numerador / denominador
            print(f"O resultado da divisão de {numerador} por {denominador} é {resultado}.")
            break


        except ValueError as ve:
            print(f"Erro: {ve}")

        except ZeroDivisionError:

            print("Erro: Divisão por zero.")
        except Exception as e:

            print(f"Erro inesperado: {e}")

def guardar_quarto_nome():

    nome_completo = input("Digite o seu nome completo: ")
    lista_nomes = nome_completo.split()

    quarto_nome = lista_nomes[3] if len(lista_nomes) > 3 else "Não tem quarto nome"
    print(f"O quarto nome é: {quarto_nome}")

def encontrar_carater():
    frase = "complementos de programacao"
    while True:
        try:
            posicao = int(input(f"Digite a posição (entre 0 e {len(frase)-1}) para encontrar o caractere na frase: complementos de programacao:  "))
            if posicao < 0 or posicao >= len(frase):
                raise ValueError("Posição fora do intervalo válido.")
            caractere = frase[posicao]
            print(f"O caractere na posição {posicao} é '{caractere}'.")
            break
        except ValueError as ve:
            print(f"Erro: {ve}")
        except Exception as e:
            print(f"Erro inesperado: {e}")

def main():
    calcular_raiz_quadrada()
    calcular_divisao()
    guardar_quarto_nome()
    encontrar_carater()

if __name__ == "__main__":
    main()
