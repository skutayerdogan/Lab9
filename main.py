import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234")
cursorObject = database.cursor()
cursorObject.execute("DROP DATABASE Marvel")

cursorObject.execute("CREATE DATABASE Marvel")

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    database='Marvel',
    password="1234")
if connection.is_connected():
    db_Info = connection.get_server_info()
    print("Connected to the MySQL server -> ", db_Info)
    cursor = connection.cursor()
    cursor.execute("select database() ")
    record = cursor.fetchone()
    print("Connected to the database -> ", record)

try:
    connection = mysql.connector.connect(
        host="localhost",
        database="Marvel",
        user="root",
        password="1234")
    mysqlQuery = """
     CREATE TABLE Marvel(
     ID int(10) NOT NULL,
     MOVIE varchar(20) NOT NULL,
     DATE varchar(20) NOT NULL,
     MCUPHASE varchar(20)
     PRIMARY KEY(ID))"""

    cursor = connection.cursor()
    result = cursor.execute(mysqlQuery)

    cursor.execute("SHOW TABLES")
    for tableName in cursor:
        print(tableName)
except mysql.connector.Error as error:
    print("FAILED: {}".format(error))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MYSQL is closed")

file = open("Marvel.txt")

try:
    connection = mysql.connector.connect(
        host="localhost",
        database="Marvel",
        user="root",
        password="1234")
    CursorObject = connection.cursor()

    while file:
        text = file.readline()
        if text == " ":
            break
        text_split = text.split()

        Insert = """INSERT INTO Marvel (ID, MOVIE, DATE, MCU_PHASE)
                 VALUES (%s, %s, %s, %s)"""
        record = (text_split[0], text_split[1], text_split[2], text_split[3])
        CursorObject.execute(Insert, record)
        connection.commit()

    print("Marvel table is updated successfully!")
    CursorObject.close()

    sql_select = "SELECT MOVIE FROM Marvel"
    cursorObject = connection.cursor()
    cursorObject.execute(sql_select)
    record = cursorObject.fetchall()

    for i in record:
        print(i)

    sql_delete = "DELETE FROM Marvel" \
                 " WHERE MOVIE= 'TheIncredibleHulk'"
    cursorObject = connection.cursor()
    cursorObject.execute(sql_delete)
    connection.commit()

    sql_phase = "SELECT * FROM Marvel" \
                " WHERE MCU_PHASE='Phase2'"
    cursorObject = connection.cursor()
    cursorObject.execute(sql_phase)
    record2 = cursorObject.fetchall()

    for i in record2:
        print(i)

    sql_update = "UPDATE Marvel SET DATE= 'November 3, 2017'" \
                 " WHERE MOVIE='Thor:Ragnarok'"
    cursorObject = connection.cursor()
    cursorObject.execute(sql_update)
    connection.commit()
except mysql.connector.Error as error:
    print("FAILED: {}".format(error))
finally:
    if connection.is_connected():
        cursorObject.close()
        connection.close()
        print("MySQL connection is closed!")
