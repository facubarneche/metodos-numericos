# 2 Elegir una f del ejercicio anterior tal que pueda usarse bisección, y aproximar una raíz de f
# con un error tal que tenga los primeros 2 decimales correctos.

# f1(x) = √x
def f(x): return 2 * x + 3

def biseccion(a, b, e):
    p = (a + b) / 2
    print(p)
    if((b - a) < e):
        print(p, ' (Raiz Apróximada)')
        return p
    if(f(p) > 0): return biseccion(a, p, e)
    else: return biseccion(p, b, e)
    
biseccion(-100, 100, 0.001)

#******************************************************************************
#******************************** Observaciones *******************************
#******************************************************************************
# Con los n decimales en 0 del valor de epzilom se va a obtener los n decimas correctos en el output
# del metodo de biseccion