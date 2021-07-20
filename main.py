import requests

print("Введите номер телефона без кода страны")
phone=input()
print("Номер телефона " + phone)
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124",
    "host": "api.sunlight.net", "Content-Type": "application/json", }

def sunlight():
    phoneSunlight = "7" + phone
    s = requests.post('https://api.sunlight.net/v3/customers/authorization/', json={"phone":phoneSunlight}, headers=headers)
    print(s.status_code)
    print(s.json())

def utair():
    utPhone = phone + "+7"
    u = requests.session()
    u.get('https://b.utair.ru/api/v1/login/')
    ut = requests.post('https://b.utair.ru/api/v1/login/', headers=headers, json={"login":utPhone})
    print(ut.status_code)
    print(ut.json())
sunlight()
utair()
