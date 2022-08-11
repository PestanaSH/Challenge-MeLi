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

O arquivo db.py consulta as seguintes tabelas:
- Tabela files que tem as seguintes colunas:
  - id
  - name
  - extension
  - owner
  - lastModify
  - visibility
- Tabela que tem as seguintes colunas:
  - id
  - name
  - visibility
  - owner

O arquivo db.py faz as seguintes operações:
- Conexão com a base de dados
- Inserir os arquivos na tabela files
- Inserir os arquivos que estão com públicos na tabela logFiles
- Consultar se o arquivo já está gravada na tabela files
- Consultar se o arquivo já está gravado na tabela logFiles
- Atualização dos arquivos que estão publicos na tabela files

### APIDrive
O arquivo APIDrive.py contém a função "api()", que faz a conexão na API do Google Drive,
e gera um arquivo token.json que armazena os tokens de acesso. O arquivo é criado automaticamente
quando a autorização se completa pela primeira vez.

### main
O arquivo main.py é onde acontece a lógica principal da aplicação, logo realiza as conexões nos bancos de dados e a
conexão na API do Google Drive. Lista todos os arquivos do Drive e valida se os arquivos já existem na base de dados, e
também valida se os arquivos são públicos ou privados. Após essas validações o programa modifica a visibilidade dos arquivos
publicos, manda o e-mail para o responsável do arquivo e atualiza as informações na base de dados.

## Bibliografia

https://docs.python.org/
https://developers.google.com/drive/api/quickstart/python
https://developers.google.com/gmail/api/quickstart/python
https://stackoverflow.com