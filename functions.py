import re



def gatherUserInput():#prompt user for their query and take input
    print("Please enter your message: \n")
    userInput = input()
    return(userInput)


def formatUserInput(userInput):#formats the user's input into the  correct format to be included in the api call
    return({"role": "user", "content": userInput})

def responseParser(response):#parses the response given by the api and returns just the message appropriate for viewing by the user.
    responseSplit = str(response).split('\'')#split at the colons
    return(responseSplit[1])
    
