'''QUICK TIME CASH PORTAL is a software which generate quick time cash to the
user in the situation of emergencies as wallet missing,short of cash etc'''

import pickle
import mysql.connector as ms
Qt_cust_ID=0
Qt_cust_Fname=" "
Qt_cust_Lname=" "
Qt_cust_FATname=" "
Qt_cust_MOTname=" "
Qt_cust_Age=0
Qt_cust_MobNo=" "
Qt_cust_Email=" "
Qt_cust_HouseNo=" "
Qt_cust_StreetNo=" "
Qt_cust_Area=" "
Qt_cust_City=" "
Qt_cust_State=" "
Qt_cust_Pin=0
Qt_cust_Nationality=" "
Qt_cust_IdProof=" "
Qt_cust_AadharNo=" "
Qt_cust_CompName=" "
Qt_cust_CompAddress=" "
Qt_cust_CompNo=" "
Qt_cust_CompCity=" "
Qt_cust_Desig=" "
Qt_cust_Salary=0.0
Qt_cust_Amt=0.0
Qt_val='i'

#function for user registration for quick time cash
def user_Input():
    Qt_cust_ID=int(input("Enter customer id"))
    Qt_cust_Fname=input("Enter your first name")
    Qt_cust_Lname=input("Enter your last name")
    Qt_cust_FATname=input("Enter your father's name")
    Qt_cust_MOTname=input("Enter your mother's name")
    Qt_cust_Age=int(input("Enter your age"))
    Qt_cust_MobNo=input("Enter your mobile no")
    Qt_cust_Email=input("Enter your email id")
    Qt_cust_HouseNo=input("Enter your house no")
    Qt_cust_StreetNo=input("Enter your street no")
    Qt_cust_Area=input("Enter your area")
    Qt_cust_City=input("Enter your city")
    Qt_cust_State=input("Enter your state")
    Qt_cust_Pin=int(input("Enter your pin code"))
    Qt_cust_Nationality=input("Enter your nationality")
    Qt_cust_IdProof=input("Enter your id proof")
    Qt_cust_AadharNo=input("Enter your aadhar no")
    Qt_cust_CompName=input("Enter your company name")
    Qt_cust_CompAddress=input("Enter your company address")
    Qt_cust_CompNo=input("Enter your company phone no")
    Qt_cust_CompCity=input("Enter the city in which your company is situated")
    print("Enter your designation category using the following criteria")
    print("Designation equivalent to Manager,Officer,CEO or Above Level: Please enter designation category A")
    print("Designation equivalent to Assistant Manager,Sub-Officer or any other category of same level: Please enter designation category B")
    print("Designation equivalent to Accountant,Clerk or any other category of same level: Please enter designation category C")
    print("Designation below these level: Please enter designation category D")
    Qt_cust_Desig=input("Enter your designation")
    Qt_cust_Salary=float(input("Enter yor salary"))

    l=[]
    fout=open("quicktime.dat","ab")
    l=[Qt_cust_ID,Qt_cust_Fname,Qt_cust_Lname,Qt_cust_FATname,Qt_cust_MOTname,Qt_cust_Age,Qt_cust_MobNo,Qt_cust_Email,
       Qt_cust_HouseNo,Qt_cust_StreetNo,Qt_cust_Area,Qt_cust_City,Qt_cust_State,Qt_cust_Pin,Qt_cust_Nationality,Qt_cust_IdProof,
       Qt_cust_AadharNo,Qt_cust_CompName,Qt_cust_CompAddress,Qt_cust_CompNo,Qt_cust_CompCity,Qt_cust_Desig,Qt_cust_Salary,Qt_val]
    pickle.dump(l,fout)
    fout.close()

#function for admin to check permissions given to all users     
def admin_view_permission():
    fin=open("quicktimepermission.dat","rb")
    try:
        while True:
            l=pickle.load(fin)
            print(l)
    except EOFError:
        pass
    fin.close()

