import streamlit as st
import app

if app.check_password():
    st.sidebar.title("Contact")
    st.sidebar.info(
        """
        [Chancee]:
        [LinkedIn]
        """
    )

    st.title("Acronym Extraction Bot Beta V.1.0.0")
    st.markdown(
    """
    This acronym extraction bot is designed specifically to assist in extracting acronyms and their definitions from any text input. It helps in identifying acronyms in:
    * Proposals
    * Technical documents
    * Manuals
    * Government documents
    * And any other documents where acronyms are used.
    """
)

    user_input = st.text_area("Enter the text or context you'd like the bot to extract acronyms from:", height=200)
    submit_button = st.button("Submit")

    if submit_button and user_input:
        with st.spinner("Loading..."):
            acronyms_and_definitions = app.extract_acronyms(user_input)
            time.sleep(1)

        if acronyms_and_definitions:
            st.markdown("### **Acronyms found:**")
            for acronym, definition in acronyms_and_definitions.items():
                st.write(f"{acronym}: {', '.join(definition)}")
        else:
            st.markdown("### **No acronyms found.**")
