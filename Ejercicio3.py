compra = float(input("Digite el valor de la compra: "))

if compra > 1000:
    desc = compra * 0.20
    tot_pag = compra - desc
    print("Tiene un descuento del 20%")
    print(f"El valor total a pagar es: {tot_pag}")
else:
    desc = 0
    print("No tiene descuento")


