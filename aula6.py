'''Tupla não é mutável como a lista é (não existem métodos na mesma) - list
Se usa quando tem um número limitado de itens, ou seja quando é imutável também, boa pra usar em páginas estáticas de formulário - tuple
Diciionario funciona como um o próprio nome diz - chave / valor (key and value), objeto JSON bem parecido com a dinâmica do JAVA pode conhecer como hashmap ou hashtable - dict
conjunto é parecido com dicionário, conjunto não tem dados repetidos, conjunto nâo é ordenado - nâo existe isso nâo tem índice - set'''

'''tupla tem poucos métodos, e não aceita substituição de métodos, ainda sim é preciso substituir totalmente a mesma, mas não é utilizado'''
tupla = ('Fabio', 'João')
dicionario = {'nome': 'Fabio', 'idade' : 34}
conjunto = {'Fabio', 'Paulo', 'Ariela'}

#FOR para TUPLA EXEMPLO
print(tupla[1])
for nome in tupla:
    print(nome)

#PROCURAR ITEM DENTEO DE TUPLA
if 'Claudio' in tupla:
    print("Fabio está na Tupla")

#IMPRESSAO DE DICIONARIO
print(dicionario)

#VERIFICAR ITEM DENTRO DO DICIONARIO UTILIZADO EM ESTRUTURA DE BANCO DE DADOS, BUSCA É MAIS EFICIENTE QUE LISTAS
print(dicionario['nome'])
print(dicionario['idade'])