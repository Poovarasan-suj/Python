import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

print(response.status_code)
pull_request=response.json()

for i in pull_request:
    print("User-",i["user"] ["login"])



