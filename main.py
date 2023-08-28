import requests

token = "xoxb-3538245060513-5821303347312-cnaQBouGIMlwFJaNPDkMYznr"
CHANNEL = "#pj"

headers = {
    'Authorization': f'Bearer {token}',
}

files = {
    'file': open('./hoge.png', 'rb'),
    'channels': (None, '#pj'),
}

print(open('./hoge.png', 'rb'))

requests.post('https://slack.com/api/files.upload', headers=headers, files=files)