from conexion import myweb , db , render_template 


#Importacion del metodo , ruta o accion a procesar 
from Endpoint.Guardar import routes_guardar


#Importacion de las tablas , se crean al momento de ejecutar el programa 
from Model.guardar import registros



# Agrupa , envuelve un  metodo exportar ,  organizando mejor la aplicación
myweb.register_blueprint(routes_guardar , url_prefix ="/Guardar")






# Que es un decorador? 

# Un decorador es una función que modifica el comportamiento de otra función sin cambiar su código directamente. Es como "envolver" una función con funcionalidad adicional.

@myweb.route('/')
def home():             #Es un bloque de codigo reutilizable
    return render_template('formulario.html')  #Renderizar , mostrar una plantilla htlml 

@myweb.route('/saludo')
def saludo():
    return "Hola mundo" #es una declaracion que se usa para devolver un valor y normalmente se usa dentro de una funcion


if __name__ == '__main__': #MAIN es una cadena especial que el interprete de python asigna a la variable __name__ cuando se ejecuta un script


    myweb.run(debug=True , host='0.0.0.0') #debug=True es una declaracion que se usa para depurar errores en el codigo 
    #El parametro host siver para poder acceder a la aplicacion desde cualquier dispositivo en la red local
    #por defecto flask usa el puerto 5000 y la ip es 127.0.0.1 que es la ip local