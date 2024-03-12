from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# import emojis from :   "https ://webfx.com/tools/emoji-cheat-sheet/"
st.set_page_config(page_title="My Webpage",page_icon=":tada",layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#use a local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# LOAD ASSETS
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("images/sofiane.png")
img_bridge_form = Image.open("images/pont_sidi_mcid.jpg")



# ------ HEADER SECTION ------------------------
with st.container():
    st.subheader("Hi, juste un test :wave:")
    st.title("Exemple utilsation de streamlit pour création page web")
    st.write("je suis passionné par ecriture des nouvelles fantastiques ")
    st.write("[Learn More>](https://pythonandvba.com)")

# ------ WHAT I DO ------------------------
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I Do")
        st.write("##")
        st.write(
           """
           dans cette page je fais la publication de nouvelles qui traitent le surnaturel et le fantastique
           supperposé à la réalité. mes histoires tirent du comique, drama, et meme les histoires folles qui
           plannent avec le lecteur pour le ramener dans les mondes incroyables de l'imaginaire....
           les personnes interessées peut poster leurs commentaires et donner leurs avis.
           """
        )
        st.write("[YouTube Channel>](https://youtube/c/codingisfun)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# les ponts
with st.container():
    st.write("---")
    st.header("Les ponts de Constantine")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    
    with image_column:
        # insert image
        st.image(img_bridge_form)

    with text_column:
        st.header("le pont suspendu sidi m'cid")
        st.write(
           """
           Le pont de Sidi M'Cid est un pont suspendu qui traverse les gorges du Rhummel et relie la médina de Constantine au centre hospitalo-universitaire. Sa construction décidée après l'ouverture de l'hôpital de la ville évite aux Constantinois de faire un long détour par le Pont d'El-Kantara pour se rendre au CHU.
           """
        )
        st.markdown("[Voir la vidéo>](https://www.youtube.com/watch?v=e4eIqaZD4eA)")

# l'Auteur
with st.container():
    st.write("---")
    st.header("l'Auteur")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    
    with image_column:
        # insert image
        st.image(img_contact_form)

    with text_column:
        st.header("comment ajouter un nouveau contact")
        st.write(
           """
           voulez-vous ajouter un nouveau contact ?
           on va montrer comment implenter une contact form avec streamlit
           """
        )
        #st.markdown("[Voir la vidéo>](https://www.youtube.com/watch?v=e4eIqaZD4eA)")

# Cotact
with st.container():
    st.write("---")
    st.header("Contactez-nous")
    st.write("##")
    
    # Documentation https://formsubmit.co/ !!!! changer email
    
    contact_form = """
    <form action="https://formsubmit.co/fsof2007@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false" required>
        <input type="text" name="nom" placeholder="Votre nom?" required>
        <input type="email" name="email" placeholder="Votre email?" required>
        <textarea name="message" placeholder="Votre message ici" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)

    with right_column:
        st.empty()