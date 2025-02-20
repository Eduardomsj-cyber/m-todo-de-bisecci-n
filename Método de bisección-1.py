def f(x):
    return x**3 - 4*x - 9

def bisection(a, b, tol):
    if f(a) * f(b) >= 0:
        print("El método de bisección no es aplicable en este intervalo.")
        return None
    
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    
    return (a + b) / 2

# Intervalo y tolerancia
a, b = 2, 3
tol = 1e-5

# Encontrar la raíz
raiz = bisection(a, b, tol)
print(f"La raíz aproximada es: {raiz}")
