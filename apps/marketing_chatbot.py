import streamlit as st
from pages import SEOChatbot
import openai

# Set up OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# GPT-3 model to use for text revision
model_engine = "text-davinci-003"

st.title("Chancee's Proposal AI Assistant Beta V.1.0.3")

st.sidebar.info(
    """
    - Hugging Face: <https://huggingface.co/Chancee12>
    - GitHub repository: <https://github.com/chancee12/>
    """
)

st.sidebar.title("Contact")
st.sidebar.info(
    """
    Chancee Vincent:
    [LinkedIn](www.linkedin.com/in/chancee-vincent-4371651b6)
    """
)
def main():
    st.set_page_config(layout="wide")


    )

    st.sidebar.title("Contact")
    st.sidebar.info(
        """
        Chancee Vincent:
        [LinkedIn](www.linkedin.com/in/chancee-vincent-4371651b6) 
        """
    )

    SEOChatbot.app()

if __name__ == "__main__":
    main()
