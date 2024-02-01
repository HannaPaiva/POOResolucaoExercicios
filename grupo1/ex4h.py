# Definir o vetor v
v = list(range(50))

print("Os primeiros 10 elementos:", v[:10])

print("Os últimos 10 elementos:", v[-10:])

print("Valores entre a posição 10 e 20:", v[10:21])

del v[5]
print("Vetor após apagar o número na posição 5:", v)

v.remove(20)
print("Vetor após apagar o número 20:", v)

print("Números por ordem inversa:", v[::-1])

conjunto_letras = ['a', 'b', 'c']
v.extend(conjunto_letras)

print("União com o conjunto ['a', 'b', 'c']:", v)
