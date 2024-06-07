taller1 = float(input("Introduce la nota del Taller 1: "))
taller2 = float(input("Introduce la nota del Taller 2: "))
quiz = float(input("Introduce la nota del Quiz: "))


examen_parcial = float(input("Introduce la nota del Examen Parcial: "))


promedio_talleres_quiz = (taller1 + taller2 + quiz) / 3


nota_final = (promedio_talleres_quiz * 0.30) + (examen_parcial * 0.70)

print("La nota final del primer parcial es:", nota_final)