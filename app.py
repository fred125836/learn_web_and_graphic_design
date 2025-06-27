from PIL import Image
import streamlit as st
from datetime import datetime

# find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Hello World", page_icon=":tada:")

# ---- LOAD ASSETS ----
img_contact_form = Image.open("images/microsoft_office.jpeg")
img_lottie_animation = Image.open("images/web_dev.png")

st.link_button("_go to_ our payment :blue[website]", "https://wa.me/message/CL576QP54YBPP1")

hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ---- HEADER SECTION ----
with st.container():
    st.subheader("My name is Onwuegbuna Okwuchukwu :wave:")
    st.title("I am a Typist, Graphic Designer, and Forex Enthusiast from Nigeria")
    st.write("I am passionate about Web Development")
    st.write("you are welcome to my page")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("MY PROJECT")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("CONTACT ME TO LEARN GRAPHIC DESIGNING AND WEB DEVELOPMENT")
        st.write(
            """
            WHAT YOU WILL BE LEARNING FROM ME
            - I WILL TEACH YOU HOW TO DEVELOP WEBSITE WITH PYTHON USING PYCHARM
            - I WILL TEACH YOU GRAPHIC DESIGN WITH CORELDRAW AND CANVA
            - I WILL TEACH YOU HOW TO USE MICROSOFT OFFICES (WORD, EXCEL AND POWERPOINT)
            """
        )
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("WHAT YOU WILL BE LEARNING IN THE MICROSOFT OFFICE PACKAGE")
        st.write(
            """
            - LEARN HOW TO TYPE AND EDIT DOCUMENT IN MICROSOFT WORD
            - LEARN HOW TO MAKE ANIMATION WITH POWERPOINT
            - LEARN HOW TO USE SPREADSHEET WITH EXCEL
            """
        )

with st.container():
    st.write("---")
    st.subheader("TRY THIS OUT :smile:")
    st.title("CHECK YOUR DATE OF BIRTH :baby:")
    current_time = datetime.now().year
    first_name = st.text_input("Enter your first name:")
    second_name = st.text_input("Enter your second name:")
    age = st.number_input("Enter your age:", min_value=0, max_value=120)
    favorite_color = st.selectbox("Select your favorite color:", ["Red", "Green", "Blue", "violet", "okwuchukwu", "Other"])
    if st.button("Submit"):
        st.write(f"Hello, **{first_name + second_name}**! 👋")
        st.write(f"You are **{age}** years old. And your birth year is **{current_time - age }**")
        st.write(f"Your favorite color is *{favorite_color}**.")

st.write("Current year:", current_time)

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get in touch with me")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/jessicasmith22025@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <textarea name="schoolname" placeholder="your school name here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()


st.markdown(
    """
    <div style="
        padding: 20px;
        background-color: white;
        border-radius: 10px;
        box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.2);
        width: fit-content;
        margin: 20px auto;
        text-align: center;
    ">
        <h3 style="margin: 0;">Box with Shadow</h3>
        <p>This box has a shadow effect!</p>
    </div>
    """,
    unsafe_allow_html=True
)


