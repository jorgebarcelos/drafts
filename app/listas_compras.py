import os

'''
Simple shop  cart algorithm
'''

shop_card = []
while True:
    print('Escolha uma opção: ')
    option = int(
        input(f'''
        {1} Inserir
        {2} Apagar
        {3} Listar
        {4} Sair
    ''')
)

    if option == 1:
        os.system('clear')

        item = input('Insira  o item: ')
        shop_card.append(item)

        os.system('clear')

    elif option == 2:

        try:
            index = int(input('Escolha o inice: \n'))
            del shop_card[index]
            print(f'O item excluido foi {item}\n')
        except ValueError:
            print('Somente numeros  inteiros')
        except IndexError:
            print('Indice não existe\n')
        except Exception:
            print('Erro desconhecido')

    elif option == 3:

        os.system('clear')

        for i, value in enumerate(shop_card):
            print(i, value,'\n')

    elif option == 4:
        exit()
