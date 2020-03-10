''' NOME: Lauro Mendes do Amaral Junior     RA: 1902047
    NOME: Ítalo Vinícius Gonçalo da Silva   RA: 1902072
'''


def calculo_salario(lista1):
    a = type(lista1[2])
    b = float
    if a != str:
        if lista1[2] >= 3000.00 and lista1[3] == "DESENVOLVEDOR" and a == b:
            salario1 = lista1[2] - ((lista1[2] * 20) / 100)
            return salario1
        elif lista1[2] < 3000.00 and lista1[3] == "DESENVOLVEDOR" and a == b:
            salario1 = lista1[2] - ((lista1[2] * 10) / 100)
            return salario1
        elif lista1[2] >= 2000.00 and lista1[3] == "ANALISTA" and a == b:
            salario1 = lista1[2] - ((lista1[2] * 25) / 100)
            return salario1
        elif lista1[2] < 2000.00 and lista1[3] == "ANALISTA" and a == b:
            salario1 = lista1[2] - ((lista1[2] * 15) / 100)
            return salario1
        elif lista1[2] >= 5000.00 and lista1[3] == "GERENTE" and a == b:
            salario1 = lista1[2] - ((lista1[2] * 30) / 100)
            return salario1
        elif lista1[2] < 5000.00 and lista1[3] == "GERENTE" and a == b:
            salario1 = lista1[2] - ((lista1[2] * 20) / 100)
            return salario1
    else:
        a = 9999999999
        return a
