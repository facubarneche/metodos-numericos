
import numpy as np
import matplotlib.pyplot as plt

# Metodo de Trisección
def trisection(f, a, b):
    count = 0

    if f(a) * f(b) > 0:
        raise ValueError("Para encontrar la raiz, tanto la f(a) como la f(b) deben tener como resultado signos opuestos")

    while (abs(b - a)) / 2.0 > e:
        count = count + 1
        c = a + (b - a) / 3.0
        d = a + 2 * (b - a) / 3.0

        if f(c) == 0:
            return c
        elif f(d) == 0:
            return d
        elif f(c) * f(d) < 0:
            a = c
            b = d
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = d

    print('El metodo de trisección tuvo ', count, ' iteraciones.')
    return (a + b) / 2.0

# Se crea variable global como contador de la bisección recursiva
globalCount = 0

def biseccion(f,a, b) -> float:
    global globalCount

    p = (a + b) / 2

    if (abs(b - a)) < e:
        print('El metodo de bisección tuvo ', globalCount, ' iteraciones.')
        return p
    
    globalCount = globalCount + 1

    if f(p) > 0: 
        return biseccion(f, a, p)
    else:
        return biseccion(f, p, b)



def plot_function(f, a, b, func_str):
    # Crea un array de valores x entre a y b
    x = np.linspace(a, b, 400)
    y = f(x)

    # Crea el gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=f'f(x) = {func_str}')
    plt.title('Gráfico de la función')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.legend()
    plt.show()



func_str = input("Ingresa la función f en términos de x: ")
f = lambda x: eval(func_str)

a = float(input("Ingresa el valor de a: "))
b = float(input("Ingresa el valor de b: "))
e = float(input("Ingresa la tolerancia: "))

print("Una posible raíz para el metodo de trisección es: ", trisection(f, a, b))
print("Una posible raíz para el metodo de bisección es: ", biseccion(f, a , b))
print('Cierre el grafico para finalizar el programa.')

plot_function(f, a, b, func_str)

#******************************************************************************
#******************************** Observaciones *******************************
#******************************************************************************
# Se implementa el metodo de triseccion y el de biseccion para comparar la eficiacia de ambos metodos entre si
# Se puede notar que generalmente el metodo de trisección necesita aproximadamente un 1.62 menos de iteraciones 
# que la biseccion (con recursividad) para encontrar la raiz de la función. Esto no implica que sea mas eficaz
# ya que tiene una cantidad mayor de condiciones y calculos.
# Si bien depende mucho del problema a resolver, la biseccion tiende a ser mas eficaz que triseccion