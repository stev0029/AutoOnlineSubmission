import helpers
import scrapers
import submission_session as sess

BASE_TEMPLATE = 'base_template/min.java'
OUT_PATH = 'out'
DELAY = 2000

sess.login('stev0029', 'stev0029')
main_page = sess.main_page()

for problemNo in scrapers.get_all_problemNo(main_page.text):
    # Using the problem page to scrape required `class_name` and `case_outputs`
    problem_page = sess.problem_page(problemNo)

    # Pre-generate class/source names and paths
    class_name = scrapers.get_class_name(problem_page.text)
    source_name = class_name + '.java'
    source_path = OUT_PATH + '/' + source_name

    # Generate specific timing and outputs
    coded_start = helpers.current_millis() + DELAY
    case_outputs = scrapers.get_outputs(problem_page.text)
    total_ms = 800

    # Make key -> value replacement dict, for java source code
    key_value = {
        'CLASS_NAME': class_name,
        'CODED_START': helpers.java_long(coded_start),
        'CASE_OUTPUTS': helpers.java_string_array(case_outputs),
        'TOTAL_MS': helpers.java_int(total_ms),
    }

    # Pre-process base template, replace all occurrences of `$key$` based on `key_value` dict
    with open(BASE_TEMPLATE) as infile, open(source_path, 'w') as outfile:
        for line in infile:
            for key, value in key_value.items():
                line = line.replace("$%s$" % key, value)
            outfile.write(line)
    
    # Submit
    token = scrapers.get_token(problem_page.text)
    submission_id = sess.upload_submission(problemNo, token, source_name, source_path)
    
    print(submission_id)

sess.logout()