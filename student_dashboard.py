import streamlit as st
from question_generation import generate_question, check_answer
from ai_responses import answer_student_question

def student_dashboard(selected_subject, difficulty):
    st.header("Student Dashboard")
    
    tab1, tab2, tab3 = st.tabs(["Practice", "Progress", "Ask a Question"])
    
    with tab1:
        practice_section(selected_subject, difficulty)
    
    with tab2:
        progress_section()
    
    with tab3:
        ask_question_section(selected_subject)

def practice_section(selected_subject, difficulty):
    st.subheader("Practice Questions")
    if st.button("Generate Practice Question"):
        question_answer = generate_question(selected_subject, difficulty)
        question, answer = question_answer.split("Answer:")
        st.session_state.current_question = question.replace("Question:", "").strip()
        st.session_state.current_answer = answer.strip()

    if 'current_question' in st.session_state:
        st.write(f"Question: {st.session_state.current_question}")
        user_answer = st.text_input("Your answer:")
        if st.button("Submit Answer"):
            result = check_answer(st.session_state.current_question, user_answer)
            st.write(result)
            
            # Update progress
            if selected_subject not in st.session_state.student_progress:
                st.session_state.student_progress[selected_subject] = {"correct": 0, "total": 0}
            st.session_state.student_progress[selected_subject]["total"] += 1
            if "Correct" in result:
                st.session_state.student_progress[selected_subject]["correct"] += 1

    quiz_section(selected_subject)

def progress_section():
    st.subheader("Your Progress")
    for subject, progress in st.session_state.student_progress.items():
        correct = progress["correct"]
        total = progress["total"]
        if total > 0:
            percentage = (correct / total) * 100
            st.progress(percentage / 100)
            st.write(f"{subject}: {correct}/{total} ({percentage:.2f}%)")

def ask_question_section(selected_subject):
    st.subheader("Ask a Question")
    student_question = st.text_area("What's your question?")
    if st.button("Get Answer"):
        if student_question:
            answer = answer_student_question(selected_subject, student_question)
            st.write("Answer:")
            st.write(answer)
        else:
            st.warning("Please enter a question.")

def quiz_section(selected_subject):
    st.subheader("Take a Quiz")
    available_quizzes = [quiz for quiz in st.session_state.teacher_quizzes.keys() if quiz.startswith(selected_subject)]
    if available_quizzes:
        selected_quiz = st.selectbox("Select a quiz:", available_quizzes)
        if st.button("Start Quiz"):
            st.session_state.current_quiz = st.session_state.teacher_quizzes[selected_quiz]
            st.session_state.quiz_answers = []
            st.session_state.quiz_index = 0

        if 'current_quiz' in st.session_state:
            if st.session_state.quiz_index < len(st.session_state.current_quiz):
                question = st.session_state.current_quiz[st.session_state.quiz_index]["question"]
                st.write(f"Question {st.session_state.quiz_index + 1}: {question}")
                answer = st.text_input(f"Your answer for question {st.session_state.quiz_index + 1}:")
                if st.button("Next Question"):
                    st.session_state.quiz_answers.append(answer)
                    st.session_state.quiz_index += 1
                    if st.session_state.quiz_index < len(st.session_state.current_quiz):
                        st.experimental_rerun()
                    else:
                        st.write("Quiz completed! Here are your results:")
                        correct = 0
                        for i, (q, a) in enumerate(zip(st.session_state.current_quiz, st.session_state.quiz_answers)):
                            result = check_answer(q["question"], a)
                            st.write(f"Question {i + 1}: {result}")
                            if "Correct" in result:
                                correct += 1
                        st.write(f"Final Score: {correct}/{len(st.session_state.current_quiz)}")
                        del st.session_state.current_quiz
                        del st.session_state.quiz_answers
                        del st.session_state.quiz_index
            else:
                st.write("Quiz completed!")
    else:
        st.write("No quizzes available for this subject.")