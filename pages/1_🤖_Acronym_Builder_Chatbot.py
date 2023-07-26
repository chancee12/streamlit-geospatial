import streamlit as st
import openai
import time
import re

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

def extract_acronyms(text):
    """Extract acronyms and their definitions from the given text."""
    pattern = re.compile(r'\(([A-Z]{2,})\)')
    acronyms = pattern.findall(text)
    definitions = {}

    for acronym in acronyms:
        definition_pattern = re.compile(r'([a-zA-Z0-9\s,]+)\s*\(' + acronym + '\)')
        definitions[acronym] = definition_pattern.findall(text)

    return definitions

def app():
    st.title("Acronym Extraction Bot Beta V.1.0.0")
    st.markdown(
    """
    This acronym extraction bot is designed specifically to assist in extracting acronyms and their definitions from any text input. Powered by GPT-3, it helps in identifying acronyms in:
    * Proposals
    * Technical documents
    * Manuals
    * Government documents
    * And any other documents where acronyms are used.
    """
)

    openai.api_key = st.secrets["OPENAI_API_KEY"]
    model_engine = "text-davinci-003"

    def run_model(prompt):
        model_response = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=2500,
            temperature=0.7
        )
        response_text = model_response['choices'][0]['text'].strip()

        # Extract acronyms from the response.
        acronyms_and_definitions = extract_acronyms(response_text)
        if acronyms_and_definitions:
            st.markdown("### **Acronyms found:**")
            for acronym, definition in acronyms_and_definitions.items():
                st.write(f"{acronym}: {', '.join(definition)}")

        return response_text

    user_input = st.text_area("Enter the text or context you'd like the bot to extract acronyms from:", height=200)
    submit_button = st.button("Submit")

    if submit_button and user_input:
        with st.spinner("Loading..."):
            output = run_model(user_input)
            time.sleep(1)

        st.markdown("### **Output:**")
        st.text_area("", value=output, height=200)

if check_password():
    st.sidebar.title("Contact")
    st.sidebar.info(
        """
        [Chancee]:
        [LinkedIn]
        """
    )

    app()
