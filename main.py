from models import Stickers, Album

def number_sticker(x):
    for _ in range(x):
        op = stickers.open_package()
        album.verify_if_i_have_the_sticker(op)


def main():

    global stickers
    global album
    
    stickers = Stickers()
    album = Album()

    print(40*('-'))
    print('ALBUM DA COPA'.center(40))
    print('FIFA WORLD CUP QATAR 2022'.center(40))
    print(40*('-'))

    while True:
        print('\nEscolha uma opção: '
        '\n 1 - Colar no album'
        '\n 2 - Ver repetidas')

        opcaoMatriz = int(input('\nInsira a opção desejada: '))
        if(opcaoMatriz == 1):

            opcao = int(input('\nQuantos pacotes com 5 figurinhas deseja abrir: '))
            number_sticker(opcao)
            print(album.get_stickers_in_album())
            
            replay = int(input('\n1 - Continuar \n2- fechar: '))
            if(replay == 1):
                pass
            elif(replay == 2):
                break
        if(opcaoMatriz == 2):
            print(album.get_repeated_stickers())

            replay = int(input('\n1 - Continuar \n2- fechar: '))
            if(replay == 1):
                pass
            elif(replay == 2):
                break


if __name__ == "__main__":
    main()

