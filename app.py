import streamlit as st

# --- Roles assigned based on email/username ---
USER_ROLES = {
    "nabeelms007@gmail.com": "admin",
    "nms236161@gmail.com": "owner",
    "nabeelms1999@outlook.com": "clinic_admin",
    "doctor@example.com": "doctor",
}

# --- Print headers (optional, for debugging) ---
st.write(st.context.headers.to_dict())

# --- Get username/email from headers ---
if 'username' not in st.session_state:
    st.session_state['username'] = st.context.headers.get("X-Replit-User-Name", "unknown")

# --- Allowed users are all keys in USER_ROLES ---
allowed_user_ids = set(USER_ROLES.keys())

# --- Access control ---
if st.session_state['username'] not in allowed_user_ids:
    st.error(f"Hi {st.session_state['username']}, you are not authorized to view this application.")
    st.stop()

# --- Assign role based on username/email ---
role = USER_ROLES.get(st.session_state['username'], "guest")

# --- Display greeting and role ---
st.write(f"### Hello, **{st.session_state['username']}** 👋")
st.write(f"#### Your role: **{role}**")
