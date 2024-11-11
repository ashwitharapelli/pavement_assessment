import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

cred=credentials.Certificate('pavement-assessment-59584f9f464d.json')
#if not firebase_admin._apps:
   # firebase_admin.initialize_app(cred)



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
    input[type="text"], input[type="email"], input[type="number"], input[type="location"], input[type="image"],input[type="password"] {
        color: #333;
        background-color: #ffffff !important; /* White background */
        border: 2px solid #ccc;
        border-radius: 5px;
        padding: 10px;
        width: 700px;
        font-size: 18px;
    }

   

    /* Area input (multiline text) */
    textarea {
        color: #333;
        background-color: #ffffff !important; /* White background */
        border: 2px solid #ccc;
        border-radius: 5px;
        padding: 10px;
        width: 700px;
        font-size: 18px;
        height: 150px;
    }
    </style>
    """
    st.header(':violet[Account Details]')
    st.markdown(custom_css, unsafe_allow_html=True)
    if 'username' not in st.session_state:
        st.session_state.username=''
    if 'useremail' not in st.session_state:
        st.session_state.useremail=''  
    
    def f():
        try:
            user=auth.get_user_by_email(email)
            #print(user.uid)
            st.write('Login Successful')
            st.balloons()
            st.session_state.username=user.uid
            st.session_state.useremail=user.email

            st.session_state.signedout=True
            st.session_state.signout=True

        except:
            st.warning('Login Failed')

    def t():
        st.session_state.signout=False
        st.session_state.signedout=False
        st.session_state.username=''

    if 'signedout' not in st.session_state:
        st.session_state.signedout=False
    if 'signout' not in st.session_state:
        st.session_state.signout=False
    
    if not st.session_state['signedout']:
        choice=st.selectbox('Login/Signup',['Login','Signup'],key='account_selectbox')

        if choice=='Login':
            email=st.text_input('Email Address')
            password=st.text_input('Password',type='password')
            st.button('Login',on_click=f)
        else:
            email=st.text_input('Email Address')
            password=st.text_input('Password',type='password')
            username=st.text_input('Enter your unique username')
            if st.button('Create my account') :
                user=auth.create_user(email=email,password=password,uid=username)

                st.success('Account created successfully')
                st.markdown('Please Login using your email and password')
                st.balloons()

    if st.session_state.signout:
        st.text('Name: '+st.session_state.username)
        st.text('Email id: '+st.session_state.useremail)
        st.button('Sign out',on_click=t)
        st.write("Please go to the home page for uploading image.")
