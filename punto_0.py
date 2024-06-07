
op  = int (input("ingresa una opción 1:suma/2: Resta/3: multiplicación/4:división"))
numero1= int (input("ingrese un numero:"))


match op:
    case (1):
        suma=int (input("ingresa un numero:"))
        resultdo= numero1 + suma
        print("el resultdo es:",resultdo)
    
    case (2):
        resta=int (input("ingresa un numero :"))
        resultdo= numero1 - resta
        print("el resultdo es:",resultdo)
        
    case (3):
        multiplicación=int (input("ingresa un numero:"))
        resultdo= numero1 * multiplicación
        print("el resultdo es:",resultdo)
        
    case (4):
        división=int (input("ingresa un numero:"))
        resultdo= numero1 / división
        print("el resultdo es:",resultdo)
        
    