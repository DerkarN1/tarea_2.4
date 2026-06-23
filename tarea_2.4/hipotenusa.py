#Fecha:23/06/2026
#Autor:Bryan Adriano Nazareno Quinonez
#Tema:Realice el proceso que encuentre la hipotenusa de un triángulo rectángulo. 
#Primero pida al usuario los 2 lados del triángulo, y luego haga el cálculo.
#Pregunte al usuario si desea realizar otro cálculo.
#En este bucle use banderas (flags true o false) para indicar el fin del programa.
#Responda: Para este ejercicio fue necesario importar librerías? Cuál y para que la usó?

import math

continuar_programa = True

while continuar_programa:
    print("\n--- Cálculo de la Hipotenusa ---")
    lado_a = float(input("Ingrese la longitud del primer lado (cateto): "))
    lado_b = float(input("Ingrese la longitud del segundo lado (cateto): "))
    
    hipotenusa = math.sqrt(lado_a**2 + lado_b**2)
    
    print(f"La hipotenusa del triángulo es: {hipotenusa:.2f}")
    
    respuesta = input("¿Desea realizar otro cálculo? (s/n): ").lower()
    
    if respuesta != 's':
        continuar_programa = False  
        print("Programa terminado.")



#Respuesta a la pregunta.
#que libreria se importo?
# la libreria que se importo para este ejercicio fue math 
# pasa que se la uso?
#Se utilizó específicamente en la función math.sqrt(), la cual sirve para calcular de manera exacta la raíz cuadrada de la suma de los catetos al cuadrado ($a^2 + b^2$),

