from DAO.Conexion import Conexion

host="localhost"
user="root"
password=""
db="empresa"

def mostrarTodosTiposClientes():
    try:
        con=Conexion(host,user,password,db)
        sql="SELECT * from tipo_cliente"
        cursor=con.ejecutar_query(sql)
        datos=cursor.fetchall()
        con.desconectar()
        input("Datos: {}".format(datos))
        return datos
    except Exception as e:
        print("Error al mostrar todos los tipos de clientes: ", e)