#function for admin to give authorisation to avail quick time cash                
def admin_validate():
    fin=open("quicktime.dat","rb")
    try:
        while True:
            l=pickle.load(fin)
            if l[23]=="i":
                print("Customer Id",l[0])
                print("Customer first name",l[1])
                print("Customer last name",l[2])
                print("Customer father name",l[3])
                print("Customer mother name",l[4])
                print("Customer age",l[5])
                print("Customer mobile number",l[6])
                print("Customer email",l[7])
                print("Customer house no",l[8])
                print("Customer street no",l[9])
                print("Customer area",l[10])
                print("Customer city",l[11])
                print("Customer state",l[12])
                print("Customer pin code",l[13])
                print("Customer nationality",l[14])
                print("Customer id proof",l[15])
                print("Customer aadhar no",l[16])
                print("Customer company name",l[17])
                print("Customer company address",l[18])
                print("Customer company number",l[19])
                print("Customer company city",l[20])
                print("Customer designation",l[21])
                print("Customer salary",l[22])
                print("Customer validation",l[23])
                vl=input("Do you want to validate this customer for quick time cash approval (y/n)")
                if vl=="y":
                    designation=l[21]
                    salary=l[22]
                    cust_Amt=0
                    cust_cat=""
                    if salary>50000 and (designation=="A" or designation=="B"):
                        cust_cat="A"
                    elif salary>35000 and (designation=="A" or designation=="B" or designation=="C"):
                        cust_cat="B"
                    elif salary>20000 and (designation=="B" or designation=="C"):
                        cust_cat="C"
                    elif salary>10000 and (designation=="C" or designation=="D"):
                        cust_cat="D"
                    mycon=ms.connect(host="localhost",user="root",passwd="jamster##@",database="quick_time")
                    cursor=mycon.cursor()
                    cursor.execute("SELECT * FROM Admin_setamt WHERE cust_cat='{}'".format(cust_cat))
                    data=cursor.fetchone()
                    cust_Amt=data[1]
                    mycon.close()
                    mycon=ms.connect(host="localhost",user="root",passwd="jamster##@",database="quick_time")
                    cursor=mycon.cursor()
                    cursor.execute("INSERT INTO cust(cust_ID,cust_Fname,cust_Lname,cust_FATname,cust_MOTname,cust_Age,cust_MobNo,cust_Email,cust_HouseNo,cust_StreetNo,cust_Area,cust_City,cust_State,cust_Pin,cust_Nationality,cust_IdProof,cust_AadharNo,cust_CompName,cust_CompAddress,cust_CompNo,cust_CompCity,cust_Desig,cust_Salary,cust_Amt) VALUES({},'{}','{}','{}','{}',{},'{}','{}','{}','{}','{}','{}','{}',{},'{}','{}','{}','{}','{}','{}','{}','{}',{},{})".format(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8],l[9],l[10],l[11],l[12],l[13],l[14],l[15],l[16],l[17],l[18],l[19],l[20],l[21],l[22],cust_Amt))
                    mycon.commit()
                    mycon.close()
                    mycon=ms.connect(host="localhost",user="root",passwd="jamster##@",database="quick_time")
                    cursor=mycon.cursor()
                    cursor.execute("INSERT INTO cus_trans(cust_ID,total_Amt,available_Amt,use_Amt,deposited_Amt,trans_date) VALUES({},{},{},{},{},'{}')".format(l[0],cust_Amt,cust_Amt,0,0,"today"))
                    mycon.commit()
                    mycon.close()
                    Qval="y"
                else:
                    Qval="n"
                fout=open("quicktimepermission.dat","ab")
                l1=[]
                Qt_cust_ID=l[0]
                Qt_val=Qval
                l1=[Qt_cust_ID,Qt_val]
                pickle.dump(l1,fout)
                fout.close() 
    except EOFError:
        pass
    fin.close()

