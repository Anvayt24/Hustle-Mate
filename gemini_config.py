import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def call_gemini(prompt: str) -> str:
    model = genai.GenerativeModel("gemini-2.5-flash") #model to 2.5-flash
    
    response = model.generate_content(prompt)
    return response.text

print(call_gemini("What is the capital of France?"))
