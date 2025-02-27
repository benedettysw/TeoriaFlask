# Flask es un microframework ----- 💀

from flask import Flask , render_template

#-----------------------------------------------------------------------------


from flask_sqlalchemy import SQLAlchemy 


# Es una extesion para flask 

#que permite interactuar con bases de datos relacionales

#En lugar de escribir consultas SQL directamente

#Es una biblioteca o clase  proporciona por flask_sqlalchemy  esta herramientas para trabajar con bases de datos relacionales. Es un ORM (Object Relational Mapper) 


#ORM significa "Mapeo Objeto-Relacional" ORM permite interactuar con la base de datos utilizando objetos de Python en lugar de escribir consultas SQL directamente. Esto facilita la manipulación de datos y hace que el código sea más limpio y mantenible.

#-----------------------------------------------------------------------------


from flask_marshmallow import Marshmallow 

#Es una extension para flask que permite serializar y deserializar objetos de Python a JSON y viceversa

#serializar es el proceso de convertir un objeto de Python en una cadena JSON

#deserializar es el proceso de convertir una cadena JSON u otro formato a un objeto de Python 

#Json javascript object notation es un formato de intercambio de datos ligero y facil de leer y escribir para humanos

#Notacion de objetos de javascript

#es util para enviar y recibir datos entre una aplicacion cliente y un servidor web

#-----------------------------------------------------------------------------


myweb = Flask(__name__)

# Flask es una clase del modulo flask
# __name__ es una variable que 'PYTHON' asigna a un script cuando se ejecuta


# Ahora myweb es una instancia de la app Flask 

#-----------------------------------------------------------------------------


#CONFIGURACION Y CONEXION A LA BASE DE DATO

myweb.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/Teoriapython'

#La instancia de Flask tiene un atributo llamado config

#Es una clave dentro del diccionario config que le dice a Flask-SQLAlchemy dónde encontrar la base de datos a la que debe conectarse.

#Es el inicio de la URI que especifica el tipo de base de datos y el conector que se utilizará 

#Es el controlador (o conector) de Python que Flask-SQLAlchemy usará para comunicarse con MySQL.

#Root  el nombre de usuario para conectarte a la base de datos.

#localhost indica que la base de datos está en la misma máquina donde se ejecuta la aplicación Flask

#-----------------------------------------------------------------------------

myweb.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Si el rastreo está activado (True):

# Flask-SQLAlchemy vigila automáticamente que cambiaste el nombre de 'María' a 'Ana', incluso antes de guardar esos cambios en la base de datos.

# Si el rastreo está desactivado (False):

# Flask-SQLAlchemy no presta atención a los cambios en el objeto usuario hasta que tú le digas:

# Mejora el rendimiento: El rastreo consume recursos del sistema, incluso si no usas esa funcionalidad.

# Evita errores: Si no estás seguro de cómo funciona el rastreo, es mejor desactivarlo.


#----------------------------------------------------------------------------


# Cuando trabajas con sesiones de usuario - Por ejemplo, para mantener un usuario logueado:

# MyWeb.secret_key = "Ferrari@#$$"


#---------------------------------------------------------------

#Crear una instancia de la clase SQLAlchemy y Marshmallow


#myweb es tu aplicación Flask, y al pasarla como argumento, le estás diciendo a SQLAlchemy que use esa aplicación para acceder a su configuración (como la URI de la base de datos).


#Pasas myweb como argumento, lo que permite a Marshmallow usar tu aplicación Flask para configurar y crear esquemas.


db = SQLAlchemy(myweb)
ma = Marshmallow(myweb)

