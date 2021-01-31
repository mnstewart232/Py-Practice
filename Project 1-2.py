# The program will read the elements in this list by chunk, each comprised of 4 integers.
# In each chunk, the first element is the instruction, the second and the third elements are the input positions and the last element is the output
#  position.
# The first element can only be of value 1 and 2. If the value is 1, the program will perform an addition (+), if the value is 2 the program will perform a
#  multiplication (*).
# The program understands the second, third, and fourth values of each chunk as index numbers. It then looks into those index positions and takes
#  the value from those positions as input. However, the fourth value is the position in which the output should be written.
# The program then continues to the next 4-element-chunk. If the value of the first element is 99, the program stops immediately.

#My version of python's deep copy. Because importing the copy library wasn't allowed.
def my_deep_copy(inputList):

    newList = []

    for i in range(0, len(inputList)):
        newList.append(inputList[i])

    return newList

def program_solver(inputlist):
    
    #print(inputlist[0], inputlist[1], inputlist[2], inputlist[3])

    for i in range(0, len(inputlist), 4):
        #print(f"i = {i}, ")
        #print(f"Before...{inputlist}")
        instruction = inputlist[i+0]

        #Check for instruction 99 before assigning further values to prevent overshooting the index of the list.
        if (instruction == 99):
            #print("Instruction 99 encountered. Ending program.")
            #print(f"Ending state: {inputlist}")
            return inputlist[0]

        input1 = inputlist[i+1]
        input2 = inputlist[i+2]
        outputPosition = inputlist[i+3]

        #print(f"Instruction set: {instruction},{input1},{input2},{outputPosition}")
        #Instruction 1: add, instruction 2: multiply.
        if (instruction == 1):
            #print(f"Adding {inputlist[input1]} + {inputlist[input2]} at index {outputPosition}")
            inputlist[outputPosition] = inputlist[input1] + inputlist[input2]
        elif (instruction == 2):
            #print(f"Multiplying {inputlist[input1]} * {inputlist[input2]} at index {outputPosition}")
            inputlist[outputPosition] = inputlist[input1] * inputlist[input2]
        else:
            #print it?
            #print(inputlist)
            #print(f"Instruction with unexpected value {instruction} encountered at index {i}.")
            return

    return


def find_x_y(inputlist, desired_result):
    #x and y are somewhere between 1 and 99
    x = 1
    y = 1

    #Make a deep copy of the input, since python passes lists by reference
    #Hopefully this will indeed generatea new list every time...
    inputListCopy = []
    inputListCopy = my_deep_copy(inputlist)

    #double loop to test every combination of x and y between 1 and 99
    while (x <= 99):
        while (y <= 99):
            
            #Overwrite list values
            inputListCopy[1] = x
            inputListCopy[2] = y

            # Run program_solver on the list copy with the values of x and y 
            n = program_solver(inputListCopy)

            #Printout for sanity checking
            #print(x,y,n)

            #If the list evaluates to our desired result, return x and y
            if (n == desired_result):
                return x,y
            else:
                #Otherwise, reset the list
                #print("Reset List...")
                inputListCopy = my_deep_copy(inputlist)
            #Increment y
            y = y + 1
        #Reset y and increment x
        y = 1
        x = x + 1

    #case in which x and y are not found.
    return 0,0


def main():
    testList1 = [2, 3, 1, 5, 1, 3, 5, 0, 99, 7, 4, 5, 3, 0, 6, 98]
    
    testList2 = [1, 14, 40, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 6, 1, 19, 2, 19, 9, 23, 1, 23, 5, 27, 2, 6, 27, 31, 1, 31, 5, 35, 1, 35, 5, 39, 2, 39, 6, 43, 2, 43, 10, 47, 1,
        47, 6, 51, 1, 51, 6, 55, 2, 55, 6, 59, 1, 10, 59, 63, 1, 5, 63, 67, 2, 10, 67, 71, 1, 6, 71, 75, 1, 5, 75, 79, 1, 10, 79, 83, 2, 83, 10, 87, 1, 87, 9, 91, 1, 91,
        10, 95, 2, 6, 95, 99, 1, 5, 99, 103, 1, 103, 13, 107, 1, 107, 10, 111, 2, 9, 111, 115, 1, 115, 6, 119, 2, 13, 119, 123, 1, 123, 6, 127, 1, 5, 127, 131, 2, 6,
        131, 135, 2, 6, 135, 139, 1, 139, 5, 143, 1, 143, 10, 147, 1, 147, 2, 151, 1, 151, 13, 0, 99, 2, 0, 14, 0]

    testList3 = my_deep_copy(testList2)

    print("Test 1. Expected value: 113")
    print(program_solver(testList1))

    print("Test 2. Expected value: 5313702")
    print(program_solver(testList2))

    print("Find X/Y:")
    print(find_x_y(testList3, 5682320))

    return

main()