#Function for user to login into quick time cash portal
def user_login():
    global ucid
    cid=int(input("Enter your ID to login"))
    uid=input("Enter your email id")
    pwd=input("Enter your Aadhar No as password")
    mycon=ms.connect(host="localhost",user="root",passwd="jamster##@",database="quick_time")
    cursor=mycon.cursor()
    cursor.execute("SELECT cust_Email,cust_AadharNo FROM cust WHERE cust_ID={}".format(cid))
    data=cursor.fetchone()
    count=cursor.rowcount
    if count>0:
        if uid==data[0] and pwd==data[1]:
            ucid=cid
            while True:
                print("Login Succesfull,Select an option to continue")
                print("1.User Checkstatus")
                print("2.User View")
                print("3.User Update")
                print("4.User ViewTransactamt")
                print("5.User Transactionamt")
                print("6.Exit")
                ch_user=int(input("Enter your choice"))
                if ch_user==1:
                    user_checkstatus()
                elif ch_user==2:
                    user_view()
                elif ch_user==3:
                    user_update()
                elif ch_user==4:
                    user_viewtransamt()
                elif ch_user==5:
                    user_transactionamt()
                elif ch_user==6:
                    break
        else:
            print("Login id or password is incorrect")
            user_login()
    else:
        print("Login id or password is incorrect")
        user_login()

#Function for user to check whether he is eligible to get quick time cash or not    
def user_checkstatus():
    fin=open("quicktimepermission.dat","rb")
    cid=int(input("Enter your customer id"))
    try:
        while True:
            l1=pickle.load(fin)
            if l1[0]==cid:
                if l1[1]=="y":
                    print("You are permitted to get quick time cash")
                else:
                    print("You are not permitted to get quick time cash")
        else:
            print("You are in waiting list to validate the documents")
    except EOFError:
        pass
    fin.close()

#Function for admin to check available amount limit for a particular category of user
def admin_viewuseramt():
    mycon=ms.connect(host="localhost",user="root",passwd="jamster##@",database="quick_time")
    cursor=mycon.cursor()
    cursor.execute("SELECT * FROM Admin_setamt")
    data=cursor.fetchall()
    print("The upper limit to assign amount for each category")
    print(data)
    mycon.close()

#Function for user to view all his personal details    
def user_view():
    global ucid
    cid=ucid
    mycon=ms.connect(host="localhost",user="root",passwd="jamster##@",database="quick_time")
    cursor=mycon.cursor()
    cursor.execute("SELECT * FROM cust WHERE cust_ID={}".format(cid))
    data=cursor.fetchone()
    count=cursor.rowcount
    if count>0:
        print("Your ID",data[0])
        print("Your First Name",data[1])
        print("Your Last Name",data[2])
        print("Your Father Name",data[3])
        print("Your Mother Name",data[4])
        print("Your Age",data[5])
        print("Your mobile number",data[6])
        print("Your Email",data[7])
        print("Your House No",data[8])
        print("Your Street No",data[9])
        print("Your Area",data[10])
        print("Your City",data[11])
        print("Your State",data[12])
        print("Your Pin Code",data[13])
        print("Your Nationality",data[14])
        print("Your Id Proof",data[15])
        print("Your Aadhar No",data[16])
        print("Your Company Name",data[17])
        print("Your Company Address",data[18])
        print("Your Company Number",data[19])
        print("Your Company City",data[20])
        print("Your Designation",data[21])
        print("Your Salary",data[22])
    else:
        print("You are not validated yet")

