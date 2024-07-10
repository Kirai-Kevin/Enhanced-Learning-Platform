from ai_responses import get_gemini_response

def generate_question(subject, difficulty):
    prompt = f"Generate a short {difficulty.lower()} {subject} question suitable for a high school student. Format as 'Question: [question] Answer: [answer]'"
    return get_gemini_response(prompt)

def check_answer(question, user_answer):
    prompt = f"""
    Question: {question}
    User's Answer: {user_answer}

    Is the user's answer correct? Respond with either 'Correct' or 'Incorrect', followed by a brief explanation and the correct answer if the user's answer is incorrect.
    """
    return get_gemini_response(prompt)

def create_quiz(subject, num_questions, difficulty):
    quiz = []
    for _ in range(num_questions):
        question_answer = generate_question(subject, difficulty)
        question, answer = question_answer.split("Answer:")
        quiz.append({
            "question": question.replace("Question:", "").strip(),
            "answer": answer.strip()
        })
    return quiz