# Enhanced Learning Platform

## Overview

The Enhanced Learning Platform is an interactive educational tool designed to support both students and teachers in the learning process. It leverages AI technology to generate practice questions, create quizzes, and provide detailed answers to subject-specific queries. The platform aims to enhance the learning experience by offering personalized practice sessions, progress tracking, and comprehensive resources for educators.

## Current Features

- **Dual Interface**: Separate dashboards for students and teachers
- **Subject Selection**: Support for multiple subjects including Math, English, Kiswahili, and more
- **Difficulty Levels**: Questions can be generated at Easy, Medium, or Hard levels
- **Student Features**:
  - Practice question generation
  - Answer submission and feedback
  - Progress tracking
  - Quiz-taking functionality
  - AI-assisted question answering
- **Teacher Features**:
  - Quiz creation tool
  - Practice question generation
  - Detailed AI-assisted answers for complex topics
- **Language Detection**: Supports questions and answers in English, Swahili, and French
- **AI Integration**: Utilizes Google's Gemini Pro AI model for content generation

## Future Features

- Integration with learning management systems
- Personalized learning paths based on student performance
- Collaborative learning tools for group study
- Mobile app version for on-the-go learning
- Advanced analytics for teachers to track class performance

## Technologies Used

- Python
- Streamlit
- Google Generative AI (Gemini Pro)
- dotenv for environment variable management

## Getting Started

To run the Enhanced Learning Platform on your local machine, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   - Create a `.env` file in the root directory
   - Add your Gemini API key:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```

4. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

5. Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`)

6. Select your role (Student or Teacher) and start using the platform!

## Contributors

- [Your Name]
- [Other Contributors]

We welcome contributions to the Enhanced Learning Platform! If you'd like to contribute, please fork the repository and submit a pull request with your changes.

```

This README provides a comprehensive overview of your project, highlighting its key features, technologies used, and instructions for getting started. You can customize it further by adding specific details about your development process, licensing information, or any other relevant details about the Enhanced Learning Platform.