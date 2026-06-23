#fecha:23/06/2026
#Nombre:Bryan Adriano Nazareno Quinonez
#Tema: Se ingresa por teclado un entero comprendido entre 1 y 12.
#Cada número corresponde con un mes del año. Si es 1 se imprime 'Enero', si es 2 se imprime 'Febrero', etc,
#Para resolver este problema NO use condicionales, use la sentencia match.





mes = int(input("Ingresa un valor entre 1 y 12 :"))

mensaje = "El valor ingresaso corresponde al mes de : "

match mes :
    case 1:
        print(f"{mensaje} Enero")
    case 2:
        print(f"{mensaje} Febrero")
    case 3:
        print(f"{mensaje} Marzo")
    case 4:
        print(f"{mensaje} Abril")
    case 5:
        print(f"{mensaje} Mayo")
    case 6:
        print(f"{mensaje} Junio")
    case 7:
        print(f"{mensaje} Julio")
    case 8:
        print(f"{mensaje} Agosto")
    case 9:
        print(f"{mensaje} Septienbre")
    case 10:
        print(f"{mensaje} Obtubre")
    case 11:
        print(f"{mensaje} Novienbre")
    case 12:
        print(f"{mensaje} Dicienbre")
    case _:
        print("El valor ingresado no esta dentro del rango de 1 a 12")        
             

    
