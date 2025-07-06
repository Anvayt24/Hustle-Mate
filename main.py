from autogen import UserProxyAgent, register_function 
from agents import get_planner_agent 
from planner_tools import extract_timetable_text, make_day_routine
from study_tool import explain_concept, generate_notes, generate_flashcards, generate_quiz, extract_text_from_image, add_doubt, get_doubts
from agents import get_study_agent
from agents import get_assignment_agent
from assignment_tool import get_assignments_from_classroom
from agents import get_reminder_agent
from reminder_tools import add_reminder , start_service , check_reminders
try:
    image_path = "timetable/timetable.jpg"
    timetable_text = extract_timetable_text(image_path)
except Exception as e:
    print(f"Timetable image not found or error in OCR: {e}")
    timetable_text = None

user_routine = input("enter your daily routine: ")

user = UserProxyAgent(
    name="StudentUser",
    human_input_mode="ALWAYS",
    code_execution_config={"work_dir": "coding", "use_docker": False}
)
# planner agent functions
planner = get_planner_agent()
study= get_study_agent()

def generate_day_plan(routine: str) -> str:
    return make_day_routine(routine, timetable_text) # tool using gemini llm

register_function(
    generate_day_plan,
    caller=planner,  # The planner agent will "call" or suggest this function
    executor=user,   # The user agent will "execute" this function
    name="generate_day_plan",
    description="Generates a student day plan based on a given routine and available timetable information."
)
 # study agent functions
register_function(
    explain_concept,
    caller = study,
    executor = user,
    name="explain_concept",
    description="Explains a concept simply to a student."
)
register_function(
    generate_notes,
    caller = study,
    executor = user,
    name="generate_notes",
    description="Generates concise study notes on a given topic."
)
register_function(
    generate_flashcards,
    caller = study,
    executor = user,
    name="generate_flashcards",
    description="Generates flashcards (question and answer pairs) for a given topic."
)
register_function(
    generate_quiz,
    caller = study,
    executor = user,
    name="generate_quiz",
    description="Generates a quiz with multiple choice questions for a given topic."
)
register_function(
    extract_text_from_image,
    caller = study,
    executor = user,
    name="extract_text_from_image",
    description="Extracts text from an image using OCR."
)
register_function(
    add_doubt,
    caller = study,
    executor = user,
    name="add_doubt",
    description="Adds a question to the list of doubts."
)
register_function(
    get_doubts,
    caller = study,
    executor = user,
    name="get_doubts",
    description="Retrieves the list of doubts added by the user."
)

# assignment agent functions 
assignment = get_assignment_agent()
register_function(
    get_assignments_from_classroom,
    caller=assignment,
    executor=user,
    name="get_assignments_from_classroom",
    description="Fetches and summarizes assignments from Google Classroom."
)
# reminder agent functions
reminder = get_reminder_agent()
register_function(
    add_reminder,
    caller=reminder,
    executor=user,
    name="add_reminder",
    description="Adds a reminder for a task at a specified time via email or WhatsApp."
)   
start_service()

user.initiate_chat(
    planner,
    message=f"plan my day on this routine: {user_routine}"
)

user.initiate_chat(
    study,
    message="I need help with my studies. I have some doubts and need explanations on various topics."
)

user.initiate_chat(
    assignment,
    message="I need to check my assignments from Google Classroom and summarize them."
)
user.initiate_chat(
    reminder,
    message="I want to set reminders for my tasks via email or WhatsApp."
)

