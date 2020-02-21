# -*- coding: utf-8 -*-

import csv
import numpy as np
import numpy as np
import matplotlib.pyplot as plt

# Numero de epocas e de padrões (q)
numEpocas = 10000
q = 5
# Taxa de Aprendizado
eta = 0.0001
m = 5   # Numero de Neeuronios na camada de entrada
N = 1   # Numero de Neeuronios na camada escondida
L = 1   # Numero de Neeuronios na camada de saida

abertura = np.array([])
fechamento = np.array([])
maximo = np.array([])
minimo = np.array([])
volume = np.array([])
with open('data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        abertura = np.append(abertura,row[1])
        fechamento = np.append(fechamento,row[2])
        maximo = np.append(maximo,row[3])
        minimo = np.append(minimo,row[4])
        volume = np.append(volume,row[5])

abertura = np.delete(abertura,0)

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

d = dMa
print(d.shape)
print(d)
# Inicia aleatoriamente as matrizes de pesos
W1 = np.random.random((N, m+1))
W2 = np.random.random((N, N+1))

# Array para armazenar os erros
E = np.zeros(q)
Etm = np.zeros(numEpocas)

# Bias
bias = 1

# Entrada do Perceptron
X = np.vstack((abertura,fechamento,maximo,minimo,volume))


'''
=======================================
            TREINAMENTO
=======================================
'''

for i in range(numEpocas):
    for j in range(q):
        # insere o bias no vetor de entrada
        Xb = np.hstack((bias, X[:,j]))
        
        Xb = map(float,Xb)

        # Saida da camada Escondida
        O1 = np.tanh(W1.dot(Xb))

        # Incluindo o bias
        O1b = np.insert(O1, 0, bias)

        # Saida da rede neural
        Y = np.tanh(W2.dot(O1b))
        print(d[j])
        e = float(d[j]) - Y
        e = np.asarray(e)

        # Erro total
        E[j] = (e.transpose().dot(e))/2

        # Imprime o erro da epoca e o erro total
        #print('i = ' + str(i) + '   E = ' + str(E))

        # Backpropagation do erro e calculo do gradiente
        print(e.size)
        print(Y.size)
        
        delta2 = np.diag(e).dot((1-Y*Y))
        vdelta2 = (W2.transpose()).dot(delta2)
        delta1 = np.diag(1 - O1b*O1b).dot(vdelta2)

        #atualização dos pesos
        W1 = W1 + eta*(np.outer(delta1[1:], Xb))
        W2 = W2 + eta*(np.outer(delta2, O1b))

    Etm[i] = E.mean()

#print("Erro total medio = " + str(Etm))
print("----------------")
plt.plot(Etm)
plt.show()
