# 7. Aplicar el método de bisección para aproximar un x que cumpla cos(x) = -1, 
# con error menor que epsilon = 1/10. 
# Notar que esto sirve para encontrar aproximaciones de pi.

import math

root = -1

def f(x): 
    return math.cos(x)

def biseccion(a, b, e):
    while(b - a >= e):
        p = (a + b) / 2
        if(f(p) > root):
            print(f(p))
            b = p
        else:
            a = p
            print(f(p))

    print(p, ' (Raiz Apróximada)')
        
biseccion(-3.2, -1, 1/10)

#******************************************************************************
#*********************************Observaciones********************************
#******************************************************************************
# Se importa la libreria math para hacer uso de cos
# Se vuelve a usar el metodo de bisección sin recursividad
# Si bien no esta a una distancia enorme, este ejercicio no se puede resolver con metodo de biseccion


