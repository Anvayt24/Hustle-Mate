import pytesseract
import cv2
from gemini_config import call_gemini 

def explain_concept(topic: str) -> str:
    prompt = f"Explain the following concept in simple terms for a student:\n\n{topic}"
    return call_gemini(prompt)

def generate_notes(keywords: str) -> str:
    prompt = f"Create concise study notes on the topic: {keywords}"
    return call_gemini(prompt)

def generate_flashcards(topic: str) -> str:
    prompt = f"Create flashcards (question and answer pairs) for the topic: {topic}"
    return call_gemini(prompt)

def generate_quiz(topic: str) -> str:
    prompt = f"Create 5 multiple choice questions with answers for the topic: {topic}"
    return call_gemini(prompt)

def extract_text_from_image(image_path: str) -> str:
    try :
        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
        text = pytesseract.image_to_string(gray)  # Extracts text from the image
        return text
    except Exception as e:
        print(f"no image provided or error : {e}")
        return None
    
doubt_list = []
def add_doubt(question: str) -> str:
    doubt_list.append(question)
    return f"doubt added: {question}"
def get_doubts() -> str:
    if not doubt_list:
        return "No doubts added yet."
    return "\n".join(f"{i+1}. {q}" for i, q in enumerate(doubt_list))


