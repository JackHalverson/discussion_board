import React, { useEffect, useState } from "react";
import queryString from "query-string";
import axios from "axios";
import { toast } from "react-toastify";

const Sidebar = ({ groups, onGroupClick }) => {
    return (
        <div className="flex flex-col h-screen w-64 bg-slate-500 text-gray-100">
            {/* Sidebar Header */}
            <div className="flex items-center justify-center h-16 bg-slate-700">
                <h1 className="text-white font-semibold">Discussion Board</h1>
            </div>

            {/* Sidebar Content */}
            <div className="flex-1 p-4 overflow-y-auto">
                <ul className="space-y-2">
                    {groups.map((group) => (
                        <li key={group.id} className="hover:bg-slate-600 rounded-md px-4 py-2 cursor-pointer" onClick={() => onGroupClick(group.id)}>
                            {group.name}
                        </li>
                    ))}
                </ul>
            </div>

            {/* Sidebar Footer */}
            <div className="flex items-center justify-center h-16 bg-slate-700">
                <p className="text-sm text-gray-300">&copy; 2024 Jackson Halverson</p>
            </div>
        </div>
    );
};

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
};

const MainContent = ({ topics, onDeleteTopic}) => {
    return (
        <div className="flex-1">
            <div className="p-8">
                <div className="flex justify-between items-center mb-4">
                    <h1 className="text-2xl font-semibold">Topics</h1>
                    <button 
                        onClick={(event) =>{
                            onClickHandler(event)
                        }} className="text-gray-500 hover:text-red-600">Logout</button>
                </div>
                <ul className="space-y-4 mt-4">
                    {topics.map((topic) => (
                        <li key={topic.id} className="relative pr-16 bg-white shadow-xl hover:shadow py-4 px-4 flex items-start justify-between">
                            <div>
                                <h2 className="text-xl font-semibold">{topic.title}</h2>
                                <hr className="mt-3" />
                                <p className="text-gray-600">{topic.description}</p>
                            </div>
                            <button className="absolute px-2 top-0 right-0 bottom-0 bg-white text-gray-400 hover:bg-red-600 hover:text-white" onClick={() => onDeleteTopic(topic.id)}>Delete</button>
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    );
};

const Home = () => {
    const [groups, setGroups] = useState([]);
    const [selectedGroupId, setSelectedGroupId] = useState(null);
    const [topics, setTopics] = useState([]);
    const [user, setUser] = useState({});

    useEffect(() => {
        // Fetch groups from backend when component mounts
        axios.get("http://localhost:8000/groups/")
            .then((response) => {
                setGroups(response.data);
            })
            .catch((error) => {
                console.error("Error fetching groups:", error);
            });
    }, []);

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

    const fetchTopics = (groupId) => {
        axios.get(`http://localhost:8000/topics/${groupId}/`)
            .then((response) => {
                setTopics(response.data);
            })
            .catch((error) => {
                console.error("Error fetching topics:", error);
            });
    };

    const onDeleteTopic = (topicId) => {
        axios.delete(`http://localhost:8000/topics/${topicId}`)
            .then(() => {
                toast.success("Topic deleted successfully");
                setTopics(topics.filter(topic => topic.id !== topicId));
                console.log("Topic deleted successfully");

            })
            .catch((error) => {
                console.error("Error deleting topic:", error);
            });
    };

    useEffect(() => {
        if (selectedGroupId !== null) {
            fetchTopics(selectedGroupId);
        }
    }, [selectedGroupId]);

    return (
        <div className="flex h-screen bg-gray-200">
            {/* Sidebar */}
            <Sidebar groups={groups} onGroupClick={setSelectedGroupId} />

            {/* Main Content */}
            <MainContent topics={topics} onDeleteTopic={onDeleteTopic} />
        </div>
    );
};

export default Home;
