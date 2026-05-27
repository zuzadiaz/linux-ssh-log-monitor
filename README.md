# Linux SSH Log Monitoring Tool

## Overview

This project is a Python-based cybersecurity tool built in Ubuntu Linux (WSL).

The script analyzes Linux authentication logs, detects failed SSH login attempts, extracts suspicious IP addresses using regex, and flags repeated failed login activity.

## Technologies Used

- Python
- Ubuntu Linux (WSL)
- Regex
- Linux authentication logs
- Command-line interface (CLI)

## Features

- Reads Linux auth logs
- Detects failed SSH login attempts
- Extracts IP addresses
- Counts repeated failed logins
- Flags suspicious activity

## How to Run

Run the script in Linux terminal:

```bash
python3 log_monitor.py
```


## Detection Logic

- LOW severity: 1–2 failed login attempts
- MEDIUM severity: 3–4 failed login attempts
- HIGH severity: 5+ failed login attempts

The script flags repeated failed SSH login attempts as potentially suspicious activity.


## Sample Output

```text
=== SSH Failed Login Analysis ===

IP Address: 192.168.1.45
Failed Attempts: 1
Severity Level: LOW

IP Address: 203.0.113.10
Failed Attempts: 3
Severity Level: MEDIUM
ALERT: 203.0.113.10 may be suspicious.
```

