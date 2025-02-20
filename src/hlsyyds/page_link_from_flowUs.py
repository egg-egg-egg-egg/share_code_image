import streamlit as st

LINKS = {
    "C0":"https://flowus.cn/kyyy/share/15886e01-1ff3-4afc-8a76-95d6c31b666b?code=DD8PQT",
    "C1":"https://flowus.cn/kyyy/share/10d9031f-91b7-4527-9aab-a605d9bdff5e?code=DD8PQT",
    "C2":"https://flowus.cn/kyyy/share/22c69717-3786-485d-9879-77af0075c9fb?code=DD8PQT",
    "C3":"https://flowus.cn/kyyy/share/70e86289-bd9d-4c99-8321-1803f4dc29bd?code=DD8PQT",
    "C4":"https://flowus.cn/kyyy/share/4568d202-4f12-436e-83f5-63d9be9c7b4c?code=DD8PQT",
}   
    
def link_button():
    cols = st.columns([1,1,1])
    for idx,(key,value) in enumerate(LINKS.items()):
        cols[idx%len(cols)].link_button(key+"知识点",value,type="primary")
    
    
    st.info("""
    这些文档都是黄老师纯手写的, 有些部分比较粗糙, 没时间整理😩。

    有没有实力哥/姐来整理一下😘。
    """)