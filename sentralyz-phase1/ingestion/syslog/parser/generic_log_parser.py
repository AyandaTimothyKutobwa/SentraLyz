import re
import datetime

def parse_log(log_line):
    parts = re.match(r"^(<\d+>)?(\w{3} \d{1,2} \d{2}:\d{2}:\d{2}) (\S+) (.*)", log_line)

    if parts:
        _, timestamp, source, message = parts.groups()
    else:
        timestamp = datetime.datetime.utcnow().isoformat()
        source = "unknown"
        message = log_line

    return {
        "timestamp": timestamp,
        "source": source,
        "message": message
    }



