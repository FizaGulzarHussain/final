import numpy as np
import pickle
import streamlit as st
import pandas as pd
dataset=pd.read_csv('final_dataset.csv')

st.markdown("""
  <style>
    /* Adjusting the height of the chatbot */
    .flowise-chatbot {
        height: 400px; /* Increase this value as needed */
    }

    /* Moving the chatbot to the bottom right */
    .flowise-chatbot {
        position: fixed;
        bottom: 5spx;
        right: 10px;
    }
  </style>
""", unsafe_allow_html=True)
def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background: url(https://i.ibb.co/6nRsDh1/133-konicaminolta.jpg);
                background-repeat: no-repeat;
                padding-top: 120px;
                background-position: 20px 20px;
            }
            [data-testid="stSidebarNav"]::before {
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

add_logo()

# loading the saved model
loaded_model = pickle.load(open('Model.pkl','rb'))

# Custom CSS for styling
custom_css = """
    <style>
        .stApp {
            background-color:#F1ECDD; /* Set your desired background color */
            font-family: Arial, sans-serif; /* Set font family */
        }
        .stTextInput>div>div>input {
            background-color: #ffffff; /* Set input field background color */
            color: #D5A413;
            font-size:25px/* Set input field text color */
        }
        .stTextInput>label {
            color: #474644;
            font-weight: bold;
            font-size:25px;
        }
        .stButton>button {
            background-color: #4CAF50; /* Set your desired button background color */
            color: white; /* Set button text color */
            font-weight: bold; /* Make button text bold */
            border-radius: 5px; /* Rounded button corners */
            border: none; /* Remove button border */
            padding: 10px 20px; /* Add padding to button */
        }
    </style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# creating a function for Prediction

def co2_prediction(input_data, c, t):
    user_input = pd.DataFrame([[input_data, c, t]], columns=['Base location', 'Destination', 'Mode of transport'])
    predicted_co2 = loaded_model.predict(user_input)

    # Introduce random noise to the prediction
    noise = np.random.normal(0, 5.48,size=predicted_co2.shape)  # You can adjust the mean and standard deviation as needed
    predicted_co2_with_noise = predicted_co2 + noise

    # Ensure predicted CO2 emission is non-negative
    predicted_co2_with_noise_abs = np.abs(predicted_co2_with_noise)

    print("Predicted CO2 Emission (in Kg):", predicted_co2_with_noise_abs[0])
    return np.round(predicted_co2_with_noise_abs[0], 2)
	  
		
	  
def main():
    st.markdown('<p style="color:#008000; font-size:55px;">Co2 Emission Prediction Web App</p>', unsafe_allow_html=True)
    # giving a title
    # getting the input data from the user
    base_location_options = dataset['Base location'].unique()
    destination_options = dataset['Destination'].unique()
    mode_of_transport_options = dataset['Mode of transport'].unique()

    Base_location = st.selectbox('Base Location', base_location_options)
    Destination = st.selectbox('Destination Location', destination_options)
    Mode_of_transport = st.selectbox('Mode of Transport', mode_of_transport_options)
    # Add the JavaScript code as a string

    
    # code for Prediction
    diagnosis = ''

    # creating a button for Prediction

    if st.button('Co2 (kg) Prediction Result'):
        diagnosis = co2_prediction(Base_location, Destination, Mode_of_transport)
    st.success(diagnosis)

        

    

    
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    