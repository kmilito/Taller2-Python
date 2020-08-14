calif1 = float(input("Ingrese la primera calificación: "))
calif2 = float(input("Ingrese la segunda calificación: "))
calif3 = float(input("Ingrese la tercera calificación: "))

prom = (calif1 + calif2 + calif3)/ 3
if prom > 70:
    print("Alumno aprobado")
else:
    print("Alumno reprobado")