# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro
# entre 1 a 10. O utilizador deve informar qual número de que deseja ver a tabuada.
while True:

    while True:
        try:
            numero = int(input(" Insira um número inteiro entre 0 e 10 para calcular a tabuada "))
        
            break

        except:
            print("Número inválido")



    if numero not in range(0, 10 + 1):
        print()
        print("O número precisa estar entre 0 e 10")
        print()
    else:
        for contador in range (0, 11):
            print (f"{numero} * {contador } = {numero*contador}")
        break