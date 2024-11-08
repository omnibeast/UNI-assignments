try:
    sum = 0
    #open the numbers.txt file
    numFile = open('numbers.txt', 'r')

    #complete the for loop to continue reading so long as the file has more values
    for line in numFile :
        #complete the num statement below to store the next int in the file into num
        #remember by default the number will come from the file as a string and need to be converted to an int
        num = int(line.strip())
        #this line prints out the num to make sure it is working
        print(num)
        #this line of code sums up all the numbers
        sum += num

    #displays the sum of the numbers
    print(sum)

    #close the file


except Exception as err:
    print(err)