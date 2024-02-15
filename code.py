#pip install streamlit_qrcode

import streamlit as st
import qrcode

url = "https://uscapston.streamlit.app/"

qr_img = qrcode.make(url)
st.image(qr_img)

