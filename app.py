from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Hemant Shankar", page_icon="📍", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_coding = load_lottieurl(
    "https://assets9.lottiefiles.com/packages/lf20_4kx2q32n.json"
)
lottie_bullet = load_lottieurl(
    "https://assets5.lottiefiles.com/packages/lf20_owsUdW27XG.json"
)

img_profile = Image.open("images/dp.jpg")

img_phish = Image.open("images/phishguard.png")
img_cap = Image.open("images/image_cap.png")
img_insights = Image.open("images/insights.png")
img_track = Image.open("images/Track.png")

img_flight = Image.open("images/flight_dash.png")
img_covid = Image.open("images/covid.png")
img_net = Image.open("images/netflix.png")
img_ecell = Image.open("images/ecell.jpeg")
img_aaveg = Image.open("images/aaveg.jpeg")

with st.container():
    image_column, text_column = st.columns((1, 6))
    with image_column:
        st.image(img_profile)

    with text_column:
        st.subheader("Hi, I am Hemant Shankar 👋")
        st.title("A Passionate Data Scientist/ Analyst")
        st.write(
            "Passionate about working with data, solving real life problems by analysis and predictions."
        )
        # if st.button("View Resume"):
        #     st.write("[Download Resume](#)")
        st.write("")
        st.markdown(
            """
    <a href="https://drive.google.com/file/d/1C1iFks381U90HJRflUkVtLy9N4FkLdpy/view?usp=drive_link" target="_blank" class="green-button">View Resume</a>
    """,
            unsafe_allow_html=True,
        )


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About Me")
        st.write("")
        st.write(
            """
            Hello! I'm Hemant Shankar, a passionate and driven individual with a strong foundation in Mathematics and Computing. 
            Currently, I am pursuing my BS-MS degree at the National Institute of Technology, Agartala, where I’ve maintained an impressive CGPA of 8.47. 
            My academic journey has shaped my analytical mindset and fueled my curiosity for data-driven solutions.

            With a keen interest in data science and machine learning, I specialize in uncovering meaningful insights from data and building innovative solutions. 
            During my internship at ARIES, I applied machine learning to analyze datasets and develop models. 
            These experiences have honed my problem-solving skills and strengthened my expertise in working with complex datasets. 
            I aim to leverage technology to solve real-world problems and contribute to transformative initiatives.

            """
        )

    with right_column:
        st_lottie(lottie_coding, height=400, key="coding")





with st.container():
    st.write("-----")
    st.header("Experience")
    st.write("")
        # Experience details
    st.subheader("Machine Learning Intern at ARIES")
    st.write("**May 2023 - July 2023**")
    st.write("""
    - Updated and optimized a script for converting .Mcs files.
    - Developed a comprehensive data preprocessing script for efficient data handling.
    - Conducted extensive Data Analysis on multiple datasets, deriving important conclusions and insights.
    - Studied and applied multiple Machine Learning (ML) algorithms for Regression, Classification, and Clustering.
    - Designed and implemented a clustering model specifically for the HEPL dataset.
    """)
        



