# Flight Ticketing System
# Group Leader :
# Muhammad Abdullah SP20-BSE-074
# Member :
# Fatima Attique    SP20-BSE-080
# Group No.4
import datetime
flight = []
customer = []
global balance
balance = 0
password = "123"
def addflight(flg):
    while(True):                         # Main Outer Loop
        print("---------------------------------------------------------------------------------------------------------------"
              "-----")
        while (True):                    # Unique ID Loop
            while (True):                # Exception Loop
                try:
                    id = int(input("Enter Flight No.(Numbers Only!): "))
                    break
                except:
                    print("Please Enter Integer Data!")
            if (len(flg) > 0):       # Filtering Flight N
                list = [] 
                for i in range(0, len(flg) - 1, 9):
                    list.append(flg[i])  # Adding Flight No. in list
                # print(list)
                check1 = id in list      # check if flight no. is in list (IN function return True or Flase.)
                if check1 == True:
                    print("Please Enter Unique ID!")  # loop repeat After executing this statement.
                else:
                    flg.append(id)       # No flight No. found in list than id added in list and break
                    break
            else:
                flg.append(id)           # No flight No. found in list than id added in list and break
                break
        flg.append(input("Enter Flight Route: "))   # Adding flight route in main list
        while(True):                     # Exceptional Loop
            try:
                a = datetime.datetime.strptime(input("Enter Flight Time (HH:MM) : "), "%H:%M")   # Only accept time like 17:00 format
                T = a.strftime("%H:%M")
                break
            except:
                print("Please Enter Correct Time In HHMM Format")
        flg.append(T)                    # Adding Time In Main list
        print("\t Tickets!")
        while(True):                     # Exceptional Loop
            try:
                flg.append(int(input("Enter Economy  Tickets: ")))
                break
            except:
                print("Please Enter Integer Data!")
        while(True):                     # Exceptional Loop                     
            try:
                flg.append(int(input("Enter Price: ")))
                break
            except:
                print("please Enter Integer Data!")
        while(True):                     # Exceptional Loop
            try:
                flg.append(int(input("Enter Business Class Tickets: ")))
                break
            except:
                print("Please Enter Integer Data!")
        while(True):                     # Exceptional Loop
            try:
                flg.append(int(input("Enter Price: ")))
                break
            except:
                print("Please Enter Integer Data!")
        while(True):                     # Exceptional Loop
            try:
                flg.append(int(input("Enter Fisrt Class Tickets: ")))
                break
            except:
                print("Please enter Integer Data!")
        while(True):                     # Exceptional Loop
            try:
                flg.append(int(input("Enter Price: ")))
                break
            except:
                print("please Enter Integer Data!")
        while (True):                    # Ask User To Repeat Loop
            check0 = input("Do You Continue (y/n): ")
            print("-----------------------------------------------------------------------------------------------------------"
                  "-----")
            if ((check0 == "n") or (check0 == "N")):
                return                   # Ending The Whole Function
            elif ((check0 == "y") or (check0 == "Y")):
                #print(flg)
                break    # Break Internal Loop and Break The Function
            else:
                print("Press (Y/N) !")   # Tell User To Enter Correct Value.


def viewflight(flg):            # Display Flight Records
    l = len(flg)                # Check Flight List Lenght
    if l == 0:
        print("No Record Entered")       # mean LIst is Empty
        print("---------------------------------------------------------------------------------------------------------------"
              "-----")
        return                  # Function Ends
    else:                       # Records Exist in list.
        for a in range(0, len(flg), 9):  # Filter Flight No.
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "
                  "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
            print("Flight No.: " + str(flg[a]) + " \t Flight  route: " + flg[a + 1] + " \t Flight Time: " + flg[a + 2] + "\n"
            "Economy Tickets: " + str(flg[a + 3]) + " \t E-Price: " + str(flg[a + 4]) +"\n"
            "Business Class Tickets: "  + str(flg[a + 5]) + " \t B-Price: " + str(flg[a + 6]) + "\n"
            "First Class Tickets : " + str(flg[a+7]) + " \t F-Price: " +str(flg[a + 8]))
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "
                  "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

