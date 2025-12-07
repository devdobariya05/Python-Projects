print("1. Observe the folloing Python code carefully and obtain the output, which will appear on the screen after execution of it.")
Text='Py9Th*1oN$'
s=''
for i in range(len(Text)):
    if Text[i].islower():
        if i%2!=0:
            s=s+Text[i].upper()
        else:
            s=s+Text[i-2:i+2]
            s=s+'*'
    elif Text[i].isdigit():
        if i%2==0:
            s=s+Text[i-1]
        else:
            s=s+Text[i-2:i+2]
            s=s+'@'
    elif Text[i].isupper():
        if i%2==0:
            s=s+Text[i].lower()
        else:
            s=s+Text[i+1]
            s=s+'#'
    else:
        s=s+'&'
print(s)

print("2.Write a program to input a word having Case alphabets only.\
Store each letter in a list and pass this list to a function that replaces each letter of the word by a letter three places\
down the alphabet i.e. each 'A' will be replaced by 'D', each 'B' will be replaced by 'E' and similarly,\
each 'Z' will be replaced by 'C'.")
def changeWord(chWord):
    nWord = ''
    shift = 3
    for l in chWord:
        nWord += chr(ord('A') + (ord(l) + shift - ord('A')) % 26)
    return nWord

w = input('Enter a word in Uppercase:')
if w.isupper() and w.isalpha():
    characters = list(w)
    nWord = changeWord(characters)
    print("Entered word:",w)
    print("Changed word:",nWord)
else:
    print('Each character must be an Uppercase only.')

print("3. Create a dictionary with the opposite mapping.")
n = int(input("How many students:"))
winlist = {}
for i in range(n):
	k = input("Name of student:")
	v = int(input("Number of competitions won:"))
	winlist[k] = v
print(winlist)
reversed_dictionary = {v : k for k, v in winlist.items()}
print(reversed_dictionary)

print("4. Write a program to find the pair of key : value to ask value.")
n = int(input("How many students:"))
st = {}
for i in range(n):
	k = input("Name of student:")
	v = int(input("Number of competitions won:"))
	st[k] = v
print(st)
ans = "y"
while ans == 'y' or ans == 'Y':
	v = int(input("Enter value:"))
	for k in st:
		if st[k] == v:
			print(k,':',st[k])
	ans = input("Do you want to check more:")

print("5. Write a function ISTOUPCOUNT() in Python to read contents from a text file WRITER.txt, to count and display the occurrence of\
the word IS,TO,UP.")
def ISTOUPCOUNT():
	c=0
	file=open('WRITER.txt','r')
	line=file.read()
	word=line.split()
	for w in word:
		if w=='IS' or w=='TO' or w=='UP':
			c=c+1
	print("Count of IS TO and UP is",c)
	file.close()
ISTOUPCOUNT()


print("6.ZeroDivisionError It is raised when the denominator in a division operation is zero.\
ValueError It is raised when a built-in method or operation receives an argument that has the right data type but mismatched or inappropriate values.")
try:
    x=50
    y=int(input("Enter the denominator: "))
    z=(x/y)
    print ("Division performed successfully.")
except ZeroDivisionError:
    print ("Denominator as ZERO is not allowed.")
except ValueError:
    print ("Only INTEGERS should be entered.")
else:
    print ("The result of division operation is ", z)
finally:
    print ("Thanking for using Exception handling.")

print("7. Write a program to add records in pickle and store it to binary  file 'student' using dictionary and functions. ")
import pickle as p
def add():
    rollno=int(input('Enter your Roll No.:'))
    name=input('Enter your Name:')
    sub1=int(input('Enter your marks of Sub1:'))
    sub2=int(input('Enter your marks of Sub2:'))
    sub3=int(input('Enter your marks of Sub3:'))
    sub4=int(input('Enter your marks of Sub4:'))
    sub5=int(input('Enter your marks of Sub5:'))
    total=sub1+sub2+sub3+sub4+sub5
    per=total/500*100
    if per>=90:
        gr='A+'
    elif per>=80:
        gr='A'
    elif per>=70:
        gr='B+'
    elif per>=60:
        gr='B'
    elif per>=50:
        gr='C+'
    elif per>=40:
        gr='C'
    elif per>=33:
        gr='D'
    else:
        gr='E'
    record={"RollNo":rollno,"Name":name,"Sub1":sub1,"Sub2":sub2,"Sub3":sub3,"Sub4":sub4,"Sub5":sub5,"Total":total,"Per(%)":per,"Grade":gr}
    with open('d:\student','ab') as f:
        p.dump(record,f)
