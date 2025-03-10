import React, { useState, useEffect } from 'react'

function App() {

    const [data, setData] = useState([{}])

    useEffect(() => {
      fetch("/apiLoop").then(
          res => res.json()
        ).then(
          data => {
            setData(data)
            console.log(data)
        }
      )
    }, [])

    return (
      <div>
      <h1>AI Response:</h1>
      <p>{data.response}</p>  
    </div>
    )
}

export default App