def sortt(num):                # bubble sortting on list
    for i in range(len(num) - 9, 0, -9):  # Loop on Flight NO.
        # check = num[i]
        # print(check)
        for j in range(0, i, 9):          # inverse Loop on Flight No.
            # check2 = num[j]
            # print("j" + str(check2))
            if num[j] > num[j + 9]:       # Swapping Flight Record
                temp = []
                temp = num[j:j + 9]
                num[j] = num[j + 9]
                num[j + 1] = num[j + 10]
                num[j + 2] = num[j + 11]
                num[j + 3] = num[j + 12]
                num[j + 4] = num[j + 13]
                num[j + 5] = num[j + 14]
                num[j + 6] = num[j + 15]
                num[j + 7] = num[j + 16]
                num[j + 8] = num[j + 17]
                num[j + 9] = temp[0]
                num[j + 10] = temp[1]
                num[j + 11] = temp[2]
                num[j + 12] = temp[3]
                num[j + 13] = temp[4]
                num[j + 14] = temp[5]
                num[j + 15] = temp[6]
                num[j + 16] = temp[7]
                num[j + 17] = temp[8]
   # viewflight(num)                             # Call Display Fuction After Sorting
    return (num)


def binary(flg):                                # Binary Search On List Function
    flight1 = sortt(flg)                        # Sorting Function Call
    # print(flight1)
     # index = -1
    # s = 0
    list1 = []
    for i in range(0, len(flight1) - 1, 9):     # Loop To Take Out Flight No. Indexes
        list1.append(flight1[i])                # Adding Flight No. in list1
    # print(list1)
    def search1(list, n):                       # Binary Search In List1
        index = -1
        l = 0
        u = (len(list) - 1)
        while l <= u:
            mid = (l + u) // 2
            if list[mid] == n:
                index = mid * 9
                # print(index)
                return index
            else:
                if list[mid] < n:
                    l = mid + 1
                else:
                    u = mid - 1
        return index

    while (True):                              # Exception Loop
        try:
            m = int(input("Enter Flight No. : "))
            break
        except:
            print("Please Enter Integer Data!")
    outindex = search1(list1, m)               # Call Binary Search Function.
    #print(outindex)
    if (search1(list1, m) != -1):              # If Function Doesn't return -1
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
              " - - - - - - - - - - - - - -")
        # print("Found on "+str(outindex)+ "index")
        print("Flight No.: " + str(flight1[outindex]) + " \t Flight Route: " + flight1[outindex + 1] + " \t Flight Time: " +flight1[outindex + 2] + "\n"
              "Economy Tickets: " + str(flight1[outindex + 3]) + " \t E-Price: " + str(flight1[outindex + 4]) + "\n"
              "Business Class Tickets: " + str(flight1[outindex + 5]) + " \t B-Price: " + str(flight1[outindex + 6]) + "\n"
              "First Class Tickets: " + str(flight1[outindex + 7]) + " \t F-Price: " + str(flight1[outindex + 8]))
    else:
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
              " - - - - - - - - - - - - - -")
        print("Not Found")

