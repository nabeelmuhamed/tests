import streamlit as st
import json
import base64

# --- Roles assigned based on email/username ---
USER_ROLES = {
    "nabeelms007@gmail.com": "admin",
    "nms236161@gmail.com": "owner",
    "nabeelms1999@outlook.com": "clinic_admin",
    "doctor@example.com": "doctor",
}

st.set_page_config(page_title="User Roles Demo", layout="centered")

# --- Print headers for debugging ---
st.write("Request headers:", st.context.headers.to_dict())

# --- Get Base64-encoded Streamlit user header ---
encoded_user = st.context.headers.get("X-Streamlit-User")

if not encoded_user:
    st.error("No user header found. Make sure this is a private Streamlit app.")
    st.stop()

# --- Decode Base64 JSON ---
try:
    decoded_bytes = base64.b64decode(encoded_user)
    user_info = json.loads(decoded_bytes)
    email = user_info.get("email", "")
    display_name = user_info.get("displayName", "Unknown")
except Exception as e:
    st.error(f"Failed to decode user info: {e}")
    st.stop()

# --- Access control ---
if email not in USER_ROLES:
    st.error(f"Hi {display_name} ({email}), you are not authorized to view this application.")
    st.stop()

# --- Assign role based on email ---
role = USER_ROLES[email]

# --- Display greeting and role ---
st.write(f"### Hello, **{display_name}** 👋")
st.write(f"#### Your email: **{email}**")
st.write(f"#### Your role: **{role}**")
