print('Formulário de Validação para Ingresso Exército')
print('Insira seus dados abaixo conforme solicitado!\n')
nome = input("Qual seu nome?: ")
idade = input("Qual sua idade?: ")
peso = input("Qual seu peso?: ")
altura = input("Qual sua altura?: ")

if idade >= '18' and peso >= '60' and altura >= '1.70':
    print('Parabéns você está apto para o Exército')
else:
    print('Desculpe você nâo pode ser do exército')