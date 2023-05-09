# Reto de la semana
entrada = input("¡Hola! Introduce tu edad: ")

edad = 0

if entrada.isnumeric() :
    edad = int(entrada)
else :
    print("Dato incorrecto, Debes introducir un número")
    exit()
    
if edad <= 0 :
    print("WOOOOOOWW!! Que joven eres. Pero, lo siento, eso no es posible")
elif edad > 115 :
    print("Vaya!!!!! ¿Cómo le haces para vivir tanto? no te creo, mejor intenta de nuevo")
elif edad < 18 :
    print("Eres menor de esad así que no puedes comprar tu cigarro")
else :
    print("eresmayor de edad, aqui tienes tu cigarrillo")   
    