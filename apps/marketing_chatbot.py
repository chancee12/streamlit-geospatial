import streamlit as st
from pages import SEOChatbot

# Define all your pages in this dictionary
# The names on the left are the names that will appear in the dropdown menu
PAGES = {
    "SEO Chatbot": SEOChatbot,
}

def main():
    st.sidebar.title("Page selection")
    # Render the page selection as a radio button
    page = st.sidebar.selectbox("Go to", list(PAGES.keys()))
    PAGES[page].app()

if __name__ == "__main__":
    main()
