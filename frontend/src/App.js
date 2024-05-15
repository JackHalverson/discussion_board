import './App.css';
import React, {useState} from 'react';
import Login from './form/Login';
import Register from './form/Register';

function App() {
  const[page, setpage] = useState('login');

  const selectPage = () => {
    if(page === 'login') {
      return <Login setpage={setpage}/>
    } 
    if(page === 'register') {
      return <Register setpage={setpage}/>
    }
  }

  return (
    <div className='min-h-screen bg-slate-600 flex justify-center items-center'>
      <div className="py-12 px-12 bg-white rounded-2xl shadow-2xl z-20">
        {selectPage()}
      </div>
    </div>
  );
}

export default App;