add()

print("8. Write a program to show records in pickle and store it to binary  file 'student' using dictionary and functions. ")
import pickle as p
def show():
    f=open('d:\student','rb')    
    print("RollNo\tName\tSub1\tSub2\tSub3\tSub4\tSub5\tTotal\tPer(%)\tGrade")
    while True:
        try:
            L=p.load(f)
            print(L["RollNo"],"\t",L["Name"],"\t",L["Sub1"],"\t",L["Sub2"],"\t",L["Sub3"],"\t",L["Sub4"],"\t",L["Sub5"],"\t",L["Total"],"\t",L["Per(%)"],"\t",L["Grade"])
        except EOFError:
            break
    f.close()
show()

print("9. Write a program to search records in pickle and store it to binary  file 'student' using dictionary and functions. ")
import pickle as p
def search(rollno):
    f=open('d:\student','rb')
    flag=False
    while True:
        try:
            L=p.load(f)
            if L["RollNo"]==rollno:
                print(L["RollNo"],"\t",L["Name"],"\t",L["Sub1"],"\t",L["Sub2"],"\t",L["Sub3"],"\t",L["Sub4"],"\t",L["Sub5"],"\t",L["Total"],"\t",L["Per(%)"],"\t",L["Grade"])
                flag=True
        except EOFError:
            break            
    if flag==False:
        print('Record not found.')    
rollno=int(input('Enter your Roll No. to Search:'))
search(rollno)

print("10. Write a program to modify records in pickle and store it to binary  file 'student' using dictionary and functions. ")
import pickle as p
def modify(rollno):
    f=open('d:\student','rb')
    rec=[]
    flag=False
    while True:
        try:
            L=p.load(f)
            if L["RollNo"]==rollno:
                print("RollNo\tName\tSub1\tSub2\tSub3\tSub4\tSub5\tTotal\tPer(%)\tGrade")
                print(L["RollNo"],"\t",L["Name"],"\t",L["Sub1"],"\t",L["Sub2"],"\t",L["Sub3"],"\t",L["Sub4"],"\t",L["Sub5"],"\t",L["Total"],"\t",L["Per(%)"],"\t",L["Grade"])
                L["Name"]=input('Enter your new Name:')
                L["Sub1"]=int(input('Enter your new marks of Sub1:'))
                L["Sub2"]=int(input('Enter your new marks of Sub2:'))
                L["Sub3"]=int(input('Enter your new marks of Sub3:'))
                L["Sub4"]=int(input('Enter your new marks of Sub4:'))
                L["Sub5"]=int(input('Enter your new marks of Sub5:'))
                L["Total"]=L["Sub1"]+L["Sub2"]+L["Sub3"]+L["Sub4"]+L["Sub5"]
                L["Per(%)"]=L["Total"]/500*100
                if L["Per(%)"]>=90:
                    L["Grade"]='A+'
                elif L["Per(%)"]>=80:
                    L["Grade"]='A'
                elif L["Per(%)"]>=70:
                    L["Grade"]='B+'
                elif L["Per(%)"]>=60:
                    L["Grade"]='B'
                elif L["Per(%)"]>=50:
                    L["Grade"]='C+'
                elif L["Per(%)"]>=40:
                    L["Grade"]='C'
                elif L["Per(%)"]>=33:
                    L["Grade"]='D'
                else:
                    L["Grade"]='E'
                flag=True
            rec.append(L)        
        except EOFError:
            break
    f.close()
    if flag==False:
        print("Record not found.")
    else:
        f=open('d:\student','wb')
        for i in rec:
            p.dump(i,f)
        f.close()
