log_file_path = "sample_logs.txt"

with open(log_file_path, "r") as file:
    for line in file:
        parts = line.split(" ")

        if len(parts) < 7:
            continue  # skip broken lines

        ip_address = parts[0]  # always first
        timestamp = parts[3].lstrip("[")  # remove the opening bracket
        request_path = parts[6]  # this is usually the URL path

        print(f"IP: {ip_address} | Time: {timestamp} | Path: {request_path}")
