import actions
option = True
while option == True:
    print('''
        1. CREATE DATABASE AND TABLE
        2. ADD ROWS OF DATA
        3. UPDATE A ROW OF DATA
        4. DELETE A ROW OF DATA
        5. DISPLAY ALL ROWS
        6. DISPLAY ONE ROW''')
    ans=input("Enter the number of what operation you would like to perform. Press E to exit")
    ans = ans.upper()
    if ans=="1":
        actions.createDatabase()
    elif ans=="2":
        actions.addRow()
    elif ans=="3":
        actions.updateRow()
        print("Row updated")
    elif ans=="4":
        code = input("What product code would you like to delete?")
        actions.deleteRow(code)
    elif ans=="5":
        actions.displayRows()
    elif ans=="6":
        code = input("What product code would you like to retrieve?")
        actions.displayARow(code)
    elif ans =="E":
        option = False
    elif ans !="":
        print("Not a valid choice")


