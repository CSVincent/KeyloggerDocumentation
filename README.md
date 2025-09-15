# Python Keylogger Project

## Overview
This project is a **Python-based keylogger** designed mainly for educational and research purposes. It demonstrates capturing keyboard input at a low level, intelligently handling special keys and key combinations to produce readable keystroke logs.

---

## Keylogger Features
- Captures all keystrokes, distinguishing between alphanumeric keys and special keys (Enter, Backspace, Space, Tab, Function keys, etc.).
- Handles modifier keys (Ctrl, Alt, Shift, Windows) to record combined keypresses like shortcuts (e.g., Ctrl+C).
- Logs keystrokes continuously with proper formatting to a text file.
- Includes a clean exit mechanism triggered by the Escape key.
- Can be compiled into a standalone, background-running executable using PyInstaller with no visible console window.

---

## Delivery Methods
- **Manual Execution:** Run directly on the target machine with Python installed.
- **Executable Packaging:** Use PyInstaller to create a single `.exe` for Windows deployment without requiring Python.
- **USB-based Delivery:** Store executable or script on removable media (manual execution recommended as autorun is disabled in modern OS).
- **Metasploit Framework with Meterpreter:**
Instead of using the above Python script, Metasploit uses its Meterpreter payload for keylogging and system control. Meterpreter is an advanced, in-memory payload that provides a comprehensive suite of post-exploitation tools, including built-in keylogging capabilities. This means:

You do not deploy or use your custom Python keylogger script.

Meterpreter operates stealthily without writing to disk, making it more evasive.

Keylogging is activated via Meterpreter’s commands such as keyscan_start and keyscan_dump.

It requires delivering payloads using Metasploit exploits or social engineering techniques..

---

## Detection Methods
- Signature and heuristic scanning by antivirus and endpoint detection software.
- Monitoring for unexpected keylogging processes or hooks.
- Network traffic analysis for suspicious outbound data transfers of logged keystrokes.
- Alerts triggered by unusual USB device activity or software autostart entries.

---

## Protective Measures
- Keep all software and operating systems up-to-date to patch vulnerabilities exploited by keyloggers.
- Use trusted antivirus and anti-malware solutions with real-time protection.
- Disable or control USB autorun features and restrict USB device usage policies.
- Use multi-factor authentication to reduce risk from captured passwords.
- Employ on-screen keyboards or password managers to mitigate keylogging in sensitive inputs.
- Regularly audit running processes and system startup entries to detect unauthorized software.

---

## Ethical Use & Disclaimer
This project is intended for **educational purposes only**. Deploying keyloggers without explicit permission is illegal and unethical. Use responsibly and always with informed consent in a controlled environment.

---

## Getting Started

### Requirements
- Python 3.x
- `keyboard` library (`pip install keyboard`)
- Optional: PyInstaller for packaging (`pip install pyinstaller`)

### Usage
