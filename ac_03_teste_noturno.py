

# PROGRAMA PRINCIPAL PARA TESTAR AS CLASSES:

# Criação do Endereço
endereco = Endereco("Rua Silva", "123", "Ap. 58", "Centro", "São Paulo", "SP", "05577-023")

# Cria do Cliente
cliente = Cliente("Paulo", "(11) 99999-4565", endereco)

# Criação do Primeiro Pedido
pedido1 = Pedido(cliente, 1.0, 3.0, "50% de Desconto", "cinza", "vermelha")

# Imprime recibo do Primerio Pedido
pedido1.emitir_recibo()

# Criação do Segundo Pedido
pedido2 = Pedido(cliente, 0.5, 2, "Estamos Atendendo", "cinza", "vermelha")

# Imprime recibo do Segundo Pedido
pedido2.emitir_recibo()

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
historico.inserir_pedido(pedido1)
historico.inserir_pedido(pedido2)

# Exibe Faturamento Total
print("Faturamento Total: ", historico.calcular_faturamento())  # 598.15
