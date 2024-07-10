import google.generativeai as genai

def get_gemini_response(prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text

def answer_student_question(subject, question):
    prompt = f"""
    As an educational AI assistant, provide a clear and concise answer to the following {subject} question for a high school student:

    {question}

    Your response should:
    1. Directly answer the question in simple terms.
    2. Be easy to understand for a high school student.
    3. Include a brief summary of key points for revision.

    Keep the entire response under 200 words.
    """
    return get_gemini_response(prompt)

def answer_teacher_question(subject, question):
    prompt = f"""
    As an educational AI assistant, provide a comprehensive answer to the following {subject} question for a high school teacher:

    {question}

    Your response should:
    1. Explain the concept in detail.
    2. Provide at least one academic reference related to the topic.
    3. Give two distinct examples to illustrate the concept.
    4. Suggest how this could be taught effectively in a classroom setting.

    Aim for a response of about 300-400 words.
    """
    return get_gemini_response(prompt)