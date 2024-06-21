# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data início: 19/06/2024.
# Data final:
# Objetivo: Menu do sistema com a junção dos arquivos 3, 4, 5, 6, e 7.

# Bibliotecas:
import os
import platform

# Declarações de variávies:
comandos = ''''''
opcao = 0


# Limpando o terminal:
if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')

# Exibindo título:
print('''
|---------------------------|
|                           |
|       Bem-vindo(a)!       |
|       Dual B Store        |
|                           |
|---------------------------|''')

# Exbindo comandos:
comandos = '''
|---------------------------|
|         Comandos:         |
|      1 - Criar conta      |
|      2 - Fazer Login      |
|      3 - Ver produtos     |
|      4 - Ver carrinho     |
|      5 - Pagamento        |
|---------------------------|'''
print(comandos)
print()

# Usuário escolhendo uma opção:
while True:
    opcao = input('Digite o número correspondente a opção que deseja executar: ')

    # Validação da opção:
    if not(opcao.isnumeric()):
        print('Por favor insirá apenas números!')
        continue
    else:
        opcao = int(opcao)
        break
print()

# Verificando qual opção o usuário escolheu e agindo de acordo:
if opcao == 1:
    pass
elif opcao == 2:
    pass
elif opcao == 3:
    pass
elif opcao == 4:
    pass
elif opcao == 5:
    pass
else:
    pass