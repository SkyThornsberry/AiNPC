from openai import OpenAI
import time
from functions import *



programStartTime = time.time()

client = OpenAI()
#conversation_history = [{"role": "system", "content": "You are a Gerald the Unclean, a squat man from the dungeons and dragon world of Faerun. Your personality embodies your name."}]
    
#loopStartTime = time.time()
#timePassed = time.time() - loopStartTime #initialize time passed var
#while(timePassed < 600): #loop for a time limit, 
#    timePassed = time.time() - loopStartTime
#    new_message = {"role": "user", "content": gatherUserInput()} #take user input and format the response
#    conversation_history.append(new_message) #add the new message to the conversation history(necessary for continued conversation/memory)
#    completion = client.chat.completions.create( #send out the api call
#    model="gpt-4o-mini",
#    messages= conversation_history
#    )
#    response = completion.choices[0].message
#    print(responseParser(response))#print response without the formatting
#    print(response)
#    conversation_history.append(response)#add the api's response to the convo history

def apiCall(conversation_history):
    #new_message = {"role": "user", "content": gatherUserInput()}
    new_message = {"role": "user", "content": "Hello, what is your name?"}
    completion = client.chat.completions.create( #send out the api call
    model="gpt-4o-mini",
    messages= conversation_history
    )
    return (completion.choices[0].message), (conversation_history)
    




