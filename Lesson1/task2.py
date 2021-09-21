import requests
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
                    'Authorization':'Token your token'}
url = "https://api.github.com/user"
req = requests.get(url, headers=headers)

data = json.loads(req.text)
with open('with_headers.json', 'w') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
