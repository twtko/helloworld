# 入場料計算プログラム

# 入場料金
child_price = 500
adalt_price = 1000
elder_price = 700

# グループ人数
child = int(input("子供料金(13歳以下)の人数："))
adalt = int(input("通常料金の(14-64歳)人数："))
elder = int(input("高齢者料金(65歳以上)の人数："))
group = child + adalt + elder

# 料金
child_total = child * child_price
adalt_total = adalt * adalt_price
elder_total = elder * elder_price
group_total = child_total + adalt_total + elder_total

no_discount = group_total

# グループ割引
if group >= 10:
    discount = str("団体割引(2割引)が適用されます。")
    group_total = group_total * 0.8
    discount_total = group_total * 0.2
else:
    discount = str("団体割引の適用はありません。")
    discount_total = 0

# 結果出力
print("子供料金:{0}人 x {1}円 = {2}円".format(child, child_price, child_total))
print("一般料金:{0}人 x {1}円 = {2}円".format(adalt, adalt_price, adalt_total))
print("高齢者料金:{0}人 x {1}円 = {2}円".format(elder, elder_price, elder_total))
print(discount)
print("合計人数:{0}人 / 合計金額:{1}円".format(group, group_total))
if group >= 10:
    print("割引額:{0}円 / 割引なしの場合の料金:{1}円".format(discount_total, no_discount))
