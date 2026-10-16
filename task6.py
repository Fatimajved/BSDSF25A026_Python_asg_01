passenger_name = input ("Enter your name: ")
age = int (input ("Enter your age: "))
travel_distance = float(input ("Enter your travel distance"))

#Distance and fare
fare = 0
if travel_distance <= 5:
    fare = 50
elif travel_distance > 5 and  travel_distance <= 15:
    fare = 100
elif travel_distance > 15 and travel_distance <= 30:
    fare = 180
else:
    fare = 250 

if travel_distance < 0:
    print ("Negative Distance, Error!!!!")
elif age < 0:
    print ("Error !!! age can't be negative")
    age = 0

if age >= 60:
    print ("Senior Citizen Discount Applied")
    fare -= 0.20

print ("Name :" , passenger_name)
print ("Age :" , age)
print ("Fare: ", fare)    

