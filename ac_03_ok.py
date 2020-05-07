'''
   NOME_1: LAURO MENDES DO AMARAL JUNIOR  -- RA: 1902047
   -----------------------------------------------------
   NOME_2: JEFFERSON OLIVEIRA DOS SANTOS  -- RA: 1901787
'''
import os


class Geradores:
    def __init__(self, nome, especificacoes, qtd_tanque, liga_desl):
        self.__nome = nome
        self.__especificacoes = especificacoes
        self.__qtd_tanque = qtd_tanque
        self.__liga_desliga = liga_desl

    def get_nome(self):
        return self.__nome

    def get_ligado_desligado(self):
        return self.__liga_desliga

    def get_qtd_tanque(self):
        return self.__qtd_tanque

    def set_ligar(self):
        self.__liga_desliga = 'Ligado'
        self.__qtd_tanque -= 50

    def set_desligar(self):
        self.__liga_desliga = 'Desligado'

    def set_abastecer(self, combustivel):
        self.__qtd_tanque += combustivel

    def get_especificacoes(self):
        return self.__especificacoes


class Especificacoes:
    def __init__(self, potencia, capac_ger_energia, tamanho_tanque):
        self.__potencia = potencia
        self.__capac_ger_energia = capac_ger_energia
        self.__tamanho_tanque = tamanho_tanque

    def get_potencia(self):
        return self.__potencia

    def get_capac_ger_energia(self):
        return self.__capac_ger_energia

    def get_tamanho_tanque(self):
        return self.__tamanho_tanque


class Menu:
    def __init__(self, opcao1, opcao2, opcao3, opcao4, opcao5, opcao6):
        self.opcao1 = opcao1
        self.opcao2 = opcao2
        self.opcao3 = opcao3
        self.opcao4 = opcao4
        self.opcao5 = opcao5
        self.opcao6 = opcao6

    def exibir_menu(self):
        print(28*'-=')
        print('                      -- MENU --')
        print()
        print('       ', self.opcao1)
        print('       ', self.opcao2)
        print('       ', self.opcao3)
        print('       ', self.opcao4)
        print('       ', self.opcao5)
        print('       ', self.opcao6)
        print()
        print(28*'-=')


menu1_manipular = Menu('1 - Acionamento manual de gerador', '2 - Status dos\
 geradores', '3 - Status dos tanques de combustível', '4 - Abastecer tanque de\
 combustível', '5 - Detalhes do gerador', '6 - Sair')

espec_g1 = Especificacoes(95, 8000, 500)
g1 = Geradores('G1', espec_g1, 40, 'Ligado')

espec_g2 = Especificacoes(85, 7000, 400)
g2 = Geradores('G2', espec_g2, 49, 'Desligado')

espec_g3 = Especificacoes(80, 6500, 400)
g3 = Geradores('G3', espec_g3, 150, 'Desligado')

espec_g4 = Especificacoes(120, 9500, 850)
g4 = Geradores('G4', espec_g4, 420, 'Desligado')

lista_geradores = [g1, g2, g3, g4]


def opcao_invalida(resp):
    if resp < 1 or resp > 2:
        os.system("cls")
        print('Opção inválida! Escolha 1 p/ "SIM" ou 2 p/ "NÃO"\
 somente')


def acionamento_man_gerador(lista_geradores):
    nome_gerador = input('Informe o Nome do Gerador: ')
    print()
    cont = 0
    if nome_gerador.strip().upper() == 'G1':
        if g1.get_ligado_desligado() == 'Desligado':
            print(f'{nome_gerador} está Desligado. Deseja\
 Ligar?\n 1 - Sim\n 2 - Não')
            resp = int(input())
            if resp == 1 and g1.get_qtd_tanque() < 50:
                print()
                os.system("cls")  #
                print('G1 não pode ser ligado por falta de combustível')
            elif resp == 1 and g1.get_qtd_tanque() > 49:
                g1.set_ligar()
                print()
                os.system("cls")  #
                print('G1 Ligado com Sucesso')
            else:  # nova linha
                opcao_invalida(resp)
        else:
            print(f'{nome_gerador} está Ligado. Deseja\
 Desligar?\n 1 - Sim\n 2 - Não')
            resp = int(input())
            if resp == 1:
                os.system("cls")  #
                print('G1 Desligado com Sucesso')
                for gerador in lista_geradores:  # atualização
                    gerador.set_desligar()
            else:
                opcao_invalida(resp)
    else:
        for gerador in lista_geradores:
            if gerador.get_nome() == nome_gerador.strip().upper():
                cont += 1
                if cont == 1:
                    if gerador.get_ligado_desligado() == 'Desligado':
                        print(f'{nome_gerador} está Desligado. Deseja\
 Ligar?\n 1 - Sim\n 2 - Não')
                        resp = int(input())
                        if resp == 1 and gerador.get_qtd_tanque() > 49 and\
                                g1.get_ligado_desligado() == 'Ligado':
                            gerador.set_ligar()
                            print()
                            os.system("cls")  #
                            print(f'{nome_gerador} Ligado com\
 Sucesso')
                        elif resp == 1 and g1.get_ligado_desligado() ==\
                                'Desligado':
                            print()
                            os.system("cls")  #
                            print(f'{nome_gerador} não pode ser ligado porque\
 G1 está desligado')
                        elif resp == 1 and gerador.get_qtd_tanque() < 50:
                            print()
                            os.system("cls")  #
                            print(f'{nome_gerador} não pode ser ligado por\
 falta de combustível')
                        else:
                            opcao_invalida(resp)
                    else:
                        print()
                        print(f'{nome_gerador} está Ligado. Deseja\
 Desligar?\n 1 - Sim\n 2 - Não ')
                        resp = int(input())
                        if resp == 1:
                            gerador.set_desligar()
                            print()
                            os.system("cls")  #
                            print(f'{nome_gerador} Desligado com\
 Sucesso')
                        else:
                            opcao_invalida(resp)
        if cont < 1:
            print()
            os.system("cls")  #
            print('ERRO... Gerador não existe. Por favor informe um valor\
 existente')


