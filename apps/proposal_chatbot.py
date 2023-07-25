import streamlit as st
from page import main_page

def app():
    st.markdown("<h1 style='text-align: center; color: #0000FF;'>Chancee's Proposal AI Assistant Beta V.1.0.2</h1>", unsafe_allow_html=True)

    st.markdown('''
        ## **About**
        This AI assistant is designed specifically to **revise government contracting proposals**.
        Utilizing GPT-3, it assists in:
        * Restructuring sentences for improved readability
        * Clarifying ambiguities
        * Eliminating unnecessary redundancies
        * Enhancing the overall presentation
    ''', unsafe_allow_html=True)

    st.markdown('''
        ## **Prompt Guidance**
        The prompt box allows you to specify how you want the AI to approach revising your text. If you leave it blank, the default prompt, which instructs the AI to revise for clarity, structure, alignment with proposal requirements, professional appeal, and so on, will be used. If you enter your own prompt, it will replace the default and guide the AI's revision process. Remember, the AI is quite flexible, so feel free to get creative with your prompts!

        **Note:**
        * Works best on around 1-6 length paragraph chunks at a time. 
        * Also if you have a specific revision you can put it in parenthesis. For example, you could put (Make this section more relatable to the client with unique examples) next to your paragraph. 
        * Lastly, site uses Chancee's Openai account and tokens, so be mindful of submissions while testing but have fun!
    ''', unsafe_allow_html=True)
def app():
    st.set_page_config(
        page_title="Chancee's Proposal AI Assistant Beta V.1.0.2",
        page_icon=":robot:",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'About': "Chancee's AI Assistant is designed specifically to revise government contracting proposals the best way possible. Utilizing OpenAI API, it assists in restructuring sentences, clarifying ambiguities, eliminating redundancies, and enhancing the overall presentation."
        }
    )

    st.sidebar.info(
        """
        Chancee Vincent, Axim Geospatial Solutions Architect:
        [LinkedIn](www.linkedin.com/in/chancee-vincent-4371651b6) | [GitHub](https://github.com/chancee12/)
        
        Axim Homepage:
        [Axim Geospatial](https://www.aximgeo.com/)  
        """
    )

    main_page()

if __name__ == "__main__":
    app()