#Function for user to update his details
def user_update():
    global ucid
    cid=ucid
    mycon=ms.connect(host="localhost",user="root",passwd="jamster##@",database="quick_time")
    cursor=mycon.cursor()
    cursor.execute("SELECT * FROM cust WHERE cust_ID={}".format(cid))
    data=cursor.fetchone()
    first_name=data[1]
    last_name=data[2]
    father_name=data[3]
    mother_name=data[4]
    age=data[5]
    mobile_number=data[6]
    email=data[7]
    house_no=data[8]
    street_no=data[9]
    area=data[10]
    city=data[11]
    state=data[12]
    pin_code=data[13]
    nationality=data[14]
    id_proof=data[15]
    aadhar_no=data[16]
    company_name=data[17]
    company_address=data[18]
    company_number=data[19]
    company_city=data[20]
    designation=data[21]
    salary=data[22]
    count=cursor.rowcount
    if count==0:
        print("You are not validated yet")
    else:
        print("Update menu")
        print("1.Your First Name")
        print("2.Your Last Name")
        print("3.Your Father Name")
        print("4.Your Mother Name")
        print("5.Your Age")
        print("6.Your Mobile Number")
        print("7.Your Email")
        print("8.Your House No")
        print("9.Your Street No")
        print("10.Your Area")
        print("11.Your City")
        print("12.Your State")
        print("13.Your Pin Code")
        print("14.Your Nationality")
        print("15.Your Id Proof")
        print("16.Your Aadhar No")
        print("17.Your Company Name")
        print("18.Your Company Address")
        print("19.Your Company Number")
        print("20.Your Company City")
        print("21.Your Designation")
        print("22.Your Salary")
        ch=int(input("Enter your choice to update your record"))
        if ch==1:
            print("Your First Name is",first_name)
            first_name=input("Enter your updated first name")
        elif ch==2:
            print("Your Last Name is",last_name)
            last_name=input("Enter your updated last name")
        elif ch==3:
            print("Your Father Name is",father_name)
            father_name=input("Enter your updated father name")
        elif ch==4:
            print("Your Mother Name is",mother_name)
            mother_name=input("Enter your updated mother name")
        elif ch==5:
            print("Your Age is",age)
            age=int(input("Enter your updated age"))
        elif ch==6:
            print("Your Mobile Number is",mobile_number)
            mobile_number=input("Enter your updated mobile number")
        elif ch==7:
            print("Your Email is",email)
            email=input("Enter your updated email")
        elif ch==8:
            print("Your House No is",house_no)
            house_no=input("Enter your updated house no")
        elif ch==9:
            print("Your Street No is",street_no)
            street_no=input("Enter your updated street no")
        elif ch==10:
            print("Your Area is",area)
            area=input("Enter your updated area")
        elif ch==11:
            print("Your City is",city)
            city=input("Enter your updated city")
        elif ch==12:
            print("Your State is",state)
            state=input("Enter your updated state")
        elif ch==13:
            print("Your Pin code is",pin_code)
            pin_code=int(input("Enter your updated pin code"))
        elif ch==14:
            print("Your Nationality is",nationality)
            nationality=input("Enter your updated nationality")
        elif ch==15:
            print("Your id proof is",id_proof)
            id_proof=input("Enter your updated id proof")
        elif ch==16:
            print("Your aadhar np is",aadhar_no)
            aadhar_no=input("Enter your updated aadhar no")
        elif ch==17:
            print("Your Company Name is",company_name)
            company_name=input("Enter your updated company name")
        elif ch==18:
            print("Your Company Address is",company_address)
            company_address=input("Enter your updated company address")
        elif ch==19:
            print("Your Company Number is",comapany_number)
            company_number=input("Enter your updated company number")
        elif ch==20:
            print("Your Company City is",company_city)
            company_city=input("Enter your updated company city")
        elif ch==21:
            print("Your Designation is",designation)
            designation=input("Enter your updated designation")
        elif ch==22:
            print("Your Salary is",salary)
            salary=float(input("Enter your updated salary"))
        mycon=ms.connect(host="localhost",user="root",passwd="jamster##@",database="quick_time")
        cursor=mycon.cursor()
        cursor.execute("UPDATE cust SET cust_Fname='{}',cust_Lname='{}',cust_FATname='{}',cust_MOTname='{}',cust_Age={},cust_MobNo='{}',cust_Email='{}',cust_HouseNo='{}',cust_StreetNo='{}',cust_Area='{}',cust_City='{}',cust_State='{}',cust_Pin={},cust_Nationality='{}',cust_IdProof='{}',cust_AadharNo='{}',cust_CompName='{}',cust_CompAddress='{}',cust_CompNo='{}',cust_CompCity='{}',cust_Desig='{}',cust_Salary={} WHERE cust_ID={}".format(first_name,last_name,father_name,mother_name,age,mobile_number,email,house_no,street_no,area,city,state,pin_code,nationality,id_proof,aadhar_no,company_name,company_address,company_number,company_city,designation,salary,cid))
        mycon.commit()
        mycon.close()
        print("Record Updated Successfully")

