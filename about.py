import streamlit as st
def app():
    st.markdown("""
    <style>
    .main {
        background-color: #F0F0F0; /* Light Gray Background */
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center';> About Pavement Assessment Application</h1>",unsafe_allow_html=True)
    st.header("Introduction")
    st.write("""
    Welcome to the Pavement Assessment Application. This tool is designed to help users assess the condition of pavements using machine learning techniques, this application aims to identify and categorize pavement conditions as satisfactory or very poor.
    """)
    st.header("Features")
    st.write("""
    - **Image Uploading**: Users can upload images of pavements to get an assessment about that pavement.
    - **Condition Classification**: The application classifies the pavement condition as either satisfactory or very poor.
    - **Automated Alerts**: Based on pavement condition, the system can notify the nearest worker for inspection and maintenance in case of poor condition.
    """)
    st.header("Contact Us")
    st.write("""
    If you have any questions, feedback, or need support, please contact us at:
    - Email: support@pavementassessment.com
    - Phone: +1 800 123 4567
    """)