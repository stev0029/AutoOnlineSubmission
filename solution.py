import helpers
import scrapers

BASE_TEMPLATE = 'base_template/mintest.java'
OUT_PATH = 'out'
DELAY_MS = 2000
RUN_MS = 800


def make(class_name, case_outputs):
    source_name = class_name + '.java'
    source_path = OUT_PATH + '/' + source_name

    java_source_table = {
        'CLASS_NAME': class_name,
        'CODED_START': helpers.java_long(helpers.current_millis + DELAY_MS),
        'CASE_OUTPUTS': helpers.java_string_array(case_outputs),
        'RUN_MS': helpers.java_int(RUN_MS)
    }

    # Pre-process base template
    # Replace all occurrences of `$key$` based on `java_source_table` dict
    with open(BASE_TEMPLATE) as infile, open(source_path, 'w') as outfile:
        for line in infile:
            for key, value in java_source_table.items():
                line = line.replace("$%s$" % key, value)
            outfile.write(line)

    return source_name, source_path
