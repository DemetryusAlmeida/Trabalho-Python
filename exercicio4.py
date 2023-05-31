#Exercício 4: Considere a tabela a seguir referente a produtos armazenados em um depósito, em que são considerados o estoque atual de cada produto e o estoque mínimo necessário.

#Código Estoque Mínimo
#1      35      20
#5      75      50
#2      43      45
#3      26      18
#20     35      20

#confirmação por parte do usuário
confirmacao = int(input('deseja inserir dados?    1 - sim   0 - não '))
if confirmacao == 1:
    produto = []
    #dados do produto já existentes
    produto1 = {'codigo': 1,
                'estoque': 35,
                'minimo': 20}
    produto2 = {'codigo': 5,
                'estoque': 75,
                'minimo': 50}
    produto3 = {'codigo': 2,
                'estoque': 43,
                'minimo': 45}
    produto = [produto1, produto2, produto3]

    #visualização dos produtos e dos dados armazenados
    print('Código / Estoque / Mínimo')
    print('  {}         {}        {}'.format(produto1['codigo'], produto1['estoque'], produto1['minimo']))
    print('  {}         {}        {}'.format(produto2['codigo'], produto2['estoque'], produto2['minimo']))
    print('  {}         {}        {}'.format(produto3['codigo'], produto3['estoque'], produto3['minimo']))

    #dados a serem alterados pelo usuário: codigo, estoque e quantidade mínima
    produto1['codigo'] = int(input('Digite o código: '))
    produto1['estoque'] = int(input('Digite o número do estoque: '))
    produto1['minimo'] = int(input('Digite o mínimo: '))

    #dados de todos os produtos armazenados e já alterados
    print('Código / Estoque / Mínimo')
    print('  {}         {}        {}'.format(produto1['codigo'], produto1['estoque'], produto1['minimo']))
    print('  {}         {}        {}'.format(produto2['codigo'], produto2['estoque'], produto2['minimo']))
    print('  {}         {}        {}'.format(produto3['codigo'], produto3['estoque'], produto3['minimo']))

#reposta para o usuário que negou o uso do programa
elif confirmacao == 0:
    print('encerrando programa...')

#caso o usuário insira chaves que não se enquadram aos requisitados
else:
    print('resposta inválida, tente novamente')
