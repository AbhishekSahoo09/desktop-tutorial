print('''                                            WELCOME TO CIS'S REPORT CARD MANAGEMENT''')
import mysql.connector as c
import maskpass as m
con=c.connect(host="localhost",user="root",passwd="tigerxc@800",database="report_card")
cur=con.cursor()
    #To Add Students Information
def add():
    query='''create table if not exists Student_information(SADMISSION_NO    VARCHAR(10) PRIMARY KEY,
    SROLL_NO	VARCHAR(5),SNAME VARCHAR(30),FNAME VARCHAR(30),MNAME VARCHAR(30) ,
    PHONE	VARCHAR(12),	ADDRESS	VARCHAR(100),SCLASS VARCHAR(5),SSECTION VARCHAR(5))'''
    cur.execute(query)
    SadmNo=input("Enter Student Admission Number : ")
    SrollNo=input("Enter Student Roll Number : ")
    Sname=input("Enter Student Name : ")
    Fname=input("Student's Father's Name : ")
    Mname=input("Student's Mother's Name : ")
    Phone=input("Enter Your Phone Number : ")
    Address=input("Enter your Address : ")
    Sclass=input("Enter Student's class : ")
    Sec=input("Enter Students Section : ")
    query='''insert into 
    Student_information values('{}','{}','{}','{}','{}','{}','{}','{}','{}')
    '''.format(SadmNo,SrollNo,Sname,Fname,Mname,Phone,Address,Sclass,Sec)
    cur.execute(query)
    cur.execute("COMMIT")
    cur.close()
#To show Information of a student
def sinfo():
    SadmNo=input("Enter Student Admission Number")
    query="Select * from Student_Information where sadmission_no='{}'".format(SadmNo)    
    cur.execute(query)
    data=cur.fetchall()
    print(data)
    cur.close()
        
#To Fetch all Details
def fetch_all():
    query="select * from Student_information"
    cur.execute(query)
    
    data=cur.fetchall()  
    print(data)
    cur.close()
#To Update
def update():
    SadmNo=input("Enter student Admission Number")    
    query="Select * from Student_information where SADMISSION_NO ='{}'".format(SadmNo)
    cur.execute(query)
    print("Press 1 To Update Student's Roll_NO : ")
    print("Press 2 To Update Student's Name : ")
    print("Press 3 To Update Student's Father's Name : ")
    print("Press 4 To Update Student's Mother's Name : ")
    print("Press 5 To Update Student's Phone Number : ")
    print("Press 6 To Update Student's Address : ")
    print("Press 7 To Update Student's Class : ")
    print("Press 8 To Update Student's Section : ")
    n=int(input)
    if n==1:
        roll=input("Enter Students Roll Number")
        query='''update student_information set sRoll_no='{}' where sadmission_no='{}' '''.format(roll,SadmNo)
        cur.execute(query)
    elif n==2:
        name=input("Enter Students Name")
        query='''update student_information set sname='{}' where sadmission_no='{}' '''.format(name,SadmNo)
        cur.execute(query)
    elif n==3:
        fname=input("Enter Student's Father's Name")
        query='''update student_information set fname='{}' where sadmission_no='{}' '''.format(fname,SadmNo)
        cur.execute(query)
    elif n==4:
        Mname=input("Enter Student's Mother's Name")
        query='''update student_information set Mname='{}' where sadmission_no='{}' '''.format(Mname,SadmNo)
        cur.execute(query)
    elif n==5:
        Phone=input("Enter Phone number")
        query='''update student_information set phone='{}' where sadmission_no='{}' '''.format(Phone,SadmNo)
        cur.execute(query)
    elif n==6:
        adds=input("Enter Student's Address")
        query='''update student_information set address='{}' where sadmission_no='{}' '''.format(adds,SadmNo)
        cur.execute(query)
    elif n==7:
        classs=input("Enter Student's class")
        query='''update student_information set sclass='{}' where sadmission_no='{}' '''.format(classs,SadmNo)
        cur.execute(query)
    else:                            
        sec=input("Enter Student's Section")
        query='''update student_information set ssection='{}' where sadmission_no='{}' '''.format(sec,SadmNo)
        cur.execute(query)   
        cur.execute("Commit")
        cur.close()
