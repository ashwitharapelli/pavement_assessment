import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore

if not firebase_admin._apps:
    cred = credentials.Certificate("admin-details-436e6-f280b2f13b03.json")
    firebase_admin.initialize_app(cred)
db = firestore.client()



def add_employee(name, age, location, phone_no):
    doc_ref = db.collection("employees").document()
    doc_ref.set({
        "name": name,
        "age": age,
        "location": location,
        "phone_no": phone_no
    })

# Function to retrieve employee details from Firestore
def get_employees():
    employees_ref = db.collection("employees")
    docs = employees_ref.stream()
    employees = []
    for doc in docs:
        employees.append(doc.to_dict())
    return employees

# Simulated admin credentials
# Function to check login credentials
def check_login(username, password,ADMINS):
    return username in ADMINS and ADMINS[username] == password

    # Function to handle logout
def logout():
    st.session_state.logged_in = False
# Function for login/signup form

def login_signup_form(ADMINS,check_login):
    st.header("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
        
    if st.button("Login"):
        if check_login(username, password,ADMINS):
            st.session_state.logged_in = True
            st.success("Logged in successfully!")
        else:
            st.error("Invalid username or password")

    st.header("Signup")
    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type="password")
        
    if st.button("Signup"):
        if new_username in ADMINS:
            st.error("Username already exists!")
        else:
            ADMINS[new_username] = new_password
            st.success("Signup successful! Please login.")
 


def app():
    ADMINS = {
        "admin": "password"
    }

    # Store employee details
    if "employees" not in st.session_state:
        st.session_state.employees = []


    # Streamlit app
    st.title("Admin Panel")

        # Tabs for navigation
    tabs = st.tabs(["Login/Signup", "Enter Employee Details", "Employee Details"])

        # Login/Signup Tab
    with tabs[0]:
        if "logged_in" not in st.session_state:
            st.session_state.logged_in = False

        if st.session_state.logged_in:
            st.write("Logged in as Admin")
            st.button("Logout", on_click=logout)
        else:
            st.sidebar.write("Please login or sign up to access the admin panel")
            login_signup_form(ADMINS,check_login)

        # Enter Employee Details Tab
    with tabs[1]:
        if st.session_state.logged_in:
            st.header("Enter Employee Details")
            with st.form(key='employee_form'):
                name = st.text_input("Name")
                age = st.number_input("Age", min_value=18, max_value=100, step=1)
                location = st.text_input("Location")
                phone_no = st.text_input("Phone no")
                submitted = st.form_submit_button("Submit")

                if submitted:
                    add_employee(name, age, location, phone_no)
                    st.success("Employee details submitted successfully!")
        else:
            st.warning("Please login to enter employee details")

        # Employee Details Tab
    with tabs[2]:
        if st.session_state.logged_in:
            st.header("Employee Details")
            employees = get_employees()
            if employees:
                for idx, employee in enumerate(employees):
                    st.subheader(f"Employee {idx + 1}")
                    st.write(f"Name: {employee['name']}")
                    st.write(f"Age: {employee['age']}")
                    st.write(f"Location: {employee['location']}")
                    st.write(f"Phone no: {employee['phone_no']}")
                    st.write("---")
            else:
                st.write("No employee details available.")
        else:
            st.warning("Please login to view employee details")



if __name__ == "__main__":
    app()
