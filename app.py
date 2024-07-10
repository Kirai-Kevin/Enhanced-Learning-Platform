import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
from student_dashboard import student_dashboard
from teacher_dashboard import teacher_dashboard

load_dotenv()

SUBJECTS = [
    "Math", "English", "Kiswahili", "Geography", "Biology", "Physics", 
    "Chemistry", "CRE", "History", "Computer Studies", "Business", 
    "Agriculture", "French"
]

DIFFICULTY_LEVELS = ["Easy", "Medium", "Hard"]

# Configure the API key
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

def main():
    st.set_page_config(page_title="Enhanced Learning Platform (Gemini Pro)", page_icon=":books:", layout="wide")
    
    st.title("Enhanced Learning Platform")

    # Initialize session state
    if 'user_role' not in st.session_state:
        st.session_state.user_role = "Student"
    if 'student_progress' not in st.session_state:
        st.session_state.student_progress = {}
    if 'teacher_quizzes' not in st.session_state:
        st.session_state.teacher_quizzes = {}

    # Sidebar
    with st.sidebar:
        st.header("Settings")
        new_role = st.radio("Select your role:", ("Student", "Teacher"))
        if new_role != st.session_state.user_role:
            st.session_state.user_role = new_role
            st.experimental_rerun()
        
        selected_subject = st.selectbox("Select a subject:", SUBJECTS)
        difficulty = st.selectbox("Select difficulty:", DIFFICULTY_LEVELS)

    # Main content area
    if st.session_state.user_role == "Student":
        student_dashboard(selected_subject, difficulty)
    elif st.session_state.user_role == "Teacher":
        teacher_dashboard(selected_subject, difficulty)

if __name__ == "__main__":
    main()