from pygal.maps.world import COUNTRIES


def get_country_code(country_name):
    """Return the Pygal 2-digit country code for the given country"""
    other = {
        'Bolivia': 'bo',
        'Congo, Dem. Rep.': 'cd',
        'Congo, Rep.': 'cg',
        'Dominica': 'do',
        'Egypt, Arab Rep.': 'eg',
        'Gambia, The': 'gm',
        'Hong Kong SAR, China': 'hk',
        'Iran, Islamic Rep.': 'ir',
        'Korea, Dem. Rep.': 'kp',
        'Korea, Rep.': 'kr',
        'Kyrgyz Republic':'kg',
        'Lao PDR': 'la',
        'Libya': 'ly',
        'Macao SAR, China': 'mo',
        'Macedonia, FYR': 'mk',
        'Moldova': 'md',
        'Slovak Republic': 'sk',
        'Tanzania': 'tz',
        'Venezuela, RB': 've',
        'Vietnam': 'vn',
        'West Bank and Gaza': 'ps',
        'Yemen, Rep.': 'ye'
    }

    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        if country_name in other:
            return other[country_name]
    return None
