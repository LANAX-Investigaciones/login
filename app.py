import pickle
from pathlib import Path
import streamlit_authenticator as stauth
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
   page_title="app",
   page_icon="🔲",
   layout="wide",
   initial_sidebar_state="expanded",
)


names = ["Ana Laura", "Rebecca Miller"]
usernames = ["pupi", "rmiller"]
# contra = abc123

file_path = Path(__file__).parent/"hashed_pw.pkl"
with file_path.open("rb") as file:
        hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords, "app", "abcdef")

name, authentication_status, username = authenticator.login("Ingresar", "main")

if authentication_status == False:
        st.error("Incorreto")
if authentication_status == None:
        st.warning("Ingresa")
if authentication_status:
        st.write("Inventario")
        # Lectura de datos
        df = pd.read_csv('bd.csv')
        # df.drop(["CONTEO"], axis=1, inplace=True)
        st.write(df)


authenticator.logout("Salir", "sidebar")
st.sidebar.title(f"Welcome {name}")
