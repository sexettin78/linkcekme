import requests
from bs4 import BeautifulSoup
header_kod = { 'User-Agent' : 'Mozilla/5.0 (Machintosh; Sexettin X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecho) Sexettin/48.0.2564.116 Naber/537.36'}
print("Örnek site: https://google.com  http/https eklemeyi unutmayın")
hedefsite = input("Hedef Url Giriniz: ")
hedefl = requests.get(hedefsite,headers=header_kod)
hedefg = hedefl.content
guzelcorba = BeautifulSoup(hedefg,"html.parser")

for i in guzelcorba.find_all("a"):
    print(i)
    print("\n ################################################################ \n")

 #print(guzelcorba.find_all("a"))
