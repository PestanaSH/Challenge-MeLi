import mysql.connector


def connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Abc@1234",
        database="driver"
    )
    print(mydb)
    return mydb


# Função para inserir os dados na base de dados
def insertData(file):
    print(file.id)
    print(file.name)
    print(file.shared)
    print(file.modifiedTime)
    print(file.owners)
    print(f'Extension: {file.mimeType}')

    mydb = connection()
    mycursor = mydb.cursor()

    sql = "INSERT INTO files (fileName, extension, fileOwner, lastModify, visibility, fileId) " \
          "VALUES (%s, %s, %s, %s, %s, %s)"
    val = (file.name, file.mimeType, file.owners, file.modifiedTime, file.shared, file.id)
    mycursor.execute(sql, val)

    mydb.commit()
    print(mycursor.rowcount, "record inserted.")


def selectAll():
    mydb = connection()

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM files")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

# insertData()
# selectAll()
