# 11 Sea a un número real. La siguiente secuencia, ¿converge? Y, en ese caso, ¿a qué valor?
# x0 = a
# xn+1 = xn / 2 + 1/xn

# Globales

# Se le asigna a 'a' un numero Real
a = 1/3
b = -1/3

# Funciones
def f(x): return x / 2 + 1 / x

# Newton
def newton(x0, f):
    for _ in range(0, 10):
        x1 = f(x0)
        print(x1)
        x0 = x1


newton(b, f)

#******************************************************************************
#******************************** Observaciones *******************************
#******************************************************************************
# Es un excelente comportamiento ya que converge hacia el -1.414213... o 1.414213..., dependiendo
# el 'a' recibido por parametros. Lo sorprendente de esta secuencia es que el valor obtenido no es
# una raiz si no que son ambos los extremos finitos de la secuencia.
