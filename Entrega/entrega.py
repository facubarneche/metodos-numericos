
import numpy as np
import matplotlib.pyplot as plt

#******************************************************************************
#********************************** Trisección ********************************
#******************************************************************************

def trisection(f, a: float, b: float, e: float, count: int = 0) -> float:
    """
    Esta función implementa el método de trisección para encontrar una raíz de la función f en el intervalo [a, b].

    * Contraints:
    f(a), f(b) -- Deben ser obligatoriamente de signo opuesto y distinto a 0 (raiz)
    
    * Parámetros:
    f -- La función para la cual se busca la raíz.
    [a, b] -- Limites de rango donde buscar la raiz.
    count -- Contador de iteraciones, seteada por defecto en 0
    
    * Devuelve:
    Una tupla que contiene un float con la aproximación de la raíz y un int con el numero de iteraciones
    """

    if f(a) * f(b) >= 0:
        raise ValueError("Para encontrar la raiz, tanto la f(a) como la f(b) deben tener como resultado signos opuestos")

    while (abs(b - a)) > e: # Mientras la diferencia absoluta entre 'b' y 'a' sea mayor que 'e'
        count = count + 1 # Incrementa el contador

        c = a + (b - a) / 3.0 # Calcula el primer tercio del intervalo
        d = a + 2 * (b - a) / 3.0 # Calcula el segundo tercio del intervalo

        if f(c) == 0:
            return c, count
        elif f(d) == 0:
            return d, count
        elif f(c) * f(d) < 0:
            a = c
            b = d
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = d

    return (a + b) / 2.0, count


#******************************************************************************
#********************************** Bisección *********************************
#******************************************************************************
def bisection(f, a: float, b: float, e: float, count: int) -> float:
    """
    Esta función implementa el método de bisección para encontrar una raíz de la función f en el intervalo [a, b].
    
    * Contraints:
    f(a), f(b) -- Deben ser obligatoriamente de signo opuesto y distinto a 0 (raiz)
    
    * Parámetros:
    f -- La función para la cual se busca la raíz.
    [a, b] -- Limites de rango donde buscar la raiz.
    count -- Contador de iteraciones, sin seteo por defecto ya que al ser una función recursiva devolvería siempre 0
    
    * Devuelve:
    Una tupla que contiene un float con la aproximación de la raíz y un int con el numero de iteraciones
    """
    # A diferencia de trisección esta linea la ejecuta constantemente a causa de la recursividad
    if f(a) * f(b) >= 0 and count == 0:
        raise ValueError("Para encontrar la raiz, tanto la f(a) como la f(b) deben tener como resultado signos opuestos")

    p = (a + b) / 2.0

    if (abs(b - a)) < e: # Si la diferencia absoluta entre 'b' y 'a' es menor que 'e' retorna la dupla con la raiz aproximada y el contador
        return p, count
    
    count = count + 1 # Incrementa el contador

    if f(b) * f(p) > 0: # Se nutre recursivamente disminuyendo el rango de busqueda
        return bisection(f, a, p, e, count)
    else:
        return bisection(f, p, b, e, count)

#******************************************************************************
#****************************** Grafico de Lineas *****************************
#******************************************************************************

def plot_function(f, a: float, b: float, func_str: str):
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


#******************************************************************************
#****************************** Grafico de Barras ******************************
#******************************************************************************

def plot_bar_chart(triCounter: int, biCounter: int):
    labels = ['Trisección (' + str(triCounter) + ')', 'Bisección (' + str(biCounter) + ')']
    iterations = [triCounter, biCounter]

    x = range(len(labels))
    bar_width = 0.5  # Anchura de las barras

    plt.bar(x, iterations, width=bar_width, color=['pink', 'brown'])
    plt.ylabel('Número de Iteraciones')
    plt.title('Comparación de Iteraciones entre Trisección y Bisección')
    plt.xticks(x, labels)  # Colocamos los nombres de los métodos en el eje x
    plt.show()  # Muestra el gráfico de barras

#******************************************************************************
#***************************** Recolección de Datos ***************************
#******************************************************************************

# Se agrega condicion para que no se ejecuten las siguientes lineas al ejecutar los test (test.py)
if __name__ == "__main__":
    func_str = input("Ingresa la función f en términos de x: ")
    f = lambda x: eval(func_str)

    a = float(input("Ingresa el valor de a: "))
    b = float(input("Ingresa el valor de b: "))
    e = float(input("Ingresa la tolerancia: "))


#******************************************************************************
#***************************** Llamada a funciones ****************************
#******************************************************************************

    (triRoot, trisectionCounter) = trisection(f, a , b, e)
    (biRoot, bisectionCounter) = bisection(f, a , b, e, 0)
    print("Una posible raíz para el metodo de trisección es: ", triRoot)
    print('El metodo de trisección tuvo ', trisectionCounter, ' iteraciones.')

    print("Una posible raíz para el metodo de bisección es: ", biRoot)
    print('El metodo de bisección tuvo ', bisectionCounter, ' iteraciones.')

    print('Cierre los graficos para finalizar el programa.')

    plot_function(f, a, b, func_str)
    plot_bar_chart(trisectionCounter, bisectionCounter)

#******************************************************************************
#******************************** Observaciones *******************************
#******************************************************************************

# 1. Se implementa el metodo de triseccion y el de biseccion para comparar la eficiacia de ambos metodos entre si
# 2. Las raíces aproximadas son bastante cercanas entre los dos métodos en la mayoría de los casos, lo que sugiere 
# que ambos métodos son efectivos para encontrar las raíces.
# 3. Se puede notar que generalmente el metodo de trisección necesita como minimo un 30% menos de iteraciones 
# que la biseccion para encontrar la raiz de la función. 
# 4. Que el metodo de trisección tenga menos iteraciones no implica que sea mas performante ya que cada iteración es mas costosa
# 5. En los test se puede apreciar que cuando hay raices dentro del intervalo limite a la misma distancia de [a,b], el metodo
# de bisección generalmente aproxima hacia la más grande. Por otro lado el metodo de trisección tiene un comportamiento bastante variado.
# Estas conclusiones son en base a unas pocas pruebas, por eso son observaciones volcadas respecto a estos tests.