def edit(flight):                # Editting 
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "
          "- - - - - - - - - - - - - - - -")
    while (True):                # Exception Loop
        try:
            i = int(input("Please Enter Flight No. You Want To Change:  "))
            break
        except:
            print("Please Enter Integer Data!")
    lista = []
    for f in range(0,len(flight)-1,9):         # Filter Flight No. indexes
        lista.append(flight[f])                # Adding Flight No. in lista
    check = i in lista                         # checking User Input In lista
    if check == True:                          # if user matches with list indexes
        a = lista.index(i)                     # Getting index of flight No. in lista
        a = a*9                                # Multiply lista index by 9 to get Real Index 
        while (True):                          # Loop Repeat Data Changing
            while (True):                      # Exception Loop
                try:
                    menu = int(input(
                        "[1] Change flight No. \n [2] Change Flight Route. \n [3] Change Flight Time. \n [4] Change "
                        "Economy Tickets. \n [5] Change E-Price. \n [6] Change Business Class Tickets. \n [7] Change B-Price. \n"
                        " [8] Change First Class \n [9] F-Price. \n [0] BACK. \n "
                        "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
                        "- - - - - - - - - - - - - - - - - - \n  :       "))
                    break
                except:
                    print("Please enter Integer Data!")
            if menu == 1:                   # If user want to change Flight No.
                while (True):               # Unique ID Loop
                    while (True):           # Exception Loop
                        try:
                            id = int(input("Enter New Flight No. :  "))
                            break
                        except:
                            print("Please Enter Integer Data!")
                    list = []
                    for n in range(0, len(flight) - 1, 9):        # Filtering Flight No. Indexes
                        list.append(flight[n])                    # Adding Flight No. in list
                    check1 = id in list                           # Check user Input In list
                    if check1 == True:                            # if user input Exit in list
                        print("Please Enter Unique Flight No.!")  # repeat loop to ask user to enter another flight No.
                    else:
                        if len(customer) != 0:                         # if Booking Exit against this Flight
                            for s in range(1, len(customer), 5):  # check on flight no. in customer list
                                 if i == customer[s]:             # if flight no. match in customer
                                     customer[s] = id             # change with flight No.
                        flight[a] = id                            # Adding New Flight No. In List
                        break
                    
            elif menu == 2:               # Change Flight Route
                flight[a + 1] = input("Enter New Flight Route :  ")
            elif menu == 3:               # Change Flight Time
                while(True):                     # Exceptional Loop
                    try:     
                        date = datetime.datetime.strptime(input("Enter Flight Time (HH:MM) : "), "%H:%M")   # Only accept time like 17:00 format
                        time = date.strftime("%H:%M")
                        break
                    except:
                        print("Please Enter Correct Time In HHMM Format")
                flight[a + 2] = time      # Adding New Time In List
            elif menu == 4:               # Change Economy Tickets
                while (True):          # Exception Loop
                    try:
                        flight[a + 3] = int(input("Enter New Economy Tickets:  "))     
                        break
                    except:
                        print("Please Enter Integer Data!")
            elif menu == 5:      # Changing Economy Price
                while(True):      # Exception Loop
                    try:
                        flight[a + 4] = int(input("Enter New E-Price:  "))
                        break
                    except:
                        print("Please Enter Integer Data!")
            elif menu == 6:      # Changing Business Tickets
                while (True):       # Exception loop
                    try:
                        flight[a + 5] = int(input("Enter New Business Class Tickets:  "))
                        break
                    except:
                        print("Please Enter Integer Data!")
            elif menu == 7:      # Changing Business Price
                while (True):      # Exception Loop
                    try:
                        flight[a + 6] = int(input("Enter New B-Price:  "))
                        break
                    except:
                        print("Please Enter Integer Data!")
            elif menu == 8:        # Changing First Class Tickets
                while (True):      # Exception Loop
                    try:
                        flight[a + 7] = int(input("Enter New First Class Tickets:  "))
                        break
                    except:
                        print("Please Enter Integer Data!")
            elif menu == 9:       # Changing First Class Price
                while (True):   # Exception Looop
                    try:
                        flight[a + 8] = int(input("Enter New F-Price:  "))
                        break
                    except:
                        print("Please Enter Integer Data!")
            elif menu == 0:      # Back
                break
        # print(flight)
        viewflight(flight)      # Calling View Record function
        return flight
    else:               # IF User Enter Wrong Flight No.
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
              "- - - - - - - - - - - - - - - - - -")
        print("Wrong ID") 
        while (True):    
            h = input("Do You Want Add New Record(y/n):    ")
            if ((h == "n") or (h == "N")):
                return    # End the Function
            elif ((h == "y") or (h == "Y")):
                addflight(flight)
                break
            else:    
                print("Press (Y/N)!")
                
                
