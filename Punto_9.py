
numero = int(input("Introduce un número entre 1 y 10: "))

if 1 <= numero <= 10:
    print("Tabla de multiplicar decreciente del", numero, ":")
    print( numero, "x 10 =", numero * 10)
    print( numero,"x 9 =", numero * 9)
    print(numero,"x 8 =", numero * 8)
    print( numero,"x 7 =", numero * 7)
    print(numero, "x 6 =", numero * 6)
    print (numero,"x 5 =", numero * 5)
    print(numero,"x 4 =", numero * 4)
    print( numero,"x 3 =", numero * 3)
    print( numero,"x 2 =", numero * 2)
    print(numero,"x 1 =", numero * 1)
else:
    print("El número ingresado no está entre 1 y 10.")
    