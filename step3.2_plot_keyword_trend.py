# code/step3.2_plot_keyword_trend.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 读取数据
df = pd.read_csv("result/concept_monthly_filtered.csv")

# 关键词列表
target_keywords = ["covid", "vaccine", "mask", "lockdown", "death", "trump", "pandemic","work","world","health"]

# 筛选并分组统计
df = df[df["keyword_std"].isin(target_keywords)]
df_grouped = df.groupby(["month", "keyword_std"])["count"].sum().reset_index() # 汇总不同方法（normal, rake, yake）后合并统计

# 转换为透视表
pivot_df = df_grouped.pivot(index="month", columns="keyword_std", values="count").fillna(0)
pivot_df = pivot_df.sort_index()

# 计算 Z-score：按行（每个关键词）标准化
zscore_df = pivot_df.apply(lambda x: (x - x.mean()) / x.std(ddof=0), axis=0).fillna(0)

# 画图
plt.figure(figsize=(24, 6), dpi=200)
sns.set_style("whitegrid")
for keyword in target_keywords:
    if keyword in zscore_df.columns:
        plt.plot(zscore_df.index, zscore_df[keyword], marker='o', label=keyword)

plt.title("Keyword Z-Score Over Time", fontsize=16)
plt.xlabel("Month")
plt.ylabel("Z-score (Standardized Frequency)")
plt.xticks(rotation=45)
plt.legend(title="Keyword")
plt.tight_layout()

#old is keyword_trend_lines.png
plt.savefig("result/keyword_trend_lines_zscore.png", dpi=300) #relative
plt.show()
