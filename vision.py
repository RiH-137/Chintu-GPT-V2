import streamlit as st
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

import os
import pathlib
import textwrap
from PIL import Image

import google.generativeai as genai


os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


## Function to load model and get responses
def get_gemini_response(input, image):
    model = genai.GenerativeModel("gemini-pro-vision")
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text


## about me
def about_author():
    author_name = "Rishi Ranjan"
    author_description = textwrap.dedent(
        """
        Date-->  19/04/2024
        🌟 **About Me:**
        https://www.linkedin.com/in/rishi-rih/

🚀 Hey there! I'm Rishi, a 2nd year passionate Computer Science & Engineering Undergraduate with a keen interest in the vast world of technology. Currently specializing in AI and Machine Learning, I'm on a perpetual quest for knowledge and thrive on learning new skills.

💻 My journey in the tech realm revolves around programming, problem-solving, and staying on the cutting edge of emerging technologies. With a strong foundation in Computer Science, I'm driven by the exciting intersection of innovation and research.

🔍 Amidst the digital landscape, I find myself delving into the realms of Blockchain, crafting Android Applications, and ML projects.
 JAVA and Python . 
My GitHub profile (https://github.com/RiH-137) showcases my ongoing commitment to refining my craft and contributing to the tech community.

🏎️ Outside the digital realm, I'm a fervent Formula 1 enthusiast, experiencing the thrill of high-speed pursuits. When I'm not immersed in code or cheering for my favorite F1 team, you might find me strategizing moves on the chessboard.

📧 Feel free to reach out if you're as passionate about technology as I am. You can connect with me at 101rishidsr@gmail.com.

Let's build, innovate, and explore the limitless possibilities of technology together! 🌐✨
        """
    )

    #caling the func that display name and description
    st.write(f"**Author:** {author_name}")
    st.write(author_description)


## Streamlit application with sidebar for navigation
st.set_page_config(page_title="Chintu GPT V2",page_icon="1.png",layout="wide")
st.sidebar.title("Navigation")
selected_page = st.sidebar.radio("Select a page", ("Chintu GPT V2", "About the Author"))

if selected_page == "Chintu GPT V2":
    st.header("Chintu GPT V2")
    st.text("Chintu GPT V2 can support image along with text input.")
    st.text(" Ask any question in English, Hinglish, German, Telegu-English etc. and get the answer.")
    input = st.text_input("Ask the sawal...", key="input")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    image = ""
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)

    submit = st.button("Generate the Jawaab...")

    if submit:
        if input and image:
            response = get_gemini_response(input, image)
            st.subheader("Generated jawaab....")
            st.write(response)
        else:
            st.write("Please enter a question and select any image....")

elif selected_page == "About the Author":
    about_author()

