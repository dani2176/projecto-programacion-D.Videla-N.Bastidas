from DAO.Conexion import Conexion

host="localhost"
user="root"
password=""
db="bd_peliculas"
def agregar(c):#c es un objeto de tipo cliente
    try:
        con=Conexion(host,user,password,db)
        sql="INSERT INTO cliente set run='{}', nombre='{}', apellido='{}', direccion='{}', " \
        "fono='{}', correo='{}', tipo_cliente={}, montoCredito={}, " \
        "deuda={}".format(c.run,c.nombre,c.apellido,c.direccion,c.fono,c.correo,
                        c.tipo_cliente,c.montoCredito,c.deuda)
        con.ejecutar_query(sql)
        con.commit()
        input("Cliente agregado exitosamente. Presione Enter para continuar...")
        con.desconectar()
    except Exception as e:
        print("Error al agregar cliente: ", e)

def editar(c): #c es una lista con los nuevos datos del cliente.
    try:
        con=Conexion(host,user,password,db)
        sql="UPDATE cliente set nombre='{}', apellido='{}', direccion='{}', " \
        "fono='{}', correo='{}', tipo_cliente={}, montoCredito={}, " \
        "deuda={} where run='{}'".format(c[1],c[2],c[3],c[4],c[5],
                                        c[6],c[7],c[8],c[0])
        con.ejecutar_query(sql)
        con.commit()
        input("Cliente editado exitosamente. Presione Enter para continuar...")
        con.desconectar()
    except Exception as e:
        print("Error al editar cliente: ", e)

def eliminar(id_cliente):
    try:
        con=Conexion(host,user,password,db)
        sql="DELETE from cliente where id_cliente='{}'".format(id_cliente)
        con.ejecutar_query(sql)
        con.commit()
        input("Cliente eliminado exitosamente. Presione Enter para continuar...")
        con.desconectar()
    except Exception as e:
        print("Error al eliminar cliente: ", e)

def mostrarTodosClientes():
    try:
        con=Conexion(host,user,password,db)
        sql="SELECT * from cliente"
        cursor=con.ejecutar_query(sql)
        datos=cursor.fetchall()
        con.desconectar()
        return datos
    except Exception as e:
        print("Error al mostrar todos los clientes: ", e)

def mostrarParticularCliente(id_cliente):
    try:
        con=Conexion(host,user,password,db)
        sql="SELECT * from cliente where id_cliente='{}'".format(id_cliente)
        cursor=con.ejecutar_query(sql)
        datos=cursor.fetchone()
        con.desconectar()
        return datos
    except Exception as e:
        print("Error al mostrar cliente: ", e)

def mostrarParcial(cant_clientes):
    try:
        con=Conexion(host,user,password,db)
        sql="SELECT * from cliente limit {}".format(cant_clientes)
        cursor=con.ejecutar_query(sql)
        datos=cursor.fetchall()
        con.desconectar()
        return datos
    except Exception as e:
        print("Error al mostrar clientes: ", e)