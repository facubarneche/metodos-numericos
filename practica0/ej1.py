# 1. Implementar en Python el proceso anterior, que use una función (externa implementada, 
# o bien pasada como parámetro), que lea el x como parámetro y un n natural, y luego sobre 
# el ex inicial aplique la f n veces, finalmente devolviendo el resultado obtenido tras la 
# última aplicación.

def myFunc(x, stop):
    for _ in range(0, stop):
        x = x ** 2 - 1
        print('* ', x)

x = float(input('Enter any number: '))
stop = int(input('Enter the number of cicles (integer): '))

myFunc(x,stop)

#******************************************************************************
#*********************************Observaciones********************************
#******************************************************************************
# Se puede notar que numeros desde el -1.61 hasta 1.61 tienen como limite a -1 
# pero saliendo de este rango tiene como limite infinito +



