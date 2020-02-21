import requests
from pprint import pprint
from datetime import *
import csv
'''
{u'lowest': 16419.00017, u'opening': 16518.69886, u'volume': 15692299.91002463, u'amount': 11831, u'avg_price': 18581.62995285, u'date': u'2019-04-02', u'closing': 19479.89, u'highest': 19990, u'quantity': 844.5061036}
'''

def getData(data):
    hoje = datetime.strptime(data,'%Y-%m-%d')
    inicio = hoje - timedelta(days=200)
    print(hoje)
    with open("data.csv", "w+") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Data','Abertura','Fechamento','Maximo','Minimo','Volume'])
        for i in range(0, 199):
            inicio = inicio + timedelta(days=1)
            ano = str(inicio.year)
            mes = str(inicio.month)
            dia = str(inicio.day)
            print(ano)
            print(mes)
            print(dia)
            r = requests.get(
                'https://www.mercadobitcoin.net/api/BTC/day-summary/'+ano+'/'+mes+'/'+dia+'/')
            print(r)
            r_dict = r.json()
            #print(r_dict)
            writer.writerow([r_dict['date'],r_dict['opening'],r_dict['closing'],r_dict['highest'],r_dict['lowest'],r_dict['volume']])

            #print(str(r_dict['date']) + ' // ' + str(r_dict['opening']) + ' // ' + str(r_dict['closing']) + ' // ' + str(r_dict['highest']) + ' // ' + str(r_dict['lowest']) + ' // ' + str(r_dict['volume']))


