import streamlit as st
import openai
import time


# Set page configuration
st.set_page_config(
    page_title="Chancee's Proposal AI Assistant Beta V.1.0.2",
    page_icon=":robot:",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "Chancee's AI Assistant is designed specifically to revise government contracting proposals the best way possible. Utilizing OpenAI API, it assists in restructuring sentences, clarifying ambiguities, eliminating redundancies, and enhancing the overall presentation."
    }
)

# Enhanced CSS for an improved and cool aesthetic
st.markdown("""
    <style>
        body {
            color: #000;
            background-color: #f5f5f5;
        }
        h1, h2, h3 {
            color: #008080;
            font-family: 'Courier New', Courier, monospace;
        }
        div {
            font-family: 'Times New Roman', Times, serif;
        }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #008080;'>Chancee's Proposal AI Assistant Beta V.1</h1>", unsafe_allow_html=True)

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

prompt_input = st.text_input("Enter the prompt for the AI:")
user_input = st.text_area("Paste the text you'd like Chancee's AI Bot to revise:", height=200)
submit_button = st.button("Submit")

# Set a default prompt
default_prompt = "Revise Axim's proposal sections for heightened clarity, structure, alignment with the proposal's specific requirements, and professional appeal, keeping in line with government contract proposal standards. If any sections contain parenthetical revision notes, such as (Make more relatable to clients' unique problems), integrate these revisions distinctly as per the comment. Apply principles of clarity, conciseness, order, and persuasion in your revision without explicitly mentioning them. Your tone should remain professional and concise, avoiding filler words, and the final text length should not deviate significantly from the original. Proceed with the following text for revision:"

# If the user hasn't provided a prompt, use the default
if prompt_input == '':
    prompt_input = default_prompt

if submit_button and user_input:
    with st.spinner("Generating revised text..."):
        revised_text, revision_length, revision_explanation = revise_text(prompt_input, user_input)
        time.sleep(1)  # Simulating some processing time, remove this line in the actual implementation

    st.markdown("### **Original Text:**")
    st.text_area("", value=user_input, height=200, max_chars=None, key=None)

    st.markdown("### **Revised Text:**")
    st.text_area("", value=revised_text, height=200, max_chars=None, key=None)  # Changed to text_area

    st.markdown("### **Revision Length:**")
    st.code(revision_length, language='')

    st.markdown("### **Revision Explanation:**")
    st.text_area("", value=revision_explanation, height=200, max_chars=None, key=None)