#inputs
name = input("Enter your name:")
marks_obtained =float( input("Enter your obtained marks:"))
total_marks = float(input("Enter total marks:"))
entry_testscore = float (input("Enter your Test Score:"))
entry_testmarksTotal = float (input ("Enter Total marks of Test: "))

#check inputs
if total_marks <=0 or entry_testmarksTotal <=0:
    print ("Error!!! total marks or test marks must be greater than zero")
elif marks_obtained <=0 or entry_testscore:
    print ("Error!! marks must be greater than zero")
elif total_marks < marks_obtained:
    print ("Error!! Total marks must be greater than obtained marks") 
elif entry_testmarksTotal < entry_testscore:
    print ("Error!! total marks must be greater ")
    
intermediate_percentage = float((marks_obtained/total_marks)*100.00)
test_percentage = float((entry_testscore/entry_testmarksTotal)*100.00)


# outputs
print ("Name:", name)
print ("Obtained Marks:", marks_obtained)
print("Total Marks:" , total_marks)
print ("Entry Test score:" , entry_testscore)
print ("Entry Test Total Marks:" , entry_testmarksTotal)
print (" Intermediate Percentage:" , intermediate_percentage)
print ("Test Percentage:" , test_percentage)

#eligibility
if intermediate_percentage >= 60.00 and test_percentage >= 50:
    print ("You are eligible for this admission ")     
elif intermediate_percentage < 60.00:
    print ("Error!! You're not eligible as your intermediate_percentage is low !!!")
elif test_percentage < 50.00:
    print ("Error!! You're not eligible as your entry test_percentage is low!!")    
    