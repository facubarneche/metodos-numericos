# 13 El método de bisección tiene entre otros requerimientos que al comienzo se cuente con
# dos números reales a y b tales que f(a) y f(b) tengan distinto signo. Si bien eso puede ser
# costoso, mostrar un algoritmo aproximado que converja hallando tales a y b en caso en que
# existan. (Nota: si no hubiera tales valores, no se pide nada del algoritmo, que incluso podría
# colgarse.)

def esPosibleBiseccion(a, b, func):
    if(func(a) * func(b) < 0): print(func(a), func(b))
    else: print('No se puede hacer bisección con estos parametros', func(a), func(b))

esPosibleBiseccion(-20, 2, lambda x: x ** 3 + x - 10)
#******************************************************************************
#******************************** Observaciones *******************************
#******************************************************************************
# Es una función para descubrir si es posible o no realizar el metodo de bisección con los parametros
# recibidos