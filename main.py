import requests

token = "xoxb-3538245060513-5821303347312-wmyPLGlz1btNYgI5dt3DqSnv"
CHANNEL = "#pj"

#####################################
# 画像を生成する例、アップロードするだけなら不要
#####################################

# # データ読み込む
# data = pd.read_table(
#     "/path/to/data/input.tsv", #なんかtsv/csv読み込むサンプル
#     header=-1,
#     names=("date","value")
# )
# # 軸の基準になるとこ
# data.index = pd.to_datetime(data.iloc[:,0])
# data.plot()
# # 保存するよ
# plt.savefig('figure.png')

###############
# 画像送信ここから
###############
headers = {
    'Authorization': 'Bearer xoxb-3538245060513-5821303347312-wmyPLGlz1btNYgI5dt3DqSnv',
}

files = {
    'file': open('./hoge.png', 'rb'),
    'channels': (None, '#pj'),
}

print(open('./hoge.png', 'rb'))

response = requests.post('https://slack.com/api/files.upload', headers=headers, files=files)
print(res)