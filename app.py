from address_sercher import addresseacher


def main():
    # ユーザーからの郵便番号を受け取る
    postal_code = input("郵便番号を入力してね: ")
    # 郵便番号を使って地名をとってくる


address_sercher = AddressSearcer()

location = adress_searcher.search(postal_code)

# 地名をprintする
print(location)

if __name__ == '__main__':
    main()
