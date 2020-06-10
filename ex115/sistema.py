from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'dados.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

cabeçalho('Sistema de Arquivo v1')
while True:
    resp = menu(['Cadastrar pessoa', 'Listar cadastrados', 'Sair do sistema'])
    if resp == 1:
        cabeçalho('Cadastramento de Pessoas')
        while True:
            nome = str(input('Nome: '))
            idade = leiaint('Idade: ')
            cadastrar(arq, nome, idade)
            r = str(input('Deseja adicionar mais pessoas? ')).strip().upper()
            if r == 'N':
                break
    elif resp == 2:
        lerArquivo(arq)
    elif resp == 3:
        cabeçalho('Saindo... Até logo!')
        sleep(1)
        break
    else:
        print('Erro! Opção invalida!')