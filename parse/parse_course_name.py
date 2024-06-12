import re


def parse_course_name(course_name):
    return re.sub(r"\[.*?\]", "", course_name).strip()
