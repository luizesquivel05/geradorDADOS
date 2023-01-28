import random
import os
import time

alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
caracterESPECIAL = "!',.;:/\|@#$%¨&*()_-=+{[}]~^º°ª"
numerosINTEIROS = "0123456789"

while True:
    print('''
            Salve, salve caro usuário, hoje iremos gerar uma quantidade de dados escolhidos por você com a quantidade de caracteres e formato por ti escolhidos. 
            
            Vale ressaltar que existem 7 formatos possíveis de carateres:
            alfabeto -> somente letras
            caracterESPECIAL -> somente caracteres especiais
    ''')
    quantidadeDADOS = int(input('Digite a quantidade de dados a ser gerada: '))
    quantidadeCARACTERES = int(input('Digite a quantidade de caracteres: '))
    os.system('cls')
    print('''
Escolha o formato, sendo:

[l] -> para alfabeto 
[c] -> para caracterESPECIAL 
[n] -> para numeroINTEIRO 

    ''')  
    formatoDADOS = str(input('Digite o formato desses caracteres: ')).lower()
    with open('log.txt','w') as arquivo:
        if formatoDADOS == 'l':
            for i in range(quantidadeDADOS):
                dados = str()
                for j in range(quantidadeCARACTERES):
                    dados += random.choice(alfabeto)
                arquivo.write(dados)
                arquivo.write("\n")
        elif formatoDADOS == 'c':
            for i in range(quantidadeDADOS):
                dados = str()
                for j in range(quantidadeCARACTERES):
                    dados += random.choice(caracterESPECIAL)
                arquivo.write(dados)
                arquivo.write("\n")
        elif formatoDADOS == 'n':
            for i in range(quantidadeDADOS):
                dados = str()
                for j in range(quantidadeCARACTERES):
                    dados += random.choice(numerosINTEIROS)
                arquivo.write(dados)
                arquivo.write("\n")
        elif formatoDADOS == 'n':
            for i in range(quantidadeDADOS):
                dados = str()
                for j in range(quantidadeCARACTERES):
                    dados += random.choice(numerosINTEIROS)
                arquivo.write(dados)
                arquivo.write("\n")
    time.sleep(5)
    print('Finalizamos a criação e salvamos no arquivo log.txt!')
    if int(input('Deseja continuar? 0 para SIM e 1 para NÃO: ')) == 1: break
    else: os.system('cls')