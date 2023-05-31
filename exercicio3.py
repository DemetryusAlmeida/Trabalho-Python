#Exercício 3: Um canal de jogos do youtube está fazendo um sorteio para angariar doações para pessoas em situação de vulnerabilidade social. A cada 10,00 doado, o nome da pessoa é inserido em uma lista de sorteio.

#importação da biblioteca
import random

#Criação de lista, preenchimento de dados: nome, quantidade doada.
cond = True
doadores = []
print('Pressione enter quando atingir o número de dados que desejava')
while(cond):
    nome=""
    nome = input('Digite o nome do doador: ')
    if (len(nome) == 0) :
        break
    doado = int(input('Digite o número doado : '))
    fator =  round(int(doado / 10))

    if fator >= 1:
        doadores.extend([nome] * fator)

    print("Lista dos Doadores {}".format(doadores))

#uso do random para embaralhar, escolher um doador e printar na tela o nome escolhido
if len(doadores) >= 1:
    random.shuffle(doadores)
    print("O ganhador do grande premio foi o {}".format(' '.join(random.choices(doadores))))