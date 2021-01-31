#First Name
#Last Name
#First Met*
#Email
#Mobile
#Other*

#Global variables:
#A pair of dictionaries keyed for the email & mobile in the check_ functions

dict_emails = {}
dict_mobile = {}


#Input: lowercase string with whitespaces stripped
#output: boolean if the email is valid
def is_valid_email(string_input):
    valid_domain = ["@gmail.com", "@yahoo.com", "@uni-kassel.de", "@student.uni-kassel.de"]

    #Convert to lowercase
    string_input = string_input.lower()
    #Strip whitespace
    string_input = string_input.strip()

    #Check string if it ends with any domain in the list
    #Potential for invalid input, something like "@gmail.com@gmail.com", which is invalid (though not explicitly stated so in the problem statement)
    for domain in valid_domain:
        if (string_input.endswith(domain)):
            print(f"{string_input} was found to have domain {domain}")
            return True

    print(f"{string_input} was not found to have a valid domain.")
    return False

#Input:
# prompt - a question to prompt user input
# is_optional - boolean for whether this question can be answered with "pass" or not
#Output:
# string with suitable output
def filter_contact_info(prompt, is_optional):

    #Base value of None instead of an empty string, which may be valid depending on is_optional
    output_string = None

    #Get input based on the prompt for the question.
    output_string = input(prompt)

    while (output_string == ""):
        output_string = input("Type \'quit\' to end user input, or enter valid input.")

    while (output_string.lower() == "pass" and is_optional == False):
        output_string = input("This question is not optional. Type \'quit\' to end user input, or enter valid input.")

    if (is_optional and output_string == "pass"):
        return ""
            
    return output_string


#Asks for input fields: First name0, last name1, first met person at (optional)2, email address3
# phone number4, other (optional)5. Type 'pass' to skip optional questions.
#Record an empty string for 'pass', and do not record anything if input is 'stop'
#Loop until correct email address is given
#Output: none
def create_new_contact():

    #Empty strings
    firstName = ""
    lastName = ""
    firstMet = ""
    email = ""
    phoneNum = ""
    other = ""

    #Not the most elegant way to check for a quit command, but the alternative is more complicated than
    # I'd like to bother with.
    firstName = filter_contact_info("First Name:", False)
    if (firstName == "quit"):
        print("Quitting.")
        return

    lastName = filter_contact_info("Last Name:", False)
    if (lastName == "quit"):
        print("Quitting.")
        return

    firstMet = filter_contact_info("Met at:", True)
    if (firstMet == "quit"):
        print("Quitting.")
        return
    
    email = filter_contact_info("Email address:", False)
    if (email == "quit"):
        print("Quitting.")
        return
    #Error checking for email addresses
    while(is_valid_email(email) == False):
            input_field = filter_contact_info("Invalid email address. Enter another:", False) 

    phoneNum = filter_contact_info("Phone number:", False)
    if (phoneNum == "quit"):
        print("Quitting.")
        return

    other = filter_contact_info("Other:", True)
    if (other == "quit"):
        print("Quitting.")
        return

    #Invoke the global variables in order to modify them
    global dict_emails
    global dict_mobile
    
    #Add list to dictionaries
    dict_emails[email] = [firstName, lastName, firstMet, phoneNum, other]
    dict_mobile[phoneNum] = [firstName, lastName, firstMet, email, other]

    return


#Print out all info about the person assoc. with this email
def check_email(email_address):
    if (email_address in dict_emails):
        print(f"Email address {email_address} is associated with: {dict_emails.get(email_address)}")
    else:
        print(f"Email address {email_address} does not exist")
    return

#Print out all info about the person assoc. with this number
def check_mobile_number(mobile_number):
    if (dict_mobile.get(mobile_number)):
        print(f"Mobile number {mobile_number} is associated with: {dict_mobile.get(mobile_number)}")
    else:
        print(f"Mobile number {mobile_number} does not exist")
        print(dict_mobile)
    return


def main():

    print("Test 1 - should pass")
    is_valid_email("uk12345@uni-kassel.de    ")

    print("Test 2 - should fail")
    is_valid_email("     uk12345")

    print("Test 3 - technically correct, but is obviously wrong")
    is_valid_email("@GMAIL.com@gmail.com")

    print("Test 4: Create new contact")
    create_new_contact()

    print("Test 5: Create another contact")
    create_new_contact()

    print("Test 6: Check mobile 1")
    check_mobile_number('5024751182')
    
    print("Test 7: Check mobile 2")
    check_mobile_number('5024383677')

    print("Test 8: Check email 1")
    check_email('matt@gmail.com')
    
    print("Test 9: Check email 2")
    check_email('james@gmail.com')
    

    return

main()
