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

    # mydb = connection()
    # mycursor = mydb.cursor()
    #
    # sql = "INSERT INTO files (id, fileName, extension, fileOwner, lastModify, visibility) " \
    #       "VALUES (%s, %s, %s, %s, %s, %s)"
    # val = (2, "testePython", ".pdf", "lucas.pestana", "2022-04-01", "publico")
    # mycursor.execute(sql, val)
    #
    # mydb.commit()
    # print(mycursor.rowcount, "record inserted.")


def selectAll():
    mydb = connection()

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM files")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

# insertData()
# selectAll()