#To store students marks
def marks():
    query='''create table if not exists marks (Sadmission_No varchar(10) primary key,Sname varchar(20),Maths float(4,2),
    Chem float(4,2),Phy float(4,2),Eng float(4,2),CS float(4,2),percentage float(10,3))'''
    cur.execute(query)
    sadmn=input("Enter student's admission number : ")
    sname=input("Enter Student name : ")
    maths=float(input("Enter marks of maths : "))
    phy=float(input("Enter marks of phy : "))
    chem=float(input("Enter marks of chem : "))
    cs=float(input("Enter marks of cs : "))
    eng=float(input("Enter marks of eng : "))
    per=(maths+phy+chem+eng+cs)/5
    query='''insert into marks values('{}','{}',{},{},{},{},{},{})'''.format(sadmn,sname,maths,chem,phy,eng,cs,per)
    cur.execute(query)
    cur.execute("Commit")
    cur.close()
    print("||Marks Entered Succefully||")
#To update Mark of a student
def updatemark():
        
    SadmNo=input("Enter student Admission Number")    
    query="Select * from marks where SADMISSION_NO ='{}'".format(SadmNo)
    cur.execute(query)
    print("Press 1 To Update Maths mark")
    print("Press 2 To Update Chem mark")
    print("Press 3 To Update Phy mark")
    print("Press 4 To update eng mark")
    print("Press 5 To Update Cs mark")
    n=int(input)
    if n==1:
        mrk=float(input("Enter Students Maths mark"))
        query='''update marks set Maths={} where sadmission_no='{}' '''.format(mrk,SadmNo)
        cur.execute(query)
        cur.execute("Select chem from marks where sadmission='{}'").format(SadmNo)
        data1=cur.fetchall()
        cur.execute("Select phy from marks where sadmission='{}'").format(SadmNo)
        data2=cur.fetchall()
        cur.execute("Select eng from marks where sadmission='{}'").format(SadmNo)
        data3=cur.fetchall()
        cur.execute("Select cs from marks where sadmission='{}'").format(SadmNo)
        data4=cur.fetchall()
        per=(data1+data2+data3+data4+mrk)/5
        cur.execute("update marks set percentage={} where sadmission='{}'").format(per,SadmNo)
    elif n==2:
        mrk=float(input("Enter Students Chem mark"))
        query='''update marks set chem={} where sadmission_no='{}' '''.format(mrk,SadmNo)
        cur.execute(query)
        cur.execute("Select maths from marks where sadmission='{}'").format(SadmNo)
        data1=cur.fetchall()
        cur.execute("Select phy from marks where sadmission='{}'").format(SadmNo)
        data2=cur.fetchall()
        cur.execute("Select eng from marks where sadmission='{}'").format(SadmNo)
        data3=cur.fetchall()
        cur.execute("Select cs from marks where sadmission='{}'").format(SadmNo)
        data4=cur.fetchall()
        per=(data1+data2+data3+data4+mrk)/5
        cur.execute("update marks set percentage={} where sadmission='{}'").format(per,SadmNo)
    elif n==3:
        mrk=float(input("Enter Students Phy mark"))
        query='''update marks set phy={} where sadmission_no='{}' '''.format(mrk,SadmNo)
        cur.execute(query)
        cur.execute("Select chem from marks where sadmission='{}'").format(SadmNo)
        data1=cur.fetchall()
        cur.execute("Select maths from marks where sadmission='{}'").format(SadmNo)
        data2=cur.fetchall()
        cur.execute("Select eng from marks where sadmission='{}'").format(SadmNo)
        data3=cur.fetchall()
        cur.execute("Select cs from marks where sadmission='{}'").format(SadmNo)
        data4=cur.fetchall()
        per=(data1+data2+data3+data4+mrk)/5
        cur.execute("update marks set percentage={} where sadmission='{}'").format(per,SadmNo)
    elif n==4:
        mrk=float(input("Enter Students Eng mark"))
        query='''update marks set eng={} where sadmission_no='{}' '''.format(mrk,SadmNo)
        cur.execute(query)
        cur.execute("Select chem from marks where sadmission='{}'").format(SadmNo)
        data1=cur.fetchall()
        cur.execute("Select phy from marks where sadmission='{}'").format(SadmNo)
        data2=cur.fetchall()
        cur.execute("Select maths from marks where sadmission='{}'").format(SadmNo)
        data3=cur.fetchall()
        cur.execute("Select cs from marks where sadmission='{}'").format(SadmNo)
        data4=cur.fetchall()
        per=(data1+data2+data3+data4+mrk)/5
        cur.execute("update marks set percentage={} where sadmission='{}'").format(per,SadmNo)
    else:                            
        mrk=float(input("Enter Students Cs mark"))
        query='''update marks set cs={} where sadmission_no='{}' '''.format(mrk,SadmNo)
        cur.execute(query)
        cur.execute("Select chem from marks where sadmission='{}'").format(SadmNo)
        data1=cur.fetchall()
        cur.execute("Select phy from marks where sadmission='{}'").format(SadmNo)
        data2=cur.fetchall()
        cur.execute("Select eng from marks where sadmission='{}'").format(SadmNo)
        data3=cur.fetchall()
        cur.execute("Select maths from marks where sadmission='{}'").format(SadmNo)
        data4=cur.fetchall()
        per=(data1+data2+data3+data4+mrk)/5
        cur.execute("update marks set percentage={} where sadmission='{}'").format(per,SadmNo)   
    cur.execute("Commit")
    cur.close()    
