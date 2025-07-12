import os
from autogen import AssistantAgent

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


#planner agent
def get_planner_agent():
    return AssistantAgent(
        name="PlannerAgent",
        system_message= """You are a smart planner agent for students. 
When a user describes their day or study plan, you must:
1. Generate a detailed schedule using the tool 'generate_day_plan'.
2. If the user mentions any topic to revise or quiz, call the appropriate tools from the StudyAgent like 'generate_notes' or 'generate_quiz'.
3. If the user asks to track assignments, call 'get_assignments_from_classroom' using AssignmentAgent.
4. If reminders are needed, call 'add_reminder' using ReminderAgent.
5. After study or assignment tasks, call 'progress_log' and optionally 'send_progress_report'.

Do all these automatically based on the users message without asking them again.
"""
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

# study agent 

def get_study_agent():
    return AssistantAgent(
        name="studyagent",
        system_message="An AI agent that helps students with study-related tasks such as explaining concepts, generating notes, flashcards, quizzes, and managing doubts, You are an agent that can collaborate with other agents in the group to complete tasks.",
        llm_config={
            "config_list":[
                {
                    "model": "gemini-2.5-flash",
                    "api_key": GEMINI_API_KEY,
                    "base_url": "https://generativelanguage.googleapis.com/v1beta/openai",
                    "api_type": "openai",
                }
            ]
        }
    )  

#assignment agent 

def get_assignment_agent():
    return AssistantAgent(
        name="AssignmentAgent",
        system_message="An AI agent that fetches and summarizes assignments from Google Classroom, You are an agent that can collaborate with other agents in the group to complete tasks.",
        llm_config={
            "config_list": [
                {
                    "model": "gemini-2.5-flash",
                    "api_key": GEMINI_API_KEY,
                    "base_url": "https://generativelanguage.googleapis.com/v1beta/openai",
                    "api_type": "openai",
                    "price" : [0.001, 0.002],
                }
            ]
        }
    )

#reminder agent
def get_reminder_agent():
    return AssistantAgent(
        name="ReminderAgent",
        system_message="An AI agent that helps students set and manage reminders for tasks via email or WhatsApp, You are an agent that can collaborate with other agents in the group to complete tasks.",
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

# progress reprot agent 

def get_progress_agent():
    return AssistantAgent(
        name="ProgressAgent",
        system_message="An AI agent that tracks and reports student progress, allowing them to log tasks and receive updates via email or WhatsApp, You are an agent that can collaborate with other agents in the group to complete tasks.",
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