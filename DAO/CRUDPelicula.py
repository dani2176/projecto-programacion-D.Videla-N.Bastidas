from DAO.Conexion import Conexion

host="localhost"
user="root"
password=""
db="bd_peliculas"

def agregar(p):

    try:

        con=Conexion(host,user,password,db)

        sql="""INSERT INTO pelicula
        (titulo_pelicula,duracion,fecha_de_estreno,
        genero,idioma,director)

        VALUES('{}',{},'{}',{},{},'{}')
        """.format(
            p.titulo_pelicula,
            p.duracion,
            p.fecha_de_estreno,
            p.genero,
            p.idioma,
            p.director
        )

        con.ejecutar_query(sql)

        con.commit()

        print("Película agregada correctamente")

        con.desconectar()

    except Exception as e:
        print("Error:",e)

def mostrarTodasPeliculas():

    try:

        con=Conexion(host,user,password,db)

        sql="SELECT * FROM pelicula"

        cursor=con.ejecutar_query(sql)

        datos=cursor.fetchall()

        con.desconectar()

        return datos

    except Exception as e:
        print("Error:",e)

def mostrarParticular(id_pelicula):

    try:

        con=Conexion(host,user,password,db)

        sql="""
        SELECT * FROM pelicula
        WHERE id_pelicula={}
        """.format(id_pelicula)

        cursor=con.ejecutar_query(sql)

        datos=cursor.fetchone()

        con.desconectar()

        return datos

    except Exception as e:
        print("Error:",e)

def mostrarParcial(texto):

    try:

        con=Conexion(host,user,password,db)

        sql="""
        SELECT * FROM pelicula
        WHERE titulo_pelicula LIKE '%{}%'
        """.format(texto)

        cursor=con.ejecutar_query(sql)

        datos=cursor.fetchall()

        con.desconectar()

        return datos

    except Exception as e:
        print("Error:",e)

def eliminar(id_pelicula):

    try:

        con=Conexion(host,user,password,db)

        sql="""
        DELETE FROM pelicula
        WHERE id_pelicula={}
        """.format(id_pelicula)

        con.ejecutar_query(sql)

        con.commit()

        print("Película eliminada correctamente")

        con.desconectar()

    except Exception as e:
        print("Error:",e)

def editar(p):

    try:

        con=Conexion(host,user,password,db)

        sql="""
        UPDATE pelicula
        SET titulo_pelicula='{}',
            duracion={},
            fecha_de_estreno='{}',
            genero={},
            idioma={},
            director='{}'
        WHERE id_pelicula={}
        """.format(
            p.titulo_pelicula,
            p.duracion,
            p.fecha_de_estreno,
            p.genero,
            p.idioma,
            p.director,
            p.id_pelicula
        )

        con.ejecutar_query(sql)

        con.commit()

        print("Película modificada correctamente")

        con.desconectar()

    except Exception as e:
        print("Error:",e)