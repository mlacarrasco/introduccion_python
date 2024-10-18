
import requests

file = open("uai.html", "w")

x = requests.get('http://www.uai.cl')
print(x.text)
file.write(x.text)
file.close()