#Function for admin to delete the user account            
def admin_delete():
    cid=int(input("Enter customer id which you want to delete"))
    mycon=ms.connect(host="localhost",user="root",passwd="jamster##@",database="quick_time")
    cursor=mycon.cursor()
    cursor.execute("DELETE FROM cust WHERE cust_ID={}".format(cid))
    mycon.commit()
    mycon.close()
    print("Record Deleted Successfully")

#Function for user to check transaction amount
def user_viewtransamt():
    global ucid
    cid=ucid
    mycon=ms.connect(host="localhost",user="root",passwd="jamster##@",database="quick_time")
    cursor=mycon.cursor()
    cursor.execute("SELECT available_Amt FROM cus_trans WHERE cust_ID={}".format(cid))
    data=cursor.fetchone()
    count=cursor.rowcount
    if count>0:
        Qt_cust_Amt=data[0]
        print("You have been assigned a total quick time cash amount:",Qt_cust_Amt)
    else:
        print("You are not validated yet")

#Function for admin to change amount limit for a particular category of customers
def admin_updateuseramt():
    cust_cat=input("Enter category name for which you want to set upper limit")
    cust_Amt=int(input("Enter the upper limit amount for category"))
    mycon=ms.connect(host="localhost",user="root",passwd="jamster##@",database="quick_time")
    cursor=mycon.cursor()
    cursor.execute("UPDATE Admin_setamt SET cust_Amt={} WHERE cust_cat='{}'".format(cust_Amt,cust_cat))
    mycon.commit()
    mycon.close()
    print("Record updated successfully")

