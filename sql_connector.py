import mysql.connector as sql
from error import *


class SQLConnector:
    """Modul to connect to the database for people with little knowledge about mysql"""

    def __init__(self, host: str, user: str, password: str):
        # Checking for errors in the parameters
        assert type(host) == str, "The host should be a string"
        assert type(user) == str, "The user should be a string"
        assert type(password) == str, "The password should be a string"

        # Assigining the parameters from the user to self
        self.__host = host
        self.__password = password
        self.__user = user
        self.__connection = self.__make_connection
        self.__cursor = self.__make_cursor

    
    #####################################
    # Setting the properties
    #####################################
    @property
    def __make_connection(self):
        """Setting up the connection"""
        try:
            conn = sql.connect(host=self.__host, user=self.__user, password=self.__password)
            return conn
        except Exception:
            raise InvalidCredentials(InvalidCredentials.err_msg)
    
    @property
    def __make_cursor(self):
        """Setting up the cursor for the databse"""
        if (self.__connection.is_connected()):
            return self.__connection.cursor()
        else:
            raise ConnectionNotSuccessful(ConnectionNotSuccessful.err_msg)
        
    #####################################
    # Methods used withing class only
    #####################################
    @staticmethod
    def __list_converter(data):
        """Converts the list of tuples to list"""
        arr = []
        for i in data:
            arr.append(i[0])
        return arr
    
    # table checks
    @staticmethod
    def __check_name(table):
        """Check the name of the table or column if valid or not"""
        if (type(table) != str) or (table[0].isdigit()) or not(table.isalnum() or "$" in table or "_" in table):
            raise IncorrectName(IncorrectName.err_msg)
        else:
            return True
    
    @staticmethod
    def __check_columns(columns):
        """Checks the repetition of columns"""
        primary_key = False
        for i in columns:
            print(i)
    
    
    #####################################
    # Methods for the users
    #####################################
    # Database mehtods
    def close(self):
        """Close the connections to database"""
        self.__cursor.close()
        self.__connection.close()

    def see_databases(self):
        self.__cursor.execute("SHOW DATABASES;")
        return self.__list_converter(self.__cursor.fetchall())
        

    def connect_database(self, database):
        """Creating the database if not existing and using it"""
        self.__cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
        self.__connection.commit()
        self.__cursor.execute(f"USE {database};")
    
    def delete_database(self, database):
        """Deleting the database"""
        if database in self.see_databases():
            self.__cursor.execute(f"DROP DATABASE {database};")
        else:
            raise DeletingNonExistingDatabase(DeletingNonExistingDatabase.err_msg)

    def see_tables(self):
        """To view all the tables present in the database"""
        self.__cursor.execute("SHOW TABLES;")
        return self.__list_converter(self.__cursor.fetchall())
    
    # Table methods
    def check_table_exist(self, table):
        self.__check_name(table)
        if table in self.see_tables():
            return True
        else:
            return False

    def create_table(self, **kwargs):
        if (self.check_table_exist(kwargs["table_name"])):
            raise TableAlreadyExists(TableAlreadyExists.err_msg)
        elif(self.__check_columns(kwargs["columns"])):
            print('False')
    