rollno=int(input('Enter your Roll No. to Modify:'))
modify(rollno)

print("11. Write a program to delete records in pickle and store it to binary  file 'student' using dictionary and functions. ")
import pickle as p
def delete(rollno):
    f=open('d:\student','rb')
    rec=[]
    flag=False
    while True:
        try:
            L=p.load(f)
            if L["RollNo"]==rollno:
                print("RollNo\tName\tSub1\tSub2\tSub3\tSub4\tSub5\tTotal\tPer(%)\tGrade")
                print(L["RollNo"],"\t",L["Name"],"\t",L["Sub1"],"\t",L["Sub2"],"\t",L["Sub3"],"\t",L["Sub4"],"\t",L["Sub5"],"\t",L["Total"],"\t",L["Per(%)"],"\t",L["Grade"])
                print("Record deleted.")
                flag=True
            else:
                rec.append(L)
        except EOFError:
            break
    f.close()
    if flag==False:
        print("Record not found.")
    else:
        f=open('d:\student','wb')
        for i in rec:
            p.dump(i,f)
        f.close()        
rollno=int(input('Enter your Roll No. to Delete:'))
delete(rollno)

print("12. Write a program to add records and store it to CSV  file 'student1.csv' using list and functions.") 
import csv as c
def add():    
    with open('d:\student1.csv','a') as f1:
        cwriter=c.writer(f1,lineterminator='\n')        
        rollno=int(input('Enter your Roll No.:'))
        name=input('Enter your Name:')
        sub1=int(input('Enter your marks of Sub1:'))
        sub2=int(input('Enter your marks of Sub2:'))
        sub3=int(input('Enter your marks of Sub3:'))
        sub4=int(input('Enter your marks of Sub4:'))
        sub5=int(input('Enter your marks of Sub5:'))
        total=sub1+sub2+sub3+sub4+sub5
        per=total/500*100
        if per>=90:
            gr='A+'
        elif per>=80:
            gr='A'
        elif per>=70:
            gr='B+'
        elif per>=60:
            gr='B'
        elif per>=50:
            gr='C+'
        elif per>=40:
            gr='C'
        elif per>=33:
            gr='D'
        else:
            gr='E'
        record=[rollno,name,sub1,sub2,sub3,sub4,sub5,total,per,gr]
        cwriter.writerow(record)
add()

print("13. Write a program to show records to CSV  file 'student1.csv' using list and functions. ")
import csv as c
def show():
    with open('d:\student1.csv','r') as f:
        creader=c.reader(f)
        for r in creader:
            print(r)            
show()

print("14. Write a program to search records and show bar graph to CSV  file 'student1.csv' using list and functions.") 
import csv as c 
def search(rollno):    
    with open('d:\student1.csv','r') as f:
        creader=c.reader(f)
        next(f)
        for r in creader:            
            if int(r[0])==rollno:
                print(r[0],'\t',r[1],'\t',r[2],'\t',r[3],'\t',r[4],'\t',r[5],'\t',r[6],'\t',r[7],'\t',r[8],'\t',r[9])
                break
        else:
            print('Record not found.')
rollno=int(input('Enter your Roll No. to Search:'))
search(rollno)

