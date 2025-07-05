import pytesseract
import cv2
from gemini_config import call_gemini

def extract_timetable_text(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    text = pytesseract.image_to_string(gray) #extracts image from photo 
    return text


def make_day_routine(user_routine,timetable_text):
    prompt = f""" you are a daily planner ai agent for a student.
    create a detailed and productive schedule for the day using the following inputs and keep it concise for student to read fast.
    student routine:
    {user_routine}

    college timetable (optional):
    {timetable_text if timetable_text else 'N/A'}
    
    respond with the plan in bullet format including study , breaks and wellness and other relatable things."""
    
    return call_gemini(prompt) 
    