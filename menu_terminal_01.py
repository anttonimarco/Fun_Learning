import time # Importação da biblioteca para usar time.

on = True   # Declarando variáveis booleanas.
off = False

while on == True:   # Enquanto variável (on) for verdadeira faça isso.
    print('\033[1:31m       # Menu #\033[m')
    print('\033[1:31m[1]\033[m \033[34mCadastrar Clientes')    #\033[1:31m textocolorido \033[m
    print('\033[1:31m[2]\033[m \033[34mConsultar Clientes')         #Códigos de cores.
    print('\033[1:31m[3]\033[m \033[34mSair\033[m')

    # Se variável choice receber o número 1 faça isso.
    choice = int(input('\033[32mDigite sua escolha: \033[m'))
    if choice == 1:
        print('\n')
        print('\033[1:31m# Cadastro de Clientes #\033[m')
        print('Digite o nome do cliente que deseja cadastrar')
        name = str(input('Nome novo Cliente: '))
        print('\nCliente Cadastrado com Sucesso!')
        print('Retornando ao Menu Principal\n')
        time.sleep(2)

    # Se variável choice receber o número 2 faça isso.
    elif choice == 2:
        print('\n')
        print('# Consulta de clientes #')
        find = str(input('Nome do cliente: '))
        if find == name:
            print(name)
        print('\n Retornando ao Menu Principal\n')
        time.sleep(2)

    # Se variável choice receber o número 3 faça isso.
    elif choice == 3:
        on == False
        print('Saindo do programa em 1 ...')
        time.sleep(1)
        print('Saindo do programa em 2 ...')
        time.sleep(1)
        print('Saindo do programa em 3 ...')
        time.sleep(1)
        break

