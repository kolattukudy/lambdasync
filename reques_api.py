import json
import requests
url = 'https://datausa.io/api/data?drilldowns=Nation&measures=Population'
r = requests.get(url)
files = r.json()
print(files)