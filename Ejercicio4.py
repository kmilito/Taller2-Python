ht = float(input("Digite el numero de horas trabajadas: "))

if ht > 40:
    he = ht - 40
    ss = he * 20 + 40 * 16
    print(f" El salario semanal del trabajador es: {ss}")
else:
    ss = ht * 16

    print(f" El salario semanal del trabajador es: {ss}")