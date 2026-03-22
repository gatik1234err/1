import random
from tabulate import tabulate
import mysql.connector as con

dbo = con.connect(host="localhost", user="root", password="admin", database="train_reservation")
co = dbo.cursor()

# NEW USER REGISTRATION SECTION
def new_user():
    dbo = con.connect(host="localhost", user="root", password="admin", database="train_reservation")
    co = dbo.cursor()
    import random
    pid = random.randint(0, 1000) * 10
    print("----------------------------------------------------------------------")
    print(" \n Welcome to our reservation system \n Register Yourself here to use our system")
    uid = input("Enter your user id: ")
    name = input("Enter your name: ")
    pno = input("Enter your phone no: ")
    eid = input("Enter your email_id: ")
    pwd = input("Enter your password: ")
    co.execute("insert into user values ('{}',{},'{}',{},'{}','{}')".format(uid, pid, name, pno, eid, pwd))
    print("************* Congratulations!!! Your id is successfully created **************")
    print("----------------------------------------------------------------------")
    
    dbo.commit()

# FORGET USER ID
def forgot_user_id():
    dbo = con.connect(host="localhost", user="root", password="admin", database="train_reservation")
    co = dbo.cursor()
    email = input("Enter your registered email: ")
    co.execute("select user_id from user where email_id like '{}'".format(email))
    emel = co.fetchall()
    for i in emel:
        print("Your user_id is: ", (i[0]))

# OLD USER ID
def old_user():
    dbo = con.connect(host="localhost", user="root", password="admin", database="train_reservation")
    co = dbo.cursor()
    print("\n---------------------------------------------------------------\n")
    uid = input("Enter your user id: ")
    co.execute("select user_id from user where user_id like '{}'".format(uid))
    b = co.fetchall()
    c = len(b)
    if c == 0:
        print("---------------- Your given id is not registered -----------------")
        print("\n------------------------------------------------------------------\n")
        print("1. Try again")
        print("2. Forgot user id")
        print("3. Register as a new user")
        choose = int(input("Choose an option from above: "))
        if choose == 1:
            old_user()
        elif choose == 2:
            forgot_user_id()
        elif choose == 3:
            new_user()
    else:
        pas = input("Enter your password: ")
        co.execute("select password from user where password like '{}'".format(pas))
        n = co.fetchall()
        for i in n:
            if pas == (i[0]):
                print("\n---------------------------------------------------------------\n")
                print("-----------Welcome back sir/ma'am what's your plan Today??---------\n")
                passenger_panel(uid)

def user_panel():
    print(" 1. Register")
    print(" 2. Login")
    print(" 3. Back")
    out = int(input("Enter your choice: "))
    if out == 1:
        new_user()
    elif out == 2:
        old_user()
    elif out == 3:
        main_menu()

# PASSWORD FUNCTION FOR ACCESS TO ADMIN FUNCTION
def adminpassword():
    password = (input("Enter your password: "))
    if password == "CLASS12CS":
        print("******************Access Granted********************")
        print("---------------------------------------------------------------------")
        admin_panel()
    else:
        print("***************ACCESS NOT GRANTED ENTER CORRECT PASSWORD************")
        print("---------------------------------------------------------------------")
        adminpassword()

# ADD TRAIN
def add_train():
    dbo = con.connect(host="localhost", user="root", password="admin", database="train_reservation")
    co = dbo.cursor()
    print("---------------------------------------------------------------------")
    a = int(input("Enter train no: "))
    b = input("Enter train name: ")
    c = input("Enter train origin: ")
    d = input("Enter train destination: ")
    e = int(input("Enter train journey distance: "))
    g = input("Enter train journey time: ")
    h = int(input("Enter no of seats in AC: "))
    i = int(input("Enter no of seats in SL: "))
    j = int(input("Enter no of seats in GEN: "))
    k = int(input("Enter price of AC: "))
    l = int(input("Enter price of SL: "))
    m = int(input("Enter price of GEN: "))
    n = input("Enter days available: ")
    print("---------------------------------------------------------------------")
    co.execute("insert into train_schedule values ({},'{}','{}','{}',{},'{}',{},{},{},{},{},{},'{}')".format(a, b, c, d, e, g, h, i, j, k, l, m, n))
    print("*********You have added a new train details successfully************")
    dbo.commit()

