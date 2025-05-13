from fastapi import FastAPI

# Create an instance of the FastAPI application
app = FastAPI()

# Root route: returns a simple Hello World message
@app.get('/')
def hello():
    return {"message": "Hello World!"}

# About route: returns info about CampusX
@app.get('/about')
def about():
    return {"message": "CampusX is an educational platform"}