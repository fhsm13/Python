lista_nomes = ['Joao', 'Claudio', 'Fabio', 'Diego']
lista_nomes.append("Geralda")
lista_nomes.remove('Fabio')
lista_nomes.insert(0,'Jose')
contador = lista_nomes.count('Joao')

print(lista_nomes.pop())
print(len(lista_nomes))
print(contador)
print(type(lista_nomes))
print(lista_nomes)