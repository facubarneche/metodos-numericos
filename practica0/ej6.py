# 6. Aplicar el método de bisección para hallar una aproximación de un x que cumpla x^2 + x = 12. 
# Calcular luego el valor exacto de otra manera, y comparar.

def f(x): 
    return x ** 2 + x

def biseccion(a, b, e):
    p = (a + b) / 2
    print(p)
    if((b - a) < e):
        print(p, ' (Raiz Apróximada)')
        return p
    if(f(p) > 12): return biseccion(a, p, e)
    else: return biseccion(p, b, e)

biseccion(0, 5, 0.01)
        


#******************************************************************************
#*********************************Observaciones********************************
#******************************************************************************
# Simplemente se cambio la condición para que se evalue con el valor 12 y no con la raiz 'f(p) > 12'.



