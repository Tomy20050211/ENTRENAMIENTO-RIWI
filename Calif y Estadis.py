#Uso el sys para que cuando haya un error, no salte a los otros input
import sys

#Determinar el estado de aprobacion
print("_________________________________")
print("¡ BIENVENID@ A LA IE.BRRI BRRI ")

try:
    calificacion = float(input("* Ingresa tu calificación (0 - 100): \n "))
except ValueError:
    print("Error: Debes ingresar un número válido.")
    sys.exit()

# Evaluar si la calificación está dentro del rango válido
if 0 <= calificacion <= 100:
    if calificacion >= 60:
        print("¡FELICIDADES...APROBASTE!")
    else:
        print("NO APROBASTE...PARA LA PROXIMA :)")
else:
    print("Error...Ingresa un valor numérico en el rango de 0 - 100...")
    sys.exit()  # Detiene el programa aquí si la calificación está fuera del rango

# Calcular el promedio 
print("________________________________")
print("¡ VAMOS A CALCULAR TU PROMEDIO !")

# Permitir al usuario ingresar una lista de calificaciones (separadas por comas)
notas = input("* Ingresa una lista de calificaciones (separadas por comas):\n ")
try:
    calificaciones = [float(nota.strip()) for nota in notas.split(',')]
except ValueError:
    print("Error: Asegúrate de ingresar solo números separados por comas.")
    sys.exit()

# Calcular y mostrar el promedio de las calificaciones en la lista
promedio = sum(calificaciones) / len(calificaciones)

# Mostrar el promedio
print("____________________________________")
print(f"TU PROMEDIO ES DE: {promedio:.2f}")


#Preguntar al usuario por un valor específico
print("_____________________________________")
print("¡ VAMOS A CONTAR LAS CALIFICACIONES MAYORES ! ")
valor_mayor = float(input("* Ingresa un valor numerico para contar cuantas calificaciones son mayores a este:\n  "))

#Inicializamos el contador (cuenta cuántas calificaciones son mayores) y el índice (para recorrer la lista)
contador = 0
indice = 0

#Usamos un ciclo while para recorrer la lista de calificaciones una por una
while indice < len(calificaciones):

#Comparamos cada calificación con el valor ingresado
    if calificaciones[indice] > valor_mayor:
        contador += 1
    indice += 1

print(f"Solo {contador} calificaciones son mayor a {valor_mayor} !!")
 
# Verificar si la calificación inicial aparece en la lista
print("_________________________________________________")
print("¡ AHORA VERIFICAREMOS Y CONTAREMOS TUS CALIFICACIONES ! ")
contador = 0
limite_busqueda = 5  # Por ejemplo, detenemos el conteo si aparece 5 veces

for nota in calificaciones:
    if nota < 0 or nota > 100:
        continue  # Salta notas fuera de rango
    if nota == calificacion:
        contador += 1
        if contador >= limite_busqueda:
            print("¡La calificación aparece muchas veces! Deteniendo búsqueda...")
            break

print(f"La calificación {calificacion} aparece {contador} vez/veces en la lista.")


#PRESENTA OTROS ERRORES, PERO YA SE ME HACE DIFICIL HACERLO PÉRFECTO.. :C

