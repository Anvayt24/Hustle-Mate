import schedule 
import time
import threading
import pywhatkit as kit
import yagmail
from datetime import datetime

reminders = []

def add_reminder(task : str, time_str : str, method: str = "email",contact: str = ""):
    reminders.append({
        "task": task,
        "time": time_str,
        "method": method,
        "contact": contact
    })
    return f"Reminder for '{task}' added at {time_str} by {method}."

def send_reminder(task,method,contact):
    message = f"Reminder: {task}"

    if method == "email":
        yag = yagmail.SMTP('your_email@gmail.com', 'your_password')
        yag.send(to=contact, subject="Reminder", contents=message)
        
    elif method == "whatsapp":
        hr, min = map(int, contact.split(':'))
        kit.sendwhatmsg(f"+91{contact}", message, hr, min)

def check_reminders():
    for reminder in reminders:
        task_time = datetime.strptime(reminder["time"], "%H:%M").time()
        schedule.every().day.at(reminder["time"]).do(
            send_reminder, 
            task=reminder["task"], 
            method=reminder["method"], 
            contact=reminder["contact"]
        )

def start_service():
    threading.Thread(target=check_reminders,daemon=True).start()        

def run_service():
    while True:
        schedule.run_pending()
        time.sleep(1)    

