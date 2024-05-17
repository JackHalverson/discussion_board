import './App.css';
import React, { useEffect, useState } from 'react';
import Login from './form/Login';
import Register from './form/Register';
import Home from './Home';
import Logout from './form/Logout';

function App() {
  const [page, setpage] = useState('login')
  const [token, setToken] = useState()

  useEffect(() => {
    const auth = localStorage.getItem("token")
    setToken(auth)
  }, [token])

  const selectPage = () => {
    if (page === 'login') {
      return <Login setpage={setpage} />
    }
    if (page === 'register') {
      return <Register setpage={setpage} />
    }
  }

  const pages = () => {
    if (token == null) {
      return <div className='min-h-screen bg-slate-600 flex justify-center items-center'>
        <div className="py-12 px-12 bg-white rounded-2xl shadow-2xl z-20">
          {selectPage()}
        </div>
      </div>
    } else {
      return <Home />
    }
  }

  return <React.Fragment>{pages()}</React.Fragment>
}

export default App;
