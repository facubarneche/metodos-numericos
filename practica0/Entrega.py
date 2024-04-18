import numpy as np
import matplotlib.pyplot as plt

def trisection(f, a, b):
    tol = float(input("Ingresa la tolerancia: "))
    if f(a) * f(b) > 0:
        raise ValueError("La función debe cambiar de signo en el intervalo")

    while (b - a) / 2.0 > tol:
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

    return (a + b) / 2.0

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

print("Una posible raíz es: ", trisection(f, a, b))

plot_function(f, a, b, func_str)