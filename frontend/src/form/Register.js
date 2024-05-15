import React, { useState } from "react";
import { Link } from "react-router-dom";
export default function Register(props) {

    const [formRegister, setFormRegister] = useState({
        email: "",
        firstName: "",
        lastName: "",
        password: "",
    });

    return (
        <React.Fragment>
            <div>
                <h1 className="text-3xl font-bold text-center mb-4 cursor-pointer">
                    Create an Account
                </h1>
                <p className="w-80 text-center text-sm mb-8 font-semibold text-gray-700 tracking-wide cursor-pointer mx-auto">
                    Welcome to the Discussion Board
                </p>
            </div>
            <form>
                <div className="space-y-4">
                    <input type="text" placeholder="Email" className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-yellow-400"></input>
                    <input type="text" placeholder="First Name" className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-yellow-400"></input>
                    <input type="text" placeholder="Last Name" className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-yellow-400"></input>
                    <input type="password" placeholder="Password" className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-yellow-400"></input>
                </div>
                <div className="text-center mt-6">
                    <button type="submit" className="py-3 w-64 text-x1 text-white bg-yellow-400 rounded-2xl hover:bg-yellow-300 active:bg-yellow-500 outline-none">Create Account</button>
                    <p className="mt-4 text-sm">
                        Already have an account? {" "}
                        <Link to="/?login" onClick={()=>{props.setpage("login")}}><span className="underline cursor-pointer">Sign In</span></Link>
                    </p>
                </div>
            </form>
        </React.Fragment>
    );
    }