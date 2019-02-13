import time


def current_millis():
    return int(round(time.time() * 1000))


def java_string_array(list):
    return 'new String[]{"%s"}' % '", "'.join([str(e) for e in list])


def java_long(num):
    return str(num) + 'L'


def java_int(num):
    return str(num)


def desanitized(s):
    return (s.replace('<span class="paraMark">&middot;</span>', ' ')
            .replace('<span class="paraMark">&para;</span>', '')
            .replace('&#039;', "'")
            .replace('\n', '\\n'))
