import re
from collections import Counter

log_file = "auth.log"
failed_ips = []

with open(log_file, "r") as file:
    for line in file:
        if "Failed password" in line:
            ip_match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)

            if ip_match:
                ip_address = ip_match.group(1)
                failed_ips.append(ip_address)

ip_counts = Counter(failed_ips)

print("\n=== SSH Failed Login Analysis ===")
print("-----------------------------------")

for ip, count in ip_counts.items():
	print(f"\nIP Address: {ip}")
	print(f"Failed Attempts: {count}")

	if count >= 5:
		severity = "HIGH"
	elif count >= 3:
		severity = "MEDIUM"
	else:
		severity = "LOW"

	print(f"Severity Level: {severity}")

	if count >= 3:
		print(f"ALERT: {ip} may be suspicious.")
