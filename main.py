from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

app = FastAPI(
    title="OOP Learning API",
    description="An educational API to learn Object-Oriented Programming concepts",
    version="1.0.0"
)


# ============== MODELS ==============

class Difficulty(str, Enum):
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"


class Lesson(BaseModel):
    id: int
    title: str
    difficulty: Difficulty
    content: str
    code_example: str
    key_concepts: List[str]


class QuizQuestion(BaseModel):
    id: int
    question: str
    options: List[str]
    correct_answer: int
    explanation: str


class Quiz(BaseModel):
    id: int
    lesson_id: int
    title: str
    questions: List[QuizQuestion]


class QuizAnswer(BaseModel):
    question_id: int
    answer: int


class QuizSubmission(BaseModel):
    answers: List[QuizAnswer]


class QuizResult(BaseModel):
    score: int
    total: int
    percentage: float
    passed: bool
    feedback: List[str]


# ============== DATA ==============

lessons_db = [
    Lesson(
        id=1,
        title="Introduction to Classes and Objects",
        difficulty=Difficulty.BEGINNER,
        content="""
Classes are blueprints for creating objects. An object is an instance of a class.
A class defines attributes (data) and methods (functions) that objects of that class will have.

Key Points:
- A class is a template
- An object is a concrete instance created from a class
- Classes group related data and behavior together
- This helps organize code and make it reusable
        """,
        code_example="""
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says: Woof!"

# Creating objects (instances)
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.bark())  # Output: Buddy says: Woof!
print(dog2.bark())  # Output: Max says: Woof!
        """,
        key_concepts=["Class", "Object", "Instance", "Attributes", "Methods", "Constructor"]
    ),
    Lesson(
        id=2,
        title="Inheritance",
        difficulty=Difficulty.INTERMEDIATE,
        content="""
Inheritance allows a class to inherit attributes and methods from another class.
The class being inherited from is called the parent (or base) class.
The class that inherits is called the child (or derived) class.

Benefits:
- Code reusability: avoid repeating code
- Logical structure: represent real-world relationships
- Polymorphism: child classes can override parent methods
        """,
        code_example="""
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Some generic sound"

class Dog(Animal):
    def make_sound(self):
        return f"{self.name} says: Woof!"

class Cat(Animal):
    def make_sound(self):
        return f"{self.name} says: Meow!"

# Both inherit from Animal
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.make_sound())  # Buddy says: Woof!
print(cat.make_sound())  # Whiskers says: Meow!
        """,
        key_concepts=["Inheritance", "Parent Class", "Child Class", "Override", "super()"]
    ),
    Lesson(
        id=3,
        title="Encapsulation",
        difficulty=Difficulty.INTERMEDIATE,
        content="""
Encapsulation is the bundling of data (attributes) and methods into a single unit (class).
It also involves hiding internal details from the outside world using access modifiers.

In Python:
- Public: accessible from anywhere (no prefix)
- Protected: intended for internal use (_prefix)
- Private: not accessible outside the class (__prefix)

Benefits:
- Data protection: control how data is accessed and modified
- Data hiding: expose only necessary interfaces
- Maintainability: change internal implementation without affecting external code
        """,
        code_example="""
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited: ${amount}"
        return "Invalid amount"

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew: ${amount}"
        return "Insufficient funds"

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
print(account.deposit(500))  # Deposited: $500
print(account.get_balance())  # 1500
# account.__balance = -1000  # Error: Cannot access private attribute
        """,
        key_concepts=["Encapsulation", "Access Modifiers", "Private", "Protected", "Public", "Getters", "Setters"]
    ),
    Lesson(
        id=4,
        title="Polymorphism",
        difficulty=Difficulty.ADVANCED,
        content="""
Polymorphism means "many forms". It allows objects of different types to be treated as objects of a common parent type.
There are two main types: compile-time (method overloading) and runtime (method overriding).

Benefits:
- Write flexible and reusable code
- Use a single interface for different data types
- Makes code extensible and maintainable
        """,
        code_example="""
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Polymorphism in action
shapes = [Circle(5), Rectangle(4, 6)]

for shape in shapes:
    print(f"Area: {shape.area()}")  # Calls appropriate method
        """,
        key_concepts=["Polymorphism", "Method Overriding", "Interface", "Dynamic Dispatch"]
    ),
    Lesson(
        id=5,
        title="Abstraction",
        difficulty=Difficulty.ADVANCED,
        content="""
Abstraction is the concept of hiding complex implementation details and showing only the necessary features.
It focuses on what an object does rather than how it does it.

In Python, we use abstract classes and abstract methods to enforce abstraction.

Benefits:
- Reduce complexity by hiding implementation details
- Define a clear interface for subclasses
- Enforce consistency across implementations
        """,
        code_example="""
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        return "Car engine started"

    def stop(self):
        return "Car engine stopped"

class Bike(Vehicle):
    def start(self):
        return "Bike engine started"

    def stop(self):
        return "Bike engine stopped"

# Cannot instantiate abstract class
# vehicle = Vehicle()  # Error

car = Car()
print(car.start())  # Car engine started
        """,
        key_concepts=["Abstraction", "Abstract Class", "Abstract Method", "ABC", "Interface"]
    )
]

