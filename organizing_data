# Python file. Sorting identity.  

class Person(object):
    is_admin = False            # member variable
    is_employee = False
    is_customer = True 
    def __init__(self, first_name, last_name, address, phone, email, dob, ssn, credit_card, debit_card, bank):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone = phone
        self.email = email
        self.dob = dob
        self.ssn = ssn
        self.credit_card = credit_card
        self.debit_card = debit_card
        self.bank = bank
        setattr(self, "dob", "NA")          #hidden variable/modifying output. 
        setattr(self, "ssn", "NA")
        setattr(self, "credit_card", "NONE")
        setattr(self, "debit_card", "NONE")
        setattr(self, "bank", "NONE")
    def description(self):
        print("First Name: %s, Last Name: %s, Phone: %s, Email: %s" % (self.first_name, self.last_name, self.phone, self.email))

    def account(self):
        self.is_employee= True
 
    def admin(self):
        self.is_admin = True
        self.is_employee = True 
 
class terminal(Person):               # derived class 
    def __init__(self, first_name, last_name, address, phone, email, dob, ssn, credit_card, debit_card, bank):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone = phone
        self.email = email
        self.dob = dob
        self.ssn = ssn
        self.credit_card = credit_card
        self.debit_card = debit_card
        self.bank = bank
        setattr(self, "dob", "NA")
        setattr(self, "ssn", "NA")
        setattr(self, "credit_card", "NONE")
        setattr(self, "debit_card", "NONE")
        setattr(self, "bank", "NONE")
    def account(self):
        self.is_employee = False
    def admin(self):
        self.is_admin = False
        self.is_employee = False


print("Storing information for 3 people, beginning with Person 1.")         # extend to n persons  
 
user1_first = input("First Name: ")
user1_last = input("Last Name: ")
user1_address = input("Address: ")
user1_phone = input("Phone: ")
user1_email = input("Email: ")  
user1_dob = input("Date of Birth: ")
user1_ssn = input("SSN: ")
user1_credit_card = input("Credit Card Number and Exp Date: ") 
user1_debit_card = input("Debit Card Number and Exp Date: ")
user1_bank = input("Bank Routing and Account Number: ")

user1 = Person(user1_first, user1_last, user1_address, user1_phone, user1_email, user1_dob, user1_ssn, user1_credit_card, user1_debit_card, user1_bank)

customer1 = {
    "First Name": user1.first_name,
    "Last Name": user1.last_name,
    "Address": user1_address,
    "Phone": user1_phone, 
    "Email": user1_email, 
    "Date of Birth": user1_dob, 
    "SSN": user1_ssn, 
    "Credit Card Info": user1_credit_card, 
    "Debit Card Info": user1_debit_card, 
    "Bank Routing/Account Number": user1_bank 
    }


print("Next set of information for Person 2.")

user2_first = input("First Name: ")
user2_last = input("Last Name: ")
user2_address = input("Address: ")
user2_phone = input("Phone: ")
user2_email = input("Email: ")  
user2_dob = input("Date of Birth: ")
user2_ssn = input("SSN: ")
user2_credit_card = input("Credit Card Number and Exp Date: ") 
user2_debit_card = input("Debit Card Number and Exp Date: ")
user2_bank = input("Bank Routing and Account Number: ")

user2 = terminal(user2_first, user2_last, user2_address, user2_phone, user2_email, user2_dob, user2_ssn, user2_credit_card, user2_debit_card, user2_bank)

customer2 = {
    "First Name": user2.first_name,
    "Last Name": user2.last_name,
    "Address": user2_address,
    "Phone": user2_phone, 
    "Email": user2_email, 
    "Date of Birth": user2_dob, 
    "SSN": user2_ssn, 
    "Credit Card Info": user2_credit_card, 
    "Debit Card Info": user2_debit_card, 
    "Bank Routing/Account Number": user2_bank 
    }


print("Information for Person 3.")

user3_first = input("First Name: ")
user3_last = input("Last Name: ")
user3_address = input("Address: ")
user3_phone = input("Phone: ")
user3_email = input("Email: ")  
user3_dob = input("Date of Birth: ")
user3_ssn = input("SSN: ")
user3_credit_card = input("Credit Card Number and Exp Date: ") 
user3_debit_card = input("Debit Card Number and Exp Date: ")
user3_bank = input("Bank Routing and Account Number: ")

user3 = Person(user3_first, user3_last, user3_address, user3_phone, user3_email, user3_dob, user3_ssn, user3_credit_card, user3_debit_card, user3_bank)

customer3 = {
    "First Name": user3.first_name,
    "Last Name": user3.last_name,
    "Address": user3_address,
    "Phone": user3_phone, 
    "Email": user3_email, 
    "Date of Birth": user3_dob, 
    "SSN": user3_ssn, 
    "Credit Card Info": user3_credit_card, 
    "Debit Card Info": user3_debit_card, 
    "Bank Routing/Account Number": user3_bank 
    }

print("\n")

directory = [customer1, customer2, customer3]

for i in range(len(directory)):
    print("Summary for %s %s." % (directory[i]["First Name"], directory[i]["Last Name"]))
    print (directory[i].items())
    print("\n")

for i in range(len(directory)):
    print("First Name: " + directory[i]["First Name"])
    print("Last Name: " + directory[i]["Last Name"])
    print("Address: " + directory[i]["Address"])
    print("Phone: " + directory[i]["Phone"])
    print("Email: " + directory[i]["Email"] +"\n")


user1.description()
user2.description()
user3.description()


last_name = [directory[i]["Last Name"] for i in range(len(directory))]
print("List of Last Names: ")
print(sorted(last_name))
print("\n") 

print("Currently, %s %s is an administrator: " % (user1.first_name, user1.last_name)) 
print(user1.is_admin)
user1.admin()               # user1 just got promoted as an admin 
print("Now, %s %s is an administrator: " % (user1.first_name, user1.last_name))
print(user1.is_admin)       # overriding previous state 
print("%s %s also became an employee: " % (user1.first_name, user1.last_name))
print(user1.is_employee)    


print("Trying to make user2 an administrator: ")
user2.admin()               # trying to make user2 an admin
print(user2.is_admin)       # failed: not possible since user2 is in the derived class. 
 


print("Printing %s %s's financial information." % (user1.first_name, user1.last_name))
print("Credit Card: " + user1.credit_card)
print("Debit Card: " + user1.debit_card)



