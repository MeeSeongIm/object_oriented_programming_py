# inventory, stock management


day = []   # a list of investory left for that day 
stock = []
shopping_list = []

quantity_available = {}
cost = {}
quantity_sold = {}
new_arrival = {}
quantity_left = {}


yes = {"yes", "ye", "y"}  
i=0 
new_item = input("New item? ").lower()  
while new_item in yes:
    stock.append(i)
    quantity_available_item = input("New Item %s Quantity: " % stock[i])
    if quantity_available_item.isnumeric() == True:
        quantity_available[i] = quantity_available_item
    else:     
        quantity_available[i] = 0
    cost_item = input("New Item %s Cost: " % stock[i])
    if cost_item.isnumeric() == True:
        cost[i] = cost_item
    else:
        cost[i] = 10                     
    new_item = input("New item? ").lower()
    i += 1

day.append(dict(quantity_available))   # initial data   

print("Each Item's Unique ID: %s" % stock)
print("Inventory Quantity: ")
for i in range(len(stock)):
    print("%s: %s " % (stock[i], quantity_available[i]) )

print("Inventory Cost: ")
for i in range(len(stock)):
    print("%s: $%s " % (stock[i], cost[i]))

for i in range(len(stock)):
    quantity_sold_item = input("Number of Item %s sold: " % stock[i])
    if quantity_sold_item.isnumeric() == True:
        if quantity_sold_item > quantity_available[i]:
            quantity_sold[i] = quantity_available[i]
            i += 1
        else:             
            quantity_sold[i] = quantity_sold_item
            i += 1
    else:
        quantity_sold[i] = 0

print("Inventory Quantity Sold: ")    
for i in range(len(stock)):
    print("%s: %s " % (stock[i], quantity_sold[i]))

print("\n") 
print("Quantifying New Arrival. ")
for i in range(len(stock)):
    new_arrival_item = input("Number of Item %s shipped in: " % stock[i])
    if new_arrival_item.isnumeric() == True:
        new_arrival[i] = new_arrival_item
    else:
        new_arrival[i] = 0
        
for i in range(len(stock)):
    quantity_left[i] = int(quantity_available[i]) - int(quantity_sold[i]) + int(new_arrival[i])

print("\n")
print("Total Inventory. ")
print("Item Number: Quantity")
for i in range(len(stock)):
    print("%s: %s " % (stock[i], quantity_left[i]))

day.append(dict(quantity_left))

print("\n") 
print("Summary of Total Inventory Per Day: %s " % day)
 


    
