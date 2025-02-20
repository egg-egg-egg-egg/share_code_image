import streamlit as st
import os



def png_show():
    st.write("## 高效刷题流程")

    path = os.path.join(r".\src\assets", "刷题方法.png"), 

    st.image(path)
