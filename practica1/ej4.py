# 4 Indicar cómo se puede usar el método de Newton para calcular la función
# f(x) = ln x para x > 0, usando otras operaciones: +. -, *, / y exponencial. Discutir una posible
# implementación práctica de esto

import math;

# Funciones

def f(x): return math.log(x)

# Derivadas
def df(x): return 1 / (2 * math.sqrt(x))


# Newton
def myFunc(x0, x1):
    x2 = x1 - ( (f(x1) * (x1 - x0)) / (f(x1) - f(x0)))
    print(x2)
    x0 = x1
    x1 = x2

myFunc(1, 10)

#******************************************************************************
#******************************** Observaciones *******************************
#******************************************************************************
# Este metodo se asemeja a Newton, vale destacar que se agrega una X arbitrariamente mas (X1 y X2)
# Este caso en general le cuesta mucho aproximar mientras mas lejos esten las X1 y X2 de la raiz
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        