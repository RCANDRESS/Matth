import os
os.system("cls")

def areaCuadrado():
    lado=float(input("ingrese el valor del lado: "))
    return print("El area del cuadrado es: ", lado**2)
areaCuadrado()

def areaRectangulo():
    base=float(input("ingrese el valor de la base: "))
    altura=float(input("ingrese el valor de la altura: "))
    return print("El area del rectangulo es: ", base * altura)
areaRectangulo()