import re



def gatherUserInput():#prompt user for their query and take input
    print("Please enter your message: \n")
    userInput = input()
    return(userInput)


def formatUserInput(userInput):#formats the user's input into the  correct format to be included in the api call
    return({"role": "user", "content": userInput})

def responseParser(response):
    # Use regex to extract the content inside the parentheses after "content=" IMPORTANT: THIS PORTION OF THE CODE IS TAKEN DIRECTLY FROM CHATGPT, I DON"T TAKE CREDIT
    match = re.search(r"content='(.*?)'", str(response))
    if match:
        return match.group(1)  # Return the captured content
    else:
        return "No content found"