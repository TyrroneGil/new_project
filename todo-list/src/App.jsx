import { useState,useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
const [message,setMessage] = useState('')
const [username,setUsername] = useState('')
const [password,setPassword] = useState('')

 async function sendData(){
    const response = await fetch('http://localhost:8000/addUser',{
      method:"POST",
      headers:{
        "Content-Type":"application/json"
      },
      body:JSON.stringify({
        "username":username,
        "password":password
      })
    })
    const result = await response.json();
    console.log(result)
  }



  return (
    <>
      <form action="">
        <input onChange={(e)=>{setUsername(e.target.value)}} type="text" />
        <input onChange={(e)=>{setPassword(e.target.value)}} type="text" />
        <button onClick={()=>{sendData()}}>submit</button>
      </form>
    </>
  )
}

export default App
