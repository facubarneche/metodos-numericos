# 12.
# a) ¿Qué ocurriría si se usa el método de Newton para resolver una ecuación lineal con una
# incógnita? Analizar todos los casos.
# b) Misma pregunta, qué ocurriría, con el método de bisección.
# c) ¿Y con el método secante?

import math

# Funciones
def fa(x): return x * 2 + 1


# Derivadas
def dfa(x): return 2

# Newton
def newton(x0, f, df):
    x1 = x0 - (f(x0) / df(x0))
    print(x1)
    x0 = x1

# Bisección
def biseccion(a, b, e, myFunc):
    p = (a + b) / 2
    print(p)
    if((b - a) < e):
        print(p, ' (Raiz Apróximada)')
        return p
    if(myFunc(p) > 0): return biseccion(a, p, e, myFunc)
    else: return biseccion(p, b, e, myFunc)

# Secante
def secante (x0, x1):
    x2 = x1 - (fa(x1) * (x1 - x0) / (fa(x1) - fa(x0)))
    print(x2)


print('Newton==========================')
newton(-2000000, fa, dfa)
print('Bisección=======================')
biseccion(-2000000, 2000000, 0.001, fa)
print('Secante=========================')
secante(-2000000, 2000000)


#******************************************************************************
#******************************** Observaciones *******************************
#******************************************************************************
# Netwon
# Se puede notar que con funciones lineales Newton encuentra la raiz en la primera iteración
#
# Biseccion
# En el metodo de bisección si bien puede encontrarse una raiz en la primera iteración, mayormente
# necesitará un numero mayor de iteraciones ya que depende muchisimo de los parametros de busqueda recibidos
# 
# Secante
# Se puede notar que secante se asemeja a Newton en todo sentido ya que tambien es capas de encontrar
# la raiz de una función lineal en una interación