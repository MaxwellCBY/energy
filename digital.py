import streamlit as st
import pandas as pd
from PIL import Image
import time
from openai import OpenAI
import plotly.figure_factory as ff
# import plotly.graph_objects as go

# # Set your OpenAI API key and assistant ID here
# api_key = st.secrets["openai_apikey"]
# assistant_id = st.secrets["assistant_id_data"]

# Set openAi client , assistant ai and assistant ai thread
# @st.cache_resource
# def load_openai_client_and_assistant():
#     client = OpenAI(api_key=api_key)
#     my_assistant = client.beta.assistants.retrieve(assistant_id)
#     thread = client.beta.threads.create()

#     return client, my_assistant, thread

# client, my_assistant, assistant_thread = load_openai_client_and_assistant()


# # check in loop  if assistant ai parse our request
# def wait_on_run(run, thread):
#     while run.status == "queued" or run.status == "in_progress":
#         run = client.beta.threads.runs.retrieve(
#             thread_id=thread.id,
#             run_id=run.id,
#         )
#         time.sleep(0.5)
#     return run


# # initiate assistant ai response
# def get_assistant_response(user_input=""):
#     message = client.beta.threads.messages.create(
#         thread_id=assistant_thread.id,
#         role="user",
#         content=user_input,
#     )

#     run = client.beta.threads.runs.create(
#         thread_id=assistant_thread.id,
#         assistant_id=assistant_id,
#     )

#     run = wait_on_run(run, assistant_thread)

#     # Retrieve all the messages added after our last user message
#     messages = client.beta.threads.messages.list(
#         thread_id=assistant_thread.id, order="asc", after=message.id
#     )

#     return messages.data[0].content[0].text.value


def load_text(file_path):
    """Utility function to load text from a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def platform_AI():
    st.title('May I help you?')

    # Load content
    default_question = load_text('questions_digital/default_question.txt')

    # User input
    user_input = st.text_area(
        label="AI consultant can understand multiple languages, including Chinese, English, Japanese, and more. Please describe the issue you need assistance with.",
        value=default_question,
        key="query",
        height=200,
    )

    # Submit button for AI assistant query
    if st.button("Submit", key="get_response"):
        # add a spinner
        with st.spinner("Processing..."):
        # wait for 5 seconds
            time.sleep(5)
        if user_input:
            # Store that submit was clicked to render subsequent content
            st.session_state['submitted'] = True

    # Check if the submit button was clicked
    if st.session_state.get('submitted', False):
        st.header("AI-Consultant", divider="rainbow")

        # Expanders for video content
        with st.expander("Company A"):
            # insert a video
            st.video("image/1.mp4")
        with st.expander("Company B"):
            # insert a image
            image2 = Image.open("image/3.png")
            st.image(image2, caption="Product", use_column_width=True)
        with st.expander("Company C"):
            # insert a image
            image3 = Image.open("image/3D.png")
            st.image(image3, caption="Product", use_column_width=True)

        st.subheader("Continue with Company AI", divider="rainbow")
        # st.write("The selected companies provide possible solutions. Would you like to apply for access?")
        
        # Button to apply
        if st.button("Apply", key="apply_button"):
            st.session_state['application_submitted'] = True

    # Check if application has been submitted and show the message
    if st.session_state.get('application_submitted', False):
        st.write("Your application has been submitted. Please check the status in <Company AI>.")



q_privacy = load_text('questions_digital/private_question.txt')
a_privacy = load_text('questions_digital/p_AI_answer.txt')


# make a fourth page
def company_AI():
    st.title('Company AI')


    st.write("The Company AI will answer your question based on the company's own knowledge base.")
    # write bold text
    # st.markdown("<br>", unsafe_allow_html=True)  # Adds two line breaks


    st.header("Application status", divider="rainbow")
    st.markdown(
                "**A Company:** Application successful, you can continue to inquire about internal materials through the AI consultant.")

    # This button will toggle the state for showing the input area
    if st.button("A Company AI]"):
        st.session_state['show_input'] = not st.session_state.get('show_input', False)

    # Check if the session state has been set to show input area
    if st.session_state.get('show_input', False):
        # Make a text area for input
        user_privacy = st.text_area(
            label="Please describe the specific information you need from the company.",
            value=st.session_state.get('q_privacy', q_privacy),  # Default value set to an empty string if not already in session_state
            key="q_privacy",
            height=200,
        )

        # Make a button for submitting the query
        if st.button("Submit Query"):
            # Assuming 'answer_privacy' is predefined somewhere in your code or session state
            if 'answer_privacy' not in st.session_state:
                st.session_state['answer_privacy'] = a_privacy

            if user_privacy:  # Checking if input was provided
                # Display spinner while processing
                with st.spinner("Processing..."):
                    result = st.session_state['answer_privacy']
                    st.header("AI-Consultant", divider="rainbow")
                    time.sleep(5)  # Delay to simulate processing
                    # Display the result with enhanced formatting
                    st.markdown(
                        f"<div style='background-color:#f0f2f6; padding:20px; border-radius:10px; font-size:16px;'>{result}</div>",
                        unsafe_allow_html=True,
                    )

    st.markdown("<br>", unsafe_allow_html=True)  # Adds two line breaks

    st.markdown("**B Company：** The application requires manual review. Please check your email later.")

    st.markdown("<br>", unsafe_allow_html=True)  # Adds two line breaks

    st.markdown("**C Company：** Application failed, the company does not currently disclose this data information.")


def base_page():
    st.title("Member Space")
    st.write("This is the member space where you can manage your local AI.")

    # Load the content of 'p_AI_answer.txt' into a variable
    cmeta = load_text('questions_digital/meta.txt')  

    # add a expander with a text area
    with st.expander("Meta Data"):
        st.write("You can manage your company's public information here.")
        st.text_area("Introduction", key="question1", value=cmeta)
        st.button("Update", key="update1")

    # add a expander with a upload file widget
    with st.expander("Knowledge Base"):
        st.write("You can upload the knowledge file.")
        st.file_uploader("Upload file", type=["csv", "txt", "pdf", "xlsx", "docx"])
        st.button("Update", key="update2")

    # add a expander with a button
    with st.expander("Setup local AI"):
        st.write("You can manage the local AI here.")
        # add a slider
        st.slider("Parameter 1", 1, 10, 2)
        st.slider("Parameter 2", 50, 200, 80)
        st.button("Update", key="update3")
    # add a expander with a button
    with st.expander("Record"):
        st.write("You can view which company has communicated with your AI.")
        # insert a table
        data = {'Company': ['Company 1', 'Company 2', 'Company 3'],
                'Hostory': ['10 rounds of conversation', '2 rounds of conversation', '21 rounds of conversation'],
                'Time': ['2024-03-01 1:00', '2024-03-02 12:00', '2024-05-03 6:00'],
                'Contact': ['enter1@m.com', '+47 96704305', 'enter3@m.com']}
        df = pd.DataFrame(data)
        st.table(df)
        st.button("Download", key="update4")



# Dictionary of pages
pages = {
    "Platform AI": platform_AI,
    "Company AI": company_AI,
    "Member space": base_page,
}

def main():
    st.sidebar.title("Menu")
    selection = st.sidebar.radio("-", list(pages.keys()))

    # Display the selected page with the session state
    page = pages[selection]
    page()

if __name__ == "__main__":
    main()