def delete():  # Deleting Record Function
    while (True):  # Deleting Menu Loop
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
              " - - - - - - - - - - - - - - - - - -")
        while (True):  # Exception Loop
            try:
                user = int(input(" [1] Delete Flight Record. \n [2] Delete All Record. \n [0] BACK \n "
                                 "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
                                 "- - - - - - - - - - - - - - - - - - \n   :  "))
                break
            except:
                print("Please Enter Integer Data!")
        if user == 2:
            flight.clear()      # Buil-In Clear Clear Function Delete Whole List
            customer.clear()
            global balance
            balance = 0 
            #print(flight)
        elif user == 0:
            break    # Back
        elif user == 1:
            while (True):  # Repeating Deletion Task
                while (True):  # Exception Loop
                    try:
                        d = int(input("Enter Flight No. You Want To Delete:  "))
                        break
                    except:
                        print("Please Enter Interger Data!")
                listid = []   # Temparory List Of Flight No.
                for l in range(0,len(flight)-1,9):
                    listid.append(flight[l])  # Adding Flight No. In Lisid
                check = d in listid    # Checking Using IN Function 
                if check == True:     # If Found
                    while(True):      # deleting all boooking against Deleted flight Record
                        listi = []    # Temparory LIst OF Booking ID
                        for x in range(1,len(customer)-1,5):
                            listi.append(customer[x])    # Adding Flight No. In LIsti in Customers booking List
                        checki = d in listi    # Checking Flight No.
                        if checki == True:       # If Booking Was Made
                            z = listi.index(d)    # GEtting Index
                            z = (z*5)+1         # Getting Index From Original Customer LIst
                            for r in range(0,5):     # Poping  Samer Index 5 Time To Delete Full Record
                                customer.pop(z-1)
                        else:     # IF Not Found
                            break   # Exit Loop
                    a = listid.index(d)   # Getting Index of Flight No.
                    a = a*9               # Mutliply By 9 to Get Original Index OF Flight List
                    for i in range(0, 9):    # Pooping Same Index 9 Times To Delete Full record
                        flight.pop(a)
                elif check == False:
                    print("Wrong ID")   # If ID Not Found
                while (True):
                    f = input("If You Want To delete Another Record Press [Y/N]:    ")
                    if ((f == "y") or (f == "Y")):
                        break
                    elif ((f == "n") or (f == "N")):
                        return  # Break The Function
                    else:
                        print("Press (Y/N)!")                
                
                
def verify(customer, flight):  # Function Verify Full Booking Record Entery
    while (True):  #Main Function To Check USer Want To Repeat Booking
        while (True): # Checking Full record
            booking = []  # Temparory List 
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
                  " - - - - - - - - - - - - - - - - -")
            addcustomer(booking, flight)  #   Calling Add Function
            if len(booking) < 5:     # If Booking Record in Booking List IS Not Full
                print("Incomplete Booking Record(Try Again)!")
            elif len(booking) == 5: # IF Record Lenght Is Full
                customer.append(booking[0])   # Adding Record In Original List
                customer.append(booking[1])
                customer.append(booking[2])
                customer.append(booking[3])
                customer.append(booking[4])
                print("Booking Successfull !")
                #print(customer)
                #print(balance)
                # print(flight)
                print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
                      " - - - - - - - - - - - - - - - - - - - - -")
                break #Interanl Loop Break
        while True:
            check0 = input("Do You Want To Make Another Book (Y/N): ")
            if (check0 == "n") or (check0 == "N"):
                return
            elif (check0 == "y") or (check0 == "Y"):
                break
            else:
                print("Press (Y/N) !)")
