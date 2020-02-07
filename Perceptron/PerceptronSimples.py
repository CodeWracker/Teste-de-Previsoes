# -*- coding: utf-8 -*-
import numpy as np

# Define o numero de epocas e o numero de amostras (q)
numEpocas = 70000
q = 6

# Atributos
peso = np.array([113,122,107,98,115,120])
pH = np.array([6.8,4.7,5.2,3.6,2.9,4.2])

# Bias
bias = 1

# Entrada do perceptron
X = np.vstack((peso,pH))
Y = np.array([-1,1,-1,-1,1,1])

# Taxa de aprendizado
eta = 0.1

# Define o vetor de pesos
W = np.zeros([1,3]) # Duas entradas + o bias

# Array para armazenar os erros
e = np.zeros(6)

def funcaoAtivacao(valor):
    # A função de ativação degrau bipolar
    if(valor < 0):
        return (-1)
    else:
        return (1)

for j in range(numEpocas):
    for k in range(q):
        # insere o bias no vetor X
        Xb = np.hstack((bias,X[:,k]))

        # Calcula o campo induzido
        V = np.dot(W, Xb)

        # calcula a saida
        Yr =  funcaoAtivacao(V)

        # Calcula o erro: e = (Y - Yr)
        e[k] = Y[k] - Yr

        # Treinamento do Perceptron
        W = W + eta*e[k]*Xb
        print("Erro: " + str(e[k]))
inputPeso = input("peso ")
inputPH = input("pH ")
Xb = np.hstack((bias, inputPeso, inputPH))
V = np.dot(W, Xb)
Yr = funcaoAtivacao(V)
if(Yr>0):
    print("Maca")
else:
    print("Laranja")

