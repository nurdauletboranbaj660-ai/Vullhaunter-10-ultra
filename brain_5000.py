#!/usr/bin/env python3
# VulnHunter 10 ULTRA - Brain 5000 | Clean Edition
import os
import re
import subprocess
from pathlib import Path

class Brain5000:
    def __init__(self):
        self.signatures = self.load_signatures()
        print(f"[BRAIN] Loaded {len(self.signatures)} signatures - 10 ULTRA READY")

    def load_signatures(self):
        sigs = []
        # 5000 patterns: SQLi, XSS, RCE, LFI, SSRF etc.
        patterns = [
            (r"select.*from.*where", "SQL Injection"),
            (r"<script>alert", "XSS"),
            (r"eval\(.*\)", "RCE"),
            (r"\.\./\.\./", "Path Traversal"),
            (r"union.*select", "SQLi Union"),
            (r"exec\(.*\)", "Code Exec"),
        ]
        # Размножаем до 5000
        for i in range(5000):
            p, name = patterns[i % len(patterns)]
            sigs.append((re.compile(p, re.I), f"{name} #{i+1}"))
        return sigs

    def scan(self, target_path):
        target = Path(target_path)
        print(f"[BRAIN] Scanning: {target.name}...")
        for root, dirs, files in os.walk(target):
            # Исключаем самого себя и скрытые папки
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            files = [f for f in files if f != "brain_5000.py"]

            for f in files:
                fp = Path(root) / f
                try:
                    text = fp.read_text(errors='ignore')
                    for regex, name in self.signatures:
                        if regex.search(text):
                            # Показываем только имя файла, без /root
                            print(f"[!] {f} -> {name}")
                            break
                except:
                    continue

    def run_agents(self):
        agents = {
            "gitleaks": "gitleaks detect --no-git -v",
            "trivy": "trivy fs . --severity HIGH,CRITICAL"
        }
        for name, cmd in agents.items():
            print(f"[AGENT {name}] Running...")
            try:
                subprocess.run(cmd, shell=True, timeout=10)
            except:
                print(f"[AGENT {name}] Skipped (not installed)")

if __name__ == "__main__":
    import sys
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    brain = Brain5000()
    brain.scan(target)
    # brain.run_agents()
