import os
import DAO.CRUDCliente
import DAO.CRUDTipoCliente
#from DTO.TipoUsuario import TipoUsuario
from DTO.Cliente import Cliente

def menuPrincipal():
    os.system("cls")
    print("=== Menú Principal ===")
    print("1. Ingresar Clientes")
    print("2. Mostrar Clientes")
    print("3. Modificar Clientes")
    print("4. Eliminar Clientes")
    print("5. Salir")
    
def menuMostrar():
    os.system("cls")
    print("=== Menú Mostrar===")
    print("1. Mostrar Todos los Clientes")
    print("2. Mostrar Cliente Particular")
    print("3. Mostrar Cliente Parcial")
    print("4. Volver")

def ingresarCliente():
    os.system("cls")
    print("=== Ingresar Cliente ===")
    run=input("Ingrese el RUN del cliente: ")
    nombre=input("Ingrese el nombre del cliente: ")
    apellido=input("Ingrese el apellido del cliente: ")
    direccion=input("Ingrese la dirección del cliente: ")
    fono=input("Ingrese el teléfono del cliente: ")
    correo=input("Ingrese el correo del cliente: ")
    tipo_cliente=int(input("Ingrese el tipo de cliente (1, 2 o 3): "))    
    #Recorrer los tipos de Clientes
    datos=DAO.CRUDTipoCliente.mostrarTodosTiposClientes()
    print("*****************************")
    print("Tipos de Clientes Disponibles:")
    print("Id Tipo - Descripción")
    for dato in datos:
        print("{} - {}".format(dato[0],dato[1]))

    tipo_cliente=int(input("Ingrese el id del tipo de cliente: "))    
    montoCredito=float(input("Ingrese el monto de crédito del cliente: "))
    deuda=float(input("Ingrese la deuda del cliente: "))

    nuevo_cliente=Cliente(run,nombre,apellido,direccion,fono,correo,tipo_cliente,montoCredito,deuda)
    DAO.CRUDCliente.agregar(nuevo_cliente)  

def mostrarTodosClientes():
    os.system("cls")
    print("=== Mostrar Todos los Clientes ===")
    datos=DAO.CRUDCliente.mostrarTodosClientes()
    print("Id Cliente - RUN - Nombre - Apellido - Dirección - Teléfono - Correo - Tipo Cliente - Monto Crédito - Deuda")
    for dato in datos:
        print("{} - {} - {} - {} - {} - {} - {} - {} - {}".format(dato[0],dato[1],dato[2],dato[3],
                                                                    dato[4],dato[5],dato[6],dato[7],dato[8]))
    input("Presione Enter para continuar...")

def mostrarUnCliente():
    os.system("cls")
    print("=== Mostrar Cliente Particular ===")
    id_cliente=int(input("Ingrese el ID del cliente a mostrar: "))
    dato=DAO.CRUDCliente.mostrarParticularCliente(id_cliente)
    print("Id Cliente                   : {}".format(dato[0]))
    print("RUN                          : {}".format(dato[1]))
    print("Nombre                       : {}".format(dato[2]))
    print("Apellido                     : {}".format(dato[3]))
    print("Dirección                    : {}".format(dato[4]))
    print("Teléfono                     : {}".format(dato[5]))
    print("Correo                       : {}".format(dato[6]))
    print("Tipo Cliente (ID)            : {}".format(dato[7]))
    print("Monto Crédito                : {}".format(dato[8]))
    print("Deuda                        : {}".format(dato[9]))
    print("***************************************************")
    input("Presione Enter para continuar...")

def mostrarParcialCliente():
    os.system("cls")
    print("=== Mostrar Cliente Parcial ===")
    cant_clientes=int(input("Ingrese la cantidad de clientes a mostrar: "))
    datos=DAO.CRUDCliente.mostrarParcial(cant_clientes)    
    print("Id Cliente - RUN - Nombre - Apellido - Dirección - Teléfono - Correo - Tipo Cliente - Monto Crédito - Deuda")
    for dato in datos:
        print("{} - {} - {} - {} - {} - {} - {} - {} - {}".format(dato[0],dato[1],dato[2],dato[3],
                                                                    dato[4],dato[5],dato[6],dato[7],dato[8]))
    input("Presione Enter para continuar...")
def mostrar():
    while True:
        menuMostrar()
        op=int(input("Seleccione una opción: "))
        if op==1:
            mostrarTodosClientes()
        elif op==2:
            mostrarUnCliente()
        elif op==3:
            mostrarParcialCliente()
        elif op==4:
            break
        else:
            print("Opción inválida. Intente nuevamente.")
#Menu principal
while True:
    menuPrincipal()
    op=int(input("Seleccione una opción: "))
    if op==1:
        ingresarCliente()
    elif op==2:
        mostrar()
    elif op==3:
        pass
    elif op==4:
        pass
    elif op==5:
        op2=int(input("¿Está seguro que desea salir? ([SI-NO]): ")).upper()
        if op2=="SI":
            print("Saliendo del programa...")
            exit()        
        else:
            print("Opción inválida. Volviendo al menú principal.")