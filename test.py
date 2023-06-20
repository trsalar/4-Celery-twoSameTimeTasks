import subprocess

# Shell komutunu çalıştırma
komut = "python manage.py runserver -l"  # Örnek bir komut, siz kendi komutunuzu kullanmalısınız

# subprocess'ı kullanarak komutu çalıştırma
try:
    cikti = subprocess.check_output(komut, shell=True, stderr=subprocess.STDOUT)
    print(cikti.decode("utf-8"))
except subprocess.CalledProcessError as e:
    print("Hata: Komut çalıştırılamadı.")
    print("Hata çıktısı:", e.output.decode("utf-8"))