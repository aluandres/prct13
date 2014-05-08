#!/usr/bin/python 
#!encoding: UTF-8
import sys
import modulo
import time
import pylab as dibujo


argumentos = sys.argv[1:]
if (len(argumentos) == 2 ):
  n = int (argumentos[0])
  aproximaciones = int (argumento[1])
  umbral = []
  for i in range (2,7):
    umbral.append(float (argumentos[i]))
  nombre_fichero = argumentos[7]
else:
  print "Introduzca el numero de intervalos (n>o)"
  n = int (raw_input())
  print "Introduzca el numero de aproximaciones:"
  aproximaciones = int (raw_input ());
  print "Introduzca 5 umbrales de error:"
  umbral = []
  for i in range (5):
    print "Introduzca el umbral", i, ""
    umbral.append (float (raw_input ()))
    lista=[]
if (n>0):
  for i in range (5):
    start =time.time()
    porcentaje = modulo.error (n, aproximaciones, umbral[i])
    finish = time.time() - start
    lista.append (finish)
  x=[1,2,3,4,5]
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
  dibujo.show() 
  

else:
  print "El valor de los intervalos tiene que ser mayor que 0"