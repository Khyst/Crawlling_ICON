from bs4 import BeautifulSoup
import requests

login_url = "https://class.likelion.org/"

email = 'kyh9432242@likelion.org'
password = '42852242'

# requests.session 메서드는 해당 requestst를 사용하는 동안 cookie를 header에 유지하도록하여
# 세션이 필요한 HTTP 요청에 사용됩니다.

params  = dict()
params['email'] = email
params['password'] = password
params['csrftoken'] = "w2EavHuNFb5xM9UEF7cjvwbBwy4iJ9mkMpIHgNKvphecT3jmHR2p4uLRvN1HCLNT"

session = requests.session()

res = session.post(login_url, data = params)
res.raise_for_status() 
#r = requests.post(login_url, data={'email': email, 'password': password})

print(res.read().decode('utf-8'))
#print(r.text)

mypage_url = 'http://class.likelion.org'
res = session.get(mypage_url)

soup = BeautifulSoup(res.text, 'html.parser')

#reading = request.urlopen("https://class.likelion.org/")

print(reading.text)
