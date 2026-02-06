# OOP Learning API - FastAPI Backend

A comprehensive FastAPI backend for teaching Object-Oriented Programming concepts to students. This API provides lessons, quizzes, code examples, and learning paths for mastering OOP principles.

## Features

- **5 Core Lessons**: Covering Classes & Objects, Inheritance, Encapsulation, Polymorphism, and Abstraction
- **Interactive Quizzes**: Multiple-choice quizzes with explanations for each lesson
- **Difficulty Levels**: Beginner, Intermediate, and Advanced content
- **Code Examples**: Practical Python code examples for each concept
- **Learning Paths**: Recommended progression through OOP concepts
- **Quiz Submission**: Get immediate feedback with percentage scores
- **Search Functionality**: Find lessons by keywords and concepts
- **Progress Tracking**: Monitor overall learning progress

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. **Clone or download the project**
```bash
cd oop-learning-api
```

2. **Create a virtual environment** (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

## Running the Server

```bash
python main.py
```

The API will be available at `http://localhost:8000`

### Interactive Documentation
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## API Endpoints

### Lessons

**Get All Lessons**
```
GET /lessons
```
Returns all available OOP lessons with full details.

**Get Specific Lesson**
```
GET /lessons/{lesson_id}
```
Returns a single lesson by ID (1-5).

**Get Lessons by Difficulty**
```
GET /lessons/difficulty/{difficulty}
```
Filter lessons by difficulty level: `beginner`, `intermediate`, or `advanced`.

**Search Lessons**
```
GET /lessons/search?keyword={keyword}
```
Search lessons by title, content, or concepts.

### Quizzes

**Get All Quizzes**
```
GET /quizzes
```
Returns all available quizzes.

**Get Specific Quiz**
```
GET /quizzes/{quiz_id}
```
Returns a single quiz with all questions and options.

**Get Quizzes for Lesson**
```
GET /quizzes/lesson/{lesson_id}
```
Returns quizzes related to a specific lesson.

**Submit Quiz Answers**
```
POST /quizzes/{quiz_id}/submit
```

Request body:
```json
{
  "answers": [
    {
      "question_id": 1,
      "answer": 1
    },
    {
      "question_id": 2,
      "answer": 2
    }
  ]
}
```

Response:
```json
{
  "score": 2,
  "total": 2,
  "percentage": 100.0,
  "passed": true,
  "feedback": [
    "Q1: ✓ Correct! A class is a blueprint...",
    "Q2: ✓ Correct! An object is an instance..."
  ]
}
```

### Learning Resources

**Get Learning Path**
```
GET /learning-path
```
Returns the recommended progression for learning OOP.

**Get Progress Summary**
```
GET /progress/summary
```
Returns statistics about available lessons and quizzes.

## Usage Examples

### Python Client Example

```python
import requests

BASE_URL = "http://localhost:8000"

# Get all lessons
response = requests.get(f"{BASE_URL}/lessons")
lessons = response.json()
print(f"Found {len(lessons)} lessons")

# Get a specific lesson
lesson = requests.get(f"{BASE_URL}/lessons/1").json()
print(f"Lesson: {lesson['title']}")
print(f"Content: {lesson['content']}")
print(f"Code Example:\n{lesson['code_example']}")

# Get beginner lessons only
beginner_lessons = requests.get(f"{BASE_URL}/lessons/difficulty/beginner").json()
print(f"Beginner lessons: {len(beginner_lessons)}")

# Get quiz for lesson
quizzes = requests.get(f"{BASE_URL}/quizzes/lesson/1").json()
quiz = quizzes[0]

# Submit quiz answers
submission = {
    "answers": [
        {"question_id": 1, "answer": 1},
        {"question_id": 2, "answer": 1},
        {"question_id": 3, "answer": 2}
    ]
}
result = requests.post(f"{BASE_URL}/quizzes/1/submit", json=submission).json()
print(f"Score: {result['score']}/{result['total']} ({result['percentage']}%)")
print(f"Passed: {result['passed']}")
for feedback in result['feedback']:
    print(f"  {feedback}")

# Get learning path
path = requests.get(f"{BASE_URL}/learning-path").json()
for step in path['path']:
    print(f"Step {step['step']}: {step['title']} ({step['difficulty']})")
```

### JavaScript/Fetch Example

```javascript
const BASE_URL = 'http://localhost:8000';

// Get all lessons
async function getLessons() {
  const response = await fetch(`${BASE_URL}/lessons`);
  const lessons = await response.json();
  console.log('Lessons:', lessons);
}

// Submit quiz
async function submitQuiz(quizId, answers) {
  const submission = { answers };
  const response = await fetch(`${BASE_URL}/quizzes/${quizId}/submit`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(submission)
  });
  const result = await response.json();
  console.log(`Score: ${result.score}/${result.total} (${result.percentage}%)`);
}

// Get learning path
async function getLearningPath() {
  const response = await fetch(`${BASE_URL}/learning-path`);
  const path = await response.json();
  console.log('Learning Path:', path);
}

getLessons();
```

## Available Lessons

### 1. Introduction to Classes and Objects (Beginner)
Learn the fundamentals of OOP: what classes are, how to create objects, and understand attributes and methods.

### 2. Inheritance (Intermediate)
Understand how classes can inherit from other classes to promote code reusability and create logical hierarchies.

### 3. Encapsulation (Intermediate)
Learn to bundle data and methods together, and control access with public, protected, and private attributes.

### 4. Polymorphism (Advanced)
Explore how different objects can respond to the same method calls in different ways.

### 5. Abstraction (Advanced)
Master the art of hiding complexity by defining abstract classes and methods.

## API Response Format

All endpoints return JSON responses. Here's the structure for lessons:

```json
{
  "id": 1,
  "title": "Introduction to Classes and Objects",
  "difficulty": "beginner",
  "content": "...",
  "code_example": "...",
  "key_concepts": ["Class", "Object", "Instance", "Attributes", "Methods"]
}
```

Quiz questions are formatted as:

```json
{
  "id": 1,
  "question": "What is a class in OOP?",
  "options": [
    "An instance of an object",
    "A blueprint for creating objects",
    "A method of a program",
    "A type of variable"
  ],
  "correct_answer": 1,
  "explanation": "A class is a blueprint..."
}
```

## Error Handling

The API returns appropriate HTTP status codes:

- **200**: Success
- **404**: Resource not found (lesson or quiz doesn't exist)
- **422**: Validation error (invalid request format)

Example error response:
```json
{
  "detail": "Lesson not found"
}
```

## Extending the API

### Add a New Lesson

Edit `main.py` and add to the `lessons_db` list:

```python
Lesson(
    id=6,
    title="Your Lesson Title",
    difficulty=Difficulty.BEGINNER,
    content="Your lesson content...",
    code_example="Your code example...",
    key_concepts=["Concept1", "Concept2"]
)
```

### Add a New Quiz

Edit `main.py` and add to the `quizzes_db` list:

```python
Quiz(
    id=3,
    lesson_id=1,
    title="Your Quiz Title",
    questions=[
        QuizQuestion(
            id=1,
            question="Your question?",
            options=["Option A", "Option B", "Option C", "Option D"],
            correct_answer=1,
            explanation="Why this is correct..."
        )
    ]
)
```

## Project Structure

```
oop-learning-api/
├── main.py              # Main FastAPI application
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Technology Stack

- **Framework**: FastAPI
- **Server**: Uvicorn
- **Data Validation**: Pydantic
- **Language**: Python 3.8+

## Performance

- In-memory data storage for instant responses
- No database overhead for quick learning
- Fast JSON serialization with Pydantic
- Suitable for classroom or small-scale deployments

## Future Enhancements

- Persistent database integration (PostgreSQL, MongoDB)
- User authentication and progress tracking
- More lessons and quizzes
- Difficulty-based recommendations
- Explanation videos/links
- Code execution environment
- Real-time collaborative features
- Mobile app integration

## License

This project is open source and available for educational purposes.

## Support

For issues or questions, please refer to the interactive API documentation:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Contributing

To add more lessons or quizzes, edit the respective `_db` lists in `main.py` and restart the server.

---

Happy Learning! 🚀