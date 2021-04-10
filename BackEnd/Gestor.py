#Importaciones

from Usuarios import Usuario
from Libros import Libro
import json

class Gestor:
    def __init__(self):
        self.usuarios =[]
        self.libros=[]

        self.libros.append(Libro("La Divina Comedia","Dante Alighieri","https://m.media-amazon.com/images/I/51FBFYOaEZL.jpg","Relata el viaje de Dante por el Infierno, el Purgatorio y el Paraíso"))
        self.libros.append(Libro("La Divina Comedia 2","Dante Alighieri","https://m.media-amazon.com/images/I/51FBFYOaEZL.jpg","Relata el viaje de Dante por el Infierno, el Purgatorio y el Paraíso"))
        self.libros.append(Libro("La Divina Comedia 3","Dante Alighieri","https://m.media-amazon.com/images/I/51FBFYOaEZL.jpg","Relata el viaje de Dante por el Infierno, el Purgatorio y el Paraíso"))
        self.libros.append(Libro("La Divina Comedia 4","Dante Alighieri","https://m.media-amazon.com/images/I/51FBFYOaEZL.jpg","Relata el viaje de Dante por el Infierno, el Purgatorio y el Paraíso"))
        
        self.usuarios.append(Usuario('admin','admin','admin','admin'))

    def obtener_usuarios(self):
        return json.dumps([ob.__dict__ for ob in self.usuarios])

    def obtener_usuario(self,user,password):
        for x in self.usuarios:
            if x.user==user and x.password==password:
                return x
        return None

    def crear_usuario(self,nombre,password,usuario,apellido):
        self.usuarios.append(Usuario(nombre,apellido,password,usuario))

    def obtener_libros(self):
        return json.dumps([ob.__dict__ for ob in self.libros])
    
    def eliminar_libro(self,titulo):
        for x in self.libros:
            if(x.titulo==titulo):
                self.libros.remove(x)
                return True
        return False

    def crear_libro(self,Libro):
        self.libros.append(Libro)

    def modificar_libro(self,nombre,Libro):
        for x in self.libros:
            if(x.titulo==nombre):
                self.libros[self.libros.index(x)]=Libro
                return True
        return False