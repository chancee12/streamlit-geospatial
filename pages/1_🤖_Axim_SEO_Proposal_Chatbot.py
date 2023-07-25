import streamlit as st
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

if check_password():
    st.sidebar.info(
    """
    - Hugging Face: <https://huggingface.co/Chancee12>
    - GitHub repository: <https://github.com/chancee12/>
    """
    )

    st.sidebar.title("Contact")
    st.sidebar.info(
        """
        Chancee Vincent, Axim Geospatial Solutions Architect:
        [LinkedIn](www.linkedin.com/in/chancee-vincent-4371651b6) | [GitHub](https://github.com/chancee12/)
        
        Axim Homepage:
        [Axim Geospatial](https://www.aximgeo.com/) 
        """
    )

    def app():

        st.set_page_config(layout="wide")

        st.title("Axim's SEO Chatbot Beta V.1.0.0")

        openai.api_key = st.secrets["OPENAI_API_KEY"]
        model_engine = "text-davinci-003"

        def run_model(prompt):
            model_response = openai.Completion.create(
                engine=model_engine,
                prompt=prompt,
                max_tokens=2500,
                temperature=0.75
            )
            return model_response['choices'][0]['text'].strip()

        tasks = ["Create a LinkedIn caption for this text",
                "Suggest SEO keywords for this blog post",
                "Generate a Tweet for this article",
                "Create a catchy title for this blog post",
                "Write a brief product description",
                "Compose a promotional email subject",
                "Write a meta description for a web page",
                "Suggest hashtags for a social media post",
                "Compose a Facebook post for this event",
                "Create a call-to-action for a newsletter"]

        task = st.selectbox("Select Task:", tasks)
        user_input = st.text_area("Enter the text or context you'd like the Chatbot to work on:", height=200)
        submit_button = st.button("Submit")

        if submit_button and user_input:
            with st.spinner("Generating text..."):
                output = run_model(f"{task}\n\n{user_input}")
                time.sleep(1)

            st.markdown("### **Output:**")
            st.text_area("", value=output, height=200)
    if __name__ == "__main__":
        main_page()
