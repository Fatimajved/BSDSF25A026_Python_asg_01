consumer_name = input ("Enter Consumer Name")
units = float(input ("Enter monthly elctricity Consumption/units"))

if units < 0:
    print ("Error!! Units can't be negative")
else:
    if units <=100:
        bill = units*10
    elif units <=200:
        bill = 100*10 +(units - 100) *15
    else:
        bill = 100*10 + 100*15 + (units - 200)*20

print ("Name :" , consumer_name)
print ("Monthly units :",  units)
print ("Total Bill :" , bill)            
