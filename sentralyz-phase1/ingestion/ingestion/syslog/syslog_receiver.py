from parser.generic_log_parser import parse_log

def receive_log(log_line):
    parsed = parse_log(log_line)
    print(parsed)

if __name__ == "__main__":
    sample = "<34>1 2023-10-12T08:12:43Z myhost app - - - Sample syslog message"
    receive_log(sample)