print("14. Write a program to modify records and store it to CSV  file 'student1.csv' using list and functions.") 
import csv as c
def modify(rollno):
    flag=0
    with open('d:\student1.csv','r') as f:
        L=[]
        field=[]
        data=c.reader(f)
        field=next(data)
        for r in data:
            if int(r[0])==rollno:
                name=input('Enter your Name:') 
                sub1=int(input('Enter your marks of Sub1:'))
                sub2=int(input('Enter your marks of Sub2:'))
                sub3=int(input('Enter your marks of Sub3:'))
                sub4=int(input('Enter your marks of Sub4:'))
                sub5=int(input('Enter your marks of Sub5:'))
                total=sub1+sub2+sub3+sub4+sub5
                per=total/500*100
                if per>=90:
                    gr='A+'
                elif per>=80:
                    gr='A'
                elif per>=70:
                    gr='B+'
                elif per>=60:
                    gr='B'
                elif per>=50:
                    gr='C+'
                elif per>=40:
                    gr='C'
                elif per>=33:
                    gr='D'
                else:
                    gr='E'
                L.append([rollno,name,sub1,sub2,sub3,sub4,sub5,total,per,gr])
                print("Record modified.")
                flag=1
            else:
                L.append(r)
        if flag==0:
            print("Record not found.")
        else:
            with open('d:\student1.csv','w') as f:
                cwriter=c.DictWriter(f,fieldnames=field,lineterminator='\n')
                cwriter.writeheader()
                cwriter=c.writer(f,lineterminator='\n')
                cwriter.writerows(L)
rollno=int(input('Enter your Roll No. to Modify:'))
modify(rollno)

print("15. Write a program to delete records to CSV  file 'student1.csv' using list and functions. ")
import csv as c
def delete(rollno): 
    flag=0
    with open('d:\student1.csv','r') as f:
        L=[]
        field=[]
        data=c.reader(f)
        field=next(data)
        for r in data:
            if int(r[0])==rollno:
                print("Record deleted.")
                flag=1
            else:
                L.append(r)
        if flag==0:
            print("Record not found.")
        else:
            with open('d:\student1.csv','w') as f:
                cwriter=c.DictWriter(f,fieldnames=field,lineterminator='\n')
                cwriter.writeheader()
                cwriter=c.writer(f,lineterminator='\n')
                cwriter.writerows(L)
rollno=int(input('Enter your Roll No. to Delete:'))
delete(rollno)

print("16. Write a program to perform push, pop, peek and display operation for stack using list.")
def isEmpty(stk):
    if stk == []:
        return True
    else:
        return False
    
#This function pushes the value in Stack.
def Push(stk, item):
    stk.append(item)
    top = len(stk) -1
    
#This function removes the last value from the Stack and returns it.
def Pop(stk):
    if isEmpty(stk):
        return "Underflow"
    else:
        item = stk.pop()
        if len(stk) == 0:
            top = None 
        else:
            top = len(stk) -1
        return item
    
#This function refers to inspecting the value at the Stack's top without removing it.
def Peek(stk):
    if isEmpty(stk):
        return "Underflow"
    else:
        top = len(stk) -1
        return stk[top]
    
#This function shows the value from Stack in Last In First Out manner.
def Display(stk):
    if isEmpty(stk):
        print("Stack empty")
    else:
        top = len(stk) -1
        print(stk[top], "<-top")
        for a in range(top -1, -1, -1):
            print(stk[a])
# __main__
stack = []
top = None
while True:
    print("1.push")
    print("2.pop")
    print("3.peek")
    print("4.display")
    print("5.exit")
    ch=int(input("enter choice"))
    if ch==1:
        sNo = int(input("Enter Student No:"))
        sName = input("Enter Student Name:")
        age = int(input("enter age:"))
        item = [sNo, sName, age]
        Push(stack, item)
    elif ch == 2:
        item = Pop(stack)
        if item == "Underflow":
            print("Underflow!!! Stack is empy!!!")
        else:
            print("Popped item is", item)
    elif ch == 3: 
        item = Peek(stack)
        if item == "Underflow":
            print("Underflow!!! Stack is empy!!!")
        else:
            print("Topmost item is", item)
    elif ch == 4:
         Display(stack)
    elif ch == 5:
        break
    else:
        print("Invalid choice")

