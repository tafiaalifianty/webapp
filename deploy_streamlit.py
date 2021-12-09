# Import Library
import pickle as pkl
import pandas as pd
import streamlit as st

# Load model
model = pkl.load(open('finalized_model.sav', 'rb'))

# Create UI
st.write('# Employee Turnover Prediction Web App')

RandD_true = st.selectbox('RandD_true', (0, 1))
hr_true = st.selectbox('hr_true', (0, 1))
management_true = st.selectbox('management_true', (0, 1))

satisfaction_level = st.number_input('satisfaction_level', 0.5, key = 1)
last_evaluation = st.number_input('last_evaluation', 0.5, key = 2)
number_project = st.number_input('number_project', 1, key = 3)
average_montly_hours = st.number_input('average_montly_hours', 0.5, key = 4)
time_spend_company = st.number_input('time_spend_company', 1, key = 5)
Work_accident = st.number_input('Work_accident', 0, key = 6)
promotion_last_5years = st.number_input('promotion_last_5years', 1, key = 7)

# Save input to DataFrame
dt = pd.DataFrame({'RandD_true':[RandD_true],
                   'hr_true':[hr_true],
                   'management_true':[management_true],
                   'satisfaction_level':[satisfaction_level],
                   'last_evaluation':[last_evaluation],
                   'number_project':[number_project],
                   'average_montly_hours':[average_montly_hours],
                   'time_spend_company':[time_spend_company],
                   'Work_accident':[Work_accident],
                   'promotion_last_5years':[promotion_last_5years]})

st.write(dt)

# Prediction
output_pred = model.predict(dt)

# Display Result
st.write('# Hasil Prediksi :', output_pred[0])