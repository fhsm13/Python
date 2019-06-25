#Exercicio para esta aula de Python
#Criar uma listra de inserção de nomes, idade, altura e peso
#Verificar se esta pessoa está apta para o exército
from typing import List

print('Programa de Insercao e validacao de Pessoas...')
print('Menus explicativos abaixo')

nome = input("Insira seu nome: ")
idade = input("Qual sua idade: ")
altura = input("Qual sua altura: ")
peso = input("Qual seu peso: ")
lista_candidatos: List[str] = [nome, idade, altura, peso]

print('Quer inserir mais algum candidato? - 1 - SIM, 2 - NAO')
opcao = input('Escolha: ')

while opcao == "1":
        nome = input("Insira seu nome: ")
        lista_candidatos.append(nome)
        idade = input("Qual sua idade: ")
        lista_candidatos.append(idade)
        altura = input("Qual sua altura: ")
        lista_candidatos.append(altura)
        peso = input("Qual seu peso: ")
        lista_candidatos.append(peso)
        print('Quer inserir mais algum candidato? - 1 - SIM, 2 - NAO')
        opcao = input('Escolha: ')
        print('Lista de Candidatos até o momento...')

else:
    print('Lista de Pessoas no momento', print(lista_candidatos))
    print('Obrigado boa tarde')

print(lista_candidatos)