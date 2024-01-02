'''
CS1026a 2023
Assignment 01 Project 01 - Part A
Krish Chandola
251371956
October 4th 2023
'''

print("Project One <01> - Part A : Fibonacci Sequence")

# ask how long should the sequence go on for
SequenceLength = int(input("Sequence ends at:"))

# put a value on the first 2 terms
n1 = 0
n2 = 1
# Variable to keep track of the term number
Number = 0

# check if the number they put in is a positive number or not
if SequenceLength + 1 > 0:
    # loop until the desired number of terms have generated
    while Number < SequenceLength + 1:
        # print the results
        print(Number,":",n1, f'{n1:,}')
        # calculate the next term by adding the previous 2 terms
        nx = n1 + n2
        # update variables
        n1 = n2
        n2 = nx
        # Keep track of how many terms have generated and end when the sequence length has been reached
        Number += 1
print("END: Project One <01> - Part A")
print("Krish Chandola    Achandol    251371956")