# UPDATE TRAIN TABLE
def update_details():
    dbo = con.connect(host="localhost", user="root", password="admin", database="train_reservation")
    co = dbo.cursor()
    print("---------------------------------------------------------------------")
    print("******Welcome to update train system******")
    print("1. Update train no")
    print("2. Update train name")
    print("3. Update train origin")
    print("4. Update train destination")
    print("5. Update journey dist")
    print("6. Update available days")
    print("7. Update journey time")
    print("8. Update no of seats in AC")
    print("9. Update no of seats in SL")
    print("10. Update no of seats in GEN")
    print("11. Update price of AC")
    print("12. Update price of SL")
    print("13. Update price of GEN")
    print("14. Exit")
    x = int(input("Enter your choice to use: "))
    while True:
        # To Update train no
        if x == 1:
            print("---------------------------------------------------------------------")
            print("**********YOU ARE GOING TO UPDATE TRAIN NO***********")
            tname = input("Enter train name whose no you want to update: ")
            tno = int(input("Enter updated train no: "))
            co.execute("update train_schedule set train_no={} where train_name='{}'".format(tno, tname))
            print("*******UPDATED SUCCESSFULLY********")
            print("---------------------------------------------------------------------")
            dbo.commit()
            return
        # To Update train name
        elif x == 2:
            print("---------------------------------------------------------------------")
            print("**********YOU ARE GOING TO UPDATE TRAIN NAME***********")
            tno = int(input("Enter train no whose name you want to update: "))
            tname = input("Enter updated train name: ")
            co.execute("update train_schedule set train_name='{}' where train_no={}".format(tname, tno))
            print("*******UPDATED SUCCESSFULLY********")
            print("---------------------------------------------------------------------")
            dbo.commit()
            return
        # To Update train origin
        elif x == 3:
            print("---------------------------------------------------------------------")
            print("**********YOU ARE GOING TO UPDATE TRAIN ORIGIN***********")
            tno = int(input("Enter train no whose origin you want to update: "))
            orgn = input("Enter updated train origin: ")
            co.execute("update train_schedule set origin='{}' where train_no={}".format(orgn, tno))
            print("*******UPDATED SUCCESSFULLY********")
            print("---------------------------------------------------------------------")
            dbo.commit()
            return
        # To Update train destination
        elif x == 4:
            print("---------------------------------------------------------------------")
            print("**********YOU ARE GOING TO UPDATE TRAIN DESTINATION***********")
            tno = int(input("Enter train no whose destination you want to update: "))
            td = input("Enter updated train destination: ")
            co.execute("update train_schedule set destination='{}' where train_no={}".format(td, tno))
            print("*******UPDATED SUCCESSFULLY********")
            print("---------------------------------------------------------------------")
            dbo.commit()
            return
        # To Update journey distance
        elif x == 5:
            print("---------------------------------------------------------------------")
            print("**********YOU ARE GOING TO UPDATE JOURNEY DISTANCE ***********")
            tno = int(input("Enter train no whose journey dist you want to update: "))
            tjd = input("Enter updated journey dist: ")
            co.execute("update train_schedule set journey_distance='{}' where train_no={}".format(tjd, tno))
            print("*******UPDATED SUCCESSFULLY********")
            print("---------------------------------------------------------------------")
            dbo.commit()
            return
        # To Update the days train is available
        elif x == 6:
            print("---------------------------------------------------------------------")
            print("**********YOU ARE GOING TO UPDATE AVAILABLE DAYS***********")
            tno = int(input("Enter train no whose avl_days you want to update: "))
            tad = input("Enter updated available days: ")
            co.execute("update train_schedule set avl_days ='{}' where train_no={}".format(tad, tno))
            print("*******UPDATED SUCCESSFULLY********")
            print("-----------------------------------------------------------------------")
            dbo.commit()
            return
        # To Update journey time
        elif x == 7:
            print("---------------------------------------------------------------------")
            print("**********YOU ARE GOING TO UPDATE JOURNEY TIME***********")
            tno = int(input("Enter train no whose journey_time you want to update: "))
            tj = input("Enter updated journey time: ")
            co.execute("update train_schedule set total_time='{}' where train_no={}".format(tj, tno))
            print("*******UPDATED SUCCESSFULLY********")
            print("---------------------------------------------------------------------")
            dbo.commit()
            return
        # To Update no of seats in ac coach of that train
        elif x == 8:
            print("---------------------------------------------------------------------")
            print("**********YOU ARE GOING TO UPDATE SEATS IN AC***********")
            tno = int(input("Enter train no whose no of seats in AC you want to update: "))
            tsa = input("Enter updated no of seats in AC: ")
            co.execute("update train_schedule set ac1='{}' where train_no={}".format(tsa, tno))
            print("*******UPDATED SUCCESSFULLY********")
            print("---------------------------------------------------------------------")
            dbo.commit()
            return
        # To Update no of seats in SL coach of that train
        elif x == 9:
            print("---------------------------------------------------------------------")
            print("**********YOU ARE GOING TO UPDATE SEATS IN SL***********")
            tno = int(input("Enter train no whose no of seats in Sl you want to update: "))
            tss = input("Enter updated no of seats in Sl: ")
            co.execute("update train_schedule set sl='{}' where train_no={}".format(tss, tno))
            print("*******UPDATED SUCCESSFULLY********")
            print("---------------------------------------------------------------------")
            dbo.commit()
            return
        # To Update no of seats in GEN coach of that train
        elif x == 10:
            print("---------------------------------------------------------------------")
            print("**********YOU ARE GOING TO UPDATE SEATS IN GEN***********")
            tno = int(input("Enter train no whose no of seats in GEN you want to update: "))
            tsg = input("Enter updated no of seats in GEN: ")
            co.execute("update train_schedule set gen='{}' where train_no={}".format(tsg, tno))
            print("*******UPDATED SUCCESSFULLY********")
            print("---------------------------------------------------------------------")
            dbo.commit()
            return
        # To Update fare price of AC of that train
        elif x == 11:
            print("---------------------------------------------------------------------")
            print("**********YOU ARE GOING TO UPDATE FARE PRICE OF AC***********")
            tno = int(input("Enter train no whose fare price of ac you want to update: "))
            tfa = input("Enter updated fare price of ac: ")
            co.execute("update train_schedule set ac_fare={} where train_no={}".format(tfa, tno))
            print("*******UPDATED SUCCESSFULLY********")
            print("---------------------------------------------------------------------")
            dbo.commit()
            return
        # To Update fare price of SL of that train
        elif x == 12:
            print("---------------------------------------------------------------------")
            print("**********YOU ARE GOING TO UPDATE FARE PRICE OF SL***********")
            tno = int(input("Enter train no whose fare price of SL you want to update: "))
            tfs = input("Enter updated fare price of SL: ")
            co.execute("update train_schedule set sl_fare={} where train_no={}".format(tfs, tno))
            print("*******UPDATED SUCCESSFULLY********")
            print("---------------------------------------------------------------------")
            dbo.commit()
            return
        # To Update fare price of GEN of that train
        elif x == 13:
            print("---------------------------------------------------------------------")
            print("**********YOU ARE GOING TO UPDATE FARE PRICE OF GEN***********")
            tno = int(input("Enter train no whose fare price of GEN you want to update: "))
            tfg = input("Enter updated fare price of GEN: ")
            co.execute("update train_schedule set gen_fare={} where train_no={}".format(tfg, tno))
            print("*******UPDATED SUCCESSFULLY********")
            print("---------------------------------------------------------------------")
            dbo.commit()
            return
        elif x == 14:
            print("**********YOU ARE NOW OUT OF UPDATE DETAILS SECTION***********")
            break
            return

