# Proyecto Unidad5 - Integrantes
  - Gonzales León Stefani 
  - Zapata More Jesus Freddy

# Metodo de uso para instalar el Proyecto
 - clonar el repositorio y crear un entorno virtual, una ves activado el entorno virtual
   instalar las librerias especificadas `pip install -r requirements.txt`
 - Crear las migraciones y migrar hacia la base de datos escogida
 - `python manage.py makemigrations` y despues `python manage.py migrate`
 - Puede crear un superusuario con el sgte comando (tiene que tener el env activado y estar dentro de la carpeta del proyecto
  al nivel de manage.py) `python manage.py createusperuser`
 
# Uso de las Rutas Definidas de la api
  - Para obtener un token debes tener un usuario ya registrado y en caso de querer registrar uno se debe ingresar a `localhost:8000/signup/` e ingresar los datos pedidos
  - Para Obtener un token solo se necesita un email (registrado) y una contraseña, que devuelve un token que sera usado en los headers de todas 
    las peticiones que se realizen dentro de la api (Authorization : Token {token_generado})

# Para mas información sobre la api (Documentacion)
  - puede ingresar a la ruta localhost:8000/swagger/ donde se mostraran todas las rutas y los metodos permitidos,
  - ![Imagen swagger](https://github.com/FreddyxD5/ProyectoU5/blob/main/static/assets/imagenV1.png)
  - Loguearse
  - ![Imagen swagger](https://github.com/FreddyxD5/ProyectoU5/blob/main/static/assets/imagenV2.png)
  - Obtener el Token
  - ![Imagen swagger](https://github.com/FreddyxD5/ProyectoU5/blob/main/static/assets/imagenV3.png)
  - Validar el token dentro de la API y ya podemos usar las diferentes rutas dependiento de los permisos que tenga el usuario
  - ![Imagen swagger](https://github.com/FreddyxD5/ProyectoU5/blob/main/static/assets/imagenV4.png)
