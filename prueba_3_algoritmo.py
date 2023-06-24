#
#
import numpy as np
import funciones_prueba3 as fn


cert_nac = 500
cert_est_conyug = 1000

op= 0

while True:
    print("__________________________")
    print("Opciones de menú: \n1.Ingresar los datos personales.\n2.Buscar datos personales.\n3.Imprimir certificados.\n4.Salir.")
    print()
    op = int(input("Ingrese el numero de la opcion que desea realizar: "))


    if op == 1:

        #  Opcion 1, grabar informacion datos personales.

        nif = int(input("Ingrese su número de NIF: "))
        if nif == nif< len(nif(8)):                                #NIF (revisar)
            print("Ingreso correcto de NIF.") 
        else:
            print("ingreso de NIF incorrecto. ")
        
          
            nombre = input("Ingrese su nombre: ")              #nombre
        if nombre > (len(8)):
            print("ingreso de nombre correcto. ")
        else:
            print("Ingreso de nombre incorrecto")

            
            edad = int(input("Ingrese su edad: "))              #edad

        if edad > 0:
            print("Ingreso correcto de edad.")
        else:
            print("Ingreso incorrecto de edad.")    

        
        

    if op == 2:

        # Buscar
        if nif == len(12):
            print("Persona pertenece a la unión Europea.")
        else:
            print("Persona no pertenece a la unión europea.")




    if op == 3:
        print() 
        print("Menú certificado a imprimir:\n1.Certificado de nacimiento UE.\n2.Estado conyugal UE.\n")
        print()                  #imprimir certificados 
        op_certificado = int(input("Ingrese una opción: "))

        if op == 1:
            cert_nac = cert_nac + 1
            print(cert_nac)


    if op == 4:                           #salir
        print("Usted ha salido del programa.")
        break










