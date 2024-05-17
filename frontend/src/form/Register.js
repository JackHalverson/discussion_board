import React, { useState } from "react";
import { Link } from "react-router-dom";
import axios from "axios";
import { toast } from "react-toastify";

export default function Register(props) {

    const [formRegister, setFormRegister] = useState({
        email: "",
        name: "",
        password: "",
    });

    const onChangeForm = (label, event) => {
        switch (label) {
            case "email":
                const email_validation = /\S+@\S+\+.\S+/
                if (email_validation.test(event.target.value) === false) {
                    setFormRegister({ ...formRegister, email: event.target.value });
                }
                break;
            case "name":
                setFormRegister({ ...formRegister, name: event.target.value });
                break;
            case "password":
                setFormRegister({ ...formRegister, password: event.target.value });
                break;
            default:
                break;
        }}

        const onSubmitHandler = async (event) => {
        event.preventDefault();
        console.log(formRegister);

        await axios.post("http://localhost:8000/auth/", formRegister)
        .then((response) => {

            toast.success("Account created successfully")

            setTimeout(() => {
                window.location.reload()
            }, 1000)

            console.log(response)
        })
        .catch((error) => {

            toast.error("Account creation failed")

            console.log(error)
        })
        };

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
                <form onSubmit={onSubmitHandler}>
                    <div className="space-y-4">
                        <input
                            type="text"
                            placeholder="Email"
                            className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-yellow-400"
                            onChange={(event) =>
                                onChangeForm("email", event)
                            }
                        />
                        <input
                            type="text"
                            placeholder="Full Name"
                            className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-yellow-400"
                            onChange={(event) =>
                                onChangeForm("name", event)
                            }
                        />
                        <input
                            type="password"
                            placeholder="Password"
                            className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-yellow-400"
                            onChange={(event) =>
                                onChangeForm("password", event)
                            }
                        />
                    </div>
                    <div className="text-center mt-6">
                        <button type="submit" className="py-3 w-64 text-x1 text-white bg-yellow-400 rounded-2xl hover:bg-yellow-300 active:bg-yellow-500 outline-none">Create Account</button>
                        <p className="mt-4 text-sm">
                            Already have an account? {" "}
                            <Link to="/?login" onClick={() => { props.setpage("login") }}><span className="underline cursor-pointer">Sign In</span></Link>
                        </p>
                    </div>
                </form>
            </React.Fragment>
        );
    }