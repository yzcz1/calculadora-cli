# calculadora.py
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b

if __name__ == "__main__":
    print("Bienvenido a la calculadora CLI.")
    print("Operaciones: suma, resta, multiplicación, división.")

