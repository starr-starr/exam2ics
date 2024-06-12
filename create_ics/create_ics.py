from parse.parse_course_name import parse_course_name
from parse.parse_date import parse_date


def create_ics(df):
    ics_content = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//Exam Schedule Calendar//mxm.dk//",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH"
    ]

    for index, row in df.iterrows():
        dt_start, dt_end = parse_date(row['考试时间'])
        course_name = parse_course_name(row['课程'])

        event = [
            "BEGIN:VEVENT",
            f"DTSTART;TZID=Asia/Shanghai:{dt_start.strftime('%Y%m%dT%H%M%S')}",
            f"DTEND;TZID=Asia/Shanghai:{dt_end.strftime('%Y%m%dT%H%M%S')}",
            f"SUMMARY:{course_name}",
            f"LOCATION:{row['考试地点']}",
            f"DESCRIPTION:Student: {row['学生']}",
            "END:VEVENT"
        ]
        ics_content.extend(event)

    ics_content.append("END:VCALENDAR")
    return "\n".join(ics_content)