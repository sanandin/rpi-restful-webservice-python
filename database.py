import sqlite3

conn = sqlite3.connect('/tmp/employeeschema.db')
print "Opened database successfully";

conn.execute("CREATE TABLE employee(age int(10), name varchar(30), empId int(100), designation varchar(30))")
print ("Table created successfully");
conn.execute("INSERT INTO employee VALUES(23,'Saicharan',67,'SE')")
print ("Records inserted successfully");
conn.close()
