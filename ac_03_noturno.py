class Endereco:
    def __init__(self, rua, numero, complemento, bairro, cidade, uf, cep):
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        self.cep = cep


class Cliente:
    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco


class Historico:
    def __init__(self):
        self.__pedidos = []

    def inserir_pedidos(self, pedido):
        self.__pedidos.append(pedido)

    def calcular_faturamento(self):
        tot = 0
        for obj in self.__pedidos:
            area = obj.altura * obj.largura
            custo_m = area * 147.00
            n_letras = 0
            for letra in obj.frase:
                if letra != ' ':
                    n_letras += 1
            custo_d = n_letras * 0.35
            tot = custo_m + custo_d + tot
        return tot


class Pedido:
    def __init__(self, cliente, altura, largura, frase, cor_placa, cor_letra):
        self.cliente = cliente
        self.altura = altura
        self.largura = largura
        self.frase = frase
        self.cor_placa = cor_placa
        self.cor_letra = cor_letra
        self.__valor_fixo_material = 147.00
        self.__valor_fixo_letra = 0.35
        self.__valor = 0

    def get_valor(self):
        area = self.altura * self.largura
        custo_material = area * self.__valor_fixo_material
        numero_letras = 0
        for letras in self.frase:
            if letras != ' ':
                numero_letras += 1
        custo_desenho = numero_letras * self.__valor_fixo_letra
        valor_placa = custo_material + custo_desenho
        self.__valor = valor_placa
        return self.__valor

    def emitir_recibo(self):
        qnt_let = 0
        for letras in self.frase:
            if letras != ' ':
                qnt_let += 1
        print(f'Cliente: {self.cliente.nome}\
 \nTelefone: {self.cliente.telefone}\nLargura da Placa: {self.largura}\nAltura\
 da Placa: {self.altura}\nFrase: {self.frase}\nQuantidade de Letras:\
 {qnt_let}\nValor: {self.__valor}')

# PROGRAMA PRINCIPAL PARA TESTAR AS CLASSES:

# Criação do Endereço


endereco = Endereco("Rua Silva", "123", "Ap. 58", "Centro", "São Paulo", "SP", "05577-023")

# Cria do Cliente
cliente = Cliente("Paulo", "(11) 99999-4565", endereco)

# Criação do Primeiro Pedido
pedido1 = Pedido(cliente, 1.0, 3.0, "50% de Desconto", "cinza", "vermelha")

# Imprime recibo do Primerio Pedido
pedido1.get_valor()
pedido1.emitir_recibo()
print()

# Criação do Segundo Pedido
pedido2 = Pedido(cliente, 0.5, 2, "Estamos Atendendo", "cinza", "vermelha")

# Imprime recibo do Segundo Pedido
pedido2.get_valor()
pedido2.emitir_recibo()
print()
# Impressao de dados para teste                                 # VALORES A SER IMPRESSOS:
print("Nome:", pedido1.cliente.nome)                            # Paulo
print("Telefone:", pedido1.cliente.telefone)                    # (11) 99999-4565
print("Rua:", pedido1.cliente.endereco.rua)                     # Rua Silva
print("Número:", pedido1.cliente.endereco.numero)               # 123
print("Complemento:", pedido1.cliente.endereco.complemento)     # Ap. 58
print("Bairro:", pedido1.cliente.endereco.bairro)               # Centro
print("Cidade:", pedido1.cliente.endereco.cidade)               # São Paulo
print("UF:", pedido1.cliente.endereco.uf)                       # SP
print("CEP:", pedido1.cliente.endereco.cep)                     # 05577-023
print("Altura:", pedido1.altura)                                # 1.0
print("Largura:", pedido1.largura)                              # 3.0
print("Frase:", pedido1.frase)                                  # 50% de Desconto
print("Cor da Placa:", pedido1.cor_placa)                       # cinza
print("Cor da Letra:", pedido1.cor_letra)                       # vermelha

print("Valor do Primeiro Pedido:", pedido1.get_valor())         # 445.55

print("Valor do Segundo Pedido:", pedido2.get_valor())          # 152.6

#cria objeto Historico
historico = Historico()

# Insere pedidos no histórico
historico.inserir_pedidos(pedido1)
historico.inserir_pedidos(pedido2)

# Exibe Faturamento Total
print("Faturamento Total: ", historico.calcular_faturamento())  # 598.15