# CANCEL TRAIN
def cancel_train():
    dbo = con.connect(host="localhost", user="root", password="admin", database="train_reservation")
    co = dbo.cursor()
    ct = int(input("enter train no which you want to cancel: "))
    co.execute("delete from train_schedule where train_no={}".format(ct))
    dbo.commit()
    print("*********** Train cancelled Successfully ****************")

# ADMIN PANEL OPTIONS
def admin_panel():
    while True:
        try:
            print("---------------------------------------------------------------------")
            print("******Welcome to admin panel******")
            print("1. Add train")
            print("2. Update details")
            print("3. Cancel Train")
            print("4. Log out")
            opt = int(input("Choose your option: "))
            if opt == 1:
                add_train()
            elif opt == 2:
                update_details()
            elif opt == 3:
                cancel_train()
            elif opt == 4:
                print("**********You are out of admin panel***********")
                print("---------------------------------------------------------------------")
                main_menu()
        except InvalidOptionError as e:
            print(f"Error: {e}")
        except:
            print("**********Choose a correct option***********")
            print("---------------------------------------------------------------------")

# PASSENGER PANEL FUNCTIONALITIES
def Train_Search():
    dbo = con.connect(host="localhost", user="root", password="admin", database="train_reservation")
    co = dbo.cursor()
    o = input("Enter your origin: ")
    d = input("Enter your destination: ")
    co.execute("select * from train_schedule where origin like '%{}%' and destination like '%{}%'".format(o, d))
    a = co.fetchall()
    for i in a:
        print("Train no.: ", a[0][0])
        print("Train name: ", a[0][1])
        print("Origin: ", a[0][2])
        print("Destination: ", a[0][3])
        print("Journey distance: ", a[0][4])
        print("Available days: ", a[0][12])
        print("total time: ", a[0][5])
        print("Seats in ac1: ", a[0][6])
        print("Seats in sl: ", a[0][7])
        print("Seats in GEN: ", a[0][8])
        print("Fare of ac1: ", a[0][9])
        print("Fare of sl: ", a[0][10])
        print("Fare of gen: ", a[0][11])
    dbo.commit()

