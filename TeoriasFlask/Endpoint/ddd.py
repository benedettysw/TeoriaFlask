from conexion import db , ma 
from Model.clientes import clientes

from flask import Blueprint , request

from sqlalchemy.exc import SQLAlchemyError


routes_guardar = Blueprint ("routes_guardar" , __name__)


@routes_guardar.route("/guardar" , methods = ['POST'])
def guardar():
    try:   
        nombre = request.json['nombre']
        apellido = request.json['apellido']

    
        usuario_registrado = db.session.query(clientes).filter(clientes.nombre == nombre).first()

        if usuario_registrado:
            return {"mensaje":"usuario existente"}

    

        DatosParaGuardar = clientes(nombre , apellido)
        db.session.add (DatosParaGuardar)
        db.session.commit()

        return {"mensaje":"datos guardados exitosamente"} , 200 

    except SQLAlchemyError as e:
            db.session.rollback() #revertir cambio en caso de error 

            return {"error":f"Error al guardar los datos: {str(e)}"} , 500

    except Exception as e:
        return {"error":f"Error inesperado {str(e)}"} , 500