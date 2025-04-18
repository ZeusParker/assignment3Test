class requisitionsystem:
    
    totalbookings=2
    approved=0
    pending=2
    noapproved=0
    ticketid=20001#KISS(keep it simple stupid)this ticket id with 20001 counter is very simple and easy to understand 

    def __init__(self, passname="", passid="", formofid="", total=0.0, status="pending", referencenumber=""):
 #KISS   principles used here for the intialization
        self.ticketid=requisitionsystem.ticketid
        requisitionsystem.ticketid=requisitionsystem.ticketid+1#cleancode:this is also easy to understand as it gives the ticket id by increasing the counter by 1
        self.passname=passname
        self.passid=passid
        self.formofid=formofid
        self.total=total
        self.status=status
        self.referencenumber=referencenumber

    def get_customer_details(self):
#single responsibility principle):this method here has only one function that is to collect some information of the passenger
        self.passname=input("Enter your name: ")
        self.passid=input("Enter your passenger ID: ")
        self.formofid=input("Enter your form of ID (Passport, driver's license): ")

        #cleancode:this below helps to give proper output which is clear and easy to understand
        passname=self.passname
        passid=self.passid
        formofid=self.formofid
        ticketid=self.ticketid
        print(f"\n\n\n\nPrinting Booking Information:\n\nForm of ID (Passport, driver's license):{formofid}\n\nID Number: {passid}\n\nPassenger Name: {passname}\n\nTicket ID: {ticketid}\n")

    def record_ferry_items(self):
#singlereponsibility:as this method is only used for the puprose of recording the purchases of passengers in ferry
        total=self.total
        print("At least one item with price should be entered for the code to run properly.")
        
        while True:
            print("If you have given the order, just press Enter to leave.")
            itemname=input("Enter the name of the product: ").strip()
            if not itemname:
                break
            try:
                itemprice=float(input("Enter the price: $"))
                total=total+itemprice
            except ValueError:
                print("Invalid input! Please type a number.")#cleancode:this principle is used in this beacause is a simple way to give an error message 
        print(f"Total price: ${total:.2f}")
        self.total=total

    def ferry_service_total(self):
        self.status="pending"
        status=self.status
        total=self.total
        ticketid=str(self.ticketid)
        ID=self.passid
        decesion=input("do you want to approve the request (yes/no)")

        if decesion=="yes":
#cleancode:again this principle is followed in this condition because if we types yes the if condition will increase the number approved tickets by +1
            status="approved"
            requisitionsystem.approved=requisitionsystem.approved+1
        elif decesion=="no":
            requisitionsystem.noapproved=requisitionsystem.noapproved+1
        # Clean Code – straightforward reference creation
        approvalreferencenumber=ID[:3]+ticketid[-2:]
        print(f"\n\n\nTotal: ${total:.2f}\n\nStatus: {status}\n\nApproval Reference Number: {approvalreferencenumber}\n\n")
        self.referencenumber=approvalreferencenumber
        self.status=status

    def display_booking(self):
        # SRP – strictly for displaying booking info
        formofid=self.formofid
        idnumber=self.passid
        ticketid=self.ticketid
        total=int(self.total)
        status=self.status
        referencenumber=self.referencenumber

        # Clean Code – consistent and user-friendly output
        print(f"\n\n\n\nPrinting Booking:\n\nForm of ID(Passport, driver's license): {formofid}\n\nID Number: {idnumber}\n\nTicket ID: {ticketid}\n\nTotal: ${total}\n\nStatus: {status}\n\nApproval Reference Number: {referencenumber}")
    
    def booking_statistic(self): 
        # SRP – only shows statistics
        # KISS – minimal logic, clear output
        totalbook=requisitionsystem.totalbookings
        approved=requisitionsystem.approved
        pending=requisitionsystem.pending
        notapproved=requisitionsystem.noapproved
        print(f"\n\n\n\n\nDisplaying the Booking Statistics:\nThe total number of bookings submitted: {totalbook}\nThe total number of approved bookings: {approved}\nThe total number of pending bookings: {pending}\nThe total number of not approved bookings: {notapproved}")

# DRY violation – duplicate passenger logic could be refactored into a reusable function
passenger1 = requisitionsystem()
passenger1.get_customer_details()
passenger1.record_ferry_items()
passenger1.ferry_service_total()
passenger1.display_booking()

passenger2 = requisitionsystem()
passenger2.get_customer_details()
passenger2.record_ferry_items()
passenger2.ferry_service_total()
passenger2.display_booking()

passenger1.booking_statistic()  # Clean Code – clear entry point to display all booking stats
