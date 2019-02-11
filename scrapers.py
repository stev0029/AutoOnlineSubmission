import re
import helpers

# Compile regex patterns
problemNo_pattern = re.compile(r'"status-(.+?)"')
output_pattern = re.compile(r'(?:<td><pre>.*?</pre></td>\s+){2}<td><pre>(.*?)</pre></td>', re.DOTALL)
class_name_pattern = re.compile(r"<div class='box'><code>(.*)\.java</code></div>")
token_pattern = re.compile(r'name="token" value="(.*)"')
submission_id_pattern = re.compile(r'ID is (.*)\.')
submission_result = re.compile(r'<td>Last Submission result:</td>\s+<td>(.*?)</td>', re.DOTALL)

def get_all_problemNo(main_page):
    return problemNo_pattern.findall(main_page.text)

def get_filtered_problemNo(main_page, predicate):
    return list(filter(predicate, get_all_problemNo(main_page)))

def get_outputs(problem_page):
    return [
        helpers.desanitized(s)
        for s in output_pattern.findall(problem_page.text)
    ]

def get_class_name(problem_page):
    match = class_name_pattern.search(problem_page.text)
    if match:
        return match.group(1)

def get_token(problem_page):
    match = token_pattern.search(problem_page.text)
    if match:
        return match.group(1)

def get_problem_payload(main_page, problemNo):
    payload_pattern = re.compile('id="try-' + problemNo + r'".*?(\{.+?\})', re.DOTALL)

    match = payload_pattern.search(main_page.text)
    if match:
        return eval(match.group(1))

def get_submission_id(submit_page):
    match = submission_id_pattern.search(submit_page.text)
    if match:
        return match.group(1)

def get_submission_result(problem_page):
    match = submission_result.search(problem_page.text)
    if match:
        return match.group(1)