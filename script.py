import requests


r = requests.get('http://www.lobo.blog.br/')
print(r.status_code)
print(r.ok)
