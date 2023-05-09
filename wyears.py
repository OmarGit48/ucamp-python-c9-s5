#Sobre el año

año_a = input ("Escribe el año actual: ")
año_c = input("Escribe un año cualquiera para calcular: ")

año_a = int(año_a)
año_c = int(año_c)

diferencia = 0

if año_a > año_c + 2 :
    print("Han pasado", (año_a - año_c), "año desde el año que has intriducido")
elif año_a < año_c - 2:
    print("faltan", año_c -año_a, "años para llegar al año que has intruducido")
elif año_a == año_c + 1:
    print("desde el", año_c, "ha pasdo 1 año")
elif año_a == año_c -1 :
    print("Para llegar a", año_c, "hace falta 1 año") 
else:
    print("Has intruducido el mismo año que el actual")
input("oprime cualquier tecla para continuar")
