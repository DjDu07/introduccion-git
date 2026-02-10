def operacion_suma(a, b):
    if a > 0 and b > 0:
        return a + b

nombre = "Diego Joaquin"
apellido = "Diaz"

saludo = "Hola "+ nombre + " " + apellido + " ¿Que tal tu dia?"

print(saludo)

a = int(input("Elige el primer numero para sumar: "))
b = int(input("Elige el segundo numero a sumar: "))
suma = operacion_suma(a,b)

print("La suma de los dos numeros es: ", suma)