print("17. Write the definition of a user-defined function PushNV (N) which accepts a list of strings in the parameter N and pushes all strings\
which have no vowels present in it, into a list named NoVowel. The program should then use the function PushNV () to create a stack of words in the list Novowel\
so that it stores only those words which do not have any vowel present in it, from the list All Thereafter, pop each word from the list NoVowel and display the popped word.\
When the stack is empty display the message 'EmptyStack'.")
NoVowel=[]
def PushNV(N):
  for i in range(len(N)):
    if 'A' in N[i] or 'E' in N[i] or 'I' in N[i] or 'O' in N[i] or 'U' in N[i]:
      pass
    else:
      NoVowel.append(N[i])

All=[]
for i in range(5):
  w=input("Enter Words:")
  All.append(w)

PushNV(All)

while True:
  if len(NoVowel)==0:
    print("EmptyStack")
    break
  else:
    print(NoVowel.pop()," ",end='')

print("18. Write the definition of a user-defined function Push3_5(N) which accepts a list of integers in a parameter N and pushes all those integers which are\
divisible by 3 or divisible by 5 from the list N into a list named Only3_5.\
Write a program in Python to input 5 integers into a list named NUM. The program should then use the function Push3_5() to create the stack of the list of Only3_5.\
Thereafter pop each integer from the list only3_5 and display the popped value. When the list is empty, display the message 'StackEmpty'.\
If the integers input into the list NUM are [10, 6, 14, 18, 30]\
Then the stack Only3 _5 should store [10, 6, 18, 30]\
And the output should be displayed as 30 18 10 StackEmpty")
Only3_5=[]
def Push3_5(N):
  for i in N:
    if i %3==0 or i%5==0:
      Only3_5.append(i)
NUM=[]
for i in range(5):
  n=int(input("Enter the number to add to list:"))
  NUM.append(n)
Push3_5(NUM)
print("List of Only 3-5:",Only3_5)
while True:
  if Only3_5==[]:
    print("StackEmpty")
    break
  else:
    print(Only3_5.pop()," ",end='')
        
print("19. Alam has a list containing 10 integers. You need to help him create a program with separate user defined functions to perform the following operations based on this list.\
Traverse the content of the list and push the even numbers into a stack.\
Pop and display the content of the stack. \
For Example: If the sample Content of the list is as follows:N=[12, 13, 34, 56, 21, 79, 98, 22, 35, 38] \
Sample Output of the code should be: 38 22 98 56 34 12")
N=[12, 13, 34, 56, 21, 79, 98, 22, 35, 38] 
 
def PUSH(S,N):
    S.append(N) 

def POP(S):
    if S!=[ ]:
        return S.pop() 
    else:
        return None 

ST=[ ] 
for k in N:
    if k%2==0:
        PUSH(ST,k)

while True:
    if ST!=[]:
        print(POP(ST),end=" ")
    else:
        break

print("20. Julie has created a dictionary containing names and marks as key value pairs of 6 students.\
Write a program, with separate user defined functions to perform the following operations:Push the keys (name of the student) of the dictionary into a stack,\
where the corresponding value (marks) is greater than 75.Pop and display the content of the stack. For example: If the sample content of the dictionary is as follows:\
R={“OM”:76, “JAI”:45, “BOB”:89, “ALI”:65, “ANU”:90, “TOM”:82}'The output from the program should be: TOM ANU BOB OM")

R={"OM":76, "JAI":45, "BOB":89, "ALI":65, "ANU":90, "TOM":82} 
#The output from the program should be: TOM ANU BOB OM
def PUSH(S,N):
    S.append(N) 
def POP(S):
    if S!=[ ]:
        return S.pop()
    else:
        return None 
ST=[ ] 
for k in R:
    if R[k]>=75:
        PUSH(ST,k) 
while True:
    if ST!=[ ]:
        print(POP(ST),end=" ")
    else:
        break 

#21.1. Write a program to implement create operation in MySQL.
CREATE DATABASE IF NOT EXISTS mydatabase;
USE mydatabase;
CREATE TABLE IF NOT EXISTS student(sid integer primary key,
     name varchar(30) not null,
     std integer default 12,
     contact_no char(13) unique,
     age integer check(age >= 15),
     gender char(1));
     
