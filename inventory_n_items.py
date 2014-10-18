# inventory, stock management

from datetime import datetime

file = open("inventory_n_items.txt", "r+")

now = datetime.now()

file.write("Date: %s/%s/%s. Time: %s:%s:%s. \n\n" % (now.month, now.day, now.year, now.hour, now.minute, now.second))

day = []   # a list of investory left for that day 
stock = []
shopping_list = []
profit = [0]

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
        quantity_available[i] = int(quantity_available_item)
    else:     
        quantity_available[i] = 0
    cost_item = input("New Item %s Cost: " % stock[i])
    if cost_item.isnumeric() == True:
        cost[i] = float(cost_item)
    else:
        cost[i] = 10                     
    new_item = input("New item? ").lower()
    i += 1

day.append(dict(quantity_available))   # initial data   

print("Each Item's Unique ID: %s" % stock)
print("Inventory Quantity: ")
file.write("Inventory Quantity: \n")
for i in range(len(stock)):
    print("%s: %s " % (stock[i], quantity_available[i]) )
    file.write("%s: %s \n" % (stock[i], quantity_available[i]))
 
file.write("\n")    

print("Inventory Cost: ")
file.write("Inventory Cost: \n")
for i in range(len(stock)):
    print("%s: $%s " % (stock[i], cost[i]))
    file.write("%s: $%s \n" % (stock[i], cost[i]))

for i in range(len(stock)):
    quantity_sold_item = input("Number of Item %s sold: " % stock[i])
    if quantity_sold_item.isnumeric() == True:
        if int(quantity_sold_item) > quantity_available[i]:
            quantity_sold[i] = quantity_available[i]
            i += 1
        else:             
            quantity_sold[i] = int(quantity_sold_item)
            i += 1
    else:
        quantity_sold[i] = 0


file.write("\n")
print("Inventory Quantity Sold: ")
file.write("Inventory Quantity Sold: \n")
for i in range(len(stock)):
    print("%s: %s " % (stock[i], quantity_sold[i]))
    file.write("%s: %s \n" % (stock[i], quantity_sold[i]))

print("\n")
file.write("\n")
print("Quantifying New Arrival/Shipment. ")
file.write("Quantifying New Arrival/Shipment: \n")
for i in range(len(stock)):
    new_arrival_item = input("Number of Item %s shipped in: " % stock[i])
    if new_arrival_item.isnumeric() == True:
        new_arrival[i] = int(new_arrival_item)
    else:
        new_arrival[i] = 0
    file.write("%s: %s \n" % (stock[i], new_arrival[i]))
        
for i in range(len(stock)):
    quantity_left[i] = quantity_available[i] - quantity_sold[i] + new_arrival[i]

print("\n")
file.write("\n")
 
print("Total Inventory. ")
file.write("Total Inventory: \n")
print("Item Number: Quantity")
for i in range(len(stock)):
    print("%s: %s " % (stock[i], quantity_left[i]))
    file.write("%s: %s \n" % (stock[i], quantity_left[i]))
    
day.append(dict(quantity_left))

gross_total = 0
net_total = 0

 
for i in range(len(stock)):
    gross_total += quantity_sold[i]*cost[i]
    

for i in range(len(stock)):
    net_total += quantity_sold[i]*cost[i]*0.10      # 10% per item sold is the net profit 


profit.append(net_total)

print("Gross Total for the Day: $%s." % gross_total)
print("Net Profit for the Day: $%s." % net_total)
file.write("\n")
file.write("Gross Total for the Day: $%s. \n" % gross_total)
file.write("Net Profit for the Day: $%s. \n\n" % net_total)


print("\n")  
print("Summary of Total Inventory Per Day. ")
file.write("Summary of Total Inventory Per Day. \n")
print("Initial Stock of Items: %s \n" % day[0])
file.write("Initial Stock of Items: %s \n\n" % day[0])
for i in range(1,len(day)):
    print("Total Stock as of %s/%s/%s %s:%s:%s: %s" % (now.month, now.day, now.year, now.hour, now.minute, now.second, day[i]))
    print("Net Total in Dollars: $%s" % profit[i])  
    file.write("Total Stock as of %s/%s/%s %s:%s:%s: %s \n" % (now.month, now.day, now.year, now.hour, now.minute, now.second, day[i]))
    file.write("Net Profit in Dollars: $%s \n" % profit[i])

file.close()




