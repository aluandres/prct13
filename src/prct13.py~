#!/usr/bin/python
#!encoding: UTF-8

import pylab as dibujo

x=[1,2,3,4,5]
lista = [0.0835480690,0.0828721523,0.0833728313,0.0828859806,0.0849580765]
y1=[11,44,11,22,55]
y2=[30,10,0,30,20]
y3=[0,0,0,0,5]
y4=[12,0,4,4,0]
y5=[38,0,44,38,12]

p1 = dibujo.subplot(211)
dibujo.title ('Porcentajes de fallos')

dibujo.plot (x,y1, marker='o', linestyle=':', color='r', label='Linea 1')
dibujo.plot (x,y2, marker='*', linestyle='--', color='b', label='Linea 2')
dibujo.plot (x,y3, marker='+', linestyle='-', color='m', label='Linea 3')
dibujo.plot (x,y4, marker='^', linestyle='-.', color='c', label='Linea 4')
dibujo.plot (x,y5, marker='s', linestyle=':', color='g', label='Linea 5')

dibujo.legend()
dibujo.xlim(0,6)
dibujo.xticks(x)

p2 = dibujo.subplot(212)

dibujo.plot (x,lista, marker='s', linestyle=':', color='g', label='Linea 5')

dibujo.xlabel ('Intervalo')
dibujo.ylabel ('Tiempo en segundos')
dibujo.legend()


dibujo.show() 