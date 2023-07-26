import streamlit as st
import requests
import re
import openai

#logging
#logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


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

if check_password():

    openai.api_key = st.secrets["OPENAI_API_KEY"]
    model_engine = "text-davinci-003"

    def get_acronym_definition(acronym, text):
        """Retrieves the definition of an acronym from OpenAI text API or Wikipedia."""
        definition_in_text = find_in_text(acronym, text)
        if definition_in_text:
            print(f"Found definition in text: {definition_in_text}")
            return definition_in_text

        fields = ["military", "GIS", "intelligence", "proposal", "AI"]

        definition = None
        for field in fields:
            try:
                response = openai.Completion.create(
                    engine=model_engine,
                    prompt=f"In the field of {field}, what does the acronym '{acronym}' stand for?",
                    max_tokens=60,
                    temperature=0.3,
                )
                result = response['choices'][0]['text'].strip()
                if result and acronym in result:
                    split_result = result.split(".")
                    if len(split_result[0].split(' ')) > 3:
                        print(f"Found definition in OpenAI API: {split_result[0]}")
                        definition = split_result[0]
                        break
                    else:
                        print(f"Found definition in OpenAI API: {'. '.join(split_result[:2])}")
                        definition = '. '.join(split_result[:2])
                        break

            except Exception as e:
                logging.error("Error occurred while using OpenAI API: ", exc_info=True)

        if definition is None:
            try:
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

                if len(wiki_response[1]) > 0 and acronym in wiki_response[2][0]:
                    split_result = wiki_response[2][0].split(".")
                    if len(split_result[0].split(' ')) > 3:
                        print(f"Found definition in Wikipedia: {split_result[0]}")
                        definition = split_result[0]
                    else:
                        print(f"Found definition in Wikipedia: {'. '.join(split_result[:2])}")
                        definition = '. '.join(split_result[:2])
            except Exception as e:
                logging.error("Error occurred while using Wikipedia API: ", exc_info=True)

        return definition or "Definition not available"

    def find_acronyms(text):
        """Finds all acronyms in the given text."""

        acronyms = re.findall(r'\b[A-Z]{2,}\b', text)
        return acronyms

    def find_acronym_definitions(user_input):
        acronyms = find_acronyms(user_input)
        acronym_definitions = {acronym: get_acronym_definition(acronym, user_input) for acronym in acronyms}
        return acronym_definitions

    def main():
        st.set_page_config(layout="wide")

        st.title("Acronym Finder and Definition Assistant")
        st.markdown(
            """
            This tool harnesses a multi-faceted approach to uncover acronyms within your text. First, it parses the text itself for immediate definitions. It then employs the power of OpenAI and Wikipedia, cross-referencing the definitions while prioritizing those most related to key fields such as GIS, Geospatial Analysis, Remote Sensing, AI, and others. This process increases highly relevant interpretations, enriching your understanding of the content at hand.
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
