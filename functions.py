'''
Autor: Fabio Martins
Email: fabio@fastmail.uk
Format se utiliza para formatar o tipo de dado inserido para cálculo posterior
sem este tipo de atributo nâo é possível efetuar o cálculo abaixo, sendo necessário formatar para que nâo ocorra erro
Também foi declarado o tipo de variável para inserção dos dados veja que o tipo float
'''

vlr_horas = input('Digite as hora VALOR: ')
dias_mes = input('Digite quantidade de dias no mês: ')
vlr_horas = float(vlr_horas)
dias_mes = float(dias_mes)

if vlr_horas > 0:
    salario = vlr_horas * dias_mes
    print("Salario: {}".format(salario))
else:
    print("Digitou 0")






