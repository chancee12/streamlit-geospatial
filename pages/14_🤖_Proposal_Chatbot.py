import streamlit as st
import openai
import time

# Set up OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# GPT-3 model to use for text revision
model_engine = "text-davinci-003"

def revise_text(prompt, text_to_revise):
    revised_text_response = openai.Completion.create(
        engine=model_engine,
        prompt=f"{prompt}\n\n{text_to_revise}",
        max_tokens=2500,
        temperature=0.75
    )

    # Extract the revised text and strip leading and trailing white spaces.
    revised_text = revised_text_response['choices'][0]['text'].strip()

    revision_length_percentage = (len(revised_text) / len(text_to_revise)) * 100
    if revision_length_percentage > 100:
        revision_length = f"{round(revision_length_percentage - 100, 1)}% longer than original"
    else:
        revision_length = f"{round(100 - revision_length_percentage, 1)}% shorter than original"

    revision_explanation_response = openai.Completion.create(
        engine=model_engine,
        prompt=f"Alright dude, I need you to give me a chill, straight-to-the-point explanation in your best surfer lingo. We're looking at some major changes to this text, and I want you to break down why we made these changes, all while keeping the government contracting proposal guidelines in mind. So, let's dive in, man:\n\nOriginal: {text_to_revise}\n\nRevised: {revised_text}",
        max_tokens=1000,  # Increase max tokens for explanation
        temperature=0.85  # Decrease temperature to make output more focused
    )

    # Extract the revision explanation and strip leading and trailing white spaces.
    revision_explanation = revision_explanation_response['choices'][0]['text'].strip()

    return revised_text, revision_length, revision_explanation

def main_page():
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
if __name__ == "__main__":
    main_page()
