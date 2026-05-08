# import Libraries
import pickle 
import streamlit as st
import numpy as np


st.title("Flower Classification App")

with open("best_model.pkl", "rb") as f:
    lr_model = pickle.load(f)

sl = st.number_input("insert a sepal length")
sw = st.number_input("insert a sepal width")  
pl = st.number_input("insert a petal length") 
pw = st.number_input("insert a petal width") 

if st.button("predict"):
    pred = lr_model.predict(np.array([sl,sw,pl,pw]))
    st.write("the flower is:",pred[0])
