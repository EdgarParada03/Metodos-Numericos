THRESHOLD = 1e-15


import math

def f(x):
  """f(x) = x^3 + 4x^2 − 10"""
  return x**3 + 4 * x**2 - 10

def g(x):
  """f(x) = x cos(x − 1) − sin(x)"""
  return x * math.cos(x-1) - math.sin(x)

def errorPorcentual(actual, anterior):
    """Calcula el error porcentual relativo entre dos aproximaciones."""
    return abs((actual - anterior) / actual) * 100

def bisection(fx, a, b, tol, n):
    """
    Inputs:
    f -- f(x)
    a -- start
    b -- end
    tol -- tolerance
    n -- max iterations
    Output:
    p -- aproximation of the 0's f(x)
    Exception in case of exhausting the max iteration
    """
    i = 1
    anterior = a  #Aqui se inicializa la variable anterior, que guarda el valor anterior de p , para calcular el error porcentual
    while i <= n:  
        p = a + (b - a) / 2 #Formula del Xe , Xe = p
        error = errorPorcentual(p, anterior) #Aqui se calcula el error porcentual entre el valor actual de p y el valor anterior.
        print("i = {0:<2}, p = {1:.12f}, error = {2:.12f} %".format(i, p ,error))
        if abs(fx(p)) <= THRESHOLD or error <= tol:
            return p
        i += 1
        if fx(a) * fx(p) > 0:
            a = p
        else:
            b = p
        anterior = p #Aqui se actualiza el valor anterior, para la siguiente iteracion 
    raise Exception("Max iteration numbers was reached")

  
 ########### We now need to call the bisection function with the f(x) and g(x)

# f(x), a = 1, b = 2, error = 0.005, N0 = 100
print("Bisection f(x):")
bisection(f, 1, 2, 0.005, 100)
# g(x), a = 4, b = 6, error = 0.005, N0 = 100
print("Bisection g(x):")
bisection(g, 4, 6, 0.005, 100)
