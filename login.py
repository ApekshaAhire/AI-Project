import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="AI Stroke Prediction using EMG Signals",
    page_icon="🌐",
    layout="centered",
)
 
# Custom CSS for appealing dark theme
dark_cyber_css = """
    <style>
        body {
            background-color: #121212;
            color: #ffffff;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
            font-family: 'Arial', sans-serif;
        }
        .login-container {
            background-color: #1f1f1f;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            width: 400px;
        }
        .stTextInput {
            background-color: #37474F;
            color: #ffffff;
            border: 1px solid #03DAC6;
            border-radius: 5px;
            padding: 10px;
            margin-bottom: 15px;
        }
        .stTextInput:hover {
            border: 1px solid #03DAC6;
        }
        .stButton {
            background-color: #03DAC6;
            color: #ffffff;
            border: 2px solid #03DAC6;
            border-radius: 5px;
            padding: 10px;
            cursor: pointer;
        }
        .sponsor-line {
            text-align: center;
            margin-top: 20px;
            color: #03DAC6;
        }
    </style>
"""

# Apply custom CSS
st.markdown(dark_cyber_css, unsafe_allow_html=True)

# Create login form
st.title("AI Stroke Prediction using EMG Signals")

with st.form(key='login_form', clear_on_submit=True):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    login_button = st.form_submit_button("Login")

# Check login credentials
if login_button:
    if username == "admin" and password == "1234":
        st.success("Login Successful! Welcome to AI Stroke Prediction using EMG Signals.")
        st.markdown("[Go to Dashboard](streamlit_app)")
    else:
        st.error("Invalid username or password. Please try again.")

# Sponsor line
st.markdown("<div class='sponsor-line'>Project Sponsored By D-Soft Technology</div>", unsafe_allow_html=True)
