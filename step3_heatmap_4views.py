import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# /opt/homebrew/Caskroom/miniforge/base/bin/python -m pip install seaborn matplotlib pandas

# 加载主表
df = pd.read_csv("result/concept_monthly_filtered.csv")

# 函数：标准化热图数据
def build_heatmap_data(df_filtered, top_n=20):
    top_keywords = (
        df_filtered.groupby("keyword_std")["count"]
        .sum()
        .sort_values(ascending=False)
        .head(top_n)
        .index
    )
    df_top = df_filtered[df_filtered["keyword_std"].isin(top_keywords)]
    data = df_top.pivot_table(
        index="keyword_std", columns="month", values="count", aggfunc="sum", fill_value=0
    )
    zscore = data.sub(data.mean(axis=1), axis=0)
    zscore = zscore.div(data.std(axis=1), axis=0).fillna(0)
    return zscore

# 1. 合并方法
df_all = df.groupby(["month", "keyword_std"])["count"].sum().reset_index()
z_all = build_heatmap_data(df_all, top_n=20)

# 2–4. 分方法
z_normal = build_heatmap_data(df[df["method"]=="normal"])
z_rake   = build_heatmap_data(df[df["method"]=="rake"])
z_yake   = build_heatmap_data(df[df["method"]=="yake"])

# 画四张图
fig, axes = plt.subplots(2, 2, figsize=(18, 12))

sns.heatmap(z_all, ax=axes[0, 0], cmap="coolwarm", linewidths=0.5)
axes[0, 0].set_title("All Methods Combined")

sns.heatmap(z_normal, ax=axes[0, 1], cmap="coolwarm", linewidths=0.5)
axes[0, 1].set_title("Normal Wordcount")

sns.heatmap(z_rake, ax=axes[1, 0], cmap="coolwarm", linewidths=0.5)
axes[1, 0].set_title("RAKE")

sns.heatmap(z_yake, ax=axes[1, 1], cmap="coolwarm", linewidths=0.5)
axes[1, 1].set_title("YAKE")

for ax in axes.flat:
    ax.set_xlabel("Month")
    ax.set_ylabel("Keyword")
    ax.tick_params(axis='x', rotation=45)

plt.suptitle("Keyword Trends Over Time (Z-score, Top 20)", fontsize=18)
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig("result/keyword_trends_4views_heatmap_filtered.png", dpi=300)
plt.show()




# ✅ 第2部分：输出4张单独热图

# 单独图 1 - All
plt.figure(figsize=(10, 6))
sns.heatmap(z_all, cmap="coolwarm", linewidths=0.5)
plt.title("All Methods Combined", fontsize=14)
plt.xlabel("Month")
plt.ylabel("Keyword")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("result/keyword_trend_all.png", dpi=300)

# 单独图 2 - Normal
plt.figure(figsize=(10, 6))
sns.heatmap(z_normal, cmap="coolwarm", linewidths=0.5)
plt.title("Normal Wordcount", fontsize=14)
plt.xlabel("Month")
plt.ylabel("Keyword")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("result/keyword_trend_normal.png", dpi=300)

# 单独图 3 - RAKE
plt.figure(figsize=(10, 6))
sns.heatmap(z_rake, cmap="coolwarm", linewidths=0.5)
plt.title("RAKE", fontsize=14)
plt.xlabel("Month")
plt.ylabel("Keyword")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("result/keyword_trend_rake.png", dpi=300)

# 单独图 4 - YAKE
plt.figure(figsize=(10, 6))
sns.heatmap(z_yake, cmap="coolwarm", linewidths=0.5)
plt.title("YAKE", fontsize=14)
plt.xlabel("Month")
plt.ylabel("Keyword")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("result/keyword_trend_yake.png", dpi=300)