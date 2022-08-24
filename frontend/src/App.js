import './App.css';
import {useState, useEffect} from 'react';

function App() {

  const [numbers, setNumbers] = useState([])

  useEffect(() => {
    fetch('http://127.0.0.1:5000/get',{
      'methods' : 'GET',
      headers: {
        'Content-Type':'applications/json'
      }
    })
    .then(resp => resp.json())
    .then(resp => setNumbers(resp))
    .then(error => console.log(error))
  }, [])

  return (
    <div className="App">
      <h1>Flask and ReactJS </h1>

      {numbers.map(number => {
        <div>
          <h2>{number.id}</h2>
        </div>
      })}

    </div>
  );
}

export default App;
