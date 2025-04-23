ingreso_mensual = 2500
deuda = 0
puntuacion_credito = 700

# Operadores lógicos
if (ingreso_mensual or puntuacion_credito ) and deuda == 0:
    print("Préstamo aprobado 💰")
else:
    print("Préstamo rechazado 🚫")