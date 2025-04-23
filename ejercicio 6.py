es_miembro = True
total_compra = 120

# Operadores lógicos y not
if total_compra > 100 and (es_miembro or not total_compra > 200):
    print("Descuento del 15% aplicado 🎉")
else:
    print("Sin descuento 😢")