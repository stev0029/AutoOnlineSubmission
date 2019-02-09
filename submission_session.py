import requests
import re
import urllib3
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
def problem_page(id):
    expr_post_data = 'id="try-' + id + r'".*?(\{.+?\})'
    match_post_data = re.search(expr_post_data, main_page().text, re.DOTALL)
    if not match_post_data:
        raise Exception('Problem ID ' + id + ' not found')

    raw_post_data = match_post_data.group(1)
    post_data = eval(raw_post_data)
    return s.post(subdir('StudentTry.php'), data=post_data)

@login_required
def upload_submission(id, token, source_name, source_path, comment=''):
    submission_data = {
        'comment': '',
        'problemNo': id,
        'token': token,
        'todo': 'processSubmission',
    }
    submission_files = {
        'upFile0': (source_name, open(source_path), 'application/octet-stream'),
    }

    submit = s.post(subdir('StudentProcessSubmit.php'), files=submission_files, data=submission_data)
    submit_id_match = re.search(r'ID is (.*)\.', submit.text)
    if not submit_id_match:
        raise Exception('Submission failed, no submission ID found')
    
    submission_id = submit_id_match.group(1)
    return submission_id