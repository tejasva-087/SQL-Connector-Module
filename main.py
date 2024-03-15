from sql_connector import SQLConnector

conn1 = SQLConnector('localhost', 'root', 'sqlconnect')
conn1.connect_database('helloworld')
print(conn1.see_databases())
print(conn1.see_tables())

conn1.close()