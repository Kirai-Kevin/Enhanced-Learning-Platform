import streamlit as st
from question_generation import generate_question, create_quiz
from ai_responses import answer_teacher_question

def teacher_dashboard(selected_subject, difficulty):
    st.header("Teacher Dashboard")

    tab1, tab2, tab3 = st.tabs(["Create Quiz", "View Quizzes", "Ask a Question"])

    with tab1:
        create_quiz_section(selected_subject, difficulty)

    with tab2:
        view_quizzes_section(selected_subject)

    with tab3:
        ask_question_section(selected_subject)

def create_quiz_section(selected_subject, difficulty):
    st.subheader("Create a Quiz")
    quiz_name = st.text_input("Quiz Name", f"{selected_subject} Quiz {len(st.session_state.teacher_quizzes) + 1}")
    num_questions = st.number_input("Number of Questions", min_value=1, max_value=10, value=5)
    if st.button("Create Quiz"):
        new_quiz = create_quiz(selected_subject, num_questions, difficulty)
        st.session_state.teacher_quizzes[quiz_name] = new_quiz
        st.success(f"Quiz '{quiz_name}' created successfully!")

    st.subheader("Generate Practice Question")
    if st.button("Generate Question"):
        question_answer = generate_question(selected_subject, difficulty)
        question, answer = question_answer.split("Answer:")
        st.write(f"Question: {question.replace('Question:', '').strip()}")
        st.write(f"Answer: {answer.strip()}")

def view_quizzes_section(selected_subject):
    st.subheader("Your Quizzes")
    for quiz_name, quiz in st.session_state.teacher_quizzes.items():
        if quiz_name.startswith(selected_subject):
            with st.expander(f"Quiz: {quiz_name}"):
                for i, q in enumerate(quiz, 1):
                    st.write(f"Q{i}: {q['question']}")
                    st.write(f"A: {q['answer']}")
                st.write("---")

def ask_question_section(selected_subject):
    st.subheader("Ask a Question")
    teacher_question = st.text_area("What's your question?")
    if st.button("Get Detailed Answer"):
        if teacher_question:
            answer = answer_teacher_question(selected_subject, teacher_question)
            st.write("Detailed Answer:")
            st.write(answer)
        else:
            st.warning("Please enter a question.")