#21.2. Write a program to implement insert operation in MySQL.
insert into student(sid, name, contact_no, age, gender) values(1, 'abc', 2514367878, 16, 'f'),(2, 'bcd', 2514367887, 17, 'm');

#21.3. Write a program to implement display operation in MySQL.
#To show the structures of a table.
desc student;
#To show the records of a table.
select * from student;

#22.1. Write a program to implement update operation in MySQL.
#To change individually value.
update student set gender = 'm' where sid = 1;
#To increase standard.
update student set std = std + 1;
#To change NULL value.
update student set city = NULL where sid = 1;
#To change multiple columns.
update student set std = 11, city = 'Surat' where sid = 1;

#22.2. Write a program to implement delete operation in MySQL.
#To delete all the rows from the table but does not free the space containing the table. 
DELETE FROM student;
#To delete all the rows from the table and free the space containing the table. 
TRUNCATE FROM student;
#To delete permanently the table. 
DROP TABLE student;
#To delete permanently the database. 
DROP DATABASE mydatabase;

#22.3. Adding a column to an existing table.
ALTER TABLE student ADD(father_name varchar(30));
#Adding a column with default value an existing table.
ALTER TABLE student ADD(city varchar(30) default "Surat");
#Modifying a data type size to an existing table.
ALTER TABLE student MODIFY name varchar(40);
#Renaming a column to an existing table.
ALTER TABLE student CHANGE name student_name varchar(40);
#Removing a column to an existing table.
ALTER TABLE student DROP city;
#Deleting PRIMARY KEY constraints to an existing table.
ALTER TABLE student DROP PRIMARY KEY;
#Adding PRIMARY KEY constraints to an existing table.
ALTER TABLE student ADD PRIMARY KEY(sid);

#23.1. Write a program to implement create operation in MySQL using Python.
def createTable():
    import mysql.connector as sql
    db = sql.connect(host="localhost",user="root",passwd="12345",database="mydatabase")
    if db.is_connected():
        print("Sucessfully connection")
    else:
        print("Error")
    c1=db.cursor()
    query="CREATE TABLE IF NOT EXISTS Marks (rollno int primary key ,SNAME varchar(20),acc int(3), bst int(3), cs int(3))" 
    print(query)        
    c1.execute(query)
    db.commit()
    print("Table Created.")
    c1.close()
    db.close()
createTable()

#23.2. Write a program to implement insert operation in MySQL using Python.
def insertRecord():
    import mysql.connector as sql
    db = sql.connect(host="localhost",user="root",passwd="12345",database="mydatabase")
    rno=int(input("Enter Rollno: "))
    sname=input("Enter Name: ")
    acc=int(input("enter acc marks "))
    bst=int(input("enter bst marks "))
    cs=int(input("enter cs marks "))
    c1=db.cursor()
    query="INSERT INTO Marks (rollno,SNAME,acc, bst, cs) VALUES ({},'{}',{},{},{})".format(rno, sname,acc,bst,cs)
    print(query)        
    c1.execute(query)
    db.commit()
    print("Record Inserted.")
    c1.close()
    db.close()
insertRecord()

#23.3. Write a program to implement show operation in MySQL using Python.
def showRecord():
    import mysql.connector as sql
    db = sql.connect(host="localhost",user="root",passwd="12345",database="mydatabase")
    c1=db.cursor()
    c1.execute("SELECT * FROM Marks")     
    data=c1.fetchall()                      
    cnt=c1.rowcount
    print("total rows: ",cnt)
    print("ROLLNO","SNAME","ACC","BST","CS")
    for  r in data :
        print(r)
    c1.close()
    db.close()
showRecord() 

#24.1. Write a program to implement search operation in MySQL using Python.
def searchRecord(rno):
    import mysql.connector as sql
    db = sql.connect(host="localhost",user="root",passwd="12345",database="mydatabase")
    c1=db.cursor()
    c1.execute("SELECT rollno,SNAME,acc,bst,cs FROM Marks WHERE rollno=%i"%(rno))
    data=c1.fetchall()
    print("ROLLNO","SNAME","ACC","BST","CS",sep="\t")
    for row in data:
        if row[0]==rno:        
            print(row[0],row[1],row[2],row[3],row[4],sep='\t')
    c1.close()
    db.close()    
