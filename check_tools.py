
import shutil
import subprocess

TOOLS = {
    "Nmap": "nmap",
    "Wireshark": "tshark",
    "YARA": "yara",
    "WhatWeb": "whatweb",
    "OWASP ZAP": "zaproxy",
    "Gitleaks": "gitleaks",
    "Trivy": "trivy",
    "SSLyze": "sslyze",
    "Retire.js": "retire",
    "Semgrep": "semgrep",
}

print("=== VulnHunter 10: Tool Check ===")

for name, command in TOOLS.items():
    path = shutil.which(command)

    if path:
        print(f"[+] {name}: FOUND ({path})")
    else:
        print(f"[-] {name}: NOT FOUND")

print("\nCheck completed.")

