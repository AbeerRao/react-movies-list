import React, { useEffect, useState } from 'react';
import './App.css';

function App() {

  const [data, setData] = useState({})
  const [urls, setUrls] = useState([])

  useEffect(() => {
    fetch('/movies').then(
      response => response.json()
    ).then(
      data => setData(data)
    )
  }, [])

  useEffect(() => {
    if (data) {
      [data].map((url) => (
        // url.url.forEach((u) => {
        //   console.log(u)
        // })
        setUrls(url.url)
      ))
    }
  })

  // [data].map((d) => {
  //   console.log("test")
  // })

  return (
    <div className="App">
      {[urls].map((url) => (
        <p>{url}</p>
      ))}
    </div>
  );
}

export default App;
