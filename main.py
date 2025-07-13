from autogen import  UserProxyAgent, register_function 
from agents import get_planner_agent 
from planner_tools import extract_timetable_text, make_day_routine
from study_tool import explain_concept, generate_notes, generate_flashcards, generate_quiz, extract_text_from_image, add_doubt, get_doubts
from agents import get_study_agent , get_assignment_agent, get_reminder_agent, get_progress_agent , get_coordinator_agent 
from assignment_tool import get_assignments_from_classroom
from reminder_tools import add_reminder , start_service , check_reminders
from progress_tools import progress_log, get_progress, send_progress
from autogen import GroupChat , GroupChatManager
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s - %(asctime)s] %(message)s',
    datefmt='%H:%M:%S'
)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

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

# coordinator agent
master_agent = get_coordinator_agent()

# planner agent functions
planner = get_planner_agent()
study= get_study_agent()

def generate_day_plan(routine: str) -> str:
    return make_day_routine(routine, timetable_text) # tool using gemini llm

register_function(
    generate_day_plan,
    caller=master_agent,  # The planner agent will "call" or suggest this function
    executor=planner,   # The user agent will "execute" this function
    name="generate_day_plan",
    description="Generates a student day plan based on a given routine and available timetable information."
)
 # study agent functions
register_function(
    explain_concept,
    caller = master_agent,
    executor = study,
    name="explain_concept",
    description="Explains a concept simply to a student."
)
register_function(
    generate_notes,
    caller = master_agent,
    executor = study,
    name="generate_notes",
    description="Generates concise study notes on a given topic."
)
register_function(
    generate_flashcards,
    caller = master_agent,
    executor = study,
    name="generate_flashcards",
    description="Generates flashcards (question and answer pairs) for a given topic."
)
register_function(
    generate_quiz,
    caller = master_agent,
    executor = study,
    name="generate_quiz",
    description="Generates a quiz with multiple choice questions for a given topic."
)
register_function(
    extract_text_from_image,
    caller = master_agent,
    executor = study,
    name="extract_text_from_image",
    description="Extracts text from an image using OCR."
)
register_function(
    add_doubt,
    caller = master_agent,
    executor = study,
    name="add_doubt",
    description="Adds a question to the list of doubts."
)
register_function(
    get_doubts,
    caller = master_agent,
    executor = study,
    name="get_doubts",
    description="Retrieves the list of doubts added by the user."
)

# assignment agent functions 
assignment = get_assignment_agent()
register_function(
    get_assignments_from_classroom,
    caller=master_agent,
    executor=assignment,
    name="get_assignments_from_classroom",
    description="Fetches and summarizes assignments from Google Classroom."
)
# reminder agent functions
reminder = get_reminder_agent()
register_function(
    add_reminder,
    caller=master_agent,
    executor= reminder,
    name="add_reminder",
    description="Adds a reminder for a task at a specified time via email or WhatsApp."
)   
start_service()

# progress agent functions
progress = get_progress_agent() #instance of progress agent

register_function(
    progress_log,
    caller=master_agent,
    executor=progress,
    name="progress_log",
    description="Logs the progress of a task with its status and timestamp."
)

register_function(
    get_progress,
    caller=master_agent,
    executor=progress,
    name="get_progress_report",
    description="Retrieves the logged progress of tasks."
)
register_function(
    send_progress,
    caller=master_agent,
    executor=progress,
    name="send_progress_report",
    description="Sends the progress report via email or WhatsApp."
)

# connecting all agents to the user
groupchat = GroupChat(
    agents=[user, planner, reminder, assignment, study, progress],
    messages=[],
    max_round=20
)

manager = GroupChatManager(
    groupchat=groupchat,
    llm_config={
            "config_list": [
                {
                    "model": "gemini-2.5-flash",
                    "api_key": GEMINI_API_KEY,
                    "base_url": "https://generativelanguage.googleapis.com/v1beta/openai",
                    "api_type": "openai",
                }
            ]
    }
)

user.initiate_chat(
    manager,
    message=f"plan my day on this routine: {user_routine}"
)




