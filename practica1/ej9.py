# 9 Para el método de Newton:
# a) Mostrar ejemplos en los cuales la iteración permanece siempre del lado derecho de la raíz.
# (Análogamente podría permanecer siempre del lado izquierdo.)
# b) ¿Es cierto que si converge, será hacia la raíz más cercana del punto inicial?

import math

# Funciones
def fa(x): return x**3 - 2*x + 2
def fb(x): return math.sin(x)


# Derivadas
def dfa(x): return (3 * (x ** 2)) - 2
def dfb(x): return math.cos(x)

# Newton
def newton(x0, f, df):
    for _ in range(0, 3):
        x1 = x0 - (f(x0) / df(x0))
        print(x1)
        x0 = x1


# newton(-2, fa, dfa)
newton(1.5, fb, dfb)
#******************************************************************************
#******************************** Observaciones *******************************
#******************************************************************************
# a. En la fa se puede ver como la iteración permanece siempre del lado derecho de la raíz.
# b. No, por ejemplo, en la funcion b con 1.5 como valor inicial tiende a la raiz -12.65...