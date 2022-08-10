import mysql.connector


def connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Abc@1234",
        database="driver"
    )
    return mydb


# Função para inserir os dados na base de dados
def insertData(file):
    print(file.id)
    print(file.name)
    print(file.shared)
    print(file.modifiedTime)
    print(file.owners)
    print(f'Extension: {file.mimeType}')

    if selectById(file.id) is False:

        mydb = connection()
        mycursor = mydb.cursor()

        sql = "INSERT INTO files (fileName, extension, fileOwner, lastModify, visibility, fileId) " \
              "VALUES (%s, %s, %s, %s, %s, %s)"
        val = (file.name, file.mimeType, file.owners, file.modifiedTime, file.shared, file.id)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        print(f'O arquivo {file.name} foi gravado na base de dados!')
        print('-=' * 50)
    else:
        print('-=' * 50)
        print(f'O item {file.name} já está salvo na base de dados!')
        print('-=' * 50)


def selectAll():
    mydb = connection()

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM files")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)


def selectById(fileId):
    mydb = connection()
    mycursor = mydb.cursor()

    mycursor.execute(f"SELECT * FROM files WHERE fileId = '{fileId}'")

    result = mycursor.fetchone()

    print(result)
    if result is None:
        return False
    else:
        return True


def insertDataLog(file):
    print(f'Inserindo na base de dados logFiles')
    mydb = connection()
    mycursor = mydb.cursor()

    sql = "insert into logFiles (name, visibility, fileId, owner) VALUES (%s, %s, %s, %s)"
    val = (file.name, file.shared, file.id, file.owners)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Data inserido na base de dados logFiles!")
    print('-=' * 100)
