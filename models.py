

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

    def open_package():
        
        # Crie uma estrutura que preencha automaticamente 5 figurinhas
        # ( número de figurinhas presente em um pacotinho)
        
        # retornar uma lista com 5 figurinhas
        pass


class Album:
    def __init__(self):
        self.stickers = []
        self.create_sticker_slots()

        # repetidos = [(QAT1, 0), (ECU1, 0) ...]

    def create_countries(self):
        return ['QAT', 'ECU', 'SEN', 'NED',
                'ENG', 'IRN', 'USA', 'WAL',
                'ARG', 'KSA', 'MEX', 'POL',
                'FRA', 'AUS', 'DEN', 'TUN',
                'ESP', 'CRC', 'GER', 'JPN',
                'BEL', 'CAN', 'MAR', 'CRO',
                'BRA', 'SRB', 'SUI', 'CMR',
                'POR', 'GHA', 'URU', 'COR']

    def create_sticker_slots(self):
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

    def verify_if_i_have_the_sticker(self, *sticker):
        if True:
            pass
        else:
            pass

    def glue_sticker(self, sticker):
        pass

    def add_in_repetidas(self, sticker):
        pass




