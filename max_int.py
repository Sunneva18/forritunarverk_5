#Allow user to input a number until the input is a negative integer.
#If the input is a positive integer larger than the previous max_int,
#assign it to the max_int.
#When user inputs a negative integer, print out the max_int.

num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code
max_int = 0

while num_int > 0:
    if num_int > max_int:
        max_int = num_int
    num_int = int(input("Input a number: "))
else:
    print("The maximum is", max_int)    # Do not change this line
