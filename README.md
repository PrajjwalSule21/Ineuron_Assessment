# Ineuron_Assessment

## Make a console with the help of Python and SQL
Functions of the console should be:
1.	User can check their bank balance
2.	User can withdraw some amount form their account
-	Bank amount should be 5000 not less then that.
3.	User can check their transaction statemtent.

#### Have a Three table in a database called as 
#### User Table (user_id, user_name, user_dob, user_email, user_created_date)
#### BankAccount Table (user_id, bank_acc_id, is_useractive, amount)
#### Transaction Table Table (transaction_date, user_id, bank_acc_id, withdrawn_amount)


## Solution:

### Step1: Python Program
* **Directory name**: Database
* **Script name**: CreateDB.py
* **Class name**: class DB
* **Function**: NA
* **Arguments take**:  ‘dbname’ as database name and ‘password’ as password of database
* **Methods**: def createDatabase()
* **Method returns**: name of database ‘self.dbname’
* **Functionality**: This class and its method is responsible to create a database and make connection with the respective database.

### Step2: Python Program
* **Directory name**: Tables
* **Script name**: CreateTB.py
* **Class name**: class TB
* **Function**: NA
* **Arguments take**:  ‘table1’ as name of first table, ‘table2’ as name of second table and ‘table3’ as name of third table. 
* **Methods**: def creatingtable1(), def creatingtable2() and creatingtable3() 
* **Method returns**: name of tables ‘self.table1’, ‘self.table2’ and ‘self.table3’
* **Functionality**: This class and its method is responsible to create a table and make connection with the respective database.

### Diagram
![2022-05-02 (2)](‪F:/Ineuron_Assesment_job/Untitled Diagram (1).jpg)

### Step3: MySQL Stored Procedure
* **Store Procedure**: checkamount
* **Argument**: IN id INT
* **Structure**:  
**`CREATE DEFINER=`root`@`localhost` PROCEDURE `checkamount`(in id int)
BEGIN
select bankaccount.amount, user.user_name
from user
inner join bankaccount on user.user_id = bankaccount.user_id
where bankaccount.Bank_acc_id = id;
END`**
* **Functionality**: This SQL stored procedure is responsible for invoke the User bank amount.

### Step4: MySQL Stored Procedure
* **Store Procedure**: withdrawn
* **Argument**: IN amt INT, IN id INT
* **Structure**:  
**`CREATE DEFINER=`root`@`localhost` PROCEDURE `withdrawn`(in amt int, in id int)
BEGIN
update bankaccount 
set amount = if(amount>5000, amount-amt, "Amount Limit Error") 
where Bank_acc_id = id;`**

**`select user_id, bank_acc_id, amount
from bankaccount
where bankaccount.Bank_acc_id = id;
END`** 
* **Functionality**: This SQL stored procedure is responsible for invoke the withdrawn amount.

### Step5: MySQL Stored Procedure
* **Store Procedure**: transactioncheck
* **Argument**: IN dt DATE, IN id INT
* **Structure**:  
**`CREATE DEFINER=`root`@`localhost` PROCEDURE `transactioncheck`(in dt date, in id int)
BEGIN
select transaction.withdrawn_amt, transaction.amount_left,  user.user_name
from user
inner join transaction on user.user_id = transaction.user_id
where transaction.transaction_date = dt and transaction.user_id = id;
END`**
* **Functionality**: This SQL stored procedure is responsible for invoke the transaction statement.


### Step6: Python Program
* **Directory name**: Insert
* **Script name**: InsertDT.py
* **Class name**: class ID
* **Function**: NA
* **Arguments take**:  It won’t be any arguments. 
* **Methods**: def insertintoUser() and def insetintoBank() 
* **Method returns**: It won’t return anything
* **Functionality**: This class and its method is responsible to insert records into respective tables.




### Step7: Python Program
* **Directory name**: Ineuron_Assesment
* **Script name**: main.py
* **Class name**: NA
* **Function**: def dataintoUser(), def dataintoBank(), CheckAmount(), withdrawn(), transactioncheck()
* **Arguments take**:   def dataintoUser(), def dataintoBank() this function won’t take any arugments, CheckAmount(), withdrawn(), transactioncheck() These functions will take arguments as per the Stored Procedure.
* **Methods**: NA
* **Method returns**: NA
* **Functionality**: This is a main script which invokes the SQL Stored Procedures