with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    bullet, image1, text_column = st.columns((1, 2, 3))

    with bullet:
        st_lottie(lottie_bullet, height=50, key="tick1")
    with image1:
        st.image(img_phish)
        
    with text_column:
        st.subheader("PhishGuard | [Link](https://phishguard4u.onrender.com/)")
        st.write(
            """
            A machine learning-based website designed to detect phishing URLs in real-time. 
            It leverages advanced algorithms like LightGBM to provide accurate and efficient classification of URLs as phishing or genuine.
            """
        )

    st.write("##")
    st.write("##")
    bullet, image2, text_column = st.columns((1, 2, 3))

    with bullet:
        st_lottie(lottie_bullet, height=50, key="tick2")

    with image2:
        st.image(img_cap)
        

    with text_column:
        st.subheader("Image Captioner | [Link](https://github.com/HemantShankar/Image_Captioner)")
        st.write(
            """
            A deep learning-based project that generates descriptive captions for images. 
            It combines convolutional neural networks (CNNs) for image feature extraction and recurrent neural networks (RNNs) for natural language generation.
            """
        )

    st.write("##")
    bullet, image3, text_column = st.columns((1, 2, 3))

    with bullet:
        st_lottie(lottie_bullet, height=50, key="tick3")

    with image3:
        st.image(img_insights)
        

    with text_column:
        st.subheader("Insights | [Link](https://insights4u.netlify.app/)")
        st.write(
            """
            A front-end website for users to get and share insights about a specific company interview experiences from people who have cleared the interviews.
            """
        )
    
    st.write("##")
    bullet, image3, text_column = st.columns((1, 2, 3))

    with bullet:
        st_lottie(lottie_bullet, height=50, key="tick4")

    with image3:
        st.image(img_track)
        

    with text_column:
        st.subheader("Track-Work | [Link](https://trackmywork.netlify.app/)")
        st.write(
            """
            A front-end website for assigning and tracking tasks of the day.
            """
        )
    
    st.write("##")
    bullet, image3, text_column = st.columns((1, 2, 3))

    with bullet:
        st_lottie(lottie_bullet, height=50, key="tick5")

    with image3:
        st.image(img_flight)
        

    with text_column:
        st.subheader("Flight Fare Analysis Dashboard | [Link](https://github.com/HemantShankar/Indian-Flight-Fare-Analysis)")
        st.write(
            """
            A dashboard which shows the price of flights in the major cities of India and helps to choose your best flight for your travel.
            """
        )
    
    st.write("##")
    bullet, image3, text_column = st.columns((1, 2, 3))

    with bullet:
        st_lottie(lottie_bullet, height=50, key="tick6")

    with image3:
        st.image(img_covid)
        

    with text_column:
        st.subheader("Covid-19 India Analysis Dashboard | [Link](https://github.com/HemantShankar/Covid_19_India-Analysis)")
        st.write(
            """
            An analysis and visualization on the dataset of Covid-19 in India to understand the waves and nature of Covid-19 virus in India.
            """
        )
    
    st.write("##")
    bullet, image3, text_column = st.columns((1, 2, 3))

    with bullet:
        st_lottie(lottie_bullet, height=50, key="tick7")

    with image3:
        st.image(img_net)
        

    with text_column:
        st.subheader("Netflix Analysis | [Link](https://github.com/HemantShankar/Netflix_Analysis)")
        st.write(
            """
            An analysis of Netflix Movies and Web Series Dataset performed using MySQL.
            """
        )


with st.container():
    st.write("----")
    st.header("Positions of Responsibility")
    st.write("#")
# Layout with columns
    col1, col2 = st.columns([1, 3])  # Adjust the ratio for logo and text

# Logos in the left column
    with col1:
        st.write("")
        st.write("")
        st.image(img_ecell, caption="E-Cell", width=100)  # Add your E-Cell logo file path
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.image(img_aaveg, caption="Drama Club", width=100)  # Add your Drama Club logo file path

# Position details in the right column
    with col2:
        st.subheader("Head of Operations and Strategies, E-Cell | 2021-2024")
        st.write("""
    - Responsible for all the operations and stratergies
    - Led and strategized operations to promote entrepreneurship at NIT Agartala.
    - Organized multiple events and mentored student startups.
    - Organized E-Summit of NIT Agartala with a team of 10 people.
    """)
        st.write("")
        
        st.subheader("Script Advisory, Drama Club | 2022-2023")
        st.write("""
        - Performed in and directed various stage productions.
    - Actively contributed to scriptwriting and event planning.
    - Wrote multiple scripts.
    - Won best team drama of the year in 2022
    """)

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("📬 Get In Touch With Me")
        st.write("##")

        contact_form = """
        <form action="https://formsubmit.co/hemantshankar9595@gmail.com" method="POST">
        <input type="HIDDEN" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your e-mail" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
        </form>
        """

        st.markdown(contact_form, unsafe_allow_html=True)

        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

        local_css("style/style.css")

    with right_column:
        st.empty()

st.write("#")
# Footer

st.markdown(
    "<p style='text-align: center; font-size: 22px; margin-top: -15px; color: default;'>© 2024 Hemant Shankar | hemantshankar9595@gmail.com</p>",
    unsafe_allow_html=True
)
# Custom HTML for social media links with icons
st.markdown("""
    <style>
        .social-icons {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: -20px;
        }
        .social-icons a {
            margin: 0 8px;
            text-decoration: none;
        }
        .social-icons img {
            width: 55px;  /* Adjust the size of icons */
            height: 55px;
        }
    </style>
""", unsafe_allow_html=True)

# Social Media Links (use your own social media URLs)
st.markdown("""
<div class="social-icons">
    <a href="https://www.linkedin.com/in/hemant-shankar/" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/e/e9/Linkedin_icon.svg" alt="LinkedIn">
    </a>
    <a href="https://github.com/HemantShankar" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/c/c2/GitHub_Invertocat_Logo.svg" alt="GitHub">
    </a>
    <a href="https://www.instagram.com/_hemantshankar_/" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" alt="Instagram">
    </a>
    
</div>
""", unsafe_allow_html=True)