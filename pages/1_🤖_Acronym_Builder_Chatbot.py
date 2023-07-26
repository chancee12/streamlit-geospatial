import streamlit as st
import requests
import re
import openai

def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True

# Load the spaCy language model
nlp = spacy.load("en_core_web_sm")

# Replace 'YOUR_OPENAI_API_KEY' with your actual API key from OpenAI
openai.api_key = 'YOUR_OPENAI_API_KEY'

def get_acronym_definition(acronym, text):
    """Retrieves the definition of an acronym from OpenAI text API or text input."""

    # Check if the acronym is present in the input text
    if acronym in text:
        definition = "Text Input"
    else:
        # Try to get the definition using the OpenAI text API
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"What is {acronym}?",
                max_tokens=100,
            )
            if response['choices'][0]['text'].strip():
                definition = response['choices'][0]['text'].strip()

        except Exception as e:
            print("Error occurred while using OpenAI API:", e)
            definition = "Definition not available"

        # If the OpenAI API fails or returns an empty response, try using the Wikipedia API
        if definition == "Definition not available":
            wiki_response = requests.get(
                "https://en.wikipedia.org/w/api.php",
                params={
                    "action": "opensearch",
                    "format": "json",
                    "limit": 1,
                    "namespace": 0,
                    "search": acronym
                }
            ).json()

            if len(wiki_response[1]) > 0:
                definition = wiki_response[2][0]  # return the first match in the wiki_response[2] list (description)

    return definition

def find_acronyms(text):
    """Finds all acronyms in the given text."""

    acronyms = re.findall(r'\b[A-Z]{2,}\b', text)
    return acronyms

def find_acronym_definitions(user_input):
    acronyms = find_acronyms(user_input)
    acronym_definitions = {}
    for acronym in acronyms:
        definition = get_acronym_definition(acronym, user_input)
        acronym_definitions[acronym] = definition

    return acronym_definitions

def prioritize_definitions(acronym_definitions, text):
    """Prioritizes military, intelligence, and GIS-related definitions based on entity recognition."""

    prioritized_definitions = {}
    doc = nlp(text)

    for acronym, definition in acronym_definitions.items():
        priority_score = 0
        words_in_definition = definition.lower().split()

        for ent in doc.ents:
            if ent.text.lower() in words_in_definition:
                if ent.label_ == "ORG" and any(keyword in ent.text.lower() for keyword in ["military", "army", "navy", "air force", "defense", "combat"]):
                    priority_score += 3
                elif ent.label_ == "ORG" and any(keyword in ent.text.lower() for keyword in ["intelligence", "security", "espionage", "surveillance", "classified"]):
                    priority_score += 2
                elif ent.label_ == "ORG" and any(keyword in ent.text.lower() for keyword in ["gis", "geospatial", "mapping", "geography", "location", "cartography"]):
                    priority_score += 1

        prioritized_definitions[acronym] = (priority_score, definition)

    return prioritized_definitions

def main():
    st.set_page_config(layout="wide")

    st.title("Acronym Finder and Definition Assistant")
    st.markdown(
        """
        This tool helps find acronyms in the text you provide and fetches their definitions from OpenAI and Wikipedia.
        """
    )

    user_input = st.text_area("Paste the text from which you'd like to extract acronyms:", height=200)
    submit_button = st.button("Submit")

    if submit_button and user_input:
        with st.spinner("Finding acronyms and their definitions..."):
            acronym_definitions = find_acronym_definitions(user_input)
            prioritized_definitions = prioritize_definitions(acronym_definitions, user_input)

        st.markdown("### **Acronyms and Definitions:**")
        for acronym, (priority_score, definition) in sorted(prioritized_definitions.items(), key=lambda x: x[1][0], reverse=True):
            st.markdown(f"{acronym} - {definition}")

if __name__ == "__main__":
    main()