#Function for user to perform transaction
def user_transactionamt():
    global ucid
    cid=ucid
    mycon=ms.connect(host="localhost",user="root",passwd="jamster##@",database="quick_time")
    cursor=mycon.cursor()
    cursor.execute("SELECT available_Amt FROM cus_trans WHERE cust_ID={}".format(cid))
    data=cursor.fetchone()
    count=cursor.rowcount
    if count>0:
        Qt_cust_Amt=data[0]
        print("You have been assigned a total quick time cash amount:",Qt_cust_Amt)
        print("Transaction menu")
        print("1.withdraw")
        print("2.deposit")
        print("3.your transaction summary")
        choice=int(input("Enter your choice"))
        if choice==1:
            cid=ucid
            mycon=ms.connect(host="localhost",user="root",passwd="jamster##@",database="quick_time")
            cursor=mycon.cursor()
            cursor.execute("SELECT * FROM cus_trans WHERE cust_ID={}".format(cid))
            data=cursor.fetchone()
            count=cursor.rowcount
            if count==0:
                print("You are not validated yet")
            else:
                available_Amt=data[2]
                use_Amt=data[3]
                dep_Amt=data[4]
            print("Now you have available amount for quick time cash",available_Amt)
            reqd_Amt=int(input("Enter the amount required for quick time cash"))
            if reqd_Amt<=available_Amt:
                print("You are assigned an amount of:",reqd_Amt)
                trans_ID=int(input("Enter your transaction ID"))
                nav_Amt=available_Amt-reqd_Amt
                nused_Amt=use_Amt+reqd_Amt
                ndep_Amt=dep_Amt+0
                t_date=input("Enter today's date")
                mycon=ms.connect(host="localhost",user="root",passwd="jamster##@",database="quick_time")
                cursor=mycon.cursor()
                cursor.execute("UPDATE cus_trans SET total_Amt={},available_Amt={},use_Amt={},deposited_Amt={},trans_date='{}' WHERE cust_ID={}".format(Qt_cust_Amt,nav_Amt,nused_Amt,ndep_Amt,t_date,cid))
                mycon.commit()
                mycon.close()
                mycon=ms.connect(host="localhost",user="root",passwd="jamster##@",database="quick_time")
                cursor=mycon.cursor()
                cursor.execute("INSERT INTO cust_trans(trans_ID,cust_ID,total_Amt,available_Amt,use_Amt,deposited_Amt,trans_date) VALUES({},{},{},{},{},{},'{}')".format(trans_ID,cid,Qt_cust_Amt,nav_Amt,nused_Amt,ndep_Amt,t_date))
                mycon.commit()
                mycon.close()
            else:
                print("The required amount is more than your available amount,please fill the amount under your limit",available_Amt)
        elif choice==2:
            cid=ucid
            mycon=ms.connect(host="localhost",user="root",passwd="jamster##@",database="quick_time")
            cursor=mycon.cursor()
            cursor.execute("SELECT * FROM cus_trans WHERE cust_ID={}".format(cid))
            data=cursor.fetchone()
            count=cursor.rowcount
            if count==0:
                print("You are not validated yet")
            else:
                available_Amt=data[2]
                use_Amt=data[3]
                dep_Amt=data[4]
                tobep_Amt=use_Amt
                print("Now you have to pay amount for quick time cash:",tobep_Amt)
                dp_Amt=int(input("Enter the amount you want to deposit in your quick time cash account"))
                nused_Amt=tobep_Amt-dp_Amt
                nav_Amt=available_Amt+dp_Amt
                ndep_Amt=dep_Amt+dp_Amt
                trans_ID=int(input("Enter your transaction id"))
                t_date=input("Enter today's date")
                mycon=ms.connect(host="localhost",user="root",passwd="jamster##@",database="quick_time")
                cursor=mycon.cursor()
                cursor.execute("UPDATE cus_trans SET total_Amt={},available_Amt={},use_Amt={},deposited_Amt={},trans_date='{}' WHERE cust_ID={}".format(Qt_cust_Amt,nav_Amt,nused_Amt,ndep_Amt,t_date,cid))
                mycon.commit()
                mycon.close()
                mycon=ms.connect(host="localhost",user="root",passwd="jamster##@",database="quick_time")
                cursor=mycon.cursor()
                cursor.execute("INSERT INTO cust_trans(trans_ID,cust_ID,total_Amt,available_Amt,use_Amt,deposited_Amt,trans_date) VALUES({},{},{},{},{},{},'{}')".format(trans_ID,cid,Qt_cust_Amt,nav_Amt,nused_Amt,ndep_Amt,t_date))
                mycon.commit()
                mycon.close()
        elif choice==3:
            cid=ucid
            mycon=ms.connect(host="localhost",user="root",passwd="jamster##@",database="quick_time")
            cursor=mycon.cursor()
            cursor.execute("SELECT * FROM cust_trans WHERE cust_ID={}".format(cid))
            data=cursor.fetchall()
            count=cursor.rowcount
            if count==0:
                print("No transaction found")
            else:
                print("Transaction summary")
                for i in data:
                    print(i)
    else:
        print("You are not validated yet")

#main function

ucid=0    
while True:
    print("**-------Welcome to QUICK TIME CASH PORTAL-------**")
    print()
    print("Select an option for quick time cash")
    print("1.For quick time cash register yourself")
    print("2.Existing user")
    print("3.admin")
    print("4.Exit")
    ch=int(input("Enter your choice"))
    if ch==1:
        user_Input()
        print("You have registered successfully, now wait for your information validation")
    elif ch==2:
        print("Press 1 for User Login")
        print("Press 2 for Exit")
        ch_user=int(input("Enter your choice"))
        if ch_user==1:
            user_login()
        elif ch_user==2:
            break
        
    elif ch==3:
        aid=input("Enter your admin id")
        apwd=input("Enter your password")
        if aid=="admin" and apwd=="admin":
            print("Welcome admin please choose an option")
            print("1.Admin Validate")
            print("2.Admin View Permission")
            print("3.Admin Delete")
            print("4.Admin view loan amount upper limit")
            print("5.Admin modify loan amount upper limit")
            print("6.Exit")
            ch_admin=int(input("Enter your choice"))
            if ch_admin==1:
                admin_validate()
            elif ch_admin==2:
                admin_view_permission()
            elif ch_admin==3:
                admin_delete()
            elif ch_admin==4:
                admin_viewuseramt()
            elif ch_admin==5:
                admin_updateuseramt()
            elif ch_admin==6:
                break
    elif ch==4:
        break
        
            

            

            
