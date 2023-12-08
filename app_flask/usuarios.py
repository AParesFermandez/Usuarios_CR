from app_flask.mysqlconnection import connectToMySQL

class Usuario:
    def __init__(self, datos):
        self.id = datos['id']
        self.nombre = datos['nombre']
        self.apellido = datos['apellido']
        self.email = datos['email']
        self.fecha_creacion = datos['fecha_creacion']
        self.fecha_actualizacion = datos['fecha_actualizacion']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        results = connectToMySQL('usuarios_cr').query_db(query)
        usuarios = []
        for u in results:
            usuarios.append( cls(u) )
        return usuarios


    @classmethod
    def save(cls, data):
        query = "INSERT INTO usuarios (nombre,apellido,email) VALUES (%(nombre)s,%(apellido)s,%(email)s);"

        # comes back as the new row id
        result = connectToMySQL('usuarios_cr').query_db(query,data)
        return result