from flask import Flask, jsonify
import time
import sys
sys.path.append('../')
from apiCaller import apiCall

app = Flask(__name__)
    
# Members API Route
@app.route("/members")
def members():
    return {"members": ["member1", "member2"]}

@app.route("/apiLoop")
def apiLoop():
    
    initialConversation = [{"role": "system", "content": "You are a Gerald the Unclean, a squat man from the dungeons and dragon world of Faerun. Your personality embodies your name."}]
    conversationHistory = initialConversation
    response, conversationHistory = apiCall(conversationHistory)
    
    return(jsonify({"response": str(response)}))
    #loopStartTime = time.time()
    #timePassed = time.time() - loopStartTime #initialize time passed var
    #while(timePassed < 600): #loop for a time limit, 
    #    timePassed = time.time() - loopStartTime
    #    response, conversationHistory = apiCall(conversationHistory)



if __name__ == "__main__":
    app.run(debug=True)




#initialConversation = [{"role": "system", "content": "You are a Gerald the Unclean, a squat man from the dungeons and dragon world of Faerun. Your personality embodies your name."}]

#conversationHistory = initialConversation

#@app.route("/airesponse")

#loopStartTime = time.time()
#timePassed = time.time() - loopStartTime #initialize time passed var
#while(timePassed < 600): #loop for a time limit, 
#    timePassed = time.time() - loopStartTime
#    response, conversationHistory = apiCall(conversationHistory)
