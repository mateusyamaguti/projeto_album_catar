

class Album:
    def __init__(self):
        self._create_countries()
        self._figure = []

    def _create_countries(self):
        countries = ['QAT', 'ECU', 'SEN', 'NED',
                   'ENG', 'IRN', 'USA', 'WAL',
                   'ARG', 'KSA', 'MEX', 'POL',
                   'FRA', 'AUS', 'DEN', 'TUN',
                   'ESP', 'CRC', 'GER', 'JPN',
                   'BEL', 'CAN', 'MAR', 'CRO',
                   'BRA', 'SRB', 'SUI', 'CMR',
                   'POR', 'GHA', 'URU', 'COR']
        return countries

    def _create_figure(self):
        countries = self._create_countries()
        figures = ['00', 'FWC1', 'FWC2', 'FWC3', 'FWC4',
                   'FWC5', 'FWC6', 'FWC7', 'FWC8', 'FWC9',
                   'FWC10', 'FWC11', 'FWC12', 'FWC13', 'FWC14',
                   'FWC15', 'FWC16', 'FWC17', 'FWC18']
        for countrie in countries:
            for cont in range(1, 21):
                figures.append(f'{countrie}{cont}')
        figures += ['FWC19', 'FWC20', 'FWC21', 'FWC22',
                    'FWC23', 'FWC24', 'FWC25', 'FWC26',
                    'FWC27', 'FWC28', 'FWC29', 'C1',
                    'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8']
        return figures

def create_control():
    control = []
    figures = Album._create_figure()
    for figure in figures:
        control.append((figure,''))
        return control
