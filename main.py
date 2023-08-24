import requests

TOKEN = "xoxb-3538245060513-5782752890023-rwIWugucDkPMBr2mmzYqr66O"
CHANNEL = "https://testchannel-vlo8440.slack.com/archives/C03F10KA7F1"

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
files = {'file': open("./hoge.png", 'rb')}
param = {
    'token':TOKEN,
    'channels':CHANNEL,
    'filename':"filename",
    'initial_comment': "initial_comment",
    'title': "title"
}
requests.post(url="https://slack.com/api/files.upload",params=param, files=files)