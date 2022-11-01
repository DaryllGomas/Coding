import requests

url = 'https://raw.githubusercontent.com/DaryllGomas/website/master/images/THM-07TDRGKZIH.png'
r = requests.get(url, allow_redirects=True)
open('THM-07TDRGKZIH.png', 'wb').write(r.content)

