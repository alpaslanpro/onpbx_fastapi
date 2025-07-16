from datetime import datetime
import time

def convert_to_unix(date_string: str) -> int:
    dt = datetime.strptime(date_string, "%Y-%m-%d %H:%M")
    return int(time.mktime(dt.timetuple()))
