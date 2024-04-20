from entrega import plot_bar_chart, trisection, bisection
import numpy as np
import inspect


# Definimos algunas funciones para probar
def f1(x):
    return x**2 - 4

def f2(x):
    return np.sin(x)

def f3(x):
    return x - 1

def f4(x):
    return x**2 - 3 * x + 2  

def f5(x):
    return x**3 - 6 * x**2 + 11 * x - 6  

def f6(x):
    return (2.718281828459045)**x - 2 

def f7(x):
    return x**3 - x**2 - x + 1  

def f8(x):
    return x**2 - 5 * x + 6  

def f9(x):
    return x**3 - 7 * x**2 + 16 * x - 12  

def f10(x):
    return 4 * x**4 - 2

def f11(x):
    return x**2 - 6 * x + 4  

def f12(x):
    return x**3 - 5 * x**2 + 8 * x - 4  

def f13(x):
    return x**5 + 2 * x + 6

def f14(x):
    return x**2 - 7 * x + 9  

def f15(x):
    return x**3 - 6*x**2 + 12*x - 8

def f16(x):
    return x**3 - 6 * x**2 + 11 * x - 6

def f17(x):
    return x**5 - 15 * x**4 + 85 * x**3 - 225 * x**2 + 274 * x - 120


functions = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17]
intervals = [
    (1, 3),         # Para f1
    (-1, 1),        # Para f2
    (-3, 3),        # Para f3
    (0.5, 1.5),     # Para f4
    (0.5, 1.5),     # Para f5
    (0, 1),         # Para f6
    (-2, 0),        # Para f7
    (1.5, 2.5),     # Para f8
    (2.6, 3.5),     # Para f9
    (0,1),          # Para f10
    (0,1),          # Para f11
    (0.6,1.4),      # Para f12
    (-2,-1),        # Para f13
    (1, 2),         # Para f14
    (1.5, 2.5),     # Para f15
    (0, 5),         # Para f16
    (0, 6)          # Para f17
]
# Error permitido
e = 0.0001
totalIterationsTri = 0
totalIterationsBi = 0

print(f'''
############################################################################
################################## TESTS ###################################
############################################################################
''')

# Probamos el método de trisección y de bisección
for i, func in enumerate(functions):
    (a, b) = intervals[i] #Obtenemos los 2 valores de la tupla intervals[i]
    (testTriRoot, testTriCounter) = trisection(func, a, b, e)
    (testBiRoot, testBiCounter) = bisection(func, a, b, e, 0)

    # Calculamos las iteraciones totales de cada metodo
    totalIterationsTri = totalIterationsTri + testTriCounter
    totalIterationsBi = totalIterationsBi + testBiCounter
    
    # Obtenemos en string la funcion para luego mostrarla por consola
    func_source = inspect.getsource(func).strip()
    func_expr = func_source[func_source.index(':')+1:].strip()
    func_expr = func_expr.replace('return ', '')

    print(f'''
############################################################################
Función f{i+1}(x) = {func_expr}
############################################################################
    ''')


    print('Metodo de Trisección:\n')
    print(f"Raíz aproximada: {testTriRoot}")
    print(f"Iteraciones: {testTriCounter}\n")

    print('Metodo de Bisección:\n')
    print(f"Raíz aproximada: {testBiRoot}")
    print(f"Iteraciones: {testBiCounter}\n")

# Llamada a gráfico de barras
plot_bar_chart(totalIterationsTri, totalIterationsBi)