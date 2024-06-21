# Curso: desenvolvivento de sistemas
# Turma: 0152
# Autor : Beatriz victoria
# Data do inicio : 19\06
# Data final:
# Objetivo: criação da conta do sistema

# biblioteca do sistema
import os

# limpando
os.system('cls')

# entrando com os dados da conta
print('-'*79)
print('criando conta')
print('='*79)

usuario = ""
senha = ""
comfirmacao = ""

while True:
    usuario = str(input('Entre com o nome de usuario: '))
    senha = str(input('Entre com a senha: '))
    comfirmacao = str(input('Digite novamente sua senha: '))
    
    if senha != comfirmacao: 
        print('Sua senha e confirmação são diferentes!')
        continue
    else:
        break

print(f'-'*79)
print(f'Bem-vindo(a) {usuario}') 