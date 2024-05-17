import React, { useEffect, useState } from "react";
import axios from "axios";
import queryString from "query-string";
import { toast } from "react-toastify";

export default function Logout() {
    const [user, setUser] = useState({});

    useEffect(() => {
        const auth_token = localStorage.getItem("token");
        const token_type = localStorage.getItem("token_type");
        const token = token_type + " " + auth_token;

        const data = queryString.stringify({});

        axios({
            method: 'get',
            url: "http://localhost:8000/users/",
            headers: {
                'Authorization': token,
                'Content-Type': 'application/x-www-form-urlencoded' // Set Content-Type to form-urlencoded
            },
            data: data // Attach the serialized data
        })
            .then((response) => {
                console.log(response)
                setUser(response.data.User)
            })
            .catch((error) => {
                console.log(error)
            });
    }, []);


    const onClickHandler = (event) => {
        event.preventDefault();
        localStorage.removeItem("token");
        localStorage.removeItem("token_type");

        toast.success("Logout successful", {
            position: "top-right",
            autoClose: 5000,
            hideProgressBar: false,
            closeOnClick: true,
            pauseOnHover: true,
            draggable: true,
            progress: undefined
        });

        setTimeout(() => {
            window.location.reload()
        }, 1500)
    }

    return (
        <div className="bg-gray-200 font-sans h-screen w-full flex flex-row justify-center items-center">
            <div className="card w-65 mx-auto bg-white shadow-xl hover:shadow">
                <div className="text-center mt-2 text-3xl font-medium">{user.name}</div>
                <div className="text-center mt-2 font-light text-sm">{user.email}</div>
                <hr className="mt-3" />
                <div className="flex p-2">
                    <div className="w-full text-center">
                        <button 
                        onClick={(event) =>{
                            onClickHandler(event)
                        }}
                        className="py-3 w-64 text-xl text-black outline-none bg-gray-50 hover:bg-gray-100 active:bg-gray-200">
                            Log out
                        </button>
                    </div>
                </div>
            </div>
        </div>
    )
}