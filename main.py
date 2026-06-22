import os
import DAO.CRUDPelicula
from DTO.Pelicula import Pelicula


def menuPrincipal():
    os.system("cls")
    print("=== MENU PRINCIPAL ===")
    print("1. Ingresar Pelicula")
    print("2. Mostrar Peliculas")
    print("3. Modificar Pelicula")
    print("4. Eliminar Pelicula")
    print("5. Salir")


def menuMostrar():
    os.system("cls")
    print("=== MENU MOSTRAR ===")
    print("1. Mostrar Todas")
    print("2. Mostrar Particular")
    print("3. Mostrar Parcial")
    print("4. Volver")


def ingresarPelicula():

    os.system("cls")

    print("=== INGRESAR PELICULA ===")

    titulo=input("Titulo: ")

    duracion=int(input("Duracion (minutos): "))

    fecha=input("Fecha Estreno (AAAA-MM-DD): ")

    print("\nGENEROS")
    print("1. Terror")
    print("2. Ciencia Ficcion")
    print("3. Drama")

    genero=int(input("Seleccione genero: "))

    print("\nIDIOMAS")
    print("1. Español")
    print("2. Ingles")
    print("3. Portugues")

    idioma=int(input("Seleccione idioma: "))

    director=input("Director: ")

    pelicula=Pelicula(
        None,
        titulo,
        duracion,
        fecha,
        genero,
        idioma,
        director
    )

    DAO.CRUDPelicula.agregar(pelicula)

    input("\nPresione ENTER para continuar...")


def mostrarTodas():

    os.system("cls")

    datos=DAO.CRUDPelicula.mostrarTodasPeliculas()

    print("ID | TITULO | DURACION | FECHA | GENERO | IDIOMA | DIRECTOR")

    for dato in datos:
        print(dato)

    input("\nPresione ENTER para continuar...")


def mostrarParticular():

    os.system("cls")

    id_pelicula=int(input("Ingrese ID pelicula: "))

    dato=DAO.CRUDPelicula.mostrarParticular(id_pelicula)

    print("\nDATOS PELICULA")
    print(dato)

    input("\nPresione ENTER para continuar...")


def mostrarParcial():

    os.system("cls")

    texto=input("Ingrese parte del titulo: ")

    datos=DAO.CRUDPelicula.mostrarParcial(texto)

    for dato in datos:
        print(dato)

    input("\nPresione ENTER para continuar...")


def modificarPelicula():

    os.system("cls")

    id_pelicula=int(input("ID Pelicula: "))

    titulo=input("Nuevo titulo: ")

    duracion=int(input("Nueva duracion: "))

    fecha=input("Nueva fecha (AAAA-MM-DD): ")

    print("\nGENEROS")
    print("1. Terror")
    print("2. Ciencia Ficcion")
    print("3. Drama")

    genero=int(input("Genero: "))

    print("\nIDIOMAS")
    print("1. Español")
    print("2. Ingles")
    print("3. Portugues")

    idioma=int(input("Idioma: "))

    director=input("Director: ")

    pelicula=Pelicula(
        id_pelicula,
        titulo,
        duracion,
        fecha,
        genero,
        idioma,
        director
    )

    DAO.CRUDPelicula.editar(pelicula)

    input("\nPresione ENTER para continuar...")


def eliminarPelicula():

    os.system("cls")

    id_pelicula=int(input("ID pelicula a eliminar: "))

    DAO.CRUDPelicula.eliminar(id_pelicula)

    input("\nPresione ENTER para continuar...")


def mostrar():

    while True:

        menuMostrar()

        op=int(input("Seleccione opcion: "))

        if op==1:
            mostrarTodas()

        elif op==2:
            mostrarParticular()

        elif op==3:
            mostrarParcial()

        elif op==4:
            break

        else:
            print("Opcion invalida")


while True:

    menuPrincipal()

    op=int(input("Seleccione opcion: "))

    if op==1:
        ingresarPelicula()

    elif op==2:
        mostrar()

    elif op==3:
        modificarPelicula()

    elif op==4:
        eliminarPelicula()

    elif op==5:

        print("Saliendo...")

        break

    else:
        print("Opcion invalida")