quizzes_db = [
    Quiz(
        id=1,
        lesson_id=1,
        title="Classes and Objects Quiz",
        questions=[
            QuizQuestion(
                id=1,
                question="What is a class in OOP?",
                options=[
                    "An instance of an object",
                    "A blueprint for creating objects",
                    "A method of a program",
                    "A type of variable"
                ],
                correct_answer=1,
                explanation="A class is a blueprint or template that defines the structure and behavior for objects."
            ),
            QuizQuestion(
                id=2,
                question="What is an object?",
                options=[
                    "A collection of variables",
                    "An instance of a class",
                    "A function definition",
                    "A data type"
                ],
                correct_answer=1,
                explanation="An object is a concrete instance created from a class. It has actual values for the attributes defined in the class."
            ),
            QuizQuestion(
                id=3,
                question="What does __init__ do in a class?",
                options=[
                    "Initializes the program",
                    "Deletes an object",
                    "Constructs and initializes a new object",
                    "Returns a value"
                ],
                correct_answer=2,
                explanation="__init__ is the constructor method that initializes a new object when it's created."
            )
        ]
    ),
    Quiz(
        id=2,
        lesson_id=2,
        title="Inheritance Quiz",
        questions=[
            QuizQuestion(
                id=1,
                question="What is inheritance?",
                options=[
                    "Passing money to children",
                    "A child class inheriting attributes and methods from a parent class",
                    "Creating multiple objects",
                    "Copying code from one file to another"
                ],
                correct_answer=1,
                explanation="Inheritance allows a class (child) to inherit attributes and methods from another class (parent)."
            ),
            QuizQuestion(
                id=2,
                question="What is the main benefit of inheritance?",
                options=[
                    "It makes code longer",
                    "It helps organize imports",
                    "Code reusability and logical structure",
                    "It slows down execution"
                ],
                correct_answer=2,
                explanation="Inheritance promotes code reusability and creates a logical hierarchical structure."
            )
        ]
    )
]


# ============== ENDPOINTS ==============

@app.get("/")
async def root():
    """Welcome endpoint with API information"""
    return {
        "message": "Welcome to OOP Learning API",
        "version": "1.0.0",
        "endpoints": {
            "lessons": "/lessons",
            "lesson_by_id": "/lessons/{lesson_id}",
            "lessons_by_difficulty": "/lessons/difficulty/{difficulty}",
            "quizzes": "/quizzes",
            "quiz": "/quizzes/{quiz_id}",
            "submit_quiz": "/quizzes/{quiz_id}/submit"
        }
    }


# ============== LESSON ENDPOINTS ==============

@app.get("/lessons", response_model=List[Lesson])
async def get_all_lessons():
    """Get all OOP lessons"""
    return lessons_db


@app.get("/lessons/{lesson_id}", response_model=Lesson)
async def get_lesson(lesson_id: int):
    """Get a specific lesson by ID"""
    lesson = next((l for l in lessons_db if l.id == lesson_id), None)
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    return lesson


@app.get("/lessons/difficulty/{difficulty}", response_model=List[Lesson])
async def get_lessons_by_difficulty(difficulty: Difficulty):
    """Get lessons filtered by difficulty level"""
    filtered = [l for l in lessons_db if l.difficulty == difficulty]
    return filtered


