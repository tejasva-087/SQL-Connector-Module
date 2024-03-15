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
    # Class methods
    #####################################
    @staticmethod
    def __list_converter(data):
        arr = []
        for i in data:
            arr.append(i[0])
        return arr
    
    #####################################
    # Methods for the users
    #####################################
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

    def see_tables(self):
        """To view all the tables present in the database"""
        self.__cursor.execute("SHOW TABLES;")
        return self.__list_converter(self.__cursor.fetchall())
    
    def delete_database(self, database):
        """Deleting the database"""
        self.__cursor.execute(f"DROP DATABASE {database};")