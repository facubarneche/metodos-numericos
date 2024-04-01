# 14 a) Discutir un posible método de bisección para hallar raíces de funciones reales
# continuas pero de más de una variable (nota: el primero conocido de ellos fue el de Davidon-
# Fletcher-Powell).
# b) Dar un método (concreto y sencillo) para aplicarse especialmente a la función
# f(x,y) = x2 + y2 – 2.
# c) Idem para f(x,y) = x + y + sen x + sen y

# 2x + 5y - 1
def f(x, y): return 2 * x  + 5 * y - 1


#******************************************************************************
#******************************** Observaciones *******************************
#******************************************************************************
# Se observa que al haber 2 variables de arranque ya puede tener varios valores por ej.
# x = 1, y = 0
# x = 0 , y = 1/5