def addcustomer(booking, flight):  # Add Customers Booking in List
    while True:  # Appending Booking Loop
        global balance
        while True:  # Unique ID Loop
            while True:  # Exception Loop
                try:
                    id = int(input("Enter Booking ID(Numbers Only!): "))
                    break
                except:
                    print("Please Enter Integer Data!")
            list = []  # Temparory list of Booking ID 
            if len(customer) > 0:
                for i in range(0, len(customer) - 1, 5):
                    list.append(customer[i])  #  Adding booking IDs In LISt
                # print(list)
                check1 = id in list  # Checking Booking Already Exist or not
                if check1 == True: # If Exist
                    print("Please Enter Unique ID!")
                else:               # If Not Exist
                    booking.append(id)  # APPEND iN TEMPARORYBOOKING LiST
                    break     # Break Unique ID Loop
            else:             # Length OF Customer Is Zero
                booking.append(id)
                break     # Break Unique ID Loop
        check3 = matchingid(booking, flight)    # Function To Check 
        booking.append(input("Enter Passport Number: ")) # Adding Passport Number In temparory LIst
        #print(check3)
        if check3 != -1: # If Flight No. Is Correct
            while(True):   #  Ticket type MEnu Loop
                while(True): #  Exception Loop
                    try:
                        tmenu = int(input(" [1] Economy tickets. \n [2] Business Class Tickets. \n [3] First Class Tickets."
                                          "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
                                          "- - - - - - - - - - - - - - - - - - \n   :        "))
                        break
                    except:
                        print("Please Enter Integer Data!")
                if tmenu == 1:    # Economy Type
                    while(True):  # Confirming Tickets In Loop
                        print(" Available Economy Tickets: " + str(flight[check3+3]) + "\n Price: "+str(flight[check3+4]))
                        t = flight[check3+3]  # Storing Number Of Ticket In  Varable t
                        while(True): # Exception Loop
                            try:
                                ticket = int(input("Enter Tickets You Want :"))
                                break
                            except:
                                print("Please Enter Integer Data!")
                        if t == 0: # if No Ticket Aviable
                            print("All Seats Booked! ")
                            break
                        elif (t >= ticket):  
                            c = (t - ticket)
                            flight[check3 + 3] = c    # Subtracting Booked Tickets From Flight LIst
                            booking.append(1)     # Adding Ticket Type In Booking List, 1 For Economy Class
                            booking.append(ticket)     # Adding Tickets In Booking
                            balance = balance + (flight[check3+4]*ticket)  # Adding Ticket Price In Balance Variable
                            #print(balance)
                            return balance
                        else:
                            print("PLease Enter Aviable Number OF Tickets")
                    break  # Breaking External Loop
                elif tmenu == 2:    # Business Type
                    while(True):  # Confirming Tickets In Loop
                        print(" Available Business Tickets: " + str(flight[check3+5]) + "\n Price: "+str(flight[check3+6]))
                        t = flight[check3+5]  # Storing Number Of Ticket In  Varable t
                        while(True):           # Exception Loop
                            try:
                                ticket = int(input("Enter Tickets You Want :"))
                                break
                            except:
                                print("Please Enter Integer Data!")
                        if t == 0: # if No Ticket Aviable
                            print("All Seats Booked! ")
                            break
                        elif (t >= ticket):
                            c = (t - ticket)
                            flight[check3 + 5] = c    # Subtracting Booked Tickets From Flight LIst
                            booking.append(2)     # Adding Ticket Type In Booking List  , 2 For Business Class
                            booking.append(ticket)    # Adding Tickets In Booking
                            balance = balance + (flight[check3+6]*ticket) # Adding Ticket Price In Balance Variable
                            #print(balance)
                            return balance
                        else:
                            print("PLease Enter Aviable Number OF Tickets")
                    break # Breaking External Loop
                elif tmenu == 3:  # First Class Type
                    while(True):      # Storing Number Of Ticket In  Varable t
                        print(" Available First Class Tickets: " + str(flight[check3+7]) + "\n Price: "+str(flight[check3+8]))
                        t = flight[check3+7] # Storing Number Of Ticket In  Varable t
                        while(True):           # Exception Loop
                            try:
                                ticket = int(input("Enter Tickets You Want :"))
                                break
                            except:
                                print("Please Enter Integer Data!")
                        if t == 0: # if No Ticket Aviable
                            print("All Seats Booked! ")
                            break
                        elif (t >= ticket):
                            c = (t - ticket)
                            flight[check3 + 7] = c  # Subtracting Booked Tickets From Flight LIst
                            booking.append(3)    # Adding Ticket Type In Booking List ,3 for first Class
                            booking.append(ticket)  # Adding Tickets In Booking
                            balance = balance + (flight[check3+8]*ticket) # Adding Ticket Price In Balance Variable
                            #print(balance)
                            return balance
                        else:
                            print("PLease Enter Aviable Number OF Tickets")
                    break # Breaking External Loop
                else:
                    print("Please Choose Correct Option!")
        break
