from openai import OpenAI
import datetime
import time


#programStartTime = time.time()

#loopStartTime = time.time()
#timePassed = time.time() - loopStartTime #initialize time passed var
#while(timePassed < 30): #loop for 30 seconds
#    timePassed = time.time() - loopStartTime
#    time.sleep(1)
#    print("time passed:" + str(timePassed))



client = OpenAI()


completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a character from the dungeons and dragon world of Faerun."},
        {
            "role": "user",
            "content": "tell me a joke about an owlbear."
        }
    ]
)

print(completion.choices[0].message)