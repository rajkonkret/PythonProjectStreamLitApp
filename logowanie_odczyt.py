import os

import streamlit as st
import getpass

user = getpass.getuser()
domain = os.environ.get("USERDOMAIN", "")
st.write(user)
st.write(domain)
