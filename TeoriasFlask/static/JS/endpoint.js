// Funcion flecha ,  sirve para agrupar un proceso y es reutilizable 

const guardar = () => {


    // Buscamos , obtenemos en el dom (Html) los valores del id 
    // Obtiene el texto que el usuario ha escrito en los campos de entrada
    const nombre = document.getElementById('nombre').value;
    const apellidos = document.getElementById('apellido').value;


    //Validamos que los input , campos de entrada no esten vacio 
    if(!nombre || !apellidos){
        alert("Todos los campos son obligatirio😉")
        return;
    }

    // Envia los datos ingresados por el usuario al backend (Flask en este caso)
    // Enviamos una solocitud http "POST" al endpoint guardar
    // AXIOS ES UNA LIBRERIA DE JS SIRVE PARA HACER PETICIONES 'enviar o recibir datos' AL SERVIDO  


    axios.post('/Guardar/guardar', {
        nombre: nombre,
        apellidos: apellidos

    })

    // Solo se ejecutado cuando el proceso es exito 'peticion , accion'
    // Response es el objeto que contine la respuesta del servido 
    .then(response => {

        // Verificar si la respuesta fue exitosa "200 quiere decir que es exitosa"
        if(response.status === 200){
            alert("Datos guardardos")
        }

        // Si la peticion del endpoint guardar fue exitosa pero hubo un error al guardar 
        // los datos se ejecuta la siguiente linea 
        else{
            alert("Datos no guardados")
        }

    })

    //Este bloque se ejecuta si hay un error en la petición (por ejemplo, si el servidor   responde con un código de error o si la conexión falla).
    // error es el objeto que contiene información sobre el fallo. 

    .catch(error => {

        // Aquí se verifica si el error viene del servidor si es status 400 
        // Es de que ya ese usuario se registro 
        if(error.response && error.response.status === 400){
            alert("Usuario ya existente");


            
        // Si el error no es un 400, muestra otra alerta con el mensaje general de error
        }else{
            alert("Hubo un error al enviar los datos:"+error);
        }
    })
}
