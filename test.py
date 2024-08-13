
import google.generativeai as genai
import streamlit as st

# Your Google API key (note: never hardcode sensitive keys in production code)
google_api_key = "AIzaSyCE8AZZ3TQjuXG7FNgXsvo43V67bAp0OqM"

# Configure the Generative AI model
genai.configure(api_key=google_api_key)

# Model initiation
model = genai.GenerativeModel('gemini-1.5-flash')

# Function to get response from the model
def getresponsefromModel(user_input):
    response = model.generate_content(user_input)
    return response.text

# Streamlit app interface
st.title("Ahmadgpt")
st.write("Made by Ahmad Muaz")

# Text input widget for user input
user_input = st.text_input("Enter your prompt:")

# Generate response if there is user input
if user_input:
    output = getresponsefromModel(user_input)
    st.write("Response:")
    st.write(output)