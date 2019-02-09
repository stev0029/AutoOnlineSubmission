import re

# Compile regex patterns
problemNo_pattern = re.compile(r'"status-(.+?)"')
output_pattern = re.compile(r'(?:<td><pre>.*?</pre></td>\s+){2}<td><pre>(.*?)</pre></td>', re.DOTALL)
class_name_pattern = re.compile(r"<div class='box'><code>(.*)\.java</code></div>")
token_pattern = re.compile(r'name="token" value="(.*)"')
submission_id_pattern = re.compile(r'ID is (.*)\.')

def get_all_problemNo(main_page_text):
    return problemNo_pattern.findall(main_page_text)

def get_filtered_problemNo(main_page_text, filter_func):
    return list(filter(filter_func, get_all_problemNo(main_page_text)))

def get_outputs(problem_page_text):
    return [
        s.replace('<span class="paraMark">&middot;</span>', ' ')
        .replace('<span class="paraMark">&para;</span>', '')
        .replace('\n', '\\n')
        
        for s in output_pattern.findall(problem_page_text)
    ]

def get_class_name(problem_page_text):
    match = class_name_pattern.search(problem_page_text)
    if match:
        return match.group(1)

def get_token(problem_page_text):
    match = token_pattern.search(problem_page_text)
    if match:
        return match.group(1)

def get_problem_payload(main_page_text, problemNo):
    payload_pattern = re.compile('id="try-' + problemNo + r'".*?(\{.+?\})', re.DOTALL)

    match = payload_pattern.search(main_page_text)
    if match:
        return eval(match.group(1))

def get_submission_id(submit_page_text):
    match = submission_id_pattern.search(submit_page_text)
    if match:
        return match.group(1)