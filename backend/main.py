from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import auth, user, group, topic, comment

origins = [
    "http://localhost:3000",
]



def create_app():
    app = FastAPI()
    app.include_router(user.router)
    app.include_router(auth.router)
    app.include_router(group.router)
    app.include_router(topic.router)
    app.include_router(comment.router)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app

app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="", port=8000)