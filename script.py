import requests
print(requests.__version__)
print(requests.get("http://google.com"))
response = requests.get("https://raw.githubusercontent.com/keanweng97/CMPUT404-Lab-1/main/script.py")
print(response.text)