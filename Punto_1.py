op = float (input("1:cuadrado- 2:rectangulo- 3:triangulo- 4:rombo- 5:circulo:"))

match op:
    case (1):
        lado=float(input("ingresa el lado:"))
        area = lado * lado
        print("el lado del cuadrado es:", area)

    case (2):

        lado=float(input("ingresa el lado:"))
        A=float(input("ingresa el altura:"))
        areaR = lado * A
        print("el lado del rectangulo es:", areaR)

    case (3):
        altura=float(input("ingresa la altura:"))
        base=float(input("ingresa la base:"))
        areat = base * altura
        print("el lado del triangulo es:", areat)   

    case (4):
        alt=float(input("ingresa la altura:"))
        bas=float(input("ingresa la base:"))
        diagonal=float(input("ingresa la diagonal:"))
        areaR = alt* bas* diagonal
        print("el lado del rombo es:", areaR)
    
    case (5):
        radio=float(input("ingresa el radio:"))
        areaC = radio * radio
        print("el radio del circulo es:", areaC)

    case (6):
    
        print("esta función no existe:")
