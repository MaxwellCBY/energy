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



def first_page():
    st.title('Public Info.')
    # st.write("公开信息包括在协会里的会员公司")

    with st.expander("Structure", expanded=False):

        image_path_1 = 'image/about/3.png'
        image_1 = Image.open(image_path_1)  
        st.image(image_1, caption="Member companies in the association.")

    # st.write("协会中注册的公司基本信息")
    st.markdown("<br><br>", unsafe_allow_html=True)  # Adds two line breaks 

    # load data
    folder_path = '数创协会/demo.xlsx'
    df = pd.read_excel(folder_path)
    # User input for keyword search
    keyword = st.text_input("Key words:", "")
    # Filter the dataframe if keyword is not empty
    if keyword:
        # This will apply the filter across all columns
        filtered_df = df[df.apply(lambda row: row.astype(str).str.contains(keyword).any(), axis=1)]
    else:
        filtered_df = df
    # Create a Plotly table figure
    table_fig = ff.create_table(filtered_df)
    # Display using Streamlit
    st.plotly_chart(table_fig, use_container_width=True)


### question in the seconde page
# Default question
default_question = """ I want to turn an anime IP into a game for children. Which company can give me advice on this?

我想将一个动漫IP做成一个适合儿童的游戏，请问哪个公司可以给我这方面的建议呢？

私はアニメIPを子供向けのゲームにしたいと思っていますが、どの会社がこの件についてアドバイスを提供できますか？
"""

# pre-defined answer
AI_answer = """

**Company 1:**
- **Case Study 1:** The "Happy Little Sprite" series games are a successful case of transforming a well-known animation IP into children’s games. Through careful market positioning and educational content design, combined with highly interactive game mechanics and child-friendly interface design, it effectively attracts the target user group. The game development team focuses on user experience, strictly adheres to children's online safety regulations, and ensures the game's continuous attraction and educational value through regular updates and feedback loops. Additionally, through a cross-media marketing strategy, the game not only won widespread praise from children and parents but also achieved good market performance.

**Company 2:**
- **Case Study 1:** The company focuses on developing children’s games with strong narrative elements and role-playing components. They are known for "Adventure Island Treasure Hunt," a game that combines traditional stories with modern educational concepts, beloved by children and parents alike. The game design emphasizes emotional development and the cultivation of social skills, helping children learn cooperation and empathy through character interaction and problem-solving tasks.
- **Case Study 2:** The company's recently launched "Virtual Zoo" project uses VR (Virtual Reality) technology, allowing children to get close to animals in a virtual environment and learn about biodiversity. This immersive learning experience effectively enhances children’s interest in natural sciences. As VR technology continues to mature, the Tongqu Game Development Group plans to expand its types of educational games to include more content about science and history.

**Company 3:**
- **Case Study 1:** The company is committed to developing educational programming games that allow children to learn coding and mathematical logic while playing. Its flagship "Code Hero" not only teaches basic programming concepts but also motivates children to create their own mini-games. The game uses a modular design, allowing the unlocking of more advanced programming challenges progressively based on the child's learning progress.
- **Case Study 2:** The company recently partnered with educational institutions to launch the "Robot Engineer" series of games, which teach mechanical and electronic knowledge through building and programming virtual robots. The company plans to use artificial intelligence technology to further optimize the game’s personalized learning paths, making them better fit each child's learning style and pace.
"""


# mage a second page
def second_page():
    st.title('Member Public Info.')
    # st.write("会员可以查看该部分信息。")

    with st.expander("Structure", expanded=False):

        image_path_2 = 'image/about/5.png'
        image_2 = Image.open(image_path_2)
        st.image(image_2, caption="1- Platform AI understands the question, 2- Platform AI sends the question to the member company's AI, 3- Member AI answers the question, 4- Platform AI summarizes the answer.")

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

q_privacy = "What is the budget range and timeline for developing such games? Is it possible to adjust the development plan based on different budgets?"
a_privacy = """

The specific budget range and timeline for developing the "Happy Little Sprite" series games:

**Budget Range:** The total budget for developing the "Happy Little Sprite" series games is approximately $2.6 million to $3.5 million. This budget includes all stages from the initial concept design, art production, programming, testing, to final release and marketing. The major costs within the budget include team salaries, technology licensing fees, outsourcing services, and marketing expenses.

-**Timeline:**The entire development cycle from project initiation to game release lasted about 15 months. This includes initial market research and concept validation (about 3 months), the main development phase (about 9 months), and the final testing and adjustment phase (about 3 months).
These budget and timeline estimates are based on our team's experience and the specific needs of the project. The specifics of each game project may vary depending on factors such as the complexity of the game, required features, and target platforms. We always work closely with clients to adjust the project plan based on actual circumstances, ensuring the success of the project and adherence to the budget.
"""
# make a fourth page
def third_page():
    st.title('Protocol Public')
    # st.write("协议公开需要企业授权同意后您才可以继续咨询解决方案、或者报价。")

    with st.expander("Structure", expanded=False):
        image_path_3 = 'image/about/7.png'
        image_3 = Image.open(image_path_3)
        st.image(image_3, caption="After obtaining permission, you can continue to converse with the company's AI assistant to obtain more information.")

    # st.write("以下公司提供可能的解决方案，是否申请访问权限？")
    # write bold text
    # st.markdown("<br>", unsafe_allow_html=True)  # Adds two line breaks


    st.header("", divider="rainbow")
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

