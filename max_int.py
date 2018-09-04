#Design an algorithm that finds the maximum positive integer input by a user.  
#The user repeatedly inputs numbers until a negative value is entered.


#create an integer that asks for a number input
#set the maximum postive number to zero
#creat a while loop that finds the largest number and outputs it to the maximum positive integer
#the loops stops when the user inputs less than zero and then prints out hte maximum positive integer



num_int = int(input("Input a number: "))    # Do not change this line

max_int = 0

while num_int >= 0:
    if num_int > max_int:
        max_num = max_int
        max_int += 1
    else:
        num_int = int(input("Input a number: ")) 
else:
    if num_int < 0:
        print("The maximum is", max_int)   
   

