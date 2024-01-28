# Definir o vetor v
v = list(range(50))

print("(a) Os primeiros 10 elementos:", v[:10])

print("(b) Os últimos 10 elementos:", v[-10:])

print("(c) Valores entre a posição 10 e 20:", v[10:21])

del v[5]
print("(d) Vetor após apagar o número na posição 5:", v)

v.remove(20)
print("(e) Vetor após apagar o número 20:", v)

print("(f) Números por ordem inversa:", v[::-1])

conjunto_letras = ['a', 'b', 'c']
v.extend(conjunto_letras)

print("(g) União com o conjunto ['a', 'b', 'c']:", v)
