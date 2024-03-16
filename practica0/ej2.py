# 2. Implementar en Python un proceso al estilo del anterior, pero que use dos funciones, 
# una f y una g, y que la aplicación iterada sea una vez f, luego g, luego f, luego g, 
# y así siguiendo, alternando una con otra, en total las veces que se especifique por 
# el parámetro n, y finalmente devuelva el resultado obtenido tras la última aplicación.

# Se crean 2 funciones totalmente randoms
def f(x):
    return x ** 2 - 1

def g(x):
    return x / 2 + 3


def myFunc(x, stop):
    for _ in range(0, stop):
        if(x % 2 == 0):
            x = f(x)
        else:
            x = g(x)
        print('* ', x)

x = float(input('Enter any number: '))
stop = int(input('Enter the number of cicles (integer): '))

myFunc(x,stop)


#******************************************************************************
#*********************************Observaciones********************************
#******************************************************************************
# Se da la curiosidad que con 2 funciones random ponga los numericos que ponga
# tiende a 6 como limite, ahora, si cambiamos las funciones su comportamiento es
# totalmente distinto, mera casualidad, pero queda como observación ya que es un
# comportamiento bastante dificil de replicar



