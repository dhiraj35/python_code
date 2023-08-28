import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from routes.api import router as api_router
import os
from dotenv import load_dotenv

# Server Settings
load_dotenv()
host = os.getenv('HOST')
port = os.getenv('PORT')

# # Server Settings
# host = "192.168.40.170"
# port = "3013"

app = FastAPI()
# origins = ["http://"+host+":"+port]
origins = ["http://"+str(host)+":"+str(port)]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

if __name__ == '__main__':
    uvicorn.run("main:app", host=host, port=int(port), log_level="info", reload=True)
    print("running")
