from sql_connector import SQLConnector

conn1 = SQLConnector('localhost', 'root', 'sqlconnect')
conn1.connect_database('helloworld')
conn1.create_table(
  table_name = 'table_name',
  columns = [
    {
      'column': 'column1',
      'type': 'INT',
      'constraint': 'PRIMARY KEY'
    }, {
      'column': 'column2',
      'type': 'CHAR',
      'constraint': ['UNIQUE', 'NOT NULL'],
      'length': 30
    }, {
      'column': 'column3',
      'type': 'CHAR',
      'constraint': 'PRIMARY KEY',
      'length': 30
    }, {
      'column': 'column4',
      'type': 'FLOAT',
      'constraint': 'CHECK',
      'condition': 'column_name < 10'
    }
  ]
)
# conn1.ma
conn1.close()