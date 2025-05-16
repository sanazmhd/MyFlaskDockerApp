import React, {useState, useEffect} from 'react';


function App() {
  const [message, setMessage] =useState('');
 useEffect(() => {
    fetch('http://localhost:5000/api/hello')
      .then(res => res.json())
      .then(data => setMessage(data.message));
  },[]);
return (
  <div> 
   <h1>This is Sanaz React</h1>
   <p>{message}</p>
  </div>
);
}

export default App;