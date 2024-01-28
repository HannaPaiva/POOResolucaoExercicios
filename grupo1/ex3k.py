# Função para gerar a série de Fibonacci até o n-ésimo termo
def fibonacci(n):
    serie = [1, 1]

    while len(serie) < n:
        termo_atual = serie[-1] + serie[-2]
        serie.append(termo_atual)

    return serie[:n]

# # Programa principal
# if __name__ == "__main__":
try:
    n = int(input("Digite o número de termos desejado na série de Fibonacci: "))
    if n <= 1:
        raise ValueError("O número de termos deve ser acima de 1.")
except:
    print(f"Insira algo válido")

else:
    # Gerar e exibir a série de Fibonacci
    serie_fibonacci = fibonacci(n)
    print(f"Série de Fibonacci até o {n}-ésimo termo: {serie_fibonacci}")