rno=int(input("Enter Rollno to Search:"))
searchRecord(rno)

#24.2. Write a program to implement modify operation in MySQL using Python.
def modifyRecord(rno):
    import mysql.connector as sql
    db = sql.connect(host="localhost",user="root",passwd="12345",database="mydatabase")
    c1=db.cursor()
    c1.execute("SELECT rollno,SNAME,acc,bst,cs FROM Marks WHERE rollno={}".format(rno))
    data=c1.fetchall()
    for row in data:
        if row[0]==rno:
            sname=input("enter New Name to be Updated: ")
            acc=int(input("enter Updated acc Marks: "))
            bst=int(input("enter Updated bst Marks: "))
            cs=int(input("enter Updated cs Marks: "))            
            query="UPDATE Marks SET SNAME='{}', acc={}, bst={}, cs={} WHERE rollno={}".format(sname,acc,bst,cs,rno)
            print(query)
            c1.execute(query)
            db.commit()
            print("Record Modified.")
    c1.close()
    db.close()    
rno=int(input("Enter Rollno to Modify:"))
modifyRecord(rno)

#24.3. Write a program to implement delete operation in MySQL using Python.
def deleteRecord(rno): 
    import mysql.connector as sql
    db = sql.connect(host="localhost",user="root",passwd="12345",database="mydatabase")
    c1=db.cursor()
    if rno==rno:        
        query="DELETE FROM Marks WHERE rollno= {}".format(rno)
        c1.execute(query)
        x=c1.rowcount
        if x>0:
             print("Records found ",x)
             db.commit()
             print("Record Deleted.")
        else:
             print("No Such record Found")
rno=int(input("Enter Rollno to Delete:"))
deleteRecord(rno)

#25. To use joining more than one tables.
CREATE TABLE student(rno integer auto_increment primary key, name varchar(30));
CREATE TABLE fees(fno integer auto_increment primary key, fees decimal(10,2), rno integer, foreign key(rno) references student(rno));
INSERT INTO student(name) VALUES('ram'),('shyam'),('om'),('shiv');
INSERT INTO fees(fees,rno) VALUES(45000,2),(50000,1);
#CARTESIAN JOIN
SELECT s.rno, s.name, f.fees FROM student s, fees f;
SELECT s.rno, s.name, f.fees FROM student s CROSS JOIN fees f;
#EQUI JOIN
SELECT s.rno, s.name, f.fees FROM student s, fees f WHERE s.rno = f.rno;
SELECT s.rno, s.name, f.fees FROM student s, fees f WHERE s.rno = f.rno ORDER BY s.rno;
#INNER JOIN
SELECT s.rno, s.name, f.fees FROM student s INNER JOIN fees f ON s.rno = f.rno;
#OUTER JOIN
SELECT s.rno, s.name, f.fees FROM student s LEFT OUTER JOIN fees f ON s.rno = f.rno;
SELECT s.rno, s.name, f.fees FROM student s RIGHT OUTER JOIN fees f ON s.rno = f.rno;
#NATURAL JOIN
SELECT s.rno, s.name, f.fees FROM student s NATURAL JOIN fees f;
#AGGREGATE FUNCTIONS AND CONDITIONS ON GROUPS (HAVING CLAUSE)
INSERT INTO fees(fees,rno) VALUES(40000,3),(50000,2),(30000,3),(50000,1);
SELECT rno, SUM(fees) FROM fees GROUP BY rno HAVING SUM(fees) >= 60000;
SELECT rno, SUM(fees) FROM fees GROUP BY rno HAVING AVG(fees) <= 60000;
SELECT rno, SUM(fees) FROM fees GROUP BY rno HAVING COUNT(*) >= 2;
SELECT rno, SUM(fees), MAX(fees), MIN(fees) FROM fees GROUP BY rno HAVING SUM(fees) >= 60000;


