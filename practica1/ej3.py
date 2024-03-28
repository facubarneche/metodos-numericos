# 3  Aproximar una raíz cada una de las funciones del ejercicio 1 usando el método de
# Newton, cuando sea posible usarlo. Para las funciones en las cuales no se pueda usar, justificar.

import math;

# euler
e = 2.7182818284

#Funciones

# f1(x) = √x
def f1(x): return math.sqrt(x)

# f2(x) = x3+1
def f2(x): return 3 * x + 1  

# f3(x) = x3- x + 1
def f3(x): return 3 * x - x + 1

# f4(x) = e-x – sen x
def f4(x): return e - x - math.sin(x)

# f5(x) = 2/x
def f5(x): return 2 / x

# f6(x) = |x + 5|
def f6(x): return abs(x + 5)

# f7(x) = 2x + 3
def f7(x): return 2 * x + 3

#Derivadas
def df1(x): return 1 / (2 * math.sqrt(x))

def df2(x): return 3

def df3(x): return 2

def df4(x): return -1 - math.cos(x)

def df5(x): return 0 / 1

def df6(x): return 1

def df7(x): return 2

# Newton
def newton(x0, f, df):
    for _ in range(0,3):
        x1 = x0 - ( f(x0) / df(x0)) 
        print(x1)
        x0 = x1

# No realizable ya que no se puede realizar la raiz cuadrada de un numero negativo
# newton(1,f1, df1)

# newton(1, f2, df2)

# newton(1, f3, df3)

# newton(1.5, f4, df4)

# No realizable ya que no se puede realizar la divicion por 0
# newton(1.5, f5, df5)

#newton(1, f6, df6)

newton(1, f7, df7)


#******************************************************************************
#******************************** Observaciones *******************************
#******************************************************************************
# Formula metodo de Newthon- Raphson
# X n+1 = X n - [f(Xn)/f'(Xn)]
# Se descubre que con biseccion la f1, f5 y f6 no eran realizables pero al implementar
# Newton la f6 si es realizable ya que no hace falta 2 variables al azar con distinto disgno
# Por otro lado se nota la velocidad con la cual se puede obtener una aproximación muy precisa.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        