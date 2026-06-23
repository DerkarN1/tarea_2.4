#Fecha:20/06/2026
#autor:Bryan Adrino Nazareno Quinonez
#tema: Adivina el numero correcto 

import random
oprtunidades = 5
num_ganador =random.randint(1, 55)
contador = 0
ganaste = False
print("Adivina el numero correcto entre 1 y 55\n***************************************\n")

while contador < oprtunidades and not ganaste:
    print(f"Oportunidad # {contador + 1}")
    aux = input("Cual es tu numero:")
     
    nun = 0
    if aux.isdigit():
        nun = int(aux)
    else:
        continue # vueleve al inicio del bucle
    if nun < num_ganador:
        print("Debesingresar un numero mas alto")
        print()
    elif nun > num_ganador:
        print("debes ingresar un numero mas bajo")
        print()
    else:
        ganaste = True
        print()
    contador+=1

if ganaste:
    print("Felicidades, ganaste un viaje a la final del mundial ")
else:
    print("Perdiste. sigue partisipando!!!")
