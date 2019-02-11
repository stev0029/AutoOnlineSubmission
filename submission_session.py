import requests
import urllib3
import scrapers
import functools

def subdir(page):
    return ROOT + '/' + page

def logged_in():
    return 'PHPSESSID' in s.cookies.keys()

def login_required(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not logged_in():
            raise Exception('Login required')
        return func(*args, **kwargs)
    return wrapper


ROOT = 'https://sel-w1.dynip.ntu.edu.sg'

s = requests.Session()
s.verify = False
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def login(loginIDOrEmail, password):
    login_payload = {
        'loginIDOrEmail': loginIDOrEmail,
        'password': password,
        'todo': 'login',
    }
    s.post(subdir('Login.php'), data=login_payload)

    if not logged_in():
        raise Exception('Login failed')

@login_required
def logout():
    s.get(subdir('Logout.php'))

@login_required
def main_page():
    return s.get(subdir('StudentMain.php'))

@login_required
def problem_page(problemNo):
    payload = scrapers.get_problem_payload(main_page(), problemNo)
    if not payload:
        raise Exception('Payload for problemNo: ' + problemNo + ' not found')
    
    return s.post(subdir('StudentTry.php'), data=payload)

@login_required
def upload_submission(problemNo, token, source_name, source_path, comment=''):
    submission_data = {
        'comment': comment,
        'problemNo': problemNo,
        'token': token,
        'todo': 'processSubmission',
    }
    submission_files = {
        'upFile0': (source_name, open(source_path), 'application/octet-stream'),
    }

    submit_page = s.post(subdir('StudentProcessSubmit.php'), files=submission_files, data=submission_data)

    submission_id = scrapers.get_submission_id(submit_page)
    if not submission_id:
        raise Exception('Submission failed, no submission ID found')
    
    return submission_id

@login_required
def error_log(submissionNo, token):
    submission_payload = {
        'submissionNo': submissionNo,
        'token': token,
        'todo': 'viewErrorLog',
    }

    return s.post(subdir('StudentReview.php'), data=submission_payload).text

@login_required
def change_email(email):
    payload = {
        'email': email,
        'todo': 'changeEmail',
    }
    return s.post(subdir('Settings.php'), data=payload)