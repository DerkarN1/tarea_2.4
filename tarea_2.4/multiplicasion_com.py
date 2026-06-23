#Fecha:23/06/2026
#Autor:Bryan Adriano Nazareno Quinonez
#Tema:Se ingresa un número entero positivo entre 1 y 10. Si el número ingresado es 5
# , se debe realizar este proceso: 1 x 2 x 3 x 4 x 5, si es número es 6,
#  se multiplica 1 x 2 x 3 x 4 x 5 x 6, etc. El proceso se repite hasta que el número ingresado sea 0.

while True:
    numero = int(input("Ingrese un número entero entre 1 y 10 (0 para salir): "))
    
    if numero == 0:
        print("Programa terminado.")
        break
        
    if 1 <= numero <= 10:
        resultado = 1
        for i in range(1, numero + 1):
            resultado = resultado * i
            
        print(f"El resultado de la multiplicación consecutiva para {numero} es: {resultado}")
    else:
        print("Número fuera del rango permitido (1-10).")