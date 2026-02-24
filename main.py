'''
This is a simple rule based chatbot that uses basic python functions, FastAPI and HTML frontend
1. Creating the rule base as a json dict
2. Accept and convert the user input query to lowercase (since all the text in the rule base are in lowercase)
3. If the query is in the rule base, return the response. Else return failure message
'''

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from routers.chat import chat_router

app = FastAPI(title="Let's talk to SimChat")

#CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Allow all origins (for development)
    allow_methods=["*"],   # Allow all HTTP methods (POST, GET, etc.)
    allow_headers=["*"],   # Allow all headers
)

app.include_router(chat_router)

