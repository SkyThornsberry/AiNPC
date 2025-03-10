from flask import Flask, jsonify, request
import time
import sys
sys.path.append('../')
from apiCaller import apiCall

app = Flask(__name__)

@app.route("/apiLoop", methods=["POST"]) #allow post methods
def apiLoop():
    
    user_input = request.json.get('input','')#get the user input

    if user_input:#dont run if user_input is undefined
        initialConversation = [{"role": "system", "content": "You are a Gerald the Unclean, a squat man from the dungeons and dragon world of Faerun. Your personality embodies your name."}]
        conversationHistory = initialConversation
        response, conversationHistory = apiCall(conversationHistory)
        
        return(jsonify({"response": str(response)}))
        #loopStartTime = time.time()
        #timePassed = time.time() - loopStartTime #initialize time passed var
        #while(timePassed < 600): #loop for a time limit, 
        #    timePassed = time.time() - loopStartTime
        #    response, conversationHistory = apiCall(conversationHistory)

    return jsonify({"response": "No input received."})#only hit this return when if loop is not entered


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
