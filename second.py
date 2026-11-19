import streamlit as st
from groq import Groq

# Initialize the Groq client
GROQ_API_KEY = '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'
client = Groq(api_key=GROQ_API_KEY)
MODEL="openai/gpt-oss-120b"

def get_groq_response(question):
    messages = [
        {
            "role": "system",
            "content": "You are a chat bot designed only to answer questions about Data Scientist Akshay Gujare. You do not know anything else. If someone asks questions on topics apart from Akshay Gujare, just say you don't know."
        },
        {
            "role": "user",
            "content": question,
        }
    ]

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        max_tokens=4096
    )

    return response.choices[0].message.content

# Streamlit app title
st.title("Domain-Specific AI Chatbot")
st.subheader("Akshay Gujare AI Biography & Career Assistant")

# Display an image placeholder
st.image("6339009801051903327.jpg", width=400, caption="Akshay Gujare")

# Input box for user query
query = st.text_input("Enter your query about Akshay Gujare :")

# Button to get response
if st.button("Search"):
    if query:
        # Get the response from the Groq model
        response = get_groq_response(query)
        # Display the response
        st.write("Response:", response)
    else:
        st.write("Please enter a query.")

# Additional Streamlit widgets for beautification
st.sidebar.header("About This App")
st.sidebar.markdown('<div class="sidebar-text">This app allows you to ask questions about the Data Scientist. Feel free to explore and learn more about his career and achievements!</div>', unsafe_allow_html=True)


