from entrega import plot_pie_chart, trisection, bisection
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
    return x**2 - 3*x + 2  

def f5(x):
    return x**3 - 6*x**2 + 11*x - 6  

def f6(x):
    return (2.718281828459045)**x -2 

def f7(x):
    return x**3 - x**2 - x + 1  

def f8(x):
    return x**2 - 5*x + 6  

def f9(x):
    return x**3 - 7*x**2 + 16*x - 12  

def f10(x):
    return 4*x**4 - 2

def f11(x):
    return x**2 - 6*x + 4  

def f12(x):
    return x**3 - 5*x**2 + 8*x - 4  

def f13(x):
    return x**5+2*x+6

def f14(x):
    return x**2 - 7*x + 9  

def f15(x):
    return x**3 - 6*x**2 + 12*x - 8  



functions = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15]
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
    (1.5, 2.5)      # Para f15
]

e = 0.00001

# Probamos el método de trisección y de bisección
for i, func in enumerate(functions):
    a, b = intervals[i]
    (testTriRoot, testTriCounter) = trisection(func, a, b)
    (testBiRoot, testBiCounter) = bisection(func, a, b, 0)
    
    func_source = inspect.getsource(func).strip()
    func_expr = func_source[func_source.index(':')+1:].strip()
    func_expr = func_expr.replace('return ', '')

    print('Metodo de Trisección\n')
    print(f"La raíz encontrada por el método de trisección para la función f{i+1}(x) = {func_expr} es: {testTriRoot}")
    print(f"El método de trisección para la función f{i+1}(x) tuvo {testTriCounter} iteraciones.\n")

    print('Metodo de Bisección\n')
    print(f"La raíz encontrada por el método de bisección para la función f{i+1}(x) = {func_expr} es: {testBiRoot}")
    print(f"El método de bisección para la función f{i+1}(x) tuvo {testBiCounter} iteraciones.\n")
    print('##########################\n')

# Gráfico de torta
# plot_pie_chart(1, 2)