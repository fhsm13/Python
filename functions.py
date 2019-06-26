vlr_horas = input('Digite as hora VALOR: ')
dias_mes = input('Digite quantidade de dias no mês: ')
vlr_horas = float(vlr_horas)
dias_mes = float(dias_mes)

if vlr_horas > 0:
    salario = vlr_horas * dias_mes
    print("Salario: {}".format(salario))
else:
    print("Digitou 0")






