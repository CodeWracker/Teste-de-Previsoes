import requests
from pprint import pprint
from datetime import *

hoje = date.today()
inicio = hoje - timedelta(days=365)
print(hoje)
for i in range(0, 364):
    inicio = inicio + timedelta(days=1)
    ano = str(inicio.year)
    mes = str(inicio.month)
    dia = str(inicio.day)
    '''print(ano)
    print(mes)
    print(dia)'''
    r = requests.get(
        'https://www.mercadobitcoin.net/api/BTC/day-summary/'+ano+'/'+mes+'/'+dia+'/')
    r_dict = r.json()
    print(str(r_dict['date'])+': ' +
          str(r_dict['opening']) + ' // ' + str(r_dict['closing']))
