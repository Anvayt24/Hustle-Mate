import os
from autogen import AssistantAgent

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


#planner agent
def get_planner_agent():
    return AssistantAgent(
        name="PlannerAgent",
        system_message="You are a helpful agent that creates productive student day plans using the available tool.",
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
        description="An AI agent that helps students with study-related tasks such as explaining concepts, generating notes, flashcards, quizzes, and managing doubts.",
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
        description="An AI agent that fetches and summarizes assignments from Google Classroom.",
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
        description="An AI agent that helps students set and manage reminders for tasks via email or WhatsApp.",
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