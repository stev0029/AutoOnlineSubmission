import helpers
import scrapers

BASE_TEMPLATE = 'base_template/min.java'
OUT_PATH = 'out'
DELAY = 2000

def replacement_table(problem_page):
    # Using the problem page to scrape required `class_name` and `case_outputs`
    # Generate specific timing and outputs
    class_name = scrapers.get_class_name(problem_page)
    coded_start = helpers.current_millis() + DELAY
    case_outputs = scrapers.get_outputs(problem_page)
    total_ms = 800

    # key -> value replacement dict, for java source code
    return {
        'CLASS_NAME': class_name,
        'CODED_START': helpers.java_long(coded_start),
        'CASE_OUTPUTS': helpers.java_string_array(case_outputs),
        'TOTAL_MS': helpers.java_int(total_ms),
    }

def make(class_name, replacement_table):
    source_name = class_name + '.java'
    source_path = OUT_PATH + '/' + source_name

    # Pre-process base template, replace all occurrences of `$key$` based on `replacement_table` dict
    with open(BASE_TEMPLATE) as infile, open(source_path, 'w') as outfile:
        for line in infile:
            for key, value in replacement_table.items():
                line = line.replace("$%s$" % key, value)
            outfile.write(line)
    
    return source_name, source_path