#Exercício 1: Escreva um programa que leia o nome de um aluno e sua nota final. Em seguida,informe o conceito conforme a tabela abaixo. A saída do programa deve exibir na tela uma frase com o padrão descrito a seguir:

#Nome do aluno: Fábio José

#Nota final: 3.5

#Frase a ser exibida: O aluno Fabio José tirou nota 3.5 e se enquadra no conceito D

#Nota Conceito
#De 0,0 a 2,9 E
#De 3,0 a 4,9 D
#De 5,0 a 6,9 C
#De 7 a 8,9 B
#De 9,0 a 10 A

#confirmação por parte do usuário
confirmacao = int(input('deseja inserir dados?    1 - sim   0 - não '))
if confirmacao == 1:
# dados a serem registrados
    nome = str(input('digite o nome do aluno: '))
    nota = float(input('digite a nota final do aluno: '))

# os dados serão processados para entregar a nota do aluno e seu devido conceito
    if nota >= 0 and nota <= 2.9:
        print('o aluno {} que tirou {} como nota, se enquadra no conceito E'.format(nome, nota))

    elif nota >= 3 and nota <= 4.9:
        print('o aluno {} que tirou {} como nota, se enquadra no conceito D'.format(nome, nota))

    elif nota >= 5 and nota <= 6.9:
        print('o aluno {} que tirou {} como nota, se enquadra no conceito C'.format(nome, nota))

    elif nota >= 7 and nota <= 8.9:
        print('o aluno {} que tirou {} como nota, se enquadra no conceito B'.format(nome, nota))

    elif nota >= 9 and nota <= 10:
        print('o aluno {} que tirou {} como nota, se enquadra no conceito A'.format(nome, nota))

# caso o usuário insira dados com requisitos inválidos
    else:
        print('dados inválidos')

#reposta para o usuário que negou o uso do programa
elif confirmacao == 0:
    print('encerrando programa...')

#caso o usuário insira chaves que não se enquadram aos requisitados
else:
    print('resposta inválida, tente novamente')