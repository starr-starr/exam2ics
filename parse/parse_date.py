from datetime import datetime


def parse_date(date_time):
    date, time = date_time.split(')')
    date = date.split('(')[0]
    time = time.strip()

    dt_start_str = f"{date} {time.split('-')[0]}"
    dt_end_str = f"{date} {time.split('-')[1]}"
    dt_start = datetime.strptime(dt_start_str, "%Y-%m-%d %H:%M")
    dt_end = datetime.strptime(dt_end_str, "%Y-%m-%d %H:%M")

    return dt_start, dt_end
