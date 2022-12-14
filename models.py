from random import choice
from utils import save_csv_file


class Stickers:
    def __init__(self):
        self.__stickers = []
        self.__create_sticker()

    def __create_countries(self):
        return ['QAT', 'ECU', 'SEN', 'NED',
                'ENG', 'IRN', 'USA', 'WAL',
                'ARG', 'KSA', 'MEX', 'POL',
                'FRA', 'AUS', 'DEN', 'TUN',
                'ESP', 'CRC', 'GER', 'JPN',
                'BEL', 'CAN', 'MAR', 'CRO',
                'BRA', 'SRB', 'SUI', 'CMR',
                'POR', 'GHA', 'URU', 'COR']

    def __create_sticker(self):
        countries = self.__create_countries()
        self.__stickers = ['00', 'FWC1', 'FWC2', 'FWC3', 'FWC4',
                   'FWC5', 'FWC6', 'FWC7', 'FWC8', 'FWC9',
                   'FWC10', 'FWC11', 'FWC12', 'FWC13', 'FWC14',
                   'FWC15', 'FWC16', 'FWC17', 'FWC18']
        for country in countries:
            for cont in range(1, 21):
                self.__stickers.append(f'{country}{cont}')
        self.__stickers += ['FWC19', 'FWC20', 'FWC21', 'FWC22',
                    'FWC23', 'FWC24', 'FWC25', 'FWC26',
                    'FWC27', 'FWC28', 'FWC29', 'C1',
                    'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8']
        return self.__stickers

    def open_package(self):
        stickers_in_package = []
        for _ in range(5):
            stickers_in_package.append(choice(self.__stickers))
        return stickers_in_package

    def get_all_stickers(self):
        return self.__stickers


class Album:
    def __init__(self):
        self.__stickers_in_album = []
        self.__repeated_stickers = {}

    def verify_sticker_in_album(self, sticker):
        if sticker in self.__stickers_in_album:
            return True
        else:
            return False

    def set_stickers(self, stickers):
        for sticker in stickers:
            if not self.verify_sticker_in_album(sticker):
                self.__glue_sticker(sticker)
            else:
                self.__add_in_repeateds(sticker)

    def __glue_sticker(self, sticker):
        self.__stickers_in_album.append(sticker)

    def __add_in_repeateds(self, sticker):
        if sticker in self.__repeated_stickers.keys():
            self.__repeated_stickers[sticker] += 1
        else:
            self.__repeated_stickers[sticker] = 1

    def get_stickers_in_album(self):
        return self.__stickers_in_album

    def get_repeated_stickers(self):
        return self.__repeated_stickers

    def create_sticker_in_album_report(self):
        save_csv_file('stickers_in_album.csv', self.__stickers_in_album, ['sticker'])

    def create_missing_stickers_in_album_report(self, all_stickers):
        missing_stickers = [sticker for sticker in all_stickers if sticker not in self.__stickers_in_album]
        save_csv_file('missing_stickers.csv', missing_stickers, ['missing sticker'])

    def create_repeated_stickers_report(self):
        save_csv_file('repeated_stickers.csv', self.__repeated_stickers.items(), ['sticker', 'quantity'])

    def change_sticker(self, sticker):
        try:
            self.__repeated_stickers[sticker] -= 1
            if self.__repeated_stickers[sticker] <= 0:
                del self.__repeated_stickers[sticker]
            return True
        except KeyError:
            return False

# to do:
# Verificar se precisa ter um atributo das figurinhas faltantes