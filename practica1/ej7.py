# 7 Dar ejemplos (gráfica o analíticamente) de funciones f para la cual el método de Newton:
# a) no encuentre una raíz para determinado valor inicial, pero sí con otro valor inicial
# b) encuentre una raíz para cualquier valor inicial
# c) caiga en un ciclo para determinado valor inicial (oscile)
# d) converja más “lentamente” a una raíz (no cuadráticamente)

import math

# Funciones
def fa(x): return math.log(x)
def fb(x): return x + 1
def fc(x): return math.cos(x)
def fd(x): return x * 2 + 1

# Derivadas
def dfa(x): return 1 / x
def dfb(x): return 1
def dfc(x): return - (math.sin(x))
def dfd(x): return 2

# Newton
def newton(x0, f, df):
    for _ in range(0, 3):
        x1 = x0 - (f(x0) / df(x0))
        print(x1)
        x0 = x1


newton(-10, fd, dfd)
#******************************************************************************
#******************************** Observaciones *******************************
#******************************************************************************
# a. 
# Con newton(0, fa, dfa) con 0 como valor inicial no se puede encontrar la raiz pero si con 0.1,
# por ejemplo, ya que es una función que converge en 0
# b.
# Se puede encontrar la raiz con cualquier valor inicial ya que su imagen convierge hacia los infinito
# y su derivada nunca va a ser 0
# c.
# Se puede encontrar distintas raices dependiendo el valor inicial, siempre se acercara al mas cerca del valor
# inicial, pero vale aclarar que al elegir 0, no se va a poder realizar ya que no se puede dividir por 0 
# (valor de su derivada al ser 0 el valor inicial)
# d.
# Una funcion de orden de convergencia linea se acerca mas lentamente a la raiz que una funcion de orden
# de convergencia lineal

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        