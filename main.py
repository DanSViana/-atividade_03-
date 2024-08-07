"""
Crie um programa que o usuário informe o nome e o programa mostre na tela uma mensagem de boas vindas com o nome do usuário. Ao terminar, envie o arquivo .py.
"""

# entrada de dados
nome = input('Informe seu nome: ')
cargo = input('Informe o cargo: ')

# saída de dados
print('Seja bem vindo ' + cargo +' '+nome + '.')
print('Seja bem vindo',cargo, nome, '.')
print('Seja bem vindo {} {}.'.format(cargo, nome))
print(f'Seja bem vindo {cargo} {nome}.')