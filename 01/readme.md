# (bad) WriteUp

# TODO

- improve loops, there are probably better ways to do this


# How I solved it:

## Task 1

To solve the first task, i started of looping through the list of numbers.
For each number i checked if it was below 2020 (I didn't check the input data, so this might be unnecessary), 
in case it wasnt, we skip this iteration. Then this number got fed in a function together with a target, 
in this case the number 2020 and the remainder of the list. Since we only compare 2 nums, 
the numbers before this one don't need to be checked if they work with the current one.

If the numbers add up to 2020, we return the number. At the end of the for loop we return false. In the first loop we
check the output of that function for false, if it isnt then we return the number.

## Task 2

The second task required some refactoring and i dont think i nailed the optimization.
This is why it's on the todo list. However, the current way i solved it was to loop through all items on every check,
change the second check so it checks if the sum is below 2020, and then add a third check to check if together they are
equal to 2020. The rest stays the same, kindof :^P
