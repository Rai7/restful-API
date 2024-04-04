import streamlit as st
import requests
from pydantic import BaseModel

class TitanicData(BaseModel):
    passanger_class: int
    gender: str
    age: float
    sibling_spouse: int
    parent_children: int
    fare: float

# Define FastAPI endpoint URL
base_url = "http://localhost:8000"

def titanic_predict(data: TitanicData):
    response = requests.post(f"{base_url}/titanic", json=data.dict())
    return response.json()

def main():
    st.title("Titanic Survival Prediction")
    
    # User input fields
    passanger_class = st.selectbox("Passenger class", [1, 2, 3])
    gender = st.radio("Gender", ["male", "female"])
    age = st.number_input("Age", value=30.0)
    sibling_spouse = st.number_input("Number of siblings/spouses aboard", value=0)
    parent_children = st.number_input("Number of parents/children aboard", value=0)
    fare = st.number_input("Fare", value=10.0)
    
    # Make prediction when user clicks the button
    if st.button("Predict"):
        data = TitanicData(
            passanger_class=passanger_class,
            gender=gender,
            age=age,
            sibling_spouse=sibling_spouse,
            parent_children=parent_children,
            fare=fare
        )
        prediction = titanic_predict(data)
        st.write("Prediction Result:")
        st.write(prediction)

if __name__ == "__main__":
    main()
