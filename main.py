import streamlit as st

col1, colo2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with colo2:
    st.title("Md Hasanuzzaman")
    st.subheader("Software Engineer")
    content = """
    Hi, I am Md. Hasnuzzaman. I am a software engineer. I love to learn new things.
    I have a passion for Full stack development using python and react.
    """
    st.write(content)