
# library system
# library management operations: registering a student, issue or return a book, late fees, etc. 

from datetime import datetime 

 
months = 1
late_fee_per_day = 0.15

class Library_Account(object):
    def __init__(self, first_name, last_name, student_id):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.student = None
        self.basket = {}

    def card(self, card_no):
        self.card_no = card_no
        
    def return_card_no(self):
        return self.card_no                                     # prints card number

    def status(self, faculty_staff, grad_student_employee):     
        self.faculty_staff = faculty_staff                      
        self.grad_student_employee = grad_student_employee      

    def checkout(self, call_number):                            
        self.call_number = call_number
        self.basket[self.call_number] = 0                       # 0 days late
        print("%s %s: this book associated to the Call Number %s is due in %s month." % (self.first_name, self.last_name, self.call_number, months) )

    def late_fee(self, days):
        self.days = days
        print("%s %s: your late fee is $%s per day. So far, your book is late by %s days." % (self.first_name, self.last_name, late_fee_per_day, self.days))
        
class Faculty_Staff_Grad(Library_Account):
    def checkout(self, call_number):
        self.call_number = call_number
        self.basket[self.call_number] = 0
        print("%s %s: this book associated to the Call Number %s is due in %s months." % (self.first_name, self.last_name, self.call_number, 6*months))

    def late_fee(self, days):
        self.days = days
        print("%s %s: your late fee is $%s per day. So far, your book is late by %s days." % (self.first_name, self.last_name, 4*late_fee_per_day, self.days))


#    def late_fee(self, days):                  
#        super(Faculty_Staff_Grad, self).late_fee()

new_student = Library_Account("Matthew", "Thompson", 898239289)
new_student.card("0923402394")
print(new_student.return_card_no())             # prints card number 

new_student.status(False, False)
print(new_student.faculty_staff)
print(new_student.grad_student_employee)

new_student.checkout("510_Am4p_v.29")
print(new_student.basket) 
new_student.late_fee(0)


new_faculty = Faculty_Staff_Grad("Mary", "Jones", "012984378")
new_faculty.card("2009834598")
print(new_faculty.return_card_no())
new_faculty.checkout("516.35_N145l")
new_faculty.late_fee(3)
print(new_faculty.basket)

new_faculty.checkout("516.36 C763s1999")
new_faculty.late_fee(0)
print(new_faculty.basket)
 
 
