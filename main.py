from sql_connector import SQLConnector

conn1 = SQLConnector('localhost', 'root', 'sqlconnect')
conn1.connect_database('helloworld')

conn1.close()