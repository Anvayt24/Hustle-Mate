from classroom_api import fetch_classroom_assignments
from gemini_config import call_gemini

def get_assignments_from_classroom(_: str = "") -> str:
    data = fetch_classroom_assignments()
    if not data:
        return "No assignments found."

    formatted_data = "\n\n".join([
        f"📘 Course: {a['course']}\n📝 Title: {a['title']}\n🗓️ Due: {a['due_date']}\n🔗 Link: {a['link']}" 
        for a in data
    ])

    prompt = f"Summarize the following assignment list and highlight urgent ones:\n{formatted_data}"
    response = call_gemini(prompt)
    return response