import pyautogui
import time

# Kullanıcıdan mesaj sayısını alma
mesaj_sayisi = int(input("Kaç tane mesaj göndermek istiyorsunuz? "))

# Kullanıcıdan gönderilecek mesajı alma
mesaj = input("Göndermek istediğiniz mesaj nedir? ")

print("WhatsApp'ı açıp mesaj göndereceğiniz yere imleci yerleştirin.")
print("5 saniye içinde hazırlanın...")

# Kullanıcıya hazırlanması için 5 saniye süre
time.sleep(5)

# Mesajları gönderme döngüsü
for i in range(mesaj_sayisi):
    pyautogui.typewrite(mesaj)  # Mesajı yazar
    pyautogui.press("enter")    # Enter tuşuna basar
    time.sleep(0.1)             # Küçük bir gecikme (spam önlemek için)

print(f"{mesaj_sayisi} adet mesaj başarıyla gönderildi!")
