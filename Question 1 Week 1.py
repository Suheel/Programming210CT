# QUESTION 1 
# WEEK 1
# Write a function that randomly shuffles an array of integers and explain the rationale behind its implementation


array = [1, 3, 5, 7, 9, 11, 13, 15] # here i have created the array of random integers
imporr random


for i in range(0, 15): #this is the loop starting from 0 to the length of the array which is 15
         p = random.radiant (0, i)) # here i have created a temporary list of the random numbers from the loop
         if p == i: # this line is saying that if the value is the same then it should be created again
                  continue
          array[p], array[p] = array[p], array[i] # this line of code replaces the temporary list created above and will be replace it with the actual array
          
          print (array)
  
