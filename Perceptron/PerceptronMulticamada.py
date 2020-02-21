# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def funcaoAtivacao(valor):
    if(valor>0):
        return 1
    else: 
        return (-1)

# Numero de epocas e de padrões (q)
numEpocas = 100
q = 13

# Taxa de Aprendizado
eta = 0.01

m = 2   # Numero de Neeuronios na camada de entrada
N = 1   # Numero de Neeuronios na camada escondida
L = 1   # Numero de Neeuronios na camada de saida

# Carrega os dados de treinamento
peso = np.array([113, 122, 107,  98, 115, 120, 104, 108, 117, 101, 112, 106, 116])
pH   = np.array([6.8, 4.7, 5.2, 3.6, 2.9, 4.2, 6.3, 4.0, 6.3, 4.2, 5.6, 3.1, 5.0])

# Vetor de classificação desejada
d = np.array([-1,1,-1,1,1,1,-1,1,-1,1,-1,1,-1])

# Inicia aleatoriamente as matrizes de pesos
W1 = np.random.random((N, m+1))
W2 = np.random.random((N, N+1))

# Array para armazenar os erros
E = np.zeros(q)
Etm = np.zeros(numEpocas)

# Bias
bias = 1

# Entrada do Perceptron
X = np.vstack((peso, pH))


'''
=======================================
            TREINAMENTO
=======================================
'''

for i in range(numEpocas):
    for j in range(q):

        # insere o bias no vetor de entrada
        Xb = np.hstack((bias, X[:,j]))

        # Saida da camada Escondida
        O1 = np.tanh(W1.dot(Xb))

        # Incluindo o bias
        O1b = np.insert(O1, 0, bias)

        # Saida da rede neural
        Y = np.tanh(W2.dot(O1b))
        e = d[j] - Y

        # Erro total
        E[j] = (e.transpose().dot(e))/2

        # Imprime o erro da epoca e o erro total
        #print('i = ' + str(i) + '   E = ' + str(E))

        # Backpropagation do erro e calculo do gradiente
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

'''
=======================================
            TESTE DA REDE
=======================================
'''

# Carrega os dados de treinamento
peso = input("peso ")
pH   = input("ph ")

# Vetor de classificação desejada.
d = np.array([-1, -1, 1, 1, 1])
Error_Test = np.zeros(5)


# Insere o bias no vetor de entrada.
Xb = [peso,pH,bias]

# Saída da Camada Escondida.
O1 = W1.dot(Xb)              

# Incluindo o bias.
O1b = np.insert(O1, 0, bias)

# Saida
Y = np.tanh(W2.dot(O1b))      #tanh é a sigmoid       
print(Y)


