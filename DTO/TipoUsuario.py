class TipoUsuario:
    def __init__(self,id_tipo_usuario,descripcion):
        self.id_tipo_usuario=id_tipo_usuario
        self.descripcion=descripcion

    def __str__(self):
        return f"TipoUsuario: {self.id_tipo_usuario} - {self.descripcion}"
    