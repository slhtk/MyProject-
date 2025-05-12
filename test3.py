import os
import shutil
import subprocess

# 1. test klasörü oluştur
if not os.path.exists("TestFolder"):
    os.mkdir("TestFolder")
    print("TestFolder klasörü oluşturuldu.")

# 2. test1.py ve test2.py dosyalarını TestFolder/ klasörüne taşı
dosyalar = ["test  1.py", "test2.py"]

for dosya in dosyalar:
    if os.path.exists(dosya):
        shutil.move(dosya, os.path.join("TestFolder", dosya))
        print(f"{dosya} TestFolder klasörüne taşındı.")
    else:
        print(f"{dosya} bulunamadı.")

# 3. Git işlemleri (subprocess ile komut çalıştır)
def git(cmd):
    result = subprocess.run(["git"] + cmd, capture_output=True, text=True)
    print(" ".join(["git"] + cmd))
    print(result.stdout)
    if result.stderr:
        print("Hata:", result.stderr)

# 4. Değişiklikleri Git'e ekle ve commit et
git(["add", "."])
git(["commit", "-m", "test klasörü oluşturuldu ve dosyalar taşındı"])

# 5. test-branch adında yeni bir branch oluştur
git(["checkout", "-b", "test-branch"])

# 6. Yeni branch'i GitHub'a gönder
git(["push", "-u", "origin", "test-branch"])
