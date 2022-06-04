from Insert.InsertDT import ID
import mysql.connector
from Tables.CreateTB import TB
from datetime import datetime
import sys

tb = TB('User', 'BankAccount', 'Transaction')
db = 'ineuron1'


def dataintoUser():
    """
    This function will call the insert query and insert record
    into User Table manually with help of user.
    """
    data = ID()
    data.insertintoUser()

def dataintoBank():
    """
        This function will call the insert query and insert record
        into BankAccount Table manually with the help of user.
    """
    data = ID()
    data.insetintoBank()

def CheckAmount(id):
    """
    This function is to invoke the Stored Procedure of mysql to check the account balance of user
    :param id: It will take User id in form of integer, example : 1,2,3,4,5,....
    :return: It won't reutrn aythind
    """
    try:
        # connecting with database
        conn = mysql.connector.connect(host='localhost', user='root', database=db,password='mysql')
        mycursor = conn.cursor()
        # invoke the stored procedure 'checkamount'
        mycursor.callproc('checkamount',[id,])
        for result in mycursor.stored_results():
            # print(result.fetchall())
            amtname = result.fetchall()
            # getting list of tuple inside amtname variable

        print(f"Amount of Customer: {amtname[0][0]}")
        # get the Balance of User
        print(f"Name of Customer: {amtname[0][1]}")
        # get the Name of User

    except mysql.connector.Error as err:
        print('CheckAmount'+" "+str(err))
        sys.exit(0)

def withdrawn(amt, Bid):
    """
    This function is to invoke the Stored Procedure called withdrawn, it will help use to Withdrawn their amount.
    and also inserting the withdrawn history into Transaction Table of user.
    :param amt: It will take amount user wanted to withdrawn, example: 100,1000,1200,129121...
    :param Bid: It will take BankAccountID of user, example: 1,2,3,4,5.....
    :return: It won't return anything.
    """
    try:
        # creating connection to the database
        conn = mysql.connector.connect(host='localhost', user='root', database=db, password='mysql')
        mycursor = conn.cursor()
        # Invoke the Stored Procedure 'withdrawn'
        mycursor.callproc('withdrawn', [amt, Bid])
        for result in mycursor.stored_results():
            result = result.fetchall()
            # get the list of tuple in variable called result

        userid = result[0][0]
        # get the User_id from result
        # bankacc = result[0][1]
        # # get the Bank_acc_id
        amtleft = result[0][2]
        # get the Amount_left from user
        withdrwndate = datetime.now().strftime("%Y-%m-%d")
        # get the date while transaction happend

        Tans = tb.creatingtable3()


        # inserting record into transaction
        trans_query = f""" INSERT INTO {db}.{Tans}(
                            Transaction_date, User_id, Bank_acc_id, Withdrawn_amt, Amount_left)
                            VALUES (%s,%s,%s,%s,%s);
         
                       """
        transData = (withdrwndate, userid, Bid, amt, amtleft)

        mycursor.execute(trans_query,transData)
        # inserting all the records into Transaction table of User

    except mysql.connector.Error as err:
        print('Withdrawn'+" "+ str(err))
        sys.exit(0)

    else:
        conn.commit()
        print('Data of Transaction has been successfully inserted')


def transactioncheck(date,Uid):
    """
    This function is to invoke the Stored Procedure for checking the user transaction,
    with the help of this user can get his/her withdrawn history very easily.
    :param date: It will take the date when Trasaction happens, example: 2022-06-04 (YYYY-MM-DD)
    :param Uid: It will take the User_id to get the statement of particular user, example: 1,2,3,4,5....
    :return: It won't return anything
    """
    try:
        # connecting to the database
        conn = mysql.connector.connect(host='localhost', user='root', database=db, password='mysql')
        mycursor = conn.cursor()
        # invoke the Stored Procedure 'transactioncheck'
        mycursor.callproc('transactioncheck', [date,Uid])
        for result in mycursor.stored_results():
            trans = result.fetchall()
            # geting all the list of tuples into trans
            print('WithdrawnAmount  AmountLeft  NameofUser')
            for data in trans:
                print(data)

    except mysql.connector.Error as err:
        print('Transactioncheck'+" "+ str(err))
        sys.exit(0)






if __name__ == '__main__':
    task = input('Provide any number for you task : '
          '1 for Check Amount,'
          ' 2 for Withdrawn your money,'
          ' 3 for Check Transaction Statement: ')
    if task == str(1):
        id = int(input('Enter the Userid you want to check: '))
        CheckAmount(id)
    elif task == str(2):
        id = int(input('Enter the Bankid you want: '))
        amt = int(input('Enter the amount you want to withdrawn: '))
        withdrawn(amt, id) # it will take BankAccID

    else:
        id = int(input('Enter the Bankid you want: '))
        date = input('Give the date of transaction in YYYY-MM-DD format: ')
        transactioncheck(date, id)



    # dataintoUser()
    # dataintoBank()
    # id = int(input('Enter the id you want: '))
    # amt = int(input('Enter the amount you want to withdrawn: '))
    # date = input('Give the date of transaction: ')
    # CheckAmount(id)
    # withdrawn(amt,id) # it will take BankAccID
    # transactioncheck(date,id)



