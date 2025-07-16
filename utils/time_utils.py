from datetime import datetime

def to_unix(date_str: str) -> int:
    dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
    return int(dt.timestamp())
