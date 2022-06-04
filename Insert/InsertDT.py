import mysql.connector
from Database.CreateDB import DB
from Tables.CreateTB import TB
import sys


class ID:
    """
    This is an ID: Insert Data class
    This will responsible for inserting the records into respective tables,
    It won't take any arguments, this will use the DT and TB arguments as their class variable to invoke them.
    """
    def __init__(self):
        self.tb = TB('User','BankAccount', 'Transaction')
        self.db = DB('ineuron1', 'mysql')
        self.dbname = self.db.createDatabase()
        self.User = self.tb.creatingtable1()
        self.Bank = self.tb.creatingtable2()
        self.Tans = self.tb.creatingtable3()
        self.connection = mysql.connector.connect(host='localhost',
                                                  database = self.dbname,
                                                   user = 'root',
                                                   password = 'mysql')
        self.cursor = self.connection.cursor()

    def insertintoUser(self):
        """
        This is first method of ID class called as insetintoUser,
        This method is responsible for inserting records into user table.
        :return: It won't return anything
        """
        try:
            i = 0
            while True:
                user = input('Enter UserName, UserDOB, UserEmail without space and should separated by comma: ').split(',')
                if len(user) > 3:
                    print('Please Provide valid input')
                    break
                # insert values into UserTable
                user_query = f""" INSERT INTO {self.dbname}.{self.User}(
                                User_name, User_dob, User_email)
                                VALUES (%s, %s, %s)
                             """
                user_data = (user[0], user[1], user[2])

                self.cursor.execute(user_query,user_data)
                i = i + 1
                if i == 10:
                    break
                # this loop will ask for 10 records form user

        except mysql.connector.Error as err:
            print('USER_TABLE'+" "+ str(err))
            sys.exit(0)

        else:
            self.connection.commit()
            print('Data of user has been successfully inserted')


    def insetintoBank(self):
        """
                This is second method of ID class called as insetintoBank,
                This method is responsible for inserting records into BankAccount table.
                :return: It won't return anything
        """
        try:
            i = 0
            while True:

                bank = input('Enter BANK_ACC_ID, IS_USER_ACTIVE, AMOUNT without space and should separated by comma: ').split(',')
                if len(bank) > 3:
                    print('Please Provide valid input')
                    break

                # inserting records into Bank table
                bank_query = f"""INSERT INTO {self.dbname}.{self.Bank}(
                                Bank_acc_id, Is_user_active, Amount)
                                VALUES (%s, %s, %s)
                              """

                bank_data = (int(bank[0]), bank[1], float(bank[2]))

                self.cursor.execute(bank_query, bank_data)
                i = i + 1
                if i == 10:
                    break
                # this loop will ask for 10 records form user

        except mysql.connector.Error as err:
            print('BANK_TABLE'+" "+ str(err))
            sys.exit(0)

        else:
            self.connection.commit()
            print('Data of bank has been successfully inserted')







