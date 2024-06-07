saldo = 1000

while saldo > 0:
    print("saldo actual:", saldo)
    retiro = int(input("Ingrese monto a retirar: "))
    
    if retiro <= saldo:
        saldo -= retiro
        print("Retiro realizado. Su nuevo saldo es:", saldo)
    else:
        print("Saldo insuficiente. Intente nuevamente.")
