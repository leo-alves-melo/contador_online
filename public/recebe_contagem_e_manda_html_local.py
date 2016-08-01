# encoding: utf-8
#programa que recebe a contagem via serial e coloca a imagem do grafico da contagem num arquivo de html que se atualiza

import serial
import sys
import time
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np


def plotaBarra(nEntradas, nSaidas):
	n_groups = 2

	means_men = (nEntradas, nSaidas)

	fig, ax = plt.subplots()

	index = np.arange(n_groups)
	bar_width = 0.15

	opacity = 0.4

	rects1 = plt.bar(index, means_men,  bar_width, alpha=opacity, color='b')

	#plt.xlabel('Tipo de passagem')
	plt.ylabel(u'Valor absoluto', size=20)
	plt.title(u'Número de passagens', size=20)
	plt.xticks(index + bar_width/2, ('Entradas', u'Saídas'), size=16)
	plt.legend()
	plt.grid(True)
	plt.axis((0, 2, 0, nSaidas + nEntradas + 1))		

	plt.tight_layout()
	#plt.show()
	plt.ylim(0,nEntradas + nSaidas + 1)
	plt.savefig('grafico.png')

nEntradas = 0	
nSaidas = 0

plotaBarra(nSaidas,nEntradas)

print "Fazendo conexao via bluetooth"
zero = serial.Serial("/dev/rfcomm0", 115200) # Upload using bluetooth



while True:
	received = zero.readline()

	if received[0] == 'e':
		nEntradas = nEntradas + 1
		plotaBarra(nEntradas, nSaidas)

	elif received[0] == 's':
		nSaidas = nSaidas + 1
		plotaBarra(nEntradas, nSaidas)

	print received + "nEntradas: " + str(nEntradas) + " - nSaidas :" + str(nSaidas)
