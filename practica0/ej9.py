# 9. Método de trisección. Implementar en Python un método para aproximar raíces al estilo de bisección, 
# pero que en vez de dividir el intervalo en 2 subintervalos lo divida en 3, 
# y en cada iteración elija uno de los 3 subintervalos que contenga una raíz. 
# Usar una condición de parada análoga a la del método de bisección.
e = 0.00000001
root = 0


def anyFunc(x):
    return x ** 2 - 4 

def triseccion(a, b, e) -> float:
    count = 0
    while((b - a) > e): 
        count = count + 1
        p1 = (a + b) / 2
        p2 = ((a + b) * 2) / 3
    
        if(anyFunc(p1) > root):
            b = p1
        elif(anyFunc(p2) < root):
            a = p2
        else:
            a = p1
            b = p2
    print('Raiz aproximada con trisección:', p1)
    print('Se precisaron ', count, ' pasos')

triseccion(-100000, 100000, e)


globalCount = 0
def biseccion(a, b, e) -> float:
    global globalCount
    p = (a + b) / 2

    if (b - a) < e:
        print('Raiz aproximada con bisección:', p)
        print('Se precisaron ', globalCount, ' pasos')
        return p
    globalCount = globalCount + 1
    if anyFunc(p) > root: 
        return biseccion(a, p, e)
    else: 
        return biseccion(p, b, e)

biseccion(-100000, 100000, e)


#******************************************************************************
#******************************** Observaciones *******************************
#******************************************************************************
# Se implementa el metodo de triseccion y el de biseccion para comparar la eficiacia de ambos metodos entre si
# Se puede notar que el metodo de biseccion (con recursividad) es hasta 4 veces mas eficas (en este caso)
# Si bien depende mucho del problema a resolver, la biseccion tiende a ser mas eficaz que triseccion



