import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# # Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# # Configure Gemini
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# # Streamlit Page Config
st.set_page_config(page_title="📚 Topic-Wise Notes Generator")
st.title("🧠 Topic-Wise Notes Generator using Gemini AI")
st.markdown("Enter any topic and get well-structured, student-friendly notes.")

# # Input field
user_topic = st.text_input("Enter your topic here:")

 # Language selector (optional)
language = st.selectbox("Select Language", ["English", "Hindi", "Spanish"], index=0)

 # Button to generate notes
if st.button("Generate Notes") and user_topic:
     with st.spinner("Generating your notes..."):
         prompt = f"""
         Generate detailed notes on the topic: {user_topic}
         Structure:
         1. Definition
         2. Key Concepts
         3. Real-world Examples
         4. FAQs or Short MCQs with answers
         5. Summary

         Language: {language}
         Audience: High school/college students
         Output must be easy to understand and structured.
         """
         try:
             response = model.generate_content(prompt)
             st.subheader("📄 Your AI-Generated Notes:")
             st.write(response.text)
         except Exception as e:
            st.error(f"Error: {str(e)}")

 # Footer
st.markdown("---")
st.caption("Powered by Google Gemini AI | Created by Group 62")