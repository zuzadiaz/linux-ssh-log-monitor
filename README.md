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
