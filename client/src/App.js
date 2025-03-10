import React, { useState, useEffect } from 'react'

function App() {

    const [data, setData] = useState([{}])

    const [userInput, setUserInput] = useState('') //state for containing user input from text field

    const [aiResponse, setAiResponse] = useState('')//state for containing response from apiLoop

    const handleInputChange = (event) => { //event handler for the text field to keep userinput updated
      setUserInput(event.target.value)
    }

    const handleSubmit = async (event) => {
      event.preventDefault()
    
    
    try {
      const response = await fetch("apiLoop", {
         method: "POST",
         headers: {
          "Content-Type": "application/json",
         },
         body: JSON.stringify({ input: userInput}),
      })

      const data = await response.json()

      setAiResponse(data.response)
    } catch (error) {
      console.error("Error sending request:", error)
    }
    }
  


    return (
      <div>
      <h1>Ask a Question:</h1> {/*header*/}

      <input 
        type="text"
        value={userInput}
        onChange={handleInputChange}//call the event handler text updates
        placeholder="Enter ye input here..."
      /> {/*text field*/}

      <button onClick={handleSubmit}>Speak ye words</button>{/*button calls event handler for sending current text field to the api */}

      {/**display the response from apicaller */}
      {aiResponse && ( //check that aiResponse is defined-do not display if undefined
        <div>
          <h2>NPC Response:</h2>
          <p>{aiResponse}</p>
        </div>
      )}
    </div>
    )
}

export default App
