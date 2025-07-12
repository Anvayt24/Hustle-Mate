import os
from autogen import AssistantAgent

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


#planner agent
def get_planner_agent():
    return AssistantAgent(
        name="PlannerAgent",
        system_message="You are a helpful agent that creates productive student day plans using the available tool. You are an agent that can collaborate with other agents in the group to complete tasks.",
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