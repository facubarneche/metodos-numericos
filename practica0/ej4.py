# 4. Aplicar el método de bisección para hallar una raíz aproximada de la función f(x) = x^3 + x - 5, 
# comenzando con el intervalo [1,2], y el error epsilon = 0.5.

def f(x): 
    return x ** 3 + x - 5

def biseccion(a, b, e):
    p = (a + b) / 2
    print(p)
    if((b - a) < e):
        print(p, ' (Raiz Apróximada)')
        return p
    if(f(p) > 0): return biseccion(a, p, e)
    else: return biseccion(p, b, e)

biseccion(1, 2, 0.5)
        


#******************************************************************************
#*********************************Observaciones********************************
#******************************************************************************
# Se optó por hacer un metodo de bisección con recursividad



