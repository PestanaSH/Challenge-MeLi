# Challenge-MeLi
Challenge Docs en Drive Públicos

Documentos de desafio no Drive Public

Desenvolva um aplicativo para inventariar em um banco de dados todos os arquivos pertencentes à unidade de disco de um usuário. O banco de dados deve ser criado dentro do aplicativo, usando qualquer mecanismo (por exemplo, MySQL ou Redis). Esta base deve armazenar o nome do arquivo, a extensão, o proprietário do arquivo, a visibilidade (pública ou privada) e o fechamento da última modificação. Caso encontre arquivos que estejam configurados como públicos e possam ser acessados ​​por qualquer pessoa, você deve modificar esta configuração para tornar o arquivo privado e enviar um e-mail ao proprietário notificando a alteração realizada. A aplicação deve ter a lógica necessária para salvar no banco de dados apenas os arquivos que não foram salvos em nenhuma execução anterior ou atualizar o bloqueio de modificação ou qualquer outro dado em caso de correspondência. Você também deve manter um inventário histórico de todos os arquivos que já foram públicos. Esta aplicação deve ser desenvolvida em Python e deve ter testes que verifiquem o seu bom funcionamento. Prima:

- Aplicar boas práticas de programação.
- Documentação e bibliografia consultadas.
- Tratamento seguro das credenciais utilizadas.
- Dockerize o aplicativo. Quanto mais fácil de reproduzir o desafio, melhor :)

## Código fonte

### Base de dados

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

- https://docs.python.org/
- https://developers.google.com/drive/api/quickstart/python
- https://developers.google.com/gmail/api/quickstart/python
- https://stackoverflow.com