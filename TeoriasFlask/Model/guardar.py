from conexion import  db , myweb 



#Esta clase define un modelo de datos para mapear la tabla de la base de datos

#Mapear es como  una libreta "base de dato" y cada hoja es una tabla "cada clase" mapear es conectar la libreta con la hoja

class registros(db.Model):
    __tablename__ = "tbregistro"

#__tablename__  es una variable que viene dentro de sqlalchemy que se usa para especificar el nombre de la tabla en la base de datos 


    
    id = db.Column(db.Integer, primary_key=True)

    #db es una instacia de SQLAlchemy
    #column es una clase de sqlalchemy que se usa para definir columnas en una tabla

    nombre = db.Column(db.String(111))
    apellido = db.Column(db.String(111))
   


    #ESTA PARTE DEL CODIGO DEFINE EL METODO CONSTRUCTOR DE LA CLASE
    #INIT ES UN METODO QUE SE EJECUTA CUANDO SE CREA UN OBJETO DE LA CLASE registross

    #init toma lso parametros que se le pasan y los asigna a las variables de la clase

    #self es una variable que se usa para hacer referencia a la instancia actual de la clase
   
   #SElf es una convecion de python 
    
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
       
      
    
with myweb.app_context():

    #crea contexto de la aplicacion  es como la creacion en la tabla de la base de datos
    #el uso de appcontext garantiza que la aplicacion este en ejecucion cuando se cree la tabla 

    db.create_all()

    #es un metodo de sqlalchemy que se usa para crear todas las tablas en la base de datos
    #si la tabla ya existe no la crea de nuevo