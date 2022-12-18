from models import Stickers, Album
import pandas as pd


def number_sticker(x):
    for _ in range(x):
        op = stickers.open_package()
        album.set_stickers(op)


def main():

    global stickers
    global album

    stickers = Stickers()
    album = Album()

    print(40 * ("-"))
    print("VAI SE QUATAR".center(40))
    print("FIFA WORLD CUP QATAR 2022".center(40))
    print(40 * ("-"))

    while True:
        print(
            "\nEscolha uma opção: "
            "\n1- Abrir pacotes e colar no álbum"
            "\n2- Mostrar álbum"
            "\n3- Mostrar Figurinhas repetidas"
            "\n4- Mostrar Figurinhas faltantes"
            "\n5- Mostrar Figurinhas salvas no CSV"
            "\n6- Mostrar Figurinhas Repetidas salvas no CSV"
            "\n7- Mostrar Figurinhas Faltantes salvas no CSV"
            "\n8- Verificar se a figurinha está no álbum"
            "\n9- Verificar se a figurinha é repetida"
            "\n10- Trocar figurinha"
            "\n11- Fechar programa"
        )

        opcaoMatriz = int(input("\nInsira a opção desejada: "))
        if opcaoMatriz == 1:

            opcao = int(input("\nQuantos pacotes com 5 figurinhas deseja abrir: "))
            number_sticker(opcao)

            qnt_unicas = len(album.get_stickers_in_album())
            qnt_repetidas = len(album.get_repeated_stickers())

            df = pd.DataFrame(
                [[qnt_unicas, qnt_repetidas]], columns=["Únicas", "Repetidas"]
            )
            df.index = ["Quantidades"]

            print("\n")
            print(df)

        elif opcaoMatriz == 2:
            print(sorted(album.get_stickers_in_album()))

            relatorio = int(
                input(
                    "\nDeseja criar relatório\n1- Sim \n2- Não\nInsira a opção desejada: "
                )
            )

            if relatorio == 1:
                album.create_stickers_in_album_report()
                print("Relatório criado")
            elif relatorio == 2:
                pass

        elif opcaoMatriz == 3:

            dict_df = album.get_repeated_stickers()
            dict_keys = dict_df.keys()
            dict_value = dict_df.values()

            details = {"Figurinhas": list(dict_keys), "Repetidas": list(dict_value)}

            df = pd.DataFrame(details)

            print(df.to_string(index=False))

            relatorio = int(
                input(
                    "\nDeseja criar relatório\n1- Sim \n2- Não\nInsira a opção desejada: "
                )
            )

            if relatorio == 1:
                album.create_repeated_stickers_report()
                print("Relatório criado")
            elif relatorio == 2:
                pass

        elif opcaoMatriz == 4:
            print(album.get_missing_stickers(stickers.get_all_stickers()))

            relatorio = int(
                input(
                    "\nDeseja criar relatório\n1- Sim \n2- Não\nInsira a opção desejada: "
                )
            )

            if relatorio == 1:
                album.create_missing_stickers_in_album_report(
                    stickers.get_all_stickers()
                )
                print("Relatório criado")
            elif relatorio == 2:
                pass

        elif opcaoMatriz == 5:
            if album.read_stickers_in_album_report():
                print((album.read_stickers_in_album_report()[1:]))
                print(
                    "Figurinhas: "
                    + str(len((album.read_stickers_in_album_report()[1:])))
                    + " Unidades"
                )
            else:
                print("Não possui CSV das figurinhas salvas")
        elif opcaoMatriz == 6:
            if album.read_repeated_stickers_report():
                print((album.read_repeated_stickers_report()[1:]))
                print(
                    "Figurinhas repetidas: "
                    + str(len((album.read_repeated_stickers_report()[1:])))
                    + " Unidades"
                )
            else:
                print("Não possui CSV das figurinhas Repetidas")
        elif opcaoMatriz == 7:
            if album.read_missing_stickers_in_album_report():
                print((album.read_missing_stickers_in_album_report()[1:]))
                print(
                    "Figurinhas Faltantes: "
                    + str(len((album.read_missing_stickers_in_album_report()[1:])))
                    + " Unidades"
                )
            else:
                print("Não possui CSV das figurinhas faltantes")
        elif opcaoMatriz == 8:
            sticker_ = input("\nDigite o nome da figurinha desejada: ").upper()
            if album.verify_sticker_in_album(sticker_):
                print("\n----- Já possui no álbum -----")
            else:
                print("\n----- Não possui no álbum -----")

        elif opcaoMatriz == 9:
            sticker_repeat = input("\nDigite o nome da figurinha desejada: ").upper()
            if album.verify_sticker_in_repeated_stickers(sticker_repeat):
                print("\n----- Figurinha repetida -----")
            else:
                print("\n----- Figurinha não repetida -----")

        elif opcaoMatriz == 10:
            sticker_repeat_change = input(
                "\nDigite o nome da figurinha desejada: "
            ).upper()
            if album.change_sticker(sticker_repeat_change):
                print("\n----- Figurinha Trocada -----")
            else:
                print("\n----- Figurinha não está no monte de repetidas -----")

        elif opcaoMatriz == 11:
            break


if __name__ == "__main__":
    main()
