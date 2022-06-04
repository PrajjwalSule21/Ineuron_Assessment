import mysql.connector
from Database.CreateDB import DB
import sys


class TB:
    """
    This is a TB : Table class
    This is responsible for creating desired tables
    It will take three arguments as table1,table2,table3
    table1: It will take the name of first table in a form of string
    table2: It will take the name of second table in a form of string
    table3: It will take the name of third table in a form of string
    """
    def __init__(self, table1, table2, table3):
        self.table1 = table1
        self.table2 = table2
        self.table3 = table3
        self.db = DB('ineuron1', 'mysql')
        self.dbname = self.db.createDatabase()
        self.connection = mysql.connector.connect(host='localhost', database = self.dbname,
                                                  user = 'root', password = 'mysql')
        self.cursor = self.connection.cursor()


    def creatingtable1(self):
        """
        It is a first method of TB class called as cretingtable1,
        This is responsible to create first table and maintain the connection,
        It will use class vairable self.table1
        :return: It will return the name of table1
        """
        try:
            #creting table no1
            table1_query = f""" CREATE TABLE IF NOT EXISTS {self.dbname}.{self.table1}(
                            User_id INT(15) AUTO_INCREMENT NOT NULL,
                            User_name VARCHAR(25),
                            User_dob DATE,
                            User_email VARCHAR(30),
                            User_created_date TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
                            PRIMARY KEY(User_id),
                            UNIQUE KEY(User_email)
                            );
                            """
            self.cursor.execute(table1_query)

        except mysql.connector.Error as err:
            print('TABLE1'+" "+ str(err))
            sys.exit(0)

        else:
            return self.table1

    def creatingtable2(self):
        """
                It is a second method of TB class called as cretingtable2,
                This is responsible to create second table and maintain the connection,
                It will use class vairable self.table2
                :return: It will return the name of table2
        """
        try:

            # creating table no 2
            table2_query = f""" CREATE TABLE IF NOT EXISTS {self.dbname}.{self.table2}(
                                            User_id INT(15) NOT NULL AUTO_INCREMENT,
                                            Bank_acc_id INT(30) NOT NULL,
                                            Is_user_active ENUM('YES', 'NO') NOT NULL,
                                            Amount int(50),
                                            PRIMARY KEY (Bank_acc_id),
                                            FOREIGN KEY (User_id) REFERENCES {self.table1}(User_id) 
                                            );
                                        """

            self.cursor.execute(table2_query)


        except mysql.connector.Error as err:
            print('TABLE2'+" "+ str(err))
            sys.exit(0)


        else:
            return self.table2

    def creatingtable3(self):
        """
                        It is a third and last method of TB class called as cretingtable3,
                        This is responsible to create third table and maintain the connection,
                        It will use class vairable self.table3
                        :return: It will return the name of table3
                """
        try:

            # cresting table no 3
            table3_query = f""" CREATE TABLE IF NOT EXISTS {self.dbname}.{self.table3}(
                                Transaction_date Date,
                                User_id INT,
                                Bank_acc_id INT,
                                Withdrawn_amt INT(30),
                                Amount_left INT(30),
                                FOREIGN KEY (Bank_acc_id) REFERENCES {self.table2}(Bank_acc_id)
                                );
                            """
            self.cursor.execute(table3_query)

        except mysql.connector.Error as err:
            print('TABLE3'+" "+ str(err))
            sys.exit(0)

        else:
            return self.table3














