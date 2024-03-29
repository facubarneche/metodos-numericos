# 6 Elegir 2 o 3 de las funciones del ejercicio anterior y resolver usando bisección de modo de
# obtener 3 decimales correctos

import math;

# Globales

# Le asigno un epzilom acorde para obtener 3 decimales correcto
e = 0.001

# Funciones

# Le agrego el valor a n por defecto random para que sea polimorfica al resto de funciones ya que la n no es de interes
def f1(x, n = 4): return x ** n # where n >= 1

def f4(x): return math.cos(x)

# Bisección
def biseccion(a, b, e, myFunc):
    p = (a + b) / 2
    print(p)
    if((b - a) < e):
        print(p, ' (Raiz Apróximada)')
        return p
    if(myFunc(p) > 0): return biseccion(a, p, e, myFunc)
    else: return biseccion(p, b, e, myFunc)

print('Función 1')
biseccion(-10, 10, e, f1)
print('=======================')
print('Función 2')
biseccion(-3, 3, e, f4)

#******************************************************************************
#******************************** Observaciones *******************************
#******************************************************************************
# Funciona correctamente aunque con un nivel muchisimo mayor de iteraciones y validaciones
# Vale aclarar que la funcion 2 siempre tiende a la primera raiz negativa
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        