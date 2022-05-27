#Let's start a coffee shop together!! We're going to build a coffee shop using some new Python programming concepts!!

#print("Hello welcome to Lily's coffee!!!!!!!!!!!!")

name = input("Hello welcome to Lily's coffee!!!!!!!!! What is ur name?\n")

print("Hello " + name + ", thank you for coming in today.\n\n\n")

#CHALLENGE 1 ----> (timestamp 12:36)

#Program the robot barista to give the customer a menu, (make the menu a variabe) ask them what they want, and tell them it will be ready in a moment. Here is an example of the output:
menu = "Coffee, Latte, Croissant"

#print("we have " + menu + " availablez.")

order = input(name + ", what do you want to eat? here is what we are serving\n" + menu + "\n")

#Sounds good customer_name! We'll have that coffee_beverage ready for you in a moment!!
print("Sounds good, " + name + "! We'll have that " + order + " out for you in a moment!")
print("thank you")
