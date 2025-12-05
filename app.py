import streamlit as st

st.set_page_config(page_title="User Roles Demo", layout="centered")

# Roles assigned based on email
USER_ROLES = {
    "nabeelms007@gmail.com": "admin",
    "nms236161@gmail.com": "owner",
    "nabeelms1999@outlook.com": "clinic_admin",
    "doctor@example.com": "doctor",
}

# Get logged-in Streamlit user (works only on Streamlit Cloud)
user = user.email

st.title(f"User Role Demo:{user}")

if user:
    email = user.email

    # Get role from dictionary (default to guest)
    role = USER_ROLES.get(email, "guest")

    st.write(f"### Hello, **{user.name}** 👋")
    st.write(f"#### Your role: **{role}**")

else:
    st.write("You are not logged in. (Streamlit Cloud required)")





