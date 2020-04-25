import requests

ip = requests.get('https://api.ipify.org').text
user = 'X'
_pass = 'X'

url = (
    f'https://{user}:{_pass}@domains.google.com/nic/update'
    f'?hostname=pi.ianmyjer.com&myip={ip}'
)
resp = requests.post(url)
print(resp.status_code)
