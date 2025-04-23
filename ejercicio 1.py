#Variables
movimiento = True
ventana_abierta = True
hora_noche = True

# Operadores lógicos
if not movimiento or (ventana_abierta and hora_noche):
    print("¡ALARMA! 🚨")
else:
    print("Todo seguro 🔒")