import os
from autogen import AssistantAgent

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

#coordinator agent
def get_coordinator_agent():
    return AssistantAgent(
        name="CoordinatorAgent",
        system_message="""
You are a smart student assistant who coordinates multiple agents:
- PlannerAgent (for creating day plans)
- StudyAgent (for notes, quizzes)
- AssignmentAgent (for tracking assignments)
- ReminderAgent (for scheduling reminders)
- ProgressAgent (for logging progress)

When a user describes their day or tasks, your job is to:
1. Understand the request.
2. Call appropriate tools from other agents.
3. Do not ask the user again; handle everything autonomously.

Examples:
- If 'revise neural networks' → call generate_notes from StudyAgent.
- If 'take quiz on CNN' → call generate_quiz from StudyAgent.
- If 'track assignment on AI' → call get_assignments from AssignmentAgent.
- If 'remind me at 4PM' → call add_reminder from ReminderAgent.
- If 'log progress' → call progress_log from ProgressAgent.
""",
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


#planner agent
def get_planner_agent():
    return AssistantAgent ( 
        name="PlannerAgent",
        system_message= "You are a smart planner agent for students that plans their study schedule, You are an agent that can collaborate with other agents in the group to complete tasks.",
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