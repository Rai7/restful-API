from fastapi import FastAPI, Request, Form, Query, HTTPException
from pydantic import BaseModel
import pickle
import pandas as pd

# init
app = FastAPI()

# open model
def open_model(model_path):
    """Helper function for loading model"""
    with open(model_path, "rb") as model_file:
        model = pickle.load(model_file)
    return model
 
model_titanic = open_model("/Users/rairamones/Desktop/back_end/titanic_pipa.pkl") 

class TitanicData(BaseModel):
    passanger_class: int = Query(..., description="Passenger class (1, 2, or 3)")
    gender: str = Query(..., description="Gender of the passenger ('male' or 'female')")
    age: float = Query(..., description="Age of the passenger")
    sibling_spouse: int = Query(..., description="Number of siblings/spouses aboard")
    parent_children: int = Query(..., description="Number of parents/children aboard")
    fare: float = Query(..., description="Fare paid by the passenger")

def titanic_inference(data):
    """Input: list with length 6 ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']
    Output: predicted class (index, label)"""
    LABEL = ["Not Survived", "Survived"]
    columns = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']
    data = pd.DataFrame([data], columns=columns)
    res = model_titanic.predict(data)
    return res[0], LABEL[res[0]]

@app.get("/")
async def home():
    return {"message": "Hello from FastAPI!!"}


@app.post("/titanic")
async def titanic_predict(data: TitanicData):
    new_data = [
        data.passanger_class, data.gender, data.age, data.sibling_spouse,
        data.parent_children, data.fare
    ]
    idx, label = titanic_inference(new_data)
    return {"result": str(idx), "label_name": label}
