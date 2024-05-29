import streamlit as st

st.set_page_config(
    layout="wide",
)

col1, colo2 = st.columns(2)

with col1:
    st.image("images/hasan.png")

with colo2:
    st.title("Md Hasanuzzaman")
    st.subheader("Software Engineer")
    content = """
    Hi, I am Md. Hasanuzzaman. I am a dedicated and passionate software engineer with a strong foundation in various programming languages and software development practices. I completed my Diploma in Software Engineering from Daffodil International Professional Training Institute (DIPTI), where I gained a robust technical base and practical experience in building software applications.

    Currently, I am pursuing a Bachelor of Science in Computer Science (BSCS) at the University of the People, where I am expanding my knowledge and skills in advanced computer science concepts and methodologies. My academic journey has been complemented by hands-on projects and coursework that have deepened my understanding of software development, algorithms, and data structures.

    My primary programming languages include Python, Java, and JavaScript, and I have developed proficiency in each through both academic and personal projects. I am particularly passionate about full stack development and have experience working with Python for backend development and React for frontend development. This combination allows me to build dynamic, responsive, and efficient web applications.

    In addition to my programming skills, I have a strong grasp of data structures and algorithms (DSA), which are critical for writing efficient code and solving complex problems. My ability to understand and implement various algorithms and data structures has been honed through continuous practice and application in real-world scenarios.

    I am always eager to learn new technologies and methodologies to stay current in the ever-evolving field of software engineering. My goal is to leverage my skills and knowledge to create innovative solutions that address real-world challenges and make a positive impact.

    Thank you for visiting my profile. I look forward to connecting and exploring opportunities to collaborate on exciting projects.
    """
    st.info(content)

