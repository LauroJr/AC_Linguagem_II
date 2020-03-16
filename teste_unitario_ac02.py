import modulo_ac02

''' NOME: Lauro Mendes do Amaral Junior     RA: 1902047
    NOME: Ítalo Vinícius Gonçalo da Silva   RA: 1902072

Foram criadas 6 funções. Cada uma testa uma condição de acordo com as normas
descrita no módulo. Além de tratar erros da função, testando assim a funciona-
lidade do código, trata erros de entradas também.

'''


def primeiro_teste():
    try:
        lista1 = ["Marco San", "marco@email.com", 5000.00, "DESENVOLVEDOR"]
        salario = modulo_ac02.calculo_salario(lista1)
        assert salario == 4000.00
        # salario >= 3000.00 (20% desconto)
        print("TESTE 1 CORRETO")
    except AssertionError:
        print("TESTE 1 INCORRETO")
    try:
        if lista1[3] != "DESENVOLVEDOR":
            raise NameError
    except NameError:
        print("CARGO INEXISTENTE PARA CONSULTA")
    try:
        a = type(lista1[2])
        if a == str or a == int:
            raise TypeError
    except TypeError:
        print("Tipo de dado incorreto. Entre com valor Float. EX:1000.00")
    print()


def segundo_teste():
    try:
        lista2 = ["Marco San", ",marco@email.com", 2500.00, "DESENVOLVEDOR"]
        salario = modulo_ac02.calculo_salario(lista2)
        assert salario == 2250.00
        # salario < 3000.00 (10% desconto)
        print("TESTE 2 CORRETO")
    except AssertionError:
        print("TESTE 2 INCORRETO")
    try:
        if lista2[3] != "DESENVOLVEDOR":
            raise NameError
    except NameError:
        print("CARGO INEXISTENTE PARA CONSULTA")
    try:
        a = type(lista2[2])
        if a == str or a == int:
            raise TypeError
    except TypeError:
        print("Tipo de dado incorreto. Entre com valor Float. EX:1000.00")
    print()


def terceiro_teste():
    try:
        lista3 = ["Ronaldo Azevedo", "ronaldo@email.com", 2000.00, "ANALISTA"]
        salario = modulo_ac02.calculo_salario(lista3)
        assert salario == 1500.00
        # salario >= 2000.00 (25% desconto)
        print("TESTE 3 CORRETO")
    except AssertionError:
        print("TESTE 3 INCORRETO")
    try:
        if lista3[3] != "ANALISTA":
            raise NameError
    except NameError:
        print("CARGO INEXISTENTE PARA CONSULTA")
    try:
        a = type(lista3[2])
        if a == str or a == int:
            raise TypeError
    except TypeError:
        print("Tipo de dado incorreto. Entre com valor Float. EX:1000.00")
    print()


def quarto_teste():
    try:
        lista4 = ["Ronaldo Azevedo", "ronaldo@email.com", 550.00, "ANALISTA"]
        salario = modulo_ac02.calculo_salario(lista4)
        assert salario == 467.50
        # salario < 2000.00 (15% desconto)
        print("TESTE 4 CORRETO")
    except AssertionError:
        print("TESTE 4 INCORRETO")
    try:
        if lista4[3] != "ANALISTA":
            raise NameError
    except NameError:
        print("CARGO INEXISTENTE PARA CONSULTA")
    try:
        a = type(lista4[2])
        if a == str or a == int:
            raise TypeError
    except TypeError:
        print("Tipo de dado incorreto. Entre com valor Float. EX:1000.00")
    print()


def quinto_teste():
    try:
        lista5 = ["Jhon Ribeiro", "ribeiro@email.com", 5000.00, "GERENTE"]
        salario = modulo_ac02.calculo_salario(lista5)
        assert salario == 3500.00
        # salario >= 5000.00 (30% desconto)
        print("TESTE 5 CORRETO")
    except AssertionError:
        print("TESTE 5 INCORRETO")
    try:
        if lista5[3] != "GERENTE":
            raise NameError
    except NameError:
        print("CARGO INEXISTENTE PARA CONSULTA")
    try:
        a = type(lista5[2])
        if a == str or a == int:
            raise TypeError
    except TypeError:
        print("Tipo de dado incorreto. Entre com valor Float. EX:1000.00")
    print()


def sexto_teste():
    try:
        lista6 = ["Jhon Ribeiro", "ribeiro@email.com", 2500.00, "GERENTE"]
        salario = modulo_ac02.calculo_salario(lista6)
        assert salario == 2000.00
        # salario < 5000.00 (20% desconto)
        print("TESTE 6 CORRETO")
    except AssertionError:
        print("TESTE 6 INCORRETO")
    try:
        if lista6[3] != "GERENTE":
            raise NameError
    except NameError:
        print("CARGO INEXISTENTE PARA CONSULTA")
    try:
        a = type(lista6[2])
        if a == str or a == int:
            raise TypeError
    except TypeError:
        print("Tipo de dado incorreto. Entre com valor Float. EX:1000.00")


primeiro_teste()
segundo_teste()
terceiro_teste()
quarto_teste()
quinto_teste()
sexto_teste()
