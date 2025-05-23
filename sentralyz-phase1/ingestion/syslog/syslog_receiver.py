import socket
import json
from parser.generic_log_parser import parse_log

UDP_IP = "0.0.0.0"
UDP_PORT = 5140

print(f"Listening on {UDP_IP}:{UDP_PORT}")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(4096)
    raw_log = data.decode("utf-8").strip()
    print(f"Received: {raw_log} from {addr}")

    parsed_log = parse_log(raw_log)

    with open("normalized_logs.json", "a") as outfile:
        outfile.write(json.dumps(parsed_log) + "\n")
