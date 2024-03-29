# 8 Para el método de bisección:
# a) Mostrar ejemplos en los cuales la iteración permanece siempre del lado derecho de la raíz.
# (Análogamente podría pedirse para el lado izquierdo.)
# b) ¿Es cierto que si bisección converge a una raíz, siempre será hacia la raíz más cercana
# del punto inicial?

import math

# Funciones
def fa(x): return math.sin(x)
def fb(x): return math.cos(x)

# Bisección
def biseccion(a, b, e, myFunc):
    p = (a + b) / 2
    print(p)
    if((b - a) < e):
        print(p, ' (Raiz Apróximada)')
        return p
    if(myFunc(p) > 0): return biseccion(a, p, e, myFunc)
    else: return biseccion(p, b, e, myFunc)


biseccion(-100, 100, 0.001, fa)
#******************************************************************************
#******************************** Observaciones *******************************
#******************************************************************************
# a. En la fa se puede ver como la funcion converge siempre para el lado derecho
# b. No, por ejemplo, en la funcion b se puede ver como siempre tienda a la raiz mas lejano del lado izquierdo