def matchingid(booking, inflight):  # Match Flight No. During Booking
    while (True):  # Verify Flight No. Loop
        while (True):  # Exception Loop
            try:
                id = int(input("Enter Flight No. (Numbers Only!): "))
                break
            except:
                print("Please Enter Integer Data!")
        list = [] # Tempartory List
        # print("12")
        if len(inflight) > 0:  # If Flight Record Exist
            for i in range(0, len(inflight) - 1, 9):
                list.append(inflight[i])  # Adding Flight No. In temparory list
            #print(list)
            check1 = id in list    # Checking Flight No. If Exist Or Not
            # print("18")
            if check1 == False:  # If Not Exist
                print("Please Enter Correct ID: ")
            else:   # If Flight No. Exist
                booking.append(id) # Adding Flight No. In booking List
                fid = list.index(id)  # Getting Index OF flight No. From temparory Lsit
                fid = fid*9 # Index In Original  List
                #print("23")
                return fid # Return Flight No. Index
        else:   # If Lenght Of Flight LIst Id Zero
            # print("27")
            print("No Movie Record Exist(Ask Admin To Add Movie Record.)!")
            return -1   # Return -1          
                
def vbooking():  # View Booking Records
    if len(customer) == 0:  # If No Booking Was Made
        print("No Booking Has Been Made!")
    else:  # If Booking Was Made
        for i in range(0, len(customer) - 1, 5):  # loop To Filter Booking ID
            id = customer[i + 1] # Flight No. Of Booking 
            # print(id)
            list2 = [] # Temporary Flight No. Lsit
            for j in range(0, len(flight) - 1, 9):
                list2.append(flight[j]) # Adding Flight No. In List
            # print(list2)
            a = list2.index(id) 
            a = (a * 9) # Flight no. Index From Flight List
            Ttype = customer[i + 3]  # Checking Ticket Type
            if Ttype == 1: # IF Tpye Is 1
                t = "Economy"
            elif Ttype == 2: # IF Tpye Is 2
                t = "Business Class"
            elif Ttype == 3: # IF Tpye Is 3
                t = "First Class"
            # print(a)
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
                  " - - - - - - - - - - - - - - ")
            print(
                " Booking ID: " + str(customer[i]) + "\n FlightNo. : " + str(customer[i + 1]) + " \t Flight Route: " + flight[
                 a + 1] + " \t Flight Time : " + flight[a + 2] + " \t Passport No. : " + str(customer[i + 2]) + "\n"
                 " Ticket Type: "+ t + " \t Ticket Booked: "+ str(customer[i + 4]))
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
                  " - - - - - - - - - - - - - - ")                
