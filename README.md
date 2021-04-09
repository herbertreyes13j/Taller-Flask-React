# Taller-Flask-React

## Back-End

- El primer paso es verificar que se tenga instalado python. Realizamos la verificacion por medio de:
  + python --version
  + pip --version

- Luego procedemos a instalar flask, por medio del siguiente comando:
  + pip install flask
  + pip install cors

- Luego procedemos a crear nuestro archivo *index.py* donde vamos a desarrollar la aplicacion.
- El siguiente paso es realizar las importaciones necesarias:
  + from flask import Flask, request, jsonify
  + from flask_cors import CORS
- Creamos nuestra aplicacion por medio de: app = flask.Flask(__name__)
- Luego procedemos a crear los endpoints necesarios
- Agregamos al final: *app.run()*
- E iniciamos nuestra aplicacion por medio de: *python index.py*

## Front-End
