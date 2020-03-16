import requests
from pprint import pprint
from datetime import *
import csv
'''
{u'lowest': 16419.00017, u'opening': 16518.69886, u'volume': 15692299.91002463, u'amount': 11831, u'avg_price': 18581.62995285, u'date': u'2019-04-02', u'closing': 19479.89, u'highest': 19990, u'quantity': 844.5061036}
'''
def funcAtivacao(diferenca):
    if(diferenca>=0):
        return 1
    else:
        return -1
        

def getInfos(data):
    hoje = datetime.strptime(data,'%Y-%m-%d')
    dtSet = 'data'
    dataFile = open(dtSet+".csv", "w+")
    inicio = hoje - timedelta(days=200)
    writer = csv.writer(dataFile)
    writer.writerow(['Data','Abertura','Fechamento','Maximo','Minimo','Volume'])
    for i in range(0, 199):
        inicio = inicio + timedelta(days=1)
        ano = str(inicio.year)
        mes = str(inicio.month)
        dia = str(inicio.day)
        print(dia)
        #print(i)
        r = requests.get('https://www.mercadobitcoin.net/api/BTC/day-summary/'+ano+'/'+mes+'/'+dia+'/')
        #print(r)
        r_dict = r.json()
        #print(r_dict)
        writer.writerow([r_dict['date'],r_dict['opening'],r_dict['closing'],r_dict['highest'],r_dict['lowest'],r_dict['volume']])
        

#getInfos('2020-03-16')
def getDataWeb(data):
    cont = 0
    arq = 'data'
    hoje = datetime.strptime(data,'%Y-%m-%d')
    print(hoje)
    dia = hoje

    arqSaidas = open("saidas.csv", "w+") 
    writerSaidas = csv.writer(arqSaidas)
    writerSaidas.writerow(['Data','subida','anterior','atual','diferenca'])
    for day in range(0,10):
        dia = hoje + timedelta(days=int(day))
        anterior = dia - timedelta(days=1)
        inicio = dia - timedelta(days=200)
        print(anterior)
        
        ano = str(dia.year)
        mes = str(dia.month)
        dia = str(dia.day)
        
        diaAnt = str(anterior.day)
        reqAtual = requests.get(
                'https://www.mercadobitcoin.net/api/BTC/day-summary/'+ano+'/'+mes+'/'+dia+'/')
        reqAnt = requests.get(
                'https://www.mercadobitcoin.net/api/BTC/day-summary/'+ano+'/'+mes+'/'+diaAnt+'/')

        atual_dict = reqAtual.json()            
        opAtual = atual_dict['opening']
        anterior_dict = reqAnt.json()
        opAnterior = anterior_dict['opening']
        diferenca = int(opAtual) - int(opAnterior)
        subida = funcAtivacao(diferenca)

        print(opAnterior)
        print(opAtual)
        print(diferenca)
        print(subida)
        print("")
        
        writerSaidas.writerow([atual_dict['date'],subida,opAnterior,opAtual,diferenca])
    

        
        dtSet = 'data' + str(day)
        dataFile = open(dtSet+".csv", "w+")
            
        writer = csv.writer(dataFile)
        writer.writerow(['Data','Abertura','Fechamento','Maximo','Minimo','Volume'])
        for i in range(0, 199):
            inicio = inicio + timedelta(days=1)
            ano = str(inicio.year)
            mes = str(inicio.month)
            dia = str(inicio.day)
            print(dia)
            #print(i)
            r = requests.get('https://www.mercadobitcoin.net/api/BTC/day-summary/'+ano+'/'+mes+'/'+dia+'/')
            #print(r)
            r_dict = r.json()
            #print(r_dict)
            writer.writerow([r_dict['date'],r_dict['opening'],r_dict['closing'],r_dict['highest'],r_dict['lowest'],r_dict['volume']])
        
            #print(str(r_dict['date']) + ' // ' + str(r_dict['opening']) + ' // ' + str(r_dict['closing']) + ' // ' + str(r_dict['highest']) + ' // ' + str(r_dict['lowest']) + ' // ' + str(r_dict['volume']))
#getDataWeb('2020-02-15')