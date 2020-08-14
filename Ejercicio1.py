cap = float(input("Ingrese el capital a invertir: "))
p_int = float(input("Ingreses la tasa de interes: "))
int = cap * p_int

if int > 7000:
    capf = cap + int
    print("Deseo reinvertir")
    print(f"El total de su cuenta es: {capf}")
else:
    print("No deseo reinvertir")
