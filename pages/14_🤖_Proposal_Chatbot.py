import streamlit as st
import openai
import time

def app():
    # Set up OpenAI API key
    openai.api_key = st.secrets["OPENAI_API_KEY"]

    # GPT-3 model to use for text revision
    model_engine = "text-davinci-003"

    st.title("Chancee's Proposal AI Assistant Beta V.1")
    st.write('This AI assistant is designed specifically to revise government contracting proposals.')
    
    st.markdown('''
    ## **Prompt Guidance**
    The prompt box allows you to specify how you want the AI to approach revising your text. If you leave it blank, the default prompt, which instructs the AI to revise for clarity, structure, alignment with proposal requirements, professional appeal, and so on, will be used. If you enter your own prompt, it will replace the default and guide the AI's revision process. Remember, the AI is quite flexible, so feel free to get creative with your prompts!
    ''')

    def revise_text(prompt, text_to_revise):
        revised_text_response = openai.Completion.create(
            engine=model_engine,
            prompt=f"{prompt}\n\n{text_to_revise}",
            max_tokens=2500,
            temperature=0.75
        )

        # Extract the revised text and strip leading and trailing white spaces.
        revised_text = revised_text_response['choices'][0]['text'].strip()

        # ... Continue the rest of the revise_text function ...

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
        st.text_area("", value=revised_text, height=200, max_chars=None, key=None)

        st.markdown("### **Revision Length:**")
        st.code(revision_length, language='')

        st.markdown("### **Revision Explanation:**")
        st.text_area("", value=revision_explanation, height=200, max_chars=None, key=None)
