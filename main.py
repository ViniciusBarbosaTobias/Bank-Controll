from cliente import Client
from conta import Account
from login import User

client = ('')
telephone = ('')
cpf = ('')
number = ('')
balance = ('0')

if User.login == User.login_accepted and User.password == User.password_accepted :
    print('Acesso permitido')  
    while True:  
        option = input('Selecione uma opção:\n(A)brir conta \n'
                       '(C)onsultar dados da conta \n'
                       '(D)epositar em conta existente \n (S)air '"\n")

        class Main:
            pass

        if option == 'A':
            client = input('Digite seu nome completo: ')  
            if len(client) <3:
                print('Caracteres invalidos')
                
            telephone = input('Digite seu telefone: ')
            if  len(telephone) <10:
                print('Telefone Invalido.')
                
            cpf = input('Digite seu cpf: ')
            if len(cpf) <11:
                print('CPF Invalido')

            number = input('Digite 5 numeros para a sua conta.')
            number = int(number)
            number = number * 3
            continue
            
        if option == 'C':
            print(f'Nome do Titular: ', {client})
            print(f'Nº CPF: ', {cpf}) 
            print(f'Numero da Conta:', {number})
            print(f'Seu Saldo: ', {balance})
        

        if option == 'S':
            print('Secão encerrada.')
            break
        else:
            break

if  User.login != User.login_accepted and User.password != User.password_accepted :
    print('Login e/ou Senha invalidos.')
