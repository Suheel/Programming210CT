#Question 9
#Week 4
#a binary search that searches for values between two given points

array = [1, 3, 5, 7, 9] # in this line of code i have created an line of numbers that a binary search can be done from
array = sorted(array) # this line will then sort out the list of numbers in low to high order
x = (input) # x is going to be the low number
y= (input)# y is the high number for the binary search


def BinarySearch (NumberArray) # this code will be the start of the binary search function
    low = 0
    high = len(NumberArray)
    found = False

    while low<=high and not found:
        middle = (low + high)//2
        if NumberArray [middle] = :
            return True

        else:
            if key < NumberArray[middle]:
                high = middle-1
                
                
            elif key > NumberArray[middle]:
                low = middle+1
            else:
                return true  
    if found is not True:               # the code will return with this result if the selected number has not been found
        ArrayModify.append(key)                   #this code will add it to ArrayModify


binarySearch(array, x)                              #this line of code does the function binarysearch using the values of array and x
binarySearch(array, y)                              #this line of code does the function binarysearch using the values of array and x


print (my_search(array,x,y))    #print array, input value x which is lo and y which is high.
