import sqlite3

conn = sqlite3.connect('mydatabase.db') #connect to database
c = conn.cursor()

def createTable():
    c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot\
    (age REAL, date TEXT, keyword TEXT, value REAL)")

def dataEntry():
    c.execute("INSERT INTO stuffToPlot VALUES(145, '2018-01-01'\
    , 'Python', 5)")
    conn.commit() #confirm data entry
    #c.close()
    #conn.close()
    
def printDB():
    result = c.execute("SELECT age, date, keyword, value FROM stuffToPlot")
    for row in result:
        print("Age:", row[0])
        print("Date:", row[1])
        print("keyword:", row[2])
        print("Value:", row[3])
    c.close()
    conn.close()
    
createTable()
dataEntry()
printDB()
