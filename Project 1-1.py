
#(i) find the name of the original trainer
#(ii) given any nameTrainee (denoted as givenNameTrainee), find out who trained the givenNameTrainee and who the givenNameTrainee trains.
#If givenNameTrainee does not exist in your database, or if the givenNameTrainee is a newly trained customer who has never held a training session
#before; the program should print out 'There is no such givenNameTrainee!'.

#inputs:
#   inputDataCert is a list of tuples of trainer/trainee pairs
#   givenNameTraineeis the search parameter
#output:
#   answer_p1_q1 is a dictionary containing the four fields indicated
def solution_p1_q1(inputDataCert, givenNameTrainee):

    #Name of original trainer in the dataset, set to the first pair to start.
    originalTrainer = inputDataCert[0][0]
    print(f"originalTrainer = {originalTrainer}")
    #Name of who trained givenNameTrainee
    trainedBy = ''
    #List of people trained by givenNameTrainee
    trainedList = []
    #Boolean flag for name checking
    isGivenNamePresent = False

    #Iterate thru the dataset and attempt to find the first trainer.
    #It should be simple - for each tuple, check if the last trainer was a trainee.
    # If so, update that variable. Eventually, the first trainer will be found.
    for certificate in inputDataCert:
        #Error checking
        if (certificate[0] == givenNameTrainee or certificate[1] == givenNameTrainee):
            isGivenNamePresent = True

        #If/when the trainer's name is found
        if (certificate[1] == givenNameTrainee):
            trainedBy = certificate[0]

        #If/when this person's trainees are found:
        if (certificate[0] == givenNameTrainee):
            trainedList.append(certificate[1])

        #Finding the original trainer:
        for each in inputDataCert:
            if (each[1] == originalTrainer and each[0] != ''):
                originalTrainer = each[0]
                #print(f"each[0] (trainer) ={each[0]}, each[1] (trainee) = {each[1]}, and originalTrainer is now {originalTrainer}")


    #check if givenNameTrainee is present in the dataset. If not, return with the error message.
    if (isGivenNamePresent == False):
        print(f"There is no such {givenNameTrainee}!")
        return

    #Expected formatting of the dictionary. Note the data type of the 'train' key is an array, all others are strings.
    answer_p1_q1 = { 'originalTrainer': originalTrainer, 'givenNameTrainee': givenNameTrainee, 'trainedBy': trainedBy, 'train':trainedList}

    return answer_p1_q1


def main():
    #Test dataset
    testInputDataCert = [('Harry', 'Tim'),('Jack', 'Gary'),('Jack', 'Harry'),('Taylor', 'Glory'),
                        ('Maria','Jim'),('Jim', 'Taylor'),('Taylor', 'Jack'),('Jim', 'Sarah'),
                        ('Jack', 'Gary')]

    testInputDataCert2 = [('Jim', 'Taylor'), ('Taylor', 'Jack'), ('Jim', 'Sarah'),
                          ('Taylor', 'Glory'), ('Jack', 'Harry'), ('Jack', 'Gary'),
                          ('Harry', 'Tim'), ('', 'Maria'), ('Maria','Jim')]

    #Call the function given the test dataset and test search parameter
    print(solution_p1_q1(testInputDataCert2, 'Jim'))

    return

#Call main
main()
