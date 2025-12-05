import streamlit as st

# --- Roles assigned based on email (or username mapping) ---
USER_ROLES = {
    "nabeelms007@gmail.com": "admin",
    "nms236161@gmail.com": "owner",
    "nabeelms1999@outlook.com": "clinic_admin",
    "doctor@example.com": "doctor",
    # If you want, you can map Replit usernames to roles too
    "matt": "admin",
}

# --- Print headers (optional, for debugging) ---
st.write(st.context.headers.to_dict())

# --- Get Replit username from headers ---
if 'username' not in st.session_state:
    st.session_state['username'] = st.context.headers.get("X-Replit-User-Name", "unknown")

# --- Access control ---
allowed_user_ids = {"matt"}  # Add authorized Replit usernames here
if st.session_state['username'] not in allowed_user_ids:
    st.error(f"Hi {st.session_state['username']}, you are not authorized to view this application.")
    st.stop()

# --- Assign role based on username/email ---
role = USER_ROLES.get(st.session_state['username'], "guest")

# --- Display greeting and role ---
st.write(f"### Hello, **{st.session_state['username']}** 👋")
st.write(f"#### Your role: **{role}**")