# BOOK TICKETS
def Book_Ticket(uid):
    dbo = con.connect(host="localhost", user="root", password="admin", database="train_reservation")
    co = dbo.cursor()
    print("THIS IS OUR ALL TRAINS AVAILABLE \n -------------------------------------------------------")
    op = "select train_no,train_name,origin,destination from train_schedule"
    co.execute(op)
    r = co.fetchall()
    columns = [i[0] for i in co.description]
    print(tabulate(r, headers=columns, tablefmt="fancy_grid"))
    print("---------------------------------------------------------------------\n\n")
    trainno = int(input("Enter your Train no: "))
    tcktno = int(input("Enter no of seats you want to book: "))
    print("1. AC TICKET")
    print("2. SL TICKET")
    print("3. GEN TICKET")
    typ = int(input("Enter your choice of class: "))
    if typ == 1:
        a = co.execute("select ac1_fare from train_schedule where train_no={}".format(trainno))
        b = co.fetchall()
        print(b[0][0])
    elif typ == 2:
        a = co.execute("select sl_fare from train_schedule where train_no={}".format(trainno))
        b = co.fetchall()
        print(b[0][0])
    elif typ == 3:
        a = co.execute("select gen_fare from train_schedule where train_no={}".format(trainno))
        b = co.fetchall()
        print(b[0][0])
    for i in range(tcktno):
        cus1 = input("Enter customer name: ")
        age = int(input("Enter your age: "))
        print("--------------- For gender M=Male, F=Female, O=Other ------------------")
        gender = input("Enter your gender: ")
        j = random.randint(100000, 999999)
        print("Your PNR no is: ", j)
        cnf = "Confirmed"
        p = b[0][0]
        co.execute("insert into booked_tickets values ('{}',{},{},'{}',{},'{}',{},'{}')".format(uid, j, trainno, cus1, age, gender, p, cnf))
        p = b[0][0]
        amt = tcktno * p
        print("Your total ticket price is: ", amt)
    dbo.commit()

def Cancel_Ticket():
    dbo = con.connect(host="localhost", user="root", password="admin", database="train_reservation")
    co = dbo.cursor()
    pnr = int(input("enter pnr no. you want to cancel: "))
    co.execute("delete from booked_tickets where pnr_no={}".format(pnr))
    dbo.commit()
    print("*********** Your ticket cancelled Successfully ****************")

# PASSENGER PANEL
def passenger_panel(uid):
    dbo = con.connect(host="localhost", user="root", password="admin", database="train_reservation")
    co = dbo.cursor()
    while True:
        print("---------------------------------------------------------------------")
        print("******Welcome to passenger panel******")
        print("1. Train Search")
        print("2. Book Ticket")
        print("3. Cancel Ticket")
        print("4. Log out")
        choic = int(input("Enter your choice to use: "))
        if choic == 1:
            Train_Search()
        elif choic == 2:
            Book_Ticket(uid)
        elif choic == 3:
            Cancel_Ticket()
        elif choic == 4:
            main_menu()
        print("*****You are successfully logged out of Passenger panel*****")
        print("---------------------------------------------------------------------")

# MAIN MENU
def main_menu():
    print("-----------------------------------------------------")
    print("********WELCOME TO TRAIN RESERVATION SYSTEM********")
    print("1. Admin panel")
    print("2. Passenger panel")
    print("3. Exit")
    ch = int(input("Enter your choice: "))
    while True:
        if ch == 1:
            adminpassword()
        elif ch == 2:
            user_panel()
        elif ch == 3:
            print("***** Thank You for using reservation system*****")
            print("---------------------------------------------------------------------")
            break
        main_menu()
