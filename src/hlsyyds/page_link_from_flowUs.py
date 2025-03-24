import streamlit as st

LINKS = {
    "C0":"https://flowus.cn/kyyy/share/15886e01-1ff3-4afc-8a76-95d6c31b666b?code=DD8PQT",
    "C1":"https://flowus.cn/kyyy/share/10d9031f-91b7-4527-9aab-a605d9bdff5e?code=DD8PQT",
    "C2":"https://flowus.cn/kyyy/share/22c69717-3786-485d-9879-77af0075c9fb?code=DD8PQT",
    "C3":"https://flowus.cn/kyyy/share/70e86289-bd9d-4c99-8321-1803f4dc29bd?code=DD8PQT",
    "C4":"https://flowus.cn/kyyy/share/48b3bc6e-e5bb-4ef6-89c8-f4730947af5d?code=DD8PQT",
}   
    
def link_button():
    cols = st.columns([1,1,1])
    for idx,(key,value) in enumerate(LINKS.items()):
        cols[idx%len(cols)].link_button(key+"知识点",value,type="primary")
    
    
    st.info("""
    这些文档都是俺纯手写的😘
    """)