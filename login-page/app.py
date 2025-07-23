import streamlit as st

st.title("🔐Login Page")

st.subheader("Please login to continue")

user_credentials = {
    "Srikanthpata":"Srikanth123"
}

with st.form("login_form"):
    username = st.text_input("Username",placeholder="Enter username")
    password = st.text_input("Password",type = "password", placeholder="Enter password")
    submitted = st.form_submit_button("Login")
    if submitted:
        if username in user_credentials and user_credentials[username] == password:
            st.success(f"Welcome, {username}!")
            st.balloons()
        else:
            st.error("Ivalid username or password")
