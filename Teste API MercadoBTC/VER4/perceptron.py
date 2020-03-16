# -*- coding: utf-8 -*-

import csv
import numpy as np
import matplotlib.pyplot as plt
import getDataSet
# Numero de epocas e de padrões (q)
numEpocas = 100
q = 10
# Taxa de Aprendizado
eta = 0.0001


abertura = np.array([])
fechamento = np.array([])
maximo = np.array([])
minimo = np.array([])
volume = np.array([])
d = np.array([])
Y = np.array([])
XD = ['','','','','','','','','','']
dG = np.array([])
arq = "data"

with open('saidas.csv', 'r') as file:
    leitor = csv.reader(file)
    for row in leitor:
        Y = np.append(Y,row[1])
Y = np.delete(Y,0)
print(Y)

for cont in range(0,q):
    dia = 1 + cont
    print(dia)
    arq = 'data'+str(cont)
    print(arq)
    abertura = np.array([])
    fechamento = np.array([])
    maximo = np.array([])
    minimo = np.array([])
    volume = np.array([])
    with open(arq+'.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            abertura = np.append(abertura,(row[1]))
            fechamento = np.append(fechamento,(row[2]))
            maximo = np.append(maximo,(row[3]))
            minimo = np.append(minimo,(row[4]))
            volume = np.append(volume,(row[5]))

    abertura = np.delete(abertura,0)
    fechamento = np.delete(fechamento,0)

    maximo = np.delete(maximo,0)

    minimo = np.delete(minimo,0)

    volume = np.delete(volume,0)

    dAb = abertura
    dFc = fechamento
    dMa = maximo
    dMi = minimo
    dVo = volume

    XD[cont] = np.hstack((abertura,fechamento,maximo,minimo,volume))
    #print(XD[cont])
    d = np.append(d,dAb)    
    print(d.shape)
    #print(d)
# Inicia aleatoriamente as matrizes de pesos
W = np.zeros([1,996])

# Array para armazenar os erros
e = np.zeros(q)
print(e)
print(Y)

# Bias
bias = 1

X = np.vstack((XD[0],XD[1],XD[2],XD[3],XD[4],XD[5],XD[6],XD[7],XD[8],XD[9]))

d = np.delete(d,0,0)
print(X[0])

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
        print(Xb.size)
        print(W.size)

        # Saida da camada Escondida
        Xb = map(float,Xb)
        V = np.dot(W,Xb)
        Yr =  getDataSet.funcAtivacao(V)
        
        # Saida da rede neural
        #print(d[j])
        print(Y[j])
        print(Yr)
        e[j] = int(Y[j]) - Yr
        print(e[j])


        # Imprime o erro da epoca e o erro total
        #print('i = ' + str(i) + '   E = ' + str(E))

        # Backpropagation do erro e calculo do gradiente
        #print(e.size)
        #print(Y.size)
        print(str(100*i/numEpocas)+"%")
        Xb = np.asarray(Xb)
        W = W + eta*e[j]*Xb

        

#print("Erro total medio = " + str(Etm))
print("----------------")
plt.plot(e)
plt.show()

data=raw_input("selecione o dia")
getDataSet.getInfos(data)
abertura = np.array([])
fechamento = np.array([])
maximo = np.array([])
minimo = np.array([])
volume = np.array([])
with open('data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        abertura = np.append(abertura,(row[1]))
        fechamento = np.append(fechamento,(row[2]))
        maximo = np.append(maximo,(row[3]))
        minimo = np.append(minimo,(row[4]))
        volume = np.append(volume,(row[5]))

abertura = np.delete(abertura,0)
fechamento = np.delete(fechamento,0)

maximo = np.delete(maximo,0)

minimo = np.delete(minimo,0)

volume = np.delete(volume,0)

XD[cont] = np.hstack((abertura,fechamento,maximo,minimo,volume))
Xb = np.hstack((bias, X[j,:]))
Xb = map(float,Xb)
V = np.dot(W,Xb)
Yr =  getDataSet.funcAtivacao(V)
print("----  Saida: "+str(Yr))