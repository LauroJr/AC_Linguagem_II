''' NOME: Lauro Mendes do Amaral Junior     RA: 1902047
    NOME: Ítalo Vinícius Gonçalo da Silva   RA: 1902072

Implemente uma função para calcular o salário de um funcionário.

Essa função recebe como entrada uma lista contendo nome, email, salário-base e
cargo e retorna como resultado o salário líquido desse funcionário.

Observe abaixo um exemplo para a lista de entrada da função:
["Marcílio dos Santos", "marcilio@email.com", 5000.00, "DESENVOLVEDOR"]

De acordo com seu cargo, a regra para cálculo do salário líquido é diferente:
Se o cargo for DESENVOLVEDOR, o funcionário terá desconto de 20% caso o
salário seja maior ou igual que 3.000,00, ou apenas 10% caso o salário seja
menor que isso.
Se o cargo for ANALISTA, o funcionário terá desconto de 25% caso o salário
seja maior ou igual que 2.000,00, ou apenas 15% caso o salário seja menor que
isso.
Se o cargo for GERENTE, o funcionário terá desconto de 30% caso o salário seja
maior ou igual que 5.000,00, ou apenas 20% caso o salário seja menor que isso.

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
