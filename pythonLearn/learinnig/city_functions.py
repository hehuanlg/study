def world(city,country,population=''):
    if population:
        full_city = city.title() + ',' + ' ' + country.title() + ' ' + '- population ' + population
        return full_city
    else:
        full_city = city.title() + ',' + ' ' + country.title()
        return full_city
