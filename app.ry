import tkinter as tk
from tkinter import filedialog
import os

def scan_file():
    path = filedialog.askopenfilename()
    if not path:
        return
    status_label.config(text=f"Сканирую: {path}...")
    with open(path, 'r', errors='ignore') as f:
        text = f.read().lower()
        bad = ["virus", "malware", "trojan"]
        for b in bad:
            if b in text:
                status_label.config(text=f"[!] УГРОЗА НАЙДЕНА: {b}", fg="red")
                return
    status_label.config(text="[✓] Файл чистый!", fg="green")

root = tk.Tk()
root.title("Vullhaunter 10 ULTRA FINAL")
root.geometry("400x300")
root.configure(bg="#1a1a2e")

title = tk.Label(root, text="VULLHAUNTER\n10 ULTRA", font=("Arial", 24, "bold"), bg="#1a1a2e", fg="#00ff88")
title.pack(pady=20)

info = tk.Label(root, text="by 12 y.o. dev from Kazakhstan\nTalgar", bg="#1a1a2e", fg="white")
info.pack()

btn = tk.Button(root, text="ВЫБРАТЬ ФАЙЛ И СКАНИРОВАТЬ", command=scan_file, bg="#00ff88", fg="black", font=("Arial", 12, "bold"), padx=20, pady=10)
btn.pack(pady=20)

status_label = tk.Label(root, text="Готов к сканированию", bg="#1a1a2e", fg="white")
status_label.pack(pady=10)

root.mainloop()