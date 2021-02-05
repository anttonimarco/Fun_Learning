import time

on = True
off = False

while on == True:
    print('\033[1:31m # Menu #\033[m')
    print('\033[1:31m[1]\033[m \033[Cadastrar Clientes')
    print('\033[1:31m[2]\033[m Consultar Clientes')
    print('\033[1:31m[3]\033[m Sair')

    choice = int(input('Digite sua escolha: '))
    if choice == 1:
        print('\n')
        print('# Cadastro de Clientes #')
        print('Digite o nome do cliente que deseja cadastrar')
        name = str(input('Nome novo Cliente: '))
        print('\nCliente Cadastrado com Sucesso!')
        print('Retornando ao Menu Principal\n')
        time.sleep(2)

    elif choice == 2:
        print('\n')
        print('# Consulta de clientes #')
        find = str(input('Nome do cliente: '))
        if find == name:
            print(name)
        print('\n Retornando ao Menu Principal\n')
        time.sleep(2)

    elif choice == 3:
        on == False
        print('Saindo do programa em 1 ...')
        time.sleep(1)
        print('Saindo do programa em 2 ...')
        time.sleep(1)
        print('Saindo do programa em 3 ...')
        time.sleep(1)
        break
















