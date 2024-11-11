import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model
from twilio.rest import Client
import streamlit as st
import numpy as np
import firebase_admin
from firebase_admin import credentials,firestore

if not firebase_admin._apps:
    cred = credentials.Certificate("admin-details-436e6-f280b2f13b03.json")
    firebase_admin.initialize_app(cred)
db = firestore.client()

def get_phone_by_location(location):
    employees_ref = db.collection("employees").where("location", "==", location).limit(1)
    docs = employees_ref.stream()
    for doc in docs:
        data = doc.to_dict()
        if "phone_no" in data:
            return data["phone_no"]
    return None

# Function to send SMS using Twilio
def send_sms(to, message):
    account_sid = 'sid'  #type your account sid in place of sid
    auth_token = 'your_token' #type your auth_token in place of your_token
    client = Client(account_sid, auth_token)

    message = client.messages.create(
            body=message,
            from_='+17068628864',
            to=to
    )



def app():
    st.markdown("""
    <style>
    .main {
        background-color: #F0F0F0; /* Light Gray Background */
    }
    </style>
    """, unsafe_allow_html=True)
    custom_css = """
        <style>
        /* Text input */
        input[type="text"], input[type="email"], input[type="number"], input[type="location"], input[type="image"] {
            color: #333;
            background-color: #ffffff !important; /* White background */
            border: 2px solid #ccc;
            border-radius: 5px;
            padding: 10px;
            width: 700px;
            font-size: 16px;
        }

        /* Password input */
        input[type="password"] {
            color: #333;
            background-color: #ffffff !important;
            border: 2px solid #ccc;
            border-radius: 5px;
            padding: 10px;
            width: 700px;
            font-size: 16px;
        }

        /* Area input (multiline text) */
        textarea {
            color: #333;
            background-color: #ffffff !important;
            border: 2px solid #ccc;
            border-radius: 5px;
            padding: 10px;
            width: 700px;
            font-size: 16px;
            height: 150px;
        }
        </style>
        """
    st.title('Welcome to :violet[Pavement Assessment]')

    if 'username' not in st.session_state:
        st.session_state.username = ''


    st.markdown(custom_css, unsafe_allow_html=True)
    model=load_model(r'C:\Users\ACER\OneDrive\Desktop\AshwiCst\Image_Classification\Image_classify (1).keras')

    data_cat=['satisfactory','very_poor']
    img_height=180
    img_width=180   
    ph=''
    if st.session_state.username=='':
        ph='Login to be able to post!!'
    else:
        ph='Post your image'
    image=st.text_input('Enter Image')
    if ph=='Post your image':
        #st.header('Welcome  to :violet[Pavement Assessment]')
        #image=st.text_input('Enter Image')
        if image:
            try:
                image_load=tf.keras.utils.load_img(image,target_size=(img_height,img_width))
                img_arr=tf.keras.utils.array_to_img(image_load)
                img_bat=tf.expand_dims(img_arr,0)

                predict=model.predict(img_bat)

                score=tf.nn.softmax(predict)
                st.image(image,width=200)

                        
                        
                if data_cat[np.argmax(score)]=='very_poor':
                    st.write("Damage detected.")
                    pavement_street=st.text_input('Enter location',key='image_area')
                    pavement_location=st.text_input('Enter area',key='image_location')
                    if pavement_location and pavement_street:
                        phone_number = get_phone_by_location(pavement_location)
                        if phone_number:   
                            message = f"Pavement Damage detected at location - {pavement_street} , {pavement_location}. Please inspect."
                            send_sms(phone_number, message)
                            st.write(f"Message sent to respected authorities.")
                        else:
                            st.write("No worker found.")
                else:
                    st.write("No significant damage detected.")
                    
            except FileNotFoundError:
                st.error("The specified image file was not found. Please check the file path.")
        else:
            st.write("Please enter an image path to get started.")   
    else:
        st.write('Please login to post') 




