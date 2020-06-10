def linha(tam=42):
    return '-'*tam


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Erro, digite um numero inteiro valido!')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuario!')
            break
        else:
            return n


def cabeçalho(msg):
    print(linha())
    print(msg.center(42))
    print(linha())


def menu(lista):
    cabeçalho('Menu Principal')
    c =1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaint('Digite a opção desejada: ')
    return opc



