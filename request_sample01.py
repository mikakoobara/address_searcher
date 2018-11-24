import requests

# 演習1: 岩手県八幡平市大更 の 情報 を requestsモジュール使って取得


response = requests.get("http://zipcloud.ibsnet.co.jp/api/search?zipcode=0287111")

print(response)

# 演習2: 他の地域 の 情報 を requestsモジュール使って取得
response = requests.get("http://zipcloud.ibsnet.co.jp/api/search?zipcode=0287401")
print(response)

# {
# 	"message": null,
# 	"results": [
# 		{
# 			"address1": "岩手県",
# 			"address2": "八幡平市",
# 			"address3": "大更",
# 			"kana1": "ｲﾜﾃｹﾝ",
# 			"kana2": "ﾊﾁﾏﾝﾀｲｼ",
# 			"kana3": "ｵｵﾌﾞｹ",
# 			# "prefcode": "3",
# 			"zipcode": "0287111"
# 		}
# 	],
# 	"status": 200
# }
