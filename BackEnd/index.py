#Realizar las importaciones
#Tener un poco de conocimiento de python

from flask import Flask, request, jsonify
from flask_cors import CORS

from Gestor import Gestor
from Libros import Libro
app = Flask(__name__)
app.config["DEBUG"] = True

CORS(app)

#Instancia de Gestor
gestor = Gestor()

#Generacion de los endpoints

@app.route('/')
def home():
    return "SERVER IS WORKING!!!!"

#Obtener usuarios
@app.route('/usuarios')
def obtener_usuarios():
    return gestor.obtener_usuarios()    

#Login
@app.route('/login/<user>/<password>')
def login(user=None,password=None):
    res = gestor.obtener_usuario(user,password)
    if res ==None:
        return '{"data":false}'
    return '{"data":true}'

#Registro de usuarios
@app.route('/registro',methods=['POST'])
def registrar_usuario():
    dato=request.json
    gestor.crear_usuario(dato['nombre'],dato['password'],dato['usuario'],dato['apellido'])
    return '{"Estado":"Usuario Creado"}'

#Obtener Libros
@app.route('/obtenerlibros')
def obtenerlibros():
    return gestor.obtener_libros()

#Eliminar Libro
@app.route('/libros/<titulo>',methods=["DELETE"])
def eliminar_libro(titulo):
    if(gestor.eliminar_libro(titulo)):
        return 'Eliminado'
    return 'Error'
#Crear Libro

@app.route('/libros',methods=['POST'])
def insertar_libro():
    dato=request.json
    gestor.crear_libro(Libro(dato['titulo'],dato['autor'],dato['imagen'],dato['descripcion']))
    return '{"Estado":"Libro Creado"}'

#Actualizar Libro
@app.route('/libros/<libro>',methods=["PUT"])
def modificar_libro(libro):
    dato=request.json
    nuevo = Libro(dato['titulo'],dato['autor'],dato['imagen'],dato['descripcion'])
    if(gestor.modificar_libro(libro,nuevo)):
        return '{"Estado":"Libro Modificado"}'
    return '{"Estado":"No existe Libro"}'

#Iniciar el servidor

if __name__ == "__main__":
    app.run(port=5000,host="0.0.0.0",debug=True)




