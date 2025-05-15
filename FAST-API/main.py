from fastapi import FastAPI
import json

# Create an instance of the FastAPI application
app = FastAPI()


def load_data():
    with open("patients.json" , 'r') as f:
        data = json.load(f)

    return data

# Root route: returns a simple Hello World message
@app.get('/')
def hello():
    return {"message": "Patient Management System API"}

# About route: returns info about CampusX
@app.get('/about')
def about():
    return {"message": "A fully functional API to manage your patient records"}


@app.get('/view')
def view():
    data = load_data()

    return data
