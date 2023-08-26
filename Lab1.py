# Program Name: Lab1.py
# Course: IT1114/Section W02
# Student Name: Ethan Morris
# Assignment Number: Lab#1
# Due Date: 08/26/ 2023
# Purpose: Program will output total cost of materials as well as square feet required after taking in simple inputs
# from user.
# List specific resources used to complete the assignment. - Mainly used YouTube tutorials to complete this project as
# well as some school resources

#Program takes in input of user
Room_Length = float(input("Room Length: "))
Room_Width = float(input("Room Width: "))
Cost = float(input("Flooring cost: "))

#Program calculates area of the room using inputs
Room_Area = Room_Length*Room_Width

#Program calculates cost of flooring using area
flooring = Room_Area*Cost
#Program calculates tax to flooring
tax = flooring*7/100
#Program calculates total for output
total = flooring+tax

#print results upto 2 decimal places
print("Square Feet: {:.1f}".format(Room_Area))
print("Flooring Cost ${:.1f}".format(flooring))
print("Tax: ${:.3f}".format(tax))
print("Total ${:.13f}".format(total))
