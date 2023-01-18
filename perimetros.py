def perCuadrado():
    lado=float(input("ingrese el valor del perimetro: "))
    return print("El area del cuadrado es: ", lado*4)
perCuadrado()


def perRectangulo():
    base=float(input("ingrese el valor de la base: "))
    altura=float(input("ingrese el valor de la altura: "))
    return print("El area del rectangulo es: ", 2 * base + 2* altura)
perRectangulo()

pi=3,141600000

def perCirculo():
    radio=float(input("ingrese el valor del radio: "))
    altura=float(input("ingrese el valor de la altura: "))
    return print("El area del circulo es: ", 2+pi * radio)
perCirculo()