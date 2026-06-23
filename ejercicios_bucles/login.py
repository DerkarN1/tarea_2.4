#Fecha:20/06/2026
#autor:Bryan Adrino Nazareno Quinonez
#tema:Login en el sistema 

#pida el usuario y comtraseña por teclado.
# el usuaario tiene 3 intentos para ingresar.
# contraseña administrador: definir por el programandor 
# Use la evaluacion en cortocircuito 
# Use bucle while 


usuario = "Avion"
contraseña = "0000"

intentos = 3
num = 0
acceso = False

print("Sistema de Inicio de Sesión ")
print("============================")

while num < intentos and not acceso:
    print(f"\nIntento {num + 1} de {intentos}")
    
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")
    
    if usuario == usuario and contraseña == contraseña:
        acceso = True
    else:
        print(" Datos invalidos Intentalo denuevo.")
        num += 1

if acceso:
    print("\nTu Ingreso fue exitoso")
else:
    print("\nHas agotado tus intentos. Intentalo mas tarde.")
