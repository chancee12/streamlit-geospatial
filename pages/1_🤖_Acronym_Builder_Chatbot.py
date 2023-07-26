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

def get_acronym_definition(acronym):
    """Retrieves the definition of an acronym from Wikipedia."""

    response = requests.get(
        "https://en.wikipedia.org/w/api.php",
        params={
            "action": "opensearch",
            "format": "json",
            "limit": 1,
            "namespace": 0,
            "search": acronym
        }
    ).json()

    if len(response[1]) > 0:
        return response[1][0]  # return the first match
    else:
        return None

def find_acronyms(text):
    """Finds all acronyms in the given text."""

    # matches any uppercase word of at least two letters
    acronyms = re.findall(r'\b[A-Z]{2,}\b', text)
    return acronyms

if check_password():
    st.set_page_config(layout="wide")

    st.sidebar.title("Contact")
    st.sidebar.info(
        """
        Chancee Vincent:
        [LinkedIn](www.linkedin.com/in/chancee-vincent-4371651b6)
        """
    )

    st.title("Acronym Finder and Definition Assistant")
    st.markdown(
        """
        This tool helps to find acronyms in the text you provide and fetches their definitions from Wikipedia.
        """
    )

    openai.api_key = st.secrets["OPENAI_API_KEY"]
    model_engine = "text-davinci-003"

    def find_acronym_definitions(user_input):
        acronyms = find_acronyms(user_input)
        acronym_definitions = {acronym: get_acronym_definition(acronym) for acronym in acronyms}
        
        prompt = f"The following acronyms were found in the text: {' '.join(acronyms)}"
        openai_response = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=100,
            temperature=0.5
        )
        structured_response = openai_response.choices[0].text.strip()

        return structured_response, acronym_definitions

    def main_page():
        user_input = st.text_area("Paste the text from which you'd like to extract acronyms:", height=200)
        submit_button = st.button("Submit")

        if submit_button and user_input:
            with st.spinner("Finding acronyms and their definitions..."):
                structured_response, acronym_definitions = find_acronym_definitions(user_input)

            st.markdown("### **Acronyms and Definitions:**")
            st.markdown(structured_response)
            for acronym, definition in acronym_definitions.items():
                if definition is not None:
                    st.markdown(f"**{acronym}**: {definition}")
                else:
                    st.markdown(f"**{acronym}**: Definition not found")

if __name__ == "__main__":
    main_page()
