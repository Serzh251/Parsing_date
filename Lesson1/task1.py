import requests
import json
url = "https://api.github.com/users/Serzh251/repos"
req = requests.get(url)

data = json.loads(req.text)
with open('list_repo.json', 'w') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)


