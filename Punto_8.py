producto = 1
N = int(input("ingrese un valor:"))

for i in range(1, N + 1):
    producto = producto * i

print("El producto de los números desde 1 hasta", N, "es:", producto)