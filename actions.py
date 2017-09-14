import sqlite3
#creates a database of products
def createDatabase():
    try:
        conn = sqlite3.connect('product.db')
        conn.execute('''CREATE TABLE PRODUCTS
                     (ProductID INT PRIMARY KEY NOT NULL,
                     AMOUNT INT DEFAULT '0',
                     DESCRIPTION TEXT NOT NULL,
                     PRICE REAL NOT NULL,
                     STORAGENUMBER INT DEFAULT '1' ,
                     STATEORIGIN CHAR(2) NOT NULL
                     );''')
        conn.close()
    #handles if the database already exists
    except sqlite3.OperationalError:
        print("The database already exists")
#adds rows of data to the table
def addRow():
    try:
        conn = sqlite3.connect('product.db')

        conn.execute('''INSERT INTO PRODUCTS
                     (ProductID,AMOUNT, DESCRIPTION,PRICE, STORAGENUMBER,STATEORIGIN)\
                     VALUES(60, 2, 'staples', 0.34, 43, 'MN');''')
        conn.execute('''INSERT INTO PRODUCTS
                         (ProductID, DESCRIPTION,PRICE, STORAGENUMBER,STATEORIGIN)\
                         VALUES(61, 'pens', 0.50, 44, 'ND');''')
        conn.execute('''INSERT INTO PRODUCTS
                         (ProductID,AMOUNT, DESCRIPTION,PRICE, STORAGENUMBER,STATEORIGIN)\
                         VALUES(62, 10, 'paper', 0.10, 43, 'CA');''')
        conn.execute('''INSERT INTO PRODUCTS
                             (ProductID,AMOUNT, DESCRIPTION,PRICE, STORAGENUMBER,STATEORIGIN)\
                             VALUES(63, 10, 'keyboards', 20.00, 23, 'TX');''')
        conn.execute('''INSERT INTO PRODUCTS
                             (ProductID,AMOUNT, DESCRIPTION,PRICE, STORAGENUMBER,STATEORIGIN)\
                             VALUES(64, 100, 'paper clips', 0.05, 43, 'VA');''')
        conn.execute('''INSERT INTO PRODUCTS
                             (ProductID,AMOUNT, DESCRIPTION,PRICE, STORAGENUMBER,STATEORIGIN)\
                             VALUES(65, 2, 'computers', 500.00, 44, 'CA');''')
        print("Rows have been added to the table")
        conn.commit()
        conn.close()
    #handles if a product code is already in the database
    except sqlite3.IntegrityError:
        print("These rows of data already exist in the table")
#updates a random row with new data
def updateRow():
    conn = sqlite3.connect('product.db')
    ProductId = 60
    newAmount = 5
    conn.execute('''UPDATE PRODUCTS SET AMOUNT = ? WHERE ProductId = ?''', (newAmount, ProductId))
    conn.commit()
    conn.close()
#delete the row a user wants to
def deleteRow(code):
    conn = sqlite3.connect('product.db')
    ProductIdD = code
    cursor = conn.execute('DELETE FROM PRODUCTS WHERE ProductId = ?', (ProductIdD,))
    #uses rowcount to see if a row was affected
    deleteStatus = (cursor.rowcount)
    #depending on if rows were affected or not a message will print
    if deleteStatus == 0:
        print("This product in not in the database")
    elif deleteStatus == 1:
        print("Row was deleted")
    conn.commit()
    conn.close()
#displays all of the rows in the database
def displayRows():
    conn = sqlite3.connect('product.db')
    cursor = conn.execute('''SELECT ProductID,AMOUNT, DESCRIPTION,PRICE, STORAGENUMBER,STATEORIGIN from
                          PRODUCTS''')
    print("Here are all the table rows")
    for row in cursor:
        print("ProductID =", row[0], "AMOUNT=", row[1], "DESCRIPTION=", row[2], "PRICE=", row[3], "STORAGENUMBER=",
              row[4], "STATEORIGIN=", row[5])
#takes in the input product code number and searched the database for it
def displayARow(code):
    conn = sqlite3.connect('product.db')
    ProductId = code
    cursor = conn.execute(
        '''SELECT ProductID,AMOUNT, DESCRIPTION,PRICE, STORAGENUMBER,STATEORIGIN FROM PRODUCTS WHERE ProductId = ?''',
        (ProductId,))
    #boolean value to see if the product was found in the databse
    found = False
    for row in cursor:
        found = True
        print("ProductID =", row[0], "AMOUNT=", row[1], "DESCRIPTION=", row[2], "PRICE=", row[3], "STORAGENUMBER=",
              row[4],
              "STATEORIGIN=", row[5])
    if not found:
        print("That product does not exist in this database")
    conn.commit()
    conn.close()
