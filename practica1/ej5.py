# 5 Para cada una de las siguientes funciones, indicar alrededor de qué raíces el método de
# Newton converge cuadráticamente:
# f1(x) = x^n (con n >= 1)
# f2(x) = ln x
# f3(x) = √x
# f4(x) = cos x
# f5(x) = 1/x
# f6(x) = sin x / x

import math;

# Funciones

# Le agrego el valor a n por defecto random para que sea polimorfica al resto de funciones ya que la n no es de interes
def f1(x, n = 4): return x ** n

def f2(x): return math.log(x)

def f3(x): return math.sqrt(x)

def f4(x): return math.cos(x)

def f5(x): return 1 / x

def f6(x): return math.sin(x) / x

# Derivadas
def df1(x, n = 4): return (n - 1) * (x ** (n - 1))

def df2(x): return 1 / x

def df3(x): return 1 / 2 * math.sqrt(x)

def df4(x): return - math.sin(x)

def df5(x): return - (1 / x ** 2)

def df6(x): return math.cos(x)

# Newton
def newton(x0, f, df):
    x1 = x0 - (f(x0) / df(x0))
    print(x1)
    x0 = x1

# newton(1, f1, df1)

# newton(1, f2, df2)

# No realizable ya que no se puede realizar la raiz cuadrada de un numero negativo
# newton(1, f3, df3)

# newton(1, f4, df4)

# Converge a infinito pero no tiene raiz
# newton(1, f5, df5)

newton(1, f6, df6)

#******************************************************************************
#******************************** Observaciones *******************************
#******************************************************************************
# Se puede ver que con el metodo newton la convergencia esta muy bien aproxamada salvo la funcion 3 en
# la que no se puede acercar porque no puede resolver raices de numeros negativos
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        