#26. To create a form.
from tkinter import *

import tkinter as tk
from tkinter import ttk
import time

root = Tk()

#Draw a Form
root.geometry('1920x1080')

#Add icon
root.iconbitmap('hotel.ico')

#Add title near icon
root.title('Student Management System')

#Add background colour
root.config(bg = 'purple')

#Title label
label = Label(root, font = ('arial',50,'bold'), width = 1, height = 1, bg="purple", fg="white", relief = 'raise', bd = 13, text="Student Management System")
label.pack(fill=X)

#Welcome label
label = Label(root, text="Registration Form", bg="purple", fg="white", font=('Orbitron', 25), relief = 'raise', bd = 10)
label.pack(fill=X)

blankspace = Label(root, text="\n")
blankspace.pack()

#Add image
image1 = PhotoImage(file="staff.png")
label = Label(root, image=image1, relief = 'raise', bd = 5)
label.pack()

labelFrame = Frame(root, bg = 'navajo white', relief = 'ridge', bd = 10,)
labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.5)

#Student Name
lb1 = Label(labelFrame,text="Student Name : ", bg='purple', fg='white',relief = 'raise', bd = 5, width = 15, height = 1, font = ('arial',15,'bold'))
lb1.place(x=50,y=10)
        
bookInfo1 = Entry(labelFrame)
bookInfo1.place(x=365,y=10, relwidth=0.62, relheight=0.08)

#Gender
lb2 = Label(labelFrame,text="Gender : ", bg='purple', fg='white', relief = 'raise', bd = 5, width = 15, height = 1, font = ('arial',15,'bold'))
lb2.place(x=50,y=60)

var = IntVar()        
Radiobutton(labelFrame,text="Male",bg = 'navajo white',padx= 5, variable= var, value=1).place(x=365,y=60)
Radiobutton(labelFrame,text="Female",bg = 'navajo white',padx= 20, variable= var, value=2).place(x=465,y=60)

#Language
lb3 = Label(labelFrame,text="Language : ", bg='purple', fg='white', relief = 'raise', bd = 5, width = 15, height = 1, font = ('arial',15,'bold'))
lb3.place(x=50,y=110)
        
var1=IntVar()
Checkbutton(labelFrame,text="Python",bg = 'navajo white',variable=var1).place(x=365,y=110)
var2=IntVar()
Checkbutton(labelFrame,text="Java",bg = 'navajo white',variable=var2).place(x=480,y=110)

#Country
lb4=Label(labelFrame,text="Country : ", bg='purple', fg='white', relief = 'raise', bd = 5, width = 15, height = 1, font = ('arial',15,'bold'))#text="Country",width=20,font=("bold",10))
lb4.place(x=50,y=160)

list_of_country=[ 'India' ,'US' , 'UK' ,'Germany' ,'Austria']
c=StringVar()
droplist=OptionMenu(labelFrame,c, *list_of_country)
droplist.config(bg = 'navajo white',width=15)
c.set('Select your Country')
droplist.place(x=365,y=160)
        
#Submit Button
def start_progress():
    progress.start()

    # Simulate a task that takes time to complete
    for i in range(101):
      # Simulate some work
        time.sleep(0.01)    
        progress['value'] = i
        # Update the GUI
        labelFrame.update_idletasks()  
    progress.stop()

# Create a progressbar widget
progress = ttk.Progressbar(labelFrame, orient="horizontal", length=300, mode="determinate")
progress.pack(pady=195)

# Button to start progress
start_button = Button(labelFrame, text="SUBMIT", command=start_progress)
start_button.place(relx=0.4,rely=0.70, relwidth=0.18,relheight=0.08)

#Quit Button    
quitBtn = Button(labelFrame,text="Quit",bg='#f7f1e3', fg='black')
quitBtn.place(relx=0.6,rely=0.70, relwidth=0.18,relheight=0.08)

root.mainloop()



