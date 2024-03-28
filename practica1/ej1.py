# 1 – Emplear el método de bisección y hacer los primeros 3 pasos, con el fin de aproximar una
# raíz para cada una de las siguientes funciones, cuando sea posible usarlo. Para las funciones
# en las cuales no se pueda usar, justificar.
# f1(x) = √x
# f2(x) = x3+1
# f3(x) = x3- x + 1
# f4(x) = e-x – sen x
# f5(x) = 2/x
# f6(x) = |x + 5|
# f7(x) = 2x + 3

import math;

# euler
e = 2.7182818284

# f1(x) = √x
def f1(x): return x ** 1/2

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



def biseccion(a, b, e, myFunc):
    p = (a + b) / 2
    print(p)
    if((b - a) < e):
        print(p, ' (Raiz Apróximada)')
        return p
    if(myFunc(p) > 0): return biseccion(a, p, e, myFunc)
    else: return biseccion(p, b, e, myFunc)

# def biseccionCosySen(a, b, epsilon, myFunc):
#     p = (a + b) / 2
#     print(p)
#     if((b - a) < epsilon):
#         print(p, ' (Raiz Apróximada)')
#         return p
#     # Función creciente
#     if(myFunc(a) < myFunc(b)):  
#         if(myFunc(p) > 0): 
#             return biseccionCosySen(a, p, epsilon, myFunc)
#         else: 
#             return biseccionCosySen(p, b, epsilon, myFunc)
#     else:  
#         # Función decreciente
#         if(myFunc(p) > 0): 
#             return biseccionCosySen(p, b, epsilon, myFunc)
#         else: 
#             return biseccionCosySen(a, p, epsilon, myFunc)

# No Realizable, es continua de [0 a inf +), tiene raiz en 0 pero arranca su imagen en 0, por ende, "a" no puede obtener un valor negativo
# biseccion(-100, 100, e, f1)

# Realizable
# biseccion(-100, 100, e, f2)

# Realizable
# biseccion(-100, 100, e, f3)

# Realizable pero con mas validaciones
# biseccion(-10, 10, e, f4)

# No realizable (se puede encontrar la raiz pero no es una f(x) continua ya que x = 0 no tiene imagen)
# biseccion(-99, 100, e, f5)

# No realizable, tiene raiz en 0 pero arranca su imagen en 0, por ende, "a" no puede obtener un valor negativo
# biseccion(-100, 100, e, f6)

# Realizable
# biseccion(-100, 100, e, f7)

#******************************************************************************
#******************************** Observaciones *******************************
#******************************************************************************
# En el actual ejercicio se puede observar algunos comportamientos anteriormente analizados:
# 1. Si la imagen empieza en 0, el metodo de biseccion no funciona ya que no se puede asignar las 2 variables
# con distinto signo
# 2. Si la funcion no es continua, en algunos casos se va a poder encontrar la raiz pero claramente como
# lo define el metodo al no ser continua no es realizable por metodo de biseccion.
# En nuestro ejercicio se puede ver que la imagen no puede ser 0, ya que 2 / 0 no existe
# 3. Las funciones que oscilan como coseno y seno, si bien se pueden realizar se debe generar algunas
# validaciones extras.
