import streamlit as st
import random
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

st.set_page_config(page_title="Email OTP Login", layout="centered")

# --- SESSION STATE ---
if "otp_sent" not in st.session_state:
    st.session_state.otp_sent = False
if "otp_verified" not in st.session_state:
    st.session_state.otp_verified = False
if "generated_otp" not in st.session_state:
    st.session_state.generated_otp = None
if "email" not in st.session_state:
    st.session_state.email = None

# --- Get email credentials from Streamlit secrets ---
EMAIL_ADDRESS = st.secrets["email"]["address"]
EMAIL_PASSWORD = st.secrets["email"]["app_password"]

# Function to send OTP via email
def send_otp(email, otp):
    try:
        msg = MIMEText(f"Your OTP is: {otp}")
        msg["Subject"] = "Your Streamlit App OTP"
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = email

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, email, msg.as_string())
        return True
    except Exception as e:
        st.error(f"Failed to send OTP: {e}")
        return False

st.title("Login with Email OTP")

if not st.session_state.otp_verified:
    email_input = st.text_input("Enter your email")

    if st.button("Send OTP"):
        if email_input:
            otp = str(random.randint(100000, 999999))
            st.session_state.generated_otp = otp
            st.session_state.email = email_input
            if send_otp(email_input, otp):
                st.session_state.otp_sent = True
                st.success(f"OTP sent to {email_input}")
        else:
            st.error("Please enter a valid email")

    if st.session_state.otp_sent:
        otp_input = st.text_input("Enter OTP")
        if st.button("Verify OTP"):
            if otp_input == st.session_state.generated_otp:
                st.session_state.otp_verified = True
                # Log user
                with open("user_log.txt", "a") as f:
                    f.write(f"{st.session_state.email} logged in at {datetime.now()}\n")
                st.success("OTP verified! You are now logged in.")
            else:
                st.error("Incorrect OTP. Try again.")
else:
    st.success(f"Logged in as {st.session_state.email}")
