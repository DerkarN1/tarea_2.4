#fecha:23/06/2026
#Nombre:Bryan Adriano Nazareno Quinonez
#Tema: Escribir un algoritmo que pida al usuario un número entero comprendido entre 10 y 1000. 
#A continuación, muestre por pantalla si este número es par o impar o es cero.
#Use condicionales anidadas (una condición dentro de otra). Use continue, cuando el número no esté en el rango solicitado. 
#El proceso se repite mientras el número ingresado por el usuario sea distinto de -1


while True:
    numero = int(input("Ingrese un número entero entre 10 y 1000 (-1 para salir): "))
    
    if numero == -1:
        print("Programa terminado.")
        break    
    if numero < 10 or numero > 1000:
        print("Número fuera de rango. Intente de nuevo.")
        continue  
        
    if numero == 0:
        print("El número es cero.")
    else:
        if numero % 2 == 0:
            print(f"El número {numero} es PAR.")
        else:
            print(f"El número {numero} es IMPAR.")