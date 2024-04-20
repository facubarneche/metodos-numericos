
import numpy as np
import matplotlib.pyplot as plt

# Se crean 2 variables globales para luego podes accederlas en el grafico de torta
globalCountTrisec = 0
globalCountBisec = 0

#******************************************************************************
#********************************** Trisección ********************************
#******************************************************************************

def trisection(f, a: float, b: float) -> float:
    """
    Esta función implementa el método de trisección para encontrar una raíz de la función f en el intervalo [a, b].
    
    Parámetros:
    f -- La función para la cual se busca la raíz.
    (a, b) -- Limites de signo opuesto del intervalo.
    
    Devuelve:
    Una float que contiene la raíz encontrada
    """
    
    global globalCountTrisec

    if f(a) * f(b) > 0:
        raise ValueError("Para encontrar la raiz, tanto la f(a) como la f(b) deben tener como resultado signos opuestos")

    while (abs(b - a)) > e:
        globalCountTrisec = globalCountTrisec + 1
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

    print('El metodo de trisección tuvo ', globalCountTrisec, ' iteraciones.')
    return (a + b) / 2.0

#******************************************************************************
#********************************** Bisección *********************************
#******************************************************************************

def bisection(f, a, b) -> float:
    """
    Esta función implementa el método de bisección para encontrar una raíz de la función f en el intervalo [a, b].
    
    Parámetros:
    f -- La función para la cual se busca la raíz.
    (a, b) -- Limites de signo opuesto del intervalo.
    
    Devuelve:
    Una float que contiene la raíz encontrada
    """
        
    global globalCountBisec

    if f(a) * f(b) > 0:
        raise ValueError("Para encontrar la raiz, tanto la f(a) como la f(b) deben tener como resultado signos opuestos")

    p = (a + b) / 2.0

    if (abs(b - a)) < e:
        print('El metodo de bisección tuvo ', globalCountBisec, ' iteraciones.')
        return p
    
    globalCountBisec = globalCountBisec + 1

    if f(b) * f(p) > 0: 
        return bisection(f, a, p)
    else:
        return bisection(f, p, b)

#******************************************************************************
#****************************** Grafico de Lineas *****************************
#******************************************************************************

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

#******************************************************************************
#****************************** Grafico de Torta ******************************
#******************************************************************************

def plot_pie_chart():
    labelTrisec = 'Trisección (' + str(globalCountTrisec) + ')'
    labelBisec = 'Bisección (' + str(globalCountBisec) + ')'
    labels = [labelTrisec, labelBisec]
    sizes = [globalCountTrisec, globalCountBisec]
    explode = [0.05, 0.05]

    #Implementa un grafico de torta con las configuraciones seteadas
    plt.pie(sizes, labels=labels, explode=explode, autopct="%1.1f%%", shadow=True, startangle=90, colors=['pink', 'yellow'])
    plt.title('Numero de Iteraciones')
    plt.legend()
    plt.show() #Muestra el grafico anteriormente seteado

#******************************************************************************
#***************************** Recolección de Datos ***************************
#******************************************************************************

func_str = input("Ingresa la función f en términos de x: ")
f = lambda x: eval(func_str)

a = float(input("Ingresa el valor de a: "))
b = float(input("Ingresa el valor de b: "))
e = float(input("Ingresa la tolerancia: "))


#******************************************************************************
#***************************** Llamada a funciones ****************************
#******************************************************************************

print("Una posible raíz para el metodo de trisección es: ", trisection(f, a, b))
print("Una posible raíz para el metodo de bisección es: ", bisection(f, a , b))
print('Cierre los graficos para finalizar el programa.')

plot_function(f, a, b, func_str)
plot_pie_chart()

#******************************************************************************
#******************************** Observaciones *******************************
#******************************************************************************

# Se implementa el metodo de triseccion y el de biseccion para comparar la eficiacia de ambos metodos entre si
# Se puede notar que generalmente el metodo de trisección necesita aproximadamente un 1.62 menos de iteraciones 
# que la biseccion para encontrar la raiz de la función. Esto no implica que sea mas performante ya que cada iteración es mas costosa
