
import streamlit as st
import openai

openai.api_key = st.secrets["openai_api_key"]

st.title("🌟 Personal Branding Agent")
st.subheader("Créateur de contenu IA pour ton personal branding sur Meta")

theme = st.selectbox("Choisis ton thème :", [
    "Location Airbnb",
    "Location de voitures",
    "Sport",
    "Danse",
    "Développement personnel"
])

style = st.selectbox("Style de post :", [
    "Éducatif",
    "Motivation",
    "Storytelling",
    "Preuve sociale"
])

format_post = st.selectbox("Format de contenu :", [
    "Carrousel",
    "Post simple",
    "Reels",
    "Story"
])

subject = st.text_input("Ton sujet ou idée de post :", placeholder="Ex: Comment augmenter ses réservations Airbnb")

if st.button("Générer le contenu 🚀"):
    with st.spinner("Génération en cours..."):
        prompt = f"""
        Tu es un expert en marketing sur Instagram et Facebook.
        Aide-moi à créer du contenu pour mon personal branding.

        Thème : {theme}
        Style : {style}
        Format : {format_post}
        Sujet : {subject}

        Génère :
        - 3 idées de posts
        - 3 titres accrocheurs
        - 2 légendes adaptées (1 courte, 1 longue)
        - Une liste de hashtags pertinents
        - Un conseil de moment de publication
        """

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4-turbo",
                messages=[
                    {"role": "system", "content": "Tu es un expert en communication sur les réseaux sociaux."},
                    {"role": "user", "content": prompt}
                ]
            )
            output = response["choices"][0]["message"]["content"]
            st.success("Contenu généré !")
            st.markdown(output)
        except Exception as e:
            st.error(f"Erreur lors de la génération : {e}")

st.caption("Créé par ton IA Personal Branding 🧑‍💻")
