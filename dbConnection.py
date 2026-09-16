import oracledb

connection = oracledb.connect(
    user = "sys",
    password="oracle",
    dsn="localhost:1521/orcl",
    mode=oracledb.SYSDBA
)

cursor = connection.cursor()
cursor.execute("select * from employtest")
for row in cursor:
    print(row)
cursor.close()
connection.close()    