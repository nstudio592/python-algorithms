'''This database stores an employee's first & last names, job title, and 
salary. It has functionality to create a database,add data
to that database, display all contents of the database, display
information unique to a specific employee, and modify/delete an
employee's details'''

import sqlite3

'''Connect to database and create cursor'''
conn = sqlite3.connect("data.db")
c = conn.cursor()

'''Function Declarations'''

def createTable():

    try:
        c.execute("CREATE TABLE IF NOT EXISTS \
        employees(ID INTEGER PRIMARY KEY\
        AUTOINCREMENT NOT NULL, fname TEXT, lname TEXT, pos TEXT,\
        salary REAL)")
        conn.commit()
        
    except sqlite3.OperationalError:
        print("Table Couldn't Be Created\n")
        
    print("Table Created\n")
    
def addEmployee():
    first = input("Enter employee's first name: ")
    last = input("Enter employee's last name: ")
    title = input("Enter employee's job title: ")
    pay = float(input("Enter employee's salary: "))
    
    c.execute("INSERT INTO employees(fname, lname, pos, salary) VALUES \
    (?, ?, ?, ?)", (first, last, title, pay))
    
    print("\n Employee data successfully added.\n")
    conn.commit()

def showAll():
    print("\nData Currently in the data base")
    print("=================================================\n")
    
    c.execute("SELECT * FROM employees")
    data = c.fetchall()
    #fetchall loads all selected data into a variable called data
    for row in data:
        print(row, "\n")
        
    print("=================================================\n")

def showEmployee():
    searchID = int(input("Enter ID of Employee \
    You'd Like To Look Up: ")) 
    c.execute("SELECT * FROM employees WHERE ID = ?", (searchID,))
    data = c.fetchall()
    print("\n", data, "\n")

def modify():
    searchID = int(input("Enter ID of employee whose data you'd\
     like to modify: "))
    
    first = input("Enter employee's first name: ")
    last = input("Enter employee's last name: ")
    title = input("Enter employee's job title: ")
    pay = float(input("Enter employee's salary: "))
    
    c.execute("UPDATE employees SET fname = ?, lname = ?, pos = ?, salary = ? \
    WHERE ID = ?",(first, last, title, pay, searchID))
    print("Data Was Successfully Updated!")
    conn.commit()

def deleteEmployee():
    searchID = int(input("Enter ID of employee you want to delete: "))
    c.execute("DELETE FROM employees WHERE ID = ?", (searchID, ))
    print("Deletion Successful!")
    conn.commit()

'''End of Function Declarations'''

def main():
    '''Create Command Line Interface and keep displaying it once 7 has
    not been selected'''
    
    print("Simple Database Management System")
    print("==================================")
    
    choice = 0
    while choice != '7': 
        print("\n1) Create Database")
        print("2) Add Employee Data")
        print("3) Display All Employees")
        print("4) Search For Specific Employee")
        print("5) Modify An Employee's Details")
        print("6) Delete An Employee's Details")
        print("7) Exit")
        choice = input("\nCoose an option: ")
        
        if choice == '1':
            createTable()
        elif choice == '2':
            addEmployee()
        elif choice == '3':
            showAll()
        elif choice == '4':
            showEmployee()
        elif choice == '5':
            modify()
        elif choice == '6':
            deleteEmployee()
        elif choice == '7':
            print("\nNow exiting... Thanks for using our program! :)")
            break
        else:
            print("\nSorry, you didn't enter a valid option. \n")

main()
