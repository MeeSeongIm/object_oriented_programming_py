# shopping list 

stock = ["item001", "item002", "item003"]
shopping_list = []

quantity_available = {
    "item001":700,
    "item002":500,
    "item003": 0
    }
cost = {
    "item001": 100.00,
    "item002": 300.00,
    "item003": 800.00 
    } 
 
print("")

quantity_item001 = input("How many %s would you like? Enter a nonnegative integer: " % stock[0])
if quantity_item001.isnumeric() == True:
    shopping_list.append(quantity_item001)
else:
    quantity_item001 = 0
    shopping_list.append(quantity_item001)

quantity_item002 = input("How many %s would you like? Enter a nonnegative integer: " % stock[1])
if quantity_item002.isnumeric() == True:
    shopping_list.append(quantity_item002)
else:
    quantity_item002 = 0
    shopping_list.append(quantity_item002)
    
quantity_item003 = input("How many %s would you like? Enter a nonnegative integer: " % stock[2])
if quantity_item003.isnumeric() == True: 
    shopping_list.append(quantity_item003)
else:
    quantity_item003 = 0
    shopping_list.append(quantity_item003)


quantity_item001 = int(quantity_item001)
quantity_item002 = int(quantity_item002)
quantity_item003 = int(quantity_item003)

print("\n")
print("Your Order: %s %s, %s %s, and %s %s." % (quantity_item001, stock[0], quantity_item002, stock[1], quantity_item003, stock[2]))


if quantity_available["item001"]>= quantity_item001:
    item001_cost = quantity_item001*cost["item001"] 
    quantity_available["item001"] -= quantity_item001 
elif quantity_item001 > quantity_available["item001"] > 0:              # backorder 
    item001_cost = quantity_available["item001"]*cost["item001"]
    print("There aren't enough %s in stock to fulfill your order. We have only %s %s in stock." % (stock[0], quantity_available["item001"], stock[0]))
    quantity_available["item001"] = 0
else:
    item001_cost = 0
    print("There are no %s in stock." % stock[0])

if quantity_available["item002"]>= quantity_item002:
    item002_cost = quantity_item002*cost["item002"] 
    quantity_available["item002"] -= quantity_item002  
elif quantity_item002 > quantity_available["item002"] > 0:
    item002_cost = quantity_available["item002"]*cost["item002"]
    print("There aren't enough %s in stock to fulfill your order. We have only %s %s in stock." % (stock[1], quantity_available["item002"], stock[1]))
    quantity_available["item002"] = 0
else:
    item002_cost = 0
    print("There are no %s in stock." % stock[1])

if quantity_available["item003"]>= quantity_item003:
    item003_cost = quantity_item003*cost["item003"] 
    quantity_available["item003"] -= quantity_item003 
elif quantity_item003 > quantity_available["item003"] > 0:
    item003_cost = quantity_available["item003"]*cost["item003"]
    print("There aren't enough %s in stock to fulfill your order. We have only %s %s in stock." % (stock[2], quantity_available["item003"], stock[2]))
    quantity_available["item003"] = 0
else:
    item003_cost = 0
    print("There are no %s in stock." % stock[2])  
print("\n") 
print("Purchasing %s will cost you $%s, " % (stock[0], item001_cost))
print("purchasing %s will cost you $%s, " % (stock[1], item002_cost))
print("purchasing %s will cost you $%s, " % (stock[2], item003_cost))


def before_taxes_total(x,y,z):
    return x+y+z

print("for a total of $%s before taxes." % before_taxes_total(item001_cost, item002_cost, item003_cost))

print("\n")

sales_tax = input("What is the sales tax in percentage? Please do not type the % sign. ")
if sales_tax.isnumeric() == True:
    sales_tax = int(sales_tax)
else:
    sales_tax = 0

print("So the sales tax in your region is %s%%." % sales_tax)

def after_taxes_total(x,y,z):
    return before_taxes_total(x,y,z)*(1+ 0.01* sales_tax)

print("Your total with the sales tax is $%s." % after_taxes_total(item001_cost, item002_cost, item003_cost) + "\n")


print("We now have %s %s, %s %s, and %s %s in stock. \n" % (quantity_available["item001"], stock[0], quantity_available["item002"], stock[1], quantity_available["item003"], stock[2])) 


print("We have a new shipment and changes in prices. \n")

# new shipment
quantity_available["item001"] += 0
quantity_available["item002"] += 50
quantity_available["item003"] += 500

# price change 
cost["item003"] -= 50

# new arrival 
quantity_available["item004"] = 80 
cost["item004"] = 50.00
stock.append("item004")

print("An update on Stock of Items: ")
print("%s: %s" % (stock[0], quantity_available["item001"]))
print("%s: %s" % (stock[1], quantity_available["item002"]))
print("%s: %s" % (stock[2], quantity_available["item003"]))
print("%s: %s \n" % (stock[3], quantity_available["item004"]))


print("Cost per Item: ")
print("%s: $%s" % (stock[0], cost["item001"]))
print("%s: $%s" % (stock[1], cost["item002"]))
print("%s: $%s" % (stock[2], cost["item003"]))
print("%s: $%s" % (stock[3], cost["item004"]))

 
