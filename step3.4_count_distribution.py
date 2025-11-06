import pandas as pd

# 读取数据
df = pd.read_csv("result/keyword_appear_months.csv")  # 根据你实际路径调整

# 查看 keyword_type 列的唯一值及其计数
type_counts = df["keyword_type"].value_counts()

# 打印结果
print(type_counts)

# 如果需要百分比，可以使用：
type_percent = df["keyword_type"].value_counts(normalize=True).round(3) * 100
print("\nPercentage Distribution:")
print(type_percent)
