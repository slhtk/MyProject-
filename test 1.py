import psutil

# CPU çalışma süreleri (toplam)
print("CPU Times:")
print(psutil.cpu_times())

# CPU kullanım yüzdesi (toplam) - 3 saniyelik örnekleme
print("\nCPU Percent (overall):")
for x in range(3):
    print(psutil.cpu_percent(interval=1))

# CPU kullanım yüzdesi (her çekirdek ayrı) - 3 saniyelik örnekleme
print("\nCPU Percent (per CPU):")
for x in range(3):
    print(psutil.cpu_percent(interval=1, percpu=True))

# CPU zamanları yüzdesel (toplam)
print("\nCPU Times Percent (total):")
for x in range(3):
    print(psutil.cpu_times_percent(interval=1, percpu=False))

# CPU çekirdek sayısı (mantıksal ve fiziksel)
print("\nCPU Count:")
print("Logical CPUs:", psutil.cpu_count())
print("Physical CPUs:", psutil.cpu_count(logical=False))

