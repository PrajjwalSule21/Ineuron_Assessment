import mysql.connector
from mysql.connector import errorcode
import sys



class DB:
    """
    This is a DB : DataBase class.
    This class is responsible for creating the database
    It takes two arguments as dbname, password
    dbname = name of database it will take string as a input
    password = password of database it will take string as a input
    """
    def __init__(self, dbname, password):
        self.dbname = dbname
        self.password = password
        self.connection = mysql.connector.connect(user='root',
                                                  password=self.password,
                                                  host='localhost')
        self.cursor = self.connection.cursor()


    def createDatabase(self):
        """
        It is a method of DB class called as createDatabase
        It will create and maintain the connection woth Database
        :return: It will return the name of DB
        """
        try:
            # creating the database
            db_query = f"CREATE DATABASE IF NOT EXISTS {self.dbname}"
            self.cursor.execute(db_query)
            return self.dbname

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
                sys.exit(0)
            else:
                print('CreateBD'+" "+str(err))
                sys.exit(0)