def delbook():    # Delete Booking
    while (True):  # Outer Repeat Function Loop
        global balance
        while (True):  # Exception Loop
            try:
                user = int(input("Enter Booking ID: "))
                break
            except:
                print("Please Enter Integer Data!")
        list1 = [] # Tempaprory Booking Id List
        for l in range(0, len(customer) - 1, 5):      # Loop To Filter Booking ID
            list1.append(customer[l]) # Adding  booking Id in list1
        check = user in list1 # Checking If Exist
        if check == False: # If Booking Not Found
            print("No Booking Record Exist Against This ID!")
        else:  # If Booking Id Exist
            a = list1.index(user)
            a = a*5                                  # mutiplying 5 to get original Index Number
            list3 = []
            for d in range(0, len(flight)-1, 9):     # Loop to filter flight No.
                list3.append(flight[d])
            #print(customer[(a * 3) + 1])
            b = list3.index(customer[a + 1])         # Adding 1 to Get Flight No. and then index
            b = b*9                                  # mutiplying 9 to get original Index Number
            ctype = customer[a + 3]
            t = customer[a + 4]
            if ctype == 1:                           # Economy Type
                flight[b + 3] += t         # Adding delete ticket in flight record
                balance = balance - (flight[b + 4]*t)    # Deducting delete booking price from Balance
            elif ctype == 2:                         # Business class Type
                flight[b + 5] += t         # Adding delete ticket in flight record
                balance = balance - (flight[b + 6]*t)    # Deducting delete booking price from Balance
            elif ctype == 3:                         # First Class Type
                flight[b + 7] += t         # Adding delete ticket in flight record
                balance = balance - (flight[b + 8]*t)    # Deducting delete booking price from Balance
            #print(b)
            for i in range(0, 5):           # Loop Repeat 5 times to pop booking record of 5 indexes.
                customer.pop(a)                 
            print("Successfully Deleted! ")
        while (True):  # Ask User To Repeat Function
            repeat = input("Do You Delete Another Booking? (Y/N).")
            if ((repeat == "Y") or (repeat == "y")):
                break
            elif ((repeat == "n") or (repeat == "N")):
                return
            else:
                print("Press (Y/N) !")               
       
def CancelFlight():    # Cancel Flight by Deleting Flight Booking and Setting Time To Cancelled
    if (len(customer) == 0):  # IF No Booking Record Exist
        print("No Booking Has Been Made Yet!")
    else: # IF Booking Was Made
        while(True):         # main LOOP
            global balance
            while(True):     # Exceptional Loop
                try:
                    user = int(input("Enter Flight No. : "))
                    break
                except:
                    print("Please Enter Integer Data! ")
            list3 = []
            for d in range(0, len(flight)-1, 9):     # Loop to filter flight No.
                list3.append(flight[d])
            check = user in list3 # Checking Flight No.
            if check == False: # If Not Found
                print("Wrong Flight No.!")
            else:
                b = list3.index(user)
                b = b* 9  # Getting Flight No. Index
                while(True):                                       # Deleting all boooking against Deleted Flight Record
                    listi = []   # Flight No. in Customers lIST
                    for x in range(1, len(customer)-1, 5):
                        listi.append(customer[x])
                    checki = user  in listi  # Checking flight no. entered By User In Listi
                    if checki == True: #  If Found
                        z = listi.index(user)
                        z = (z*5)-1   # Booking ID
                        ctype = customer[z + 3]  # Ticket type
                        t = customer[z + 4] 
                        if ctype == 1:                              # Economy Type
                            flight[b + 3] += t         # Adding delete ticket in flight record
                            balance = balance - (flight[b + 4]*t)    # Deducting delete booking price from Balance
                        elif ctype == 2:                            # Business class Type
                            flight[b + 5] += t        # Adding delete ticket in flight record
                            balance = balance - (flight[b + 6]*t)    # Deducting delete booking price from Balance
                        elif ctype == 3:                            # First Class Type
                            flight[b + 7] += t         # Adding delete ticket in flight record
                            balance = balance - (flight[b + 8]*t)    # Deducting delete booking price from Balance
                        for r in range(0,5):
                            customer.pop(z)
                    else:
                        print("Successfully Deleted ALL Bookings ")
                        flight[b + 2] = "Cancelled"   # Flight time Set to Cancelled
                        flight[b + 3] = 0
                        flight[b + 4] = 0
                        flight[b + 5] = 0
                        flight[b + 6] = 0
                        flight[b + 7] = 0
                        flight[b + 8] = 0
                        break
            while(True):
                check0 = input("Do You Want To Cancel Another Flight (Y/N): ")
                if (check0 == "n") or (check0 == "N"):
                    return
                elif (check0 == "y") or (check0 == "Y"):
                    break
                else:
                    print("Press (Y/N) !)")      
       
       
       

