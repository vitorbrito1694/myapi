# Python's FastAPI Framework with JwtAuth

This sample was created using Python 3.9.0

## Getting started

Create a virtual environment for the project:  
`python -m venv venv`

Then activate the virtual environment:  
`cd venv/scripts/`
`activate`
`cd..`
`cd..`

Now install the dependencies for the project:  
`pip install -r requirements.txt`

Run the API with Uvicorn:  
`uvicorn main:app --reload`

Hit the unprotected endpoint with cURL:  
`curl localhost:8000/unprotected`

Hit the protected endpoint with cURL to get a 403:  
`curl localhost:8000/protected`

Register a user:  
`curl --header "Content-Type: application/json" --request POST --data '{"username": "ian", "password": "secretpassword"}' localhost:8000/register`

Log in and get a token:  
`curl --header "Content-Type: application/json" --request POST --data '{"username": "ian", "password": "secretpassword"}' localhost:8000/login`

Then use that token as an auth header to get a valid response from the protected endpoint:  
`curl --header "Authorization: Bearer <TOKEN>" localhost:8000/protected`
