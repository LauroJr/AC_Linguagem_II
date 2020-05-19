# Linguagem de Programação II
# AC04 - Banco
#
# Nome Aluno 1: LAURO MENDES DO AMARAL JUNIOR     -- RA: 1902047
# Nome Aluno 2: JEFFERSON OLIVEIRA DOS SANTOS     -- RA: 1901787
# Nome Aluno 3: ÍTALO VINÍCIUS GONÇALO DA SILVA   -- RA: 1902072


class Cliente():
    """
    Classe Cliente.
    possui os atributos PRIVADOS:
    - nome,
    - telefone,
    - email.
    caso o email não seja válido (verificar se contém o @) gera um ValueError
    (deve apenas gerar a exceção com raise ValuError,
    nao precisa fazer o try-except),
    caso o telefone não seja um número inteiro gera um TypeError
    """
    def __init__(self, nome: str, telefone: int, email: str):
        if type(telefone) != int:
            raise TypeError
        existe = False
        for char in email:
            if char == '@':
                existe = True
                # self.__email = email
        if existe is False:
            raise ValueError

        self.__nome = nome
        self.__telefone = telefone
        self.__email = email

    def get_nome(self):
        return self.__nome

    def get_telefone(self):
        return self.__telefone

    def set_telefone(self, novo_telefone: int):
        if type(novo_telefone) != int:
            raise TypeError
        self.__telefone = novo_telefone
        """
        Altera o atributo telefone.
        Caso não receba um número inteiro, gera um TypeError
        """

    def get_email(self):
        return self.__email

    def set_email(self, novo_email: str):
        """
        Altera o atributo Email.
        Caso não receba um email válido (contendo o @), gera um ValueError.
        """
        existe = False
        for char in novo_email:
            if char == '@':
                existe = True
                self.__email = novo_email
        if existe is False:
            raise ValueError


class Banco:
    """
    Os atributos devem ser privado
    A classe Banco deverá receber em seu construtor o nome do banco e deverá
    implementar os métodos:
    - abrir_conta(): abre uma nova conta, atribuindo AUTOMATICAMENTE o numero
    da conta em ordem crescente, a partir de 1 para a primeira conta aberta.
    - listar_contas(): retorna uma lista com todas as contas do banco

    DICA: utilize o atributo __lista_contas para armazenar as contas do banco
    DICA2: utilize o atributo __numero_conta para gerar automaticamente o
    número das contas do banco (incrementar sempre que uma conta é aberta)
    """
    def __init__(self, nome: str):
        self.__nome = nome
        self.__lista_contas = []
        self.__numero_conta = 1

    def get_nome(self):
        return self.__nome

    def abrir_conta(self, cliente, saldo: float):
        """
        Método para abertura de nova conta
        Recebe um objeto cliente e o saldo inicial da conta.
        Cria um objeto da classe Conta e armazena na lista de contas
        Caso o saldo inicial seja menor que 0 gera um ValueError
        Armazena todas as contas abertas na lista self.__lista_contas
        """
        if saldo < 0:
            raise ValueError
        else:
            c = Conta(cliente, self.__numero_conta, saldo)
            self.__lista_contas.append(c)
            self.__numero_conta += 1

    def listar_contas(self):
        return self.__lista_contas


class Conta:
    """
    Classe Conta: os atributos devem ser privados
    - Caso o saldo inicial seja menor que zero deve gerar um ValueError
    - Todas as operações (saldo inicial, saque e deposito) devem aparecer
      no extrato como tuplas.
      Exemplo: (saldo_inicial, 500), ('saque', 100), ('deposito', 200).
    - A criação da conta deve aparecer no extrato com o valor
      do saldo_inicial, exemplo: ('saldo_inicial', 1000)

    DICA: Utilize a lista __operacoes para guardar as operações feitas na conta
    """

    def __init__(self, cliente, numero: int, saldo: float):
        if saldo < 0:
            raise ValueError
        self.__cliente = cliente
        self.__numero = numero
        self.__saldo = saldo
        self.__operacoes = []
        if self.__operacoes == []:
            tupla0 = ('saldo_inicial', self.__saldo)
            self.__operacoes.append(tupla0)

    def get_cliente(self):
        return self.__cliente

    def get_saldo(self):
        return self.__saldo

    def get_numero(self):
        return self.__numero

    def sacar(self, valor: float):
        """
        Realiza saque na classe Conta, operação deve aparecer no extrato
        Caso o valor do saque seja maior que o saldo da conta,
        deve gerar um ValueError, e não efetuar o saque
        """
        if valor > self.__saldo:
            raise ValueError
        else:
            self.__saldo -= valor
            tupla1 = ('saque', valor)
            self.__operacoes.append(tupla1)

    def depositar(self, valor: float):
        """Realiza depósito na Conta, operação deve aparecer no extrato"""
        self.__saldo += valor
        tupla2 = ('deposito', valor)
        self.__operacoes.append(tupla2)

    def extrato(self):
        """
        Retorna uma lista de tuplas com todas as operações realizadas na Conta
        (saldo inicial, saque e deposito),
        exemplo: [('saldo_inicial', 500), ('saque', 100), ('deposito', 200)]
        """
        return self.__operacoes
