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
        print(tot)


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
        return numero_letras

    def emitir_recibo(self, qtd_letras):
        print(f'Cliente: {self.cliente.nome}\
 \nTelefone: {self.cliente.telefone}\nLargura da Placa: {self.largura}\nAltura\
 da Placa: {self.altura}\nFrase: {self.frase}\nQuantidade de Letras:\
 {qtd_letras}\nValor: {self.__valor}')


#  Primeiro cliente:
obj_end = Endereco('Rua João Mateus Rendon', 'n 145 a', 'Casa 2', 'Pq São\
 Rafael', 'São Paulo', 'SP', '08320-170')

obj_cliente = Cliente('Lauro Jr', '(11)96187-0730', obj_end)

obj_pedido1 = Pedido(obj_cliente, 0.45, 1.20, 'Olá Mundo!', 'Branco', '\
 Vermelho')

qtd_letras = obj_pedido1.get_valor()
obj_pedido1.emitir_recibo(qtd_letras)

#  Segundo cliente:
print()
obj_end = Endereco('Rua João Mateus Rendon', 'n 145 a', 'Casa 2', 'Pq São\
 Rafael', 'São Paulo', 'SP', '08320-170')

obj_cliente = Cliente('Paulo', '(11)96187-0730', obj_end)

obj_pedido2 = Pedido(obj_cliente, 1.0, 3.0, '50% de Desconto', 'Branco', '\
 Vermelho')

qtd_letras = obj_pedido2.get_valor()
obj_pedido2.emitir_recibo(qtd_letras)

obj_hist = Historico()
obj_hist.inserir_pedidos(obj_pedido1)
obj_hist.inserir_pedidos(obj_pedido2)

obj_hist.calcular_faturamento()
