import tkinter as tk
import psutil
import time

class CpuMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CPU Takip Paneli")
        self.root.geometry("500x600")
        self.root.configure(bg="yellow")

        self.label_title = tk.Label(root, text="Toplam CPU Kullanımı", font=("Arial", 16, "bold"), bg="black", fg="white")
        self.label_title.pack(pady=10)

        self.label_total = tk.Label(root, text="", font=("Arial", 14), bg="black", fg="cyan")
        self.label_total.pack()

        self.label_percpu_title = tk.Label(root, text="Çekirdek Bazlı Kullanım:", font=("Arial", 14, "bold"), bg="black", fg="white")
        self.label_percpu_title.pack(pady=10)

        self.core_labels = []
        for i in range(psutil.cpu_count()):
            lbl = tk.Label(root, text="", font=("Arial", 12), bg="black", fg="lightgreen", anchor="w")
            lbl.pack(fill="x", padx=20)
            self.core_labels.append(lbl)

        self.update_stats()

    def update_stats(self):
        # Toplam CPU yüzdesi
        total = psutil.cpu_percent(interval=1)
        self.label_total.config(text=f"{total:.1f} %")

        # Her çekirdek için ayrı
        per_cpu = psutil.cpu_percent(interval=0.1, percpu=True)
        for i, usage in enumerate(per_cpu):
            self.core_labels[i].config(text=f"Çekirdek {i+1}: {usage:.1f} %")

        self.root.after(1000, self.update_stats)

# Programı başlat
if __name__ == "__main__":
    root = tk.Tk()
    app = CpuMonitorApp(root)
    root.mainloop()