@app.get("/lessons/search")
async def search_lessons(keyword: str):
    """Search lessons by keyword"""
    keyword_lower = keyword.lower()
    results = [
        {
            "id": l.id,
            "title": l.title,
            "difficulty": l.difficulty,
            "matching_concepts": [c for c in l.key_concepts if keyword_lower in c.lower()]
        }
        for l in lessons_db
        if keyword_lower in l.title.lower() or keyword_lower in l.content.lower()
    ]
    return results


# ============== QUIZ ENDPOINTS ==============

@app.get("/quizzes", response_model=List[Quiz])
async def get_all_quizzes():
    """Get all available quizzes"""
    return quizzes_db


@app.get("/quizzes/{quiz_id}", response_model=Quiz)
async def get_quiz(quiz_id: int):
    """Get a specific quiz by ID"""
    quiz = next((q for q in quizzes_db if q.id == quiz_id), None)
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")
    return quiz


@app.get("/quizzes/lesson/{lesson_id}", response_model=List[Quiz])
async def get_quizzes_for_lesson(lesson_id: int):
    """Get all quizzes for a specific lesson"""
    quizzes = [q for q in quizzes_db if q.lesson_id == lesson_id]
    return quizzes


@app.post("/quizzes/{quiz_id}/submit", response_model=QuizResult)
async def submit_quiz(quiz_id: int, submission: QuizSubmission):
    """Submit quiz answers and get results"""
    quiz = next((q for q in quizzes_db if q.id == quiz_id), None)
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")

    score = 0
    feedback = []

    for answer in submission.answers:
        question = next((q for q in quiz.questions if q.id == answer.question_id), None)
        if not question:
            continue

        if answer.answer == question.correct_answer:
            score += 1
            feedback.append(f"Q{answer.question_id}: ✓ Correct! {question.explanation}")
        else:
            feedback.append(f"Q{answer.question_id}: ✗ Incorrect. {question.explanation}")

    total = len(quiz.questions)
    percentage = (score / total * 100) if total > 0 else 0
    passed = percentage >= 70

    return QuizResult(
        score=score,
        total=total,
        percentage=round(percentage, 2),
        passed=passed,
        feedback=feedback
    )


# ============== PROGRESS TRACKING ==============

@app.get("/progress/summary")
async def get_progress_summary():
    """Get summary of available lessons and quizzes"""
    return {
        "total_lessons": len(lessons_db),
        "lessons_by_difficulty": {
            "beginner": len([l for l in lessons_db if l.difficulty == Difficulty.BEGINNER]),
            "intermediate": len([l for l in lessons_db if l.difficulty == Difficulty.INTERMEDIATE]),
            "advanced": len([l for l in lessons_db if l.difficulty == Difficulty.ADVANCED])
        },
        "total_quizzes": len(quizzes_db),
        "total_quiz_questions": sum(len(q.questions) for q in quizzes_db)
    }


# ============== LEARNING PATH ==============

@app.get("/learning-path")
async def get_learning_path():
    """Get recommended learning path for OOP"""
    return {
        "title": "Complete OOP Learning Path",
        "description": "A recommended progression to learn OOP concepts",
        "path": [
            {
                "step": 1,
                "lesson_id": 1,
                "title": "Introduction to Classes and Objects",
                "difficulty": "beginner",
                "time_estimate": "30 minutes"
            },
            {
                "step": 2,
                "lesson_id": 2,
                "title": "Inheritance",
                "difficulty": "intermediate",
                "time_estimate": "40 minutes"
            },
            {
                "step": 3,
                "lesson_id": 3,
                "title": "Encapsulation",
                "difficulty": "intermediate",
                "time_estimate": "40 minutes"
            },
            {
                "step": 4,
                "lesson_id": 4,
                "title": "Polymorphism",
                "difficulty": "advanced",
                "time_estimate": "45 minutes"
            },
            {
                "step": 5,
                "lesson_id": 5,
                "title": "Abstraction",
                "difficulty": "advanced",
                "time_estimate": "45 minutes"
            }
        ]
    }