#To show report card all of students  
def reportcard():
    query="select * from marks"
    cur.execute(query)  
    data=cur.fetchall()
    n=len(data[0])
    for i in range (n):
        print("Name : ",data[i][1])
        print("Admission Number : ",data[i][0])
        print("Maths mark : ",data[i][2])
        print("Chem mark : ",data[i][3])
        print("Phy mark : ",data[i][4])
        print("Eng mark : ",data[i][5])
        print("Cs mark: ",data[i][6])
        print("Percentage : ",data[i][7])
        print()
        print("------------------------------")
        print()
    
        
    cur.close()
#To show report card of a student
def repcard():
    Sadmno=input("Enter student Admission number")
    query="select * from marks where sadmission_no ='{}'".format(Sadmno) 
    cur.execute(query)
    data=cur.fetchall()
    
    print("Name : ",data[0][1])
    print("Admission Number : ",data[0][0])
    print("Maths mark : ",data[0][2])
    print("Chem mark : ",data[0][3])
    print("Phy mark : ",data[0][4])
    print("Eng mark : ",data[0][5])
    print("Cs mark: ",data[0][6])
    print("Percentage : ",data[0][7])
    
    cur.close()
    
#LOGin and main body
passs=()
usern=()
print('''Press :
      1. To create account if don't have
      2. To log in''')

n=int(input())
if n == 1:
    print("Give Username")
    u=input()
    print("Give Password")
    p=input()
    y=list(passs)
    y.append(p)
    passs=tuple(y)
    x=list(usern)
    x.append(u)
    usern=tuple(x)
    print("Want to log in ?")
    a=input()
    if a=="yes":
        n=2
    
if n == 2:
    username = input('Enter your username: ')
    if username =="as":
        print("checking username")
        print("username is right")
        password = m.askpass(input('Enter your password: '))
        print()
        if password == "a":
            print("||ADMIN LOGIN SUCESSFULLY")
            print('''Enter 1 to Add Student's Information ''')
            print('''Enter 2 to Fetch all Details ''')
            print('''Enter 3 to Update Student's Information ''')
            print('''Enter 4 to Add Students's Marks ''')
            print("Enter 5 to Update Marks of students")
            print('''Enter 6 to Show report card of all students ''')
            print('''Enter 7 to Show report card of A Student ''')
            print('''Enter 8 to show information of a student''')
            n=int(input())
            if n==1:
                add()
            elif n==2:
                fetch_all()
            elif n==3:
                update()
            elif n==4:
                marks()
            elif n==5:
                updatemark() 
            elif n==6:
                reportcard()
            elif n==7:
              repcard()
            elif n==8:
                sinfo()   
            else:
                print("Give Valid Choice!!!")     
                                   
        else:
             print("Wrong Password")
             
    if username in usern:
        print("checking username.............")
        print("username is right.............") 
        password = m.advpass(input('Enter your password: ') )
        print()
        if password in passs:
            print("||STUDENT LOGIN SUCESSFULLLLY||")
            print("Press 1 To See Students information")
            print("Press 2 to See report card ")
            n=int(input())
            if n==1:
                sinfo()
            elif n==2:
                repcard()
            else:
                print("Give Valid Number!!")        
                
        else:
            print("Wrong password")             
else:
 exit()    
