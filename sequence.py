#Allow user to input a positive integer
#print out the first n numbers of the sequense
n = int(input("Enter the length of the sequence: "))  # Do not change this line

first = 0
second = 1
third = 2
counter = 1
sum = 0

    while counter <= n:
        if counter == 1:
            print(counter)
            counter += 1
        elif counter == 2:
            print(counter)
            counter += 1
        elif num > 2 and num <= n:
            sum = first + second + third
            print(sum)
            first = second
            second = third
            third = sum
            counter += 1