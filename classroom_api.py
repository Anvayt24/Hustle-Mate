from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/classroom.student-submissions.me.readonly","https://www.googleapis.com/auth/classroom.courses.readonly"]

def fetch_classroom_assignments():
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)
    service = build('classroom', 'v1', credentials=creds)

    assignments = []
    courses = service.courses().list().execute().get('courses', []) # get list of courses

    for course in courses:
        coursework = service.courses().courseWork().list(courseId=course['id']).execute().get('courseWork', []) # get work for each course
        for work in coursework:
            assignments.append({
                'course': course['name'],
                'title': work['title'],
                'due_date': work.get('dueDate', {}),
                'description': work.get('description', 'No description'),
                'link': work.get('alternateLink', '')
            })
    return assignments