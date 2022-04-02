# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 13:47:42 2022

@author: piyush
"""

import numpy as np
import pickle
import pandas as pd
import xgboost as xgb

import streamlit as st 

#pickle_in = open("Final_RF_Model.pkl","rb")
#model=pickle.load(pickle_in)
model1 = xgb.XGBRegressor()
model1.load_model("final_xg_model.txt")




def predict_car_price(YEAR,KMSDRIVEN,FUELTYPE,MILEAGE,TRANSMISSIONTYPE,SELLERTYPE,ENGINE,SEATS):
    
    prediction=model1.predict([[YEAR,KMSDRIVEN,FUELTYPE,MILEAGE,TRANSMISSIONTYPE,SELLERTYPE,ENGINE,SEATS]])
    print(prediction)
    prediction = np.round(prediction,2)
    return prediction


def main():
    
    st.title("Car Price prediction")
    YEAR=st.slider("Insert Year",2000,2022)
    KMSDRIVEN=st.number_input("Insert Kms Driven")
    FUELTYPE = st.selectbox("Insert Fuel Type",("Diesel","Petrol","CNG","lPG","Electric"),key="1")
    MILEAGE=st.number_input("Insert Mileage")
    TRANSMISSIONTYPE=st.selectbox("Insert Transmission Type",("Manual","Automatic"),key="2")
    SELLERTYPE=st.selectbox("Insert Seller Type",("Dealer","Individual","Trustmark Dealer"),key="3")
    ENGINE=st.number_input("Insert Engine")
    SEATS=st.number_input("Insert Seats")
    
    if FUELTYPE == "Diesel":
        FUELTYPE = 0
    elif FUELTYPE == "Petrol":
       FUELTYPE = 1
    elif FUELTYPE == "CNG":  
        FUELTYPE = 2
    elif FUELTYPE == "lPG":  
        FUELTYPE = 3
    elif FUELTYPE == "Electric":  
        FUELTYPE = 4
        
    if TRANSMISSIONTYPE == "Manual":
        TRANSMISSIONTYPE = 0
    elif TRANSMISSIONTYPE == "Automatic":
       TRANSMISSIONTYPE = 1
       
    if SELLERTYPE == "Dealer":
        SELLERTYPE = 0
    elif SELLERTYPE == "Individual":
       SELLERTYPE = 1
    elif SELLERTYPE == "Trustmark Dealer":  
        SELLERTYPE = 2
        
    result=""
    if st.button("Predict"):
        result=predict_car_price(YEAR,KMSDRIVEN,FUELTYPE,MILEAGE,TRANSMISSIONTYPE,SELLERTYPE,ENGINE,SEATS)
    st.success('The output is {} lakhs'.format(result))
    if st.button("About"):
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
