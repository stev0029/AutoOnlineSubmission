import time
import re

def current_millis():
    return int(round(time.time() * 1000))

def get_available_id(main_page_text):
    return re.findall(r'"status-(.+?)"', main_page_text)

def get_outputs(problem_page_text):
    return [
        s.replace('<span class="paraMark">&middot;</span>', ' ')
        .replace('<span class="paraMark">&para;</span>', '')
        .replace('\n', '\\n')
        
        for s in re.findall(
            r'(?:<td><pre>.*?</pre></td>\s+){2}<td><pre>(.*?)</pre></td>',
            problem_page_text,
            re.DOTALL
        )
    ]

def get_class_name(problem_page_text):
    return re.search(r"<div class='box'><code>(.*)\.java</code></div>", problem_page_text).group(1)

def get_token(problem_page_text):
    return re.search(r'name="token" value="(.*)"', problem_page_text).group(1)

def java_string_array(list):
    return 'new String[]{"%s"}' % '", "'.join([str(e) for e in list])

def java_long(num):
    return str(num) + 'L'

def java_int(num):
    return str(num)