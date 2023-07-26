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

openai.api_key = st.secrets["OPENAI_API_KEY"]
model_engine = "text-davinci-003"
def get_acronym_definition(acronym):
    """Retrieves the definition of an acronym from OpenAI text API or Wikipedia."""

    fields = ["military", "GIS", "intelligence", "proposal"]

    for field in fields:
        # Try to get the definition using the OpenAI text API
        try:
            response = openai.Completion.create(
                engine=model_engine,
                prompt=f"In the context of {field}, what is {acronym}?",
                max_tokens=100,
            )
            if response['choices'][0]['text'].strip():
                return response['choices'][0]['text'].strip()

        except Exception as e:
            print("Error occurred while using OpenAI API:", e)

    # If the OpenAI API fails or returns an empty response, try using the Wikipedia API
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
        return wiki_response[2][0]  # return the first match in the wiki_response[2] list (description)
    else:
        return "Definition not available"

def find_acronyms(text):
    """Finds all acronyms in the given text."""

    acronyms = re.findall(r'\b[A-Z]{2,}\b', text)
    return acronyms

def find_acronym_definitions(user_input):
    acronyms = find_acronyms(user_input)
    acronym_definitions = {acronym: get_acronym_definition(acronym) for acronym in acronyms}
    return acronym_definitions

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

        st.markdown("### **Acronyms and Definitions:**")
        for acronym, definition in acronym_definitions.items():
            st.markdown(f"{acronym} - {definition}")

if __name__ == "__main__":
    main()
