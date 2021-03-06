# -*- coding: utf-8 -*-

import csv
import numpy as np
import numpy as np
import matplotlib.pyplot as plt
import APITest 
import saveDataSet
# Numero de epocas e de padrões (q)
numEpocas = 100
q = 15
# Taxa de Aprendizado
eta = 0.0001


abertura = np.array([])
fechamento = np.array([])
maximo = np.array([])
minimo = np.array([])
volume = np.array([])
dataG = np.array([])
d = np.array([])
XD = ['','','','','','','','','','','','','','','']
dG = np.array([])
arq = "data"
dataOrigem = input("Origem do dataSet - 1 para web 2 para local: ")
for cont in range(0,q):
    dia = 1 + cont
    print(dia)
    arq = 'data'+str(cont)
    print(arq)
    if(dataOrigem == 1):
        APITest.getDataWeb('2019-08-'+str(dia),arq)
    abertura = np.array([])
    fechamento = np.array([])
    maximo = np.array([])
    minimo = np.array([])
    volume = np.array([])
    with open(arq+'.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            abertura = np.append(abertura,row[1])
            fechamento = np.append(fechamento,row[2])
            maximo = np.append(maximo,row[3])
            minimo = np.append(minimo,row[4])
            volume = np.append(volume,row[5])

    abertura = np.delete(abertura,0)
    #print(abertura)
    fechamento = np.delete(fechamento,0)

    maximo = np.delete(maximo,0)

    minimo = np.delete(minimo,0)

    volume = np.delete(volume,0)

    # Vetor de classificação desejada
    dAb = abertura
    dFc = fechamento
    dMa = maximo
    dMi = minimo
    dVo = volume

    dAb = np.delete(dAb,(dAb.size-1)) 
    dFc = np.delete(dFc,(dFc.size-1)) 
    dMa = np.delete(dMa,(dMa.size-1)) 
    dMi = np.delete(dMi,(dMi.size-1)) 
    dVo = np.delete(dVo,(dVo.size-1)) 
    '''
    for a in dataG:
        print(a)
    '''
    XD[cont] = np.hstack((abertura,fechamento,maximo,minimo,volume))
    d = np.append(d,dAb)    
    print(d.shape)
    #print(d)
# Inicia aleatoriamente as matrizes de pesos
W = np.zeros([1,996])

# Array para armazenar os erros
e = np.zeros(q)

# Bias
bias = 1
for a in XD:
    print(a.size)
X = np.vstack((XD[0],XD[1],XD[2],XD[3],XD[4],XD[5],XD[6],XD[7],XD[8],XD[9],XD[10],XD[11],XD[12],XD[13],XD[14]))
d = np.delete(d,0,0)

'''
=======================================
            TREINAMENTO
=======================================
'''

for i in range(numEpocas):
    for j in range(q):
        # insere o bias no vetor de entrada
        Xb = np.hstack((bias, X[j,:]))
        print(Xb)
        #print(W1.size)
        Xb = map(float,Xb)

        # Saida da camada Escondida
        V = np.dot(W,Xb)
        
        
        # Saida da rede neural
        #print(d[j])
        e = float(d[j]) - V
        e = np.asarray(e)


        # Imprime o erro da epoca e o erro total
        #print('i = ' + str(i) + '   E = ' + str(E))

        # Backpropagation do erro e calculo do gradiente
        #print(e.size)
        #print(Y.size)
        print(str(100*i/numEpocas)+"%")
        print(V)
        

        W = W + eta*e[j]*Xb

        

#print("Erro total medio = " + str(Etm))
print("----------------")
plt.plot(e)
plt.show()
