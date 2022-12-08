from random import choice

class Stickers:
    def __init__(self):
        self.stickers = []
        self.create_sticker()

    def create_countries(self):
        return ['QAT', 'ECU', 'SEN', 'NED',
                'ENG', 'IRN', 'USA', 'WAL',
                'ARG', 'KSA', 'MEX', 'POL',
                'FRA', 'AUS', 'DEN', 'TUN',
                'ESP', 'CRC', 'GER', 'JPN',
                'BEL', 'CAN', 'MAR', 'CRO',
                'BRA', 'SRB', 'SUI', 'CMR',
                'POR', 'GHA', 'URU', 'COR']

    def create_sticker(self):
        countries = self.create_countries()
        self.stickers = ['00', 'FWC1', 'FWC2', 'FWC3', 'FWC4',
                   'FWC5', 'FWC6', 'FWC7', 'FWC8', 'FWC9',
                   'FWC10', 'FWC11', 'FWC12', 'FWC13', 'FWC14',
                   'FWC15', 'FWC16', 'FWC17', 'FWC18']
        for country in countries:
            for cont in range(1, 21):
                self.stickers.append(f'{country}{cont}')
        self.stickers += ['FWC19', 'FWC20', 'FWC21', 'FWC22',
                    'FWC23', 'FWC24', 'FWC25', 'FWC26',
                    'FWC27', 'FWC28', 'FWC29', 'C1',
                    'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8']
        return self.stickers

    def open_package(self):
        stickers_in_package = []
        for _ in range(5):
            stickers_in_package.append(choice(self.stickers))
        return stickers_in_package


class Album:
    def __init__(self):
        self.stickers_in_album = []
        self.repeated_stickers = {}

    def verify_if_i_have_the_sticker(self, stickers):
        for sticker in stickers:
            if not sticker in self.stickers_in_album:
                self.glue_sticker(sticker)
            else:
                self.add_in_repeateds(sticker)

    def glue_sticker(self, sticker):
        self.stickers_in_album.append(sticker)

    def add_in_repeateds(self, sticker):
        if sticker in self.repeated_stickers.keys():
            self.repeated_stickers[sticker] += 1
        else:
            self.repeated_stickers[sticker] = 1
