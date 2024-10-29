import random
import requests
import time

harfler = "abcdefghjklmnoprstvyz1234567890"

base_url = "https://api.mojang.com/users/profiles/minecraft/"

for _ in range(200):
    username = "".join(random.sample(harfler, 3))
    get_url = f"{base_url}{username}"
    response = requests.get(get_url)

    if response.status_code == 200:
        print(f"Kullanıcı Adı: {username} (Mevcut)")
    elif response.status_code == 204:
        print(f"Kullanıcı Adı: {username} (Kullanılabilir)")
    else:
        print(f"Kullanıcı Adı: {username} (Api rate limited)")
        time.sleep(200)
        print("devam ediyor")