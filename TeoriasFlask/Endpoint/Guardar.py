from conexion import db , ma 
from Model.guardar import registros

from flask import Blueprint , request

#Blueprint es una clase de Flask que te permite organizar tus rutas en archivos separados.
 
#Un Blueprint en Flask es como una "mini aplicación" dentro de tu app principal. Sirve para agrupar rutas y mantener tu código organizado.

routes_guardar = Blueprint ("routes_guardar" , __name__)


#-------------------------------------------------------------


#Es un decorador que se utiliza para asociar una función a una URL específica dentro del Blueprint.

#endpoint es La URL específica que apunta a un recurso o acción en tu aplicación.

#Si intentas acceder a /guardar con un método diferente (como GET), recibirás un error HTTP 405 (Método no permitido).

#Tipos de metodos HTTP "Get para obtener datos 'Mostrar' " "Post para enviar datos" "Put para actualizar datos" "Delete para eliminar datos"

#Por defecto, Flask asocia una ruta con el método GET si no especificas nada

@routes_guardar.route("/guardar" , methods = ['Post'])
def guardar():

    #request es un objeto que representa la solicitud HTTP enviada por el cliente a tu aplicación de Flask.

    #request.json es un diccionario que contiene los datos enviados por el cliente en formato JSON. y los transforma a un diccionario de python

    nombre = request.json['nombre']
    apellido = request.json['apellidos']

    print(f"Hola {nombre} , {apellido} me recuerdas")

    


    #Query es un método de SQLAlchemy que se utiliza para realizar consultas en la base de datos.

    #first() es un método de SQLAlchemy que se utiliza para obtener el primer resultado de una consulta. si no devuelve nada, devuelve None.

    usuario_registrado = db.session.query(registros).filter(registros.nombre == nombre).first()

    if usuario_registrado:
        return "usuario existente" , 400 # Código de estado 400 para indicar error

    
    #CREAR UNA INSTANCIA DE LA CLASE CLIENTES miguel es el nombre que guarda al objeto creado
    miguel = registros(nombre , apellido)

    db.session.add (miguel)
    db.session.commit()

    return "datos guardados exitosamente"


# Proceso completo:
# Recibes los datos del cliente (nombre y apellido).
# Creas un objeto del modelo clientes con esos datos.
# Agregas el objeto a la sesión de la base de datos.
# Confirmas y aplicas los cambios con commit.
# Respondes al cliente que la operación fue exitosa.