while (True):  # Outer Main Loop
    print(
        "----------------------------------------------------------------------------------------------------------------------")
    while (True):  # Exception Loop
        try:
            outmenu = int(input(" [1] Admin View \n [2] Costumer View \n [0] Exit \n "
                "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
                "- - - - - - - - - - - - - - - - - - \n : "))
            break
        except:
            print("please Enter Integer Data!")
    print(
        "----------------------------------------------------------------------------------------------------------------------")
    if outmenu == 1:  # Admin View
        while(True):
            pwd = input("Enter Password: ")
            if (pwd == password) :
                while (True):  # Menu Loop
                    print("-----------------------------------------------------------------------------------------------------------"
                          "-----")
                    while (True):  # Exception Loop
                        try:
                            menu = int(input(
                                " [1] Add Flight Record. \n [2] View Flight Record. \n [3] View Flight With SORTING. "
                                "\n [4] Search Flight Record By ID. \n [5] Edit Flight Record. \n [6] Delete Flight Record. \n [7] View Booking. \n "
                                "[8] Delete Booking. \n [9]Cancel Fight. \n [10] Balance. \n [0] BACK \n"
                                "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "
                                "- - - - - - - - - - - - - -  \n : "))
                            break
                        except:
                            print("Please Enter Integer Data!")
                    print("-----------------------------------------------------------------------------------------------------------"
                          "-----")
                    if menu == 1:
                        addflight(flight)
                        #print(flight)
                    elif menu == 2:
                        viewflight(flight)
                    elif menu == 3:
                        sortt(flight)
                    elif menu == 4:
                        binary(flight)
                    elif menu == 5:
                        edit(flight)
                    elif menu == 6:
                        delete()
                    elif menu == 7:
                        vbooking()
                    elif menu == 8:
                        delbook()
                    elif menu == 9:
                        CancelFlight()
                    elif menu == 10:
                        print("Current Balance Is: " + str(balance))
                    elif menu == 0:
                        break
                    else:
                        print("Enter Correct Number! ")
                break
            else:
                print("Wrong Password!")
                print("-----------------------------------------------------------------------------------------------------------"
                      "-----")
    elif outmenu == 2:  # User View
        while (True):
            print("-----------------------------------------------------------------------------------------------------------"
                  "----")
            while (True):  # Exception Loop
                try:
                    menu2 = int(input(" [1] View Flight Record \n [2] Add Booking \n [3] Veiw Bookings \n [0] Back \n"
                              "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "
                              "- - - - - - - - - - - - - - \n :"))
                    break
                except:
                    print("Please Enter Integer Data!")
            print("------------------------------------------------------------------------------------------------------------"
                  "---")
            if menu2 == 1:
                viewflight(flight)
            elif menu2 == 2:
                verify(customer, flight)
            elif menu2 == 3:
                vbooking()
            elif menu2 == 0:
                break
            else:
                print("Enter Correct Number!")
    elif outmenu == 0:  # Program Exit
        exit ()
    else:
        print("Choose Correct Option!")


