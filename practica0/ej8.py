# 8. Modificar la implementación del método de bisección para que:
# a) haga la menor cantidad posible de evaluaciones de la f en cada iteración -OK-
# b) vaya imprimiendo la secuencia de los puntos p que van aproximando a la raíz buscada -OK-
# c) que tenga una cota (grande) en la cantidad total de pasos que dará antes de devolver algo -OK-
# d) que devuelva, además del p encontrado, la cantidad de pasos que fueron necesarios para 
# llegar a la aproximación buscada -OK-

root = 0
count = 0
cota = 50
e = 0.00000001

def biseccion(a: float, b: float, e: float, func) -> float:
    global count
    p = (a + b) / 2
    if (b - a) < e or count > cota:
        print('Raiz aproximada:', p)
        print('La cantidad de pasos necesarios fue de:', count)
        return p
    count = count + 1
    if func(p) > root: 
        print(p)
        return biseccion(a, p, e, func)
    else: 
        print(p)
        return biseccion(p, b, e, func)

biseccion(-100000, 100000, e, lambda x: x ** 3 + x - 10)


#******************************************************************************
#*********************************Observaciones********************************
#******************************************************************************
# Se implemento recursividad para implementar la menor cantidad de validaciones
# Implementacion cota superior como criterio de salida
# Implementacion error absoluto como otro citerio de salida
# Implementacion funcion que pueda recibir una lambda como parametro



