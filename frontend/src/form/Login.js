import React, {useState} from "react";
import { Link } from "react-router-dom";
import axios from "axios";
import queryString from 'query-string';
import {toast} from 'react-toastify';

export default function Login(props) {

    const [loginForm, setLoginform] = useState({
        username: "",
        password: "",
    });

    const onChangeForm = (label,event) => {
        switch(label) {
            case "username":
                setLoginform({...loginForm, username: event.target.value});
                break;
            case "password":
                setLoginform({...loginForm, password: event.target.value});
                break;
        }
    };
    
    const onSubmitHandler = async (event) => {
    event.preventDefault();

    const formData = {
        username: loginForm.username,
        password: loginForm.password
    };

    try {
        const response = await axios.post(
            "http://localhost:8000/auth/token",
            queryString.stringify(formData), // Serialize data to x-www-form-urlencoded format
            {
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded' // Set the Content-Type header
                }
            }
        );
        console.log(response.data);
        localStorage.setItem("token", response.data.access_token);
        localStorage.setItem("token_type", response.data.token_type);

        toast.success("Login successful");

        setTimeout(() => {
            window.location.reload()
        }, 1000)

    } catch (error) {
        console.error("Login error:", error.response.data);
        toast.error(error.response.data.detail);
    }
};

    return (
        <React.Fragment>
            <div>
                <h1 className="text-3xl font-bold text-center mb-4 cursor-pointer">
                    Welcome to the Discussion Board
                </h1>
                <p className="w-80 text-center text-sm mb-8 font-semibold text-gray-700 tracking-wide cursor-pointer mx-auto">
                    Please login to continue
                </p>
            </div>
            <form onSubmit={onSubmitHandler}>
                <div className="space-y-4">
                    <input 
                    type="text" 
                    placeholder="Email" 
                    className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-yellow-400"
                    onChange={(event)=>{
                        onChangeForm("username",event);
                    }}>
                    </input>
                    <input 
                    type="password" 
                    placeholder="Password" 
                    className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-yellow-400"
                    onChange={(event)=>{
                        onChangeForm("password",event);
                    }}>
                    </input>
                </div>
                <div className="text-center mt-6">
                    <button type="submit" className="py-3 w-64 text-x1 text-white bg-yellow-400 rounded-2xl hover:bg-yellow-300 active:bg-yellow-500 outline-none">Sign In</button>
                    <p className="mt-4 text-sm">Don't have an account? {" "}
                    <Link to="/?register" onClick={()=>{props.setpage("register")}}><span className="underline cursor-pointer">Register</span></Link>{" "}
                    </p>
                </div>
            </form>
        </React.Fragment>
    );
    }