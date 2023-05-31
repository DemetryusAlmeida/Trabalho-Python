#Exercício 2: Faça uma função que receba o nome e sobrenome de uma pessoa e retorne a primeira letra de seu nome e seu sobrenome, concatenando com a string "@algoritmos.com.br". No algoritmo principal deverá ser apresentada a mensagem ao usuário contendo seu nome completo e seu email. Imprima na tela um teste do seu programa utilizando o seu nome e sobrenome concatenado com os dois últimos dígitos do seu RU.

#Exemplo: Sra Luciane Kanashiro, seu email é lkanashiro16@algoritmos.com.br

#confirmação por parte do usuário
confirmacao = int(input('deseja inserir dados?    1 - sim   0 - não '))
#dados a serem inseridos e processados: nome, sobrenome, ru para construção do email
if confirmacao == 1:
    nome = str(input('insira seu nome: '))
    sobrenome = str(input('insira seu sobrenome: '))
    ru = input('insira seu ru: ')
    v_concat = nome + sobrenome + ru[5:7]
    print('')
    print('Seus dados')
    print('')
    print('Nome: {}'.format(nome))
    print('Sobrenome: {}'.format(sobrenome))
    print('ru: {}'.format(ru))
    print('email: {}@algoritmos.com.br'.format(v_concat.lower()))

#reposta para o usuário que negou o uso do programa
elif confirmacao == 0:
    print('encerrando programa...')

#caso o usuário insira chaves que não se enquadram aos requisitados
else:
    print('resposta inválida, tente novamente')