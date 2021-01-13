import requests

# prints version of the requests library
print("="*10 + "requests library version" + "="*10)
print(requests.__version__)

# GET the Google homepage using requests library
print("="*10 + "Google homepage" + "="*10)
print(requests.get("http://google.com"))

# GET and prints source code of this script from GitHub
print("="*10 + "source code" + "="*10)
response = requests.get("https://raw.githubusercontent.com/keanweng97/CMPUT404-Lab-1/main/script.py")
print(response.text)