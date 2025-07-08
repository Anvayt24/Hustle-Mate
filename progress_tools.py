from datetime import datetime
import smtplib
import pywhatkit as kit
progress_log = []

def progress_log(task:str , status:str)-> str:
    progress_log.append({
        "task": task,
        "status": status,
        "timestamp": datetime.now().isoformat()
    })

def get_progress(_:str = "") -> str:
    if not progress_log:
        return "No progress logged yet."
    
    lines = [
        f"{i+1}. [{entry['time'][:19]}] {entry['task']} → {entry['status']}"
        for i, entry in enumerate(progress_log)
    ]
    return "📊 Your Progress:\n" + "\n".join(lines)

def send_progress(method: str, contact: str="") -> str:
    report = get_progress()
    
    if method == "email":
        sender = "youremail@gmail.com"
        password = "yourpassword"  # or use app password
        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
                smtp.starttls()
                smtp.login(sender, password)
                smtp.sendmail(sender, contact, f"Subject: Your Progress Report\n\n{report}")
            return "📧 Progress report sent via email."
        except Exception as e:
            return f"Email failed: {e}"

    elif method == "whatsapp":
        try:
            now = datetime.now()
            kit.sendwhatmsg(contact, report, now.hour, (now.minute + 1) % 60)
            return "📱 Progress report scheduled to send on WhatsApp."
        except Exception as e:
            return f"WhatsApp failed: {e}"

    return "Invalid method. Use 'email' or 'whatsapp'."