def status_geradores(lista_geradores):
    print('STATUS DOS GERADORES:')
    print()
    for gerador in lista_geradores:
        print(f'{gerador.get_nome()} - {gerador.get_ligado_desligado()}')


def status_tanques_combustivel(lista_geradores):
    print('STATUS DOS TANQUES: ')
    print()
    for gerador in lista_geradores:
        porcentual = gerador.get_especificacoes().get_tamanho_tanque()
        porcentual = porcentual * 20 / 100
        if gerador.get_qtd_tanque() < porcentual:
            print(f'{gerador.get_nome()} - {gerador.get_qtd_tanque()} /\
 {gerador.get_especificacoes().get_tamanho_tanque()} (ABASTECER)')
        else:
            print(f'{gerador.get_nome()} - {gerador.get_qtd_tanque()} /\
 {gerador.get_especificacoes().get_tamanho_tanque()}')


def abastecer_tanque(lista_geradores):
    cont = 0
    nome_gerador = input('Nome do Gerador: ')
    qtd_diesel = int(input('Quantidade de Litros de Combustível: '))
    if qtd_diesel < 1:
        os.system("cls")
        print('ERRO... Entre com valor positivo p/ abastecer!')
        cont += 1
    else:
        for gerador in lista_geradores:
            if gerador.get_nome() == nome_gerador.strip().upper():
                cont += 1
                if cont == 1:
                    if gerador.get_especificacoes().get_tamanho_tanque() >=\
                            qtd_diesel + gerador.get_qtd_tanque():
                        gerador.set_abastecer(qtd_diesel)
                        print()
                        print('Abastecimento concluído com sucesso')
                    else:
                        print()
                        print('Valor a ser abastecido ultrapassa o limite do\
 Tanque')
    if cont < 1:
        print()
        print(f'ERRO... {nome_gerador} não existe. Digite um valor válido!')


def detalhes_gerador(lista_geradores):
    nome_gerador = input('Informe o Nome do Gerador: ')
    os.system("cls")
    cont = 0
    for gerador in lista_geradores:
        if nome_gerador.strip().upper() == gerador.get_nome():
            cont += 1
            if cont == 1:
                print('DETALHES DO GERADOR')
                print()
                print('Nome: ', gerador.get_nome())
                print('Potência: \
 ', gerador.get_especificacoes().get_potencia())
                print('Capacidade de geração de energia: \
 ', gerador.get_especificacoes().get_capac_ger_energia())
                print('Tamanho do Tanque: \
 ', gerador.get_especificacoes().get_tamanho_tanque())
                print('Status: ', gerador.get_ligado_desligado())
    if cont < 1:
        os.system("cls")
        print(f'ERRO... {nome_gerador} não existe. Digite um valor válido!')


voltas = True

while voltas is True:
    menu1_manipular.exibir_menu()
    try:
        print()
        menu = int(input('Escolha uma das opções acima: '))
        if menu == 1:
            os.system("cls")
            acionamento_man_gerador(lista_geradores)
        elif menu == 2:
            os.system("cls")
            status_geradores(lista_geradores)
        elif menu == 3:
            os.system("cls")
            status_tanques_combustivel(lista_geradores)
        elif menu == 4:
            os.system("cls")
            abastecer_tanque(lista_geradores)
        elif menu == 5:
            os.system("cls")
            detalhes_gerador(lista_geradores)
        elif menu == 6:
            voltas = False
            os.system("cls")
        else:
            try:
                if menu < 1 or menu > 6:
                    raise ValueError
            except ValueError:
                os.system("cls")
                print('ERRO... Você está digitando fora do intervalo de 1 a\
 6!')
                print('Por favor escolha um número inteiro de 1 a 6')
    except ValueError:
        os.system("cls")
        print('ERRO! Entre com números inteiros.')

print('|---------------------------------------|')
print('| OBRIGADO POR UTILIZAR NOSSOS SERVIÇOS |')
print('|---------------------------------------|')
