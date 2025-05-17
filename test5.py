import tkinter as tk
import time
import threading
import psutil
import matplotlib.pyplot as plt
from datetime import datetime

# GLOBAL DEĞİŞKENLER
running = False
data_log = []

# 30 saniyede bir veri toplama
def track_usage():
    while running:
        timestamp = datetime.now().strftime("%H:%M:%S")
        total_time = 0
        google_time = 0

        for proc in psutil.process_iter(['pid', 'name']):
            try:
                name = proc.info['name']
                if name:
                    total_time += 1
                    if 'chrome' in name.lower() or 'firefox' in name.lower():
                        google_time += 1
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

        data_log.append((timestamp, total_time, google_time))
        time.sleep(30)

# İzlemeyi başlat
def start_tracking():
    global running
    running = True
    threading.Thread(target=track_usage, daemon=True).start()
    status_label.config(text="Durum: İzleniyor...")

# İzlemeyi durdur
def stop_tracking():
    global running
    running = False
    status_label.config(text="Durum: Durduruldu.")

# Grafik ile analiz et
def analyze_data():
    if not data_log:
        status_label.config(text="Henüz veri yok!")
        return

    times = [entry[0] for entry in data_log]
    usage = [entry[1] for entry in data_log]
    google = [entry[2] for entry in data_log]

    plt.figure()
    plt.plot(times, usage, label="Toplam Aktif İşlem Sayısı")
    plt.plot(times, google, label="Google (Tarayıcı) İşlemleri")
    plt.xlabel("Zaman")
    plt.ylabel("İşlem Sayısı")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.title("Kullanım Analizi")
    plt.show()

# GUI Arayüzü
root = tk.Tk()
root.title("Kullanım Takipçisi")
root.geometry("300x200")

start_button = tk.Button(root, text="Başlat", command=start_tracking)
start_button.pack(pady=5)

stop_button = tk.Button(root, text="Durdur", command=stop_tracking)
stop_button.pack(pady=5)

analyze_button = tk.Button(root, text="Analiz Et", command=analyze_data)
analyze_button.pack(pady=5)

status_label = tk.Label(root, text="Durum: Hazır")
status_label.pack(pady=10)

root.mainloop()
