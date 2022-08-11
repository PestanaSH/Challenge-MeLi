# Challenge-MeLi
Challenge Docs en Drive Públicos

Desarrollar una aplicación para inventariar en una Base de Datos todos los archivos
pertenecientes a la unidad de Drive de un usuario.
La base de datos debe ser creada desde la aplicación, pudiéndose utilizar cualquier motor
(por ejemplo MySQL o Redis). Dicha base deberá almacenar el nombre del archivo, la
extensión, el owner del archivo, la visibilidad (público o privado) y la fecha de última
modificación.
En el caso de encontrar archivos que estén configurados como públicos y puedan ser
accedidos por cualquier persona, deberá modificar dicha configuración para establecer el
archivo como privado y enviar un e-mail al owner notificando el cambio realizado.
La aplicación deberá tener la lógica necesaria para guardar en la base sólo aquellos
archivos que no hayan sido almacenados en alguna corrida anterior o actualizar la fecha de
modificación o cualquier otro dato en caso de corresponder. Asimismo, deberá mantener un
inventario histórico de todos los archivos que fueron en algún momento públicos.
Esta aplicación debe ser desarrollada en Python y deberá contar con tests que verifiquen su
buen funcionamiento.
Bonús:
- Aplicar buenas prácticas de programación.
- Documentación y bibliografía consultada.
- Tratamiento seguro de las credenciales utilizadas.
- Dockerizar la aplicación.
Cuanto más fácil sea reproducir el challenge, mejor :)

## Código fuente

### Base de datos

El archivo db.py crear las siguientes tablas:
- Tabla de archivos que tiene las siguientes columnas:
  - identificación
  - nombre
  - extensión
  - dueño
  - últimoModificar
  - visibilidad
- Tabla que tiene las siguientes columnas:
  - identificación
  - nombre
  - visibilidad
  - dueño

El archivo db.py realiza las siguientes operaciones:
- Conexión de base de datos
- Insertar los archivos en la tabla de archivos
- Insertar los archivos que tienen público en la tabla logFiles
- Consultar si el archivo ya está registrado en la tabla de archivos
- Consulta si el archivo ya está registrado en la tabla logFiles
- Actualizar los archivos que son públicos en la tabla de archivos

### APIDrive
El archivo APIDrive.py contiene la función "api()", que realiza la conexión en la API de Google Drive,
y genera un archivo token.json que almacena los tokens de acceso. El archivo se crea automáticamente.
cuando la autorización se completa por primera vez.

### main
El archivo main.py es donde sucede la lógica principal de la aplicación, luego hace las conexiones en las bases de datos y el
conexión a la API de Google Drive. Enumera todos los archivos de Drive y valida que los archivos ya existen en la base de datos, y
también valida si los archivos son públicos o privados. Tras estas validaciones, el programa modifica la visibilidad de los archivos
público, enviar el correo electrónico al responsable del fichero y actualizar la información en la base de datos.

## Bibliografía

- https://docs.python.org/
- https://developers.google.com/drive/api/quickstart/python
- https://developers.google.com/gmail/api/quickstart/python
- https://stackoverflow.com
