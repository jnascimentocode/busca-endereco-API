import requests
import os
from time import sleep

os.system('cls')

while True:

    print('-'*50)
    print('CONSULTA CEP'.center(50))
    print('-'*50)

    while True:
        cep = input('CEP: ')
        if len(cep) != 8:
            print('Valor inválido!')
            print('-'*50)
        else: 
            break
        
    requisição = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))

    endereço = requisição.json()

    if 'erro' not in endereço:
        cep = endereço['cep']
        rua = endereço['logradouro']
        bairro = endereço['bairro']
        cidade = endereço['localidade']
        estado = endereço['uf']

        print('-'*50)
        print(f'Rua: {rua} \nBairro: {bairro} \nCidade: {cidade} \nEstado: {estado} \nCEP: {cep}')
        print('-'*50)
    else:
        print('CEP não encontrado.')
        print('-'*50)
    
    while True:
        while True:
            resp = str(input('Deseja realizar nova consulta? [S/N]: ')).upper()
            if resp in 'SN':
                break
            else:
                print('Favor digitar S OU N.')

        if resp == 'N':
            sleep(1)
            print('SESSÃO ENCERRADA')
            print('-'*50)
            exit()        
        else:
            break
            

