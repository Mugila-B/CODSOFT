import streamlit as st
import datetime


st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Smart Chatbot")
st.write("This is a simple virtual assistant chatbot built using Streamlit. How may I assist you today?")


if "messages" not in st.session_state:
    st.session_state.messages = []


for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])


user_input = st.chat_input("Type your message...")


def bot_reply(text):
    text = text.lower().strip()
    words = text.split()

    
    if "hi" in words or "hello" in words:
        return "Hello. How may I assist you today?"

    
    elif "my name is" in text:
        name = text.split("my name is")[-1].strip().title()
        st.session_state.name = name
        return f"Nice to meet you, {name}. How can I assist you today?"

    elif "what is my name" in text:
        return f"Your name is {st.session_state.get('name', 'not available at the moment.')}"

    
    elif "how are you" in text:
        return "I am functioning properly. How may I assist you further?"

    elif "what can you do" in text:
        return "I can assist you with general questions, provide basic information, and engage in simple conversations."

    elif "who are you" in text:
        return "I am a virtual assistant chatbot designed to help answer your queries."

    
    elif "help" in text:
        return "Certainly. Please let me know your query, and I will do my best to assist you."

    
    elif "time" in text:
        return f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}"

    elif "date" in text:
        return f"Today's date is {datetime.datetime.now().strftime('%Y-%m-%d')}"

    
    elif "python" in text:
        return "Python is a high-level programming language known for its simplicity and readability."

    elif "machine learning" in text:
        return "Machine learning is a field of artificial intelligence that enables systems to learn from data."

    
    elif "weather" in text:
        return "I currently do not have real-time weather data, but I can assist with general queries."

    
    elif "thank you" in text:
        return "You're welcome. If you need any further assistance, feel free to ask."

    elif "sorry" in words:
        return "No problem at all. How can I assist you further?"

    
    elif "bye" in words or "goodbye" in words:
        return "Thank you for your time. Have a great day."

    
    else:
        return "I'm sorry, I did not understand your request. Could you please rephrase it?"


if user_input and user_input.strip() != "":

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    
    with st.chat_message("user"):
        st.write(user_input)

   
    reply = bot_reply(user_input)

    
    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })

    
    with st.chat_message("assistant"):
        st.write(reply)
        
