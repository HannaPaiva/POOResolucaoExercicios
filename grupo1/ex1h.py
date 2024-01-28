# Fórmula de conversão de Fahrenheit pra Celsius
# Celsius = (Fahrenheit - 32) * 5/9

def fahrenheit_para_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius


def obter_temperatura():
    while True:
        try:
            fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
            return fahrenheit
        except:
            print("Por favor, digite um número válido.")


temperatura_fahrenheit = obter_temperatura()

temperatura_celsius = fahrenheit_para_celsius(temperatura_fahrenheit)

# Exibir o resultado
print(f"{temperatura_fahrenheit} Fahrenheit é igual a {temperatura_celsius:.2f} Celsius.")
