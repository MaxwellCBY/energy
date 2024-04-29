import streamlit as st
import pandas as pd
from PIL import Image
import time
# from openai import OpenAI
import re
import plotly.graph_objects as go


def load_text(file_path):
    """Utility function to load text from a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
    
def first_page():
    st.title('Public Info.')
    # st.write("公开信息包括在协会里的会员公司")

    with st.expander("Structure", expanded=False):

        image_path_1 = r'image\about\3.png'
        image_1 = Image.open(image_path_1)  
        st.image(image_1, caption="Member companies in the association.")

    # st.write("协会中注册的公司基本信息")
    st.markdown("<br><br>", unsafe_allow_html=True)  # Adds two line breaks 


    # Load data safely
    try:
        folder_path = r'F:\PhD\x\oilgas.xlsx'
        df = pd.read_excel(folder_path)
    except Exception as e:
        st.error(f"Failed to load data: {e}")
        st.stop()

    # Define a regex search function
    def regex_search(dataframe, query):
        try:
            pattern = re.compile(query, re.IGNORECASE)  # Compile a regex pattern, ignoring case
            return dataframe.apply(lambda row: row.astype(str).apply(lambda x: bool(pattern.search(x))).any(), axis=1)
        except re.error as e:
            st.error(f"Regex error: {e}")
            return pd.Series([False] * len(dataframe))

    # Get user input for keyword search
    keyword = st.text_input("Enter keywords to search (use comma for multiple keywords):", "")

    # Process multiple keywords
    if keyword:
        keywords = keyword.split(',')  # Split keywords by comma
        mask = pd.Series([True] * len(df))
        for key in keywords:
            key = key.strip()  # Remove leading/trailing whitespaces
            if key:
                current_mask = regex_search(df, key)
                mask &= current_mask  # Combine masks for all keywords using logical AND

        filtered_df = df[mask]

        # Check if the filtered dataframe is empty
        if filtered_df.empty:
            st.warning("No results found. Try different keywords or check for typos.")
        else:
            st.dataframe(filtered_df)
    else:
        # If no keyword is given, sample 10 random rows from the dataframe
        filtered_df = df.sample(10, random_state=1)  # Use a fixed seed for consistency
        st.dataframe(filtered_df)

    # --- this table doesn't allow to download the data
    # -------------------------------------------------

    # # Filter the dataframe based on the keyword search


    # # Create a Plotly table figure using graph_objects with enhanced styles for larger font sizes
    # fig = go.Figure(data=[go.Table(
    #     header=dict(
    #         values=list(filtered_df.columns),
    #         fill_color='navy',  # Darker header color
    #         align='center',
    #         font=dict(color='white', size=16)  # Increased font size for header
    #     ),
    #     cells=dict(
    #         values=[filtered_df[col] for col in filtered_df.columns],
    #         fill=dict(color=['paleturquoise', 'white']),  # Alternating row colors
    #         align='left',
    #         font=dict(color='black', size=14),  # Increased font size for cells
    #         height=30  # Adjust cell height for better readability
    #     )
    # )])

    # # Adjust table layout for a better visual appeal
    # fig.update_layout(
    #     margin=dict(l=10, r=10, t=10, b=10),  # Reducing the margin for a tighter fit
    #     paper_bgcolor="lightgray",  # Background color outside the table
    # )

    # # Display the table using Streamlit
    # st.plotly_chart(fig, use_container_width=True)



# mage a second page
def second_page():
    st.title('Member Public Info.')
    # st.write("会员可以查看该部分信息。")

    with st.expander("Structure", expanded=False):

        image_path_2 = r'image\about\5.png'
        image_2 = Image.open(image_path_2)
        st.image(image_2, caption="1- Platform AI understands the question, 2- Platform AI sends the question to companies' AIs, 3- Companies' AIs answer the question, 4- Platform AI summarizes the answers.")

    # st.write("会员可以利用AI顾问访问协会的半公开数据。")
    st.markdown("<br>", unsafe_allow_html=True)  # Adds two line breaks 

    # Initialize session state for login status if not already set
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if not st.session_state['logged_in']:
        # Login form
        with st.form("login_form"):
            username = st.text_input("Username", value="admin")
            password = st.text_input("Password", value = "admin", type="password")
            login_button = st.form_submit_button("Login")

            if login_button and username == "admin" and password == "admin":
                st.session_state['logged_in'] = True
                st.success("Login successful!")
            elif login_button:
                st.error("Invalid username or password. Please try again.")
    else:
        # st.write("AI顾问会帮助你寻找你需要的信息，请描述您需要的问题。")  
        st.markdown("<br><br><br>", unsafe_allow_html=True)  # Adds two line breaks 

        # Load content
        default_question = load_text('default_question.txt')
        AI_answer = load_text('AI_answer.txt')      

        # Input for AI assistant
        user_input = st.text_area(
            label="AI consultants can understand multiple languages, including Chinese, English, Japanese, and more. Please describe the issue you need assistance with.",
            value=default_question,
            key="query",
            height=200,
        )

        # Submit button for AI assistant query
        if st.button("Submit", key="get_response"):
            if user_input:
                # Display spinner while processing
                with st.spinner("Wait for it..."):
                    # Simulate a delay - replace this with your function call if needed
                    time.sleep(5)

                    # Store result in session state
                    st.session_state['result'] = AI_answer
                    st.header("AI-Consultant", divider="rainbow")

                    # Display the result with enhanced formatting
                    st.markdown(
                        f"<div style='background-color:#f0f2f6; padding:20px; border-radius:10px; font-size:16px;'>{st.session_state['result']}</div>",
                        unsafe_allow_html=True,
                    )

                # Flag to indicate response has been displayed
                st.session_state['response_displayed'] = True

        # add 2 line breaks
        st.markdown("<br><br>", unsafe_allow_html=True)  # Adds two line breaks
        # Conditional display of the button for private data access
        if st.session_state.get('response_displayed', False):
            if st.button("Apply for access to private data"):
                # Processing or showing additional information
                st.success("Your application has been submitted. Please check the status.")


# make a fourth page
def third_page():
    st.title('Protocol Public')
    # st.write("协议公开需要企业授权同意后您才可以继续咨询解决方案、或者报价。")

    with st.expander("Structure", expanded=False):
        image_path_3 = r'image\about\7.png'
        image_3 = Image.open(image_path_3)
        st.image(image_3, caption="After obtaining permission, you can continue to converse with the company's AI assistant to obtain more information.")

    # st.write("以下公司提供可能的解决方案，是否申请访问权限？")
    # write bold text
    # st.markdown("<br>", unsafe_allow_html=True)  # Adds two line breaks

    # load question
    q_privacy = load_text('private_question.txt')
    a_privacy = load_text('p_AI_answer.txt')
    st.header(" ", divider="rainbow")
    st.markdown(
                "**Company 1:** Application successful, you can continue to inquire about internal materials through the AI consultant.")

    # This button will toggle the state for showing the input area
    if st.button("AI-Consultant"):
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
                    time.sleep(1)  # Delay to simulate processing
                    # Display the result with enhanced formatting
                    st.markdown(
                        f"<div style='background-color:#f0f2f6; padding:20px; border-radius:10px; font-size:16px;'>{result}</div>",
                        unsafe_allow_html=True,
                    )

    st.markdown("<br>", unsafe_allow_html=True)  # Adds two line breaks

    st.markdown("**Company 2：** The application requires manual review. Please check your email later.")

    st.markdown("<br>", unsafe_allow_html=True)  # Adds two line breaks

    st.markdown("**Company 3：** Application failed, the company does not currently disclose this data information.")


# Dictionary of pages
pages = {

    "Public": first_page,
    "Member public": second_page,
    "Protocol public": third_page
}

def main():
    st.sidebar.title("Menu")
    selection = st.sidebar.radio("-", list(pages.keys()))

    # Display the selected page with the session state
    page = pages[selection]
    page()

if __name__ == "__main__":
    main()

