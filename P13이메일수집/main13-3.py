import requests
import re

url = 'https://news.v.daum.net/v/20220708183033551'

headers = {
    'User-Agent' : 'Mozilla/5.0',
    'Content-Type' : 'text/html; charset=utf-8'
}

response = requests.get(url, headers=headers)

results = re.findall(r'[\w\.-]+@[\w\.-]+', response.text)
results = list(set(results))

print(results)