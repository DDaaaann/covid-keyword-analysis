# code/step3.3_RAKE_YAKE.py

import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import rbo  # pip install rbo
# from sklearn.metrics import jaccard_score
# from sklearn.preprocessing import MultiLabelBinarizer

# 读取文件
rake_df = pd.read_csv("rake/output_rake/global_top_rake.csv")
yake_df = pd.read_csv("yake/output_yake/global_top_yake.csv")

# 提取关键词列表（确保都是小写/统一格式）
rake_keywords = rake_df['keyword'].str.lower().tolist()
yake_keywords = yake_df['keyword'].str.lower().tolist()

# ✅ Jaccard 相似度（集合方式，不考虑排名）
set_rake = set(rake_keywords)
set_yake = set(yake_keywords)
jaccard = len(set_rake & set_yake) / len(set_rake | set_yake)

print("Jaccard 相似度：", round(jaccard, 3))

# ✅ RBO 相似度（考虑排名，默认 p=0.9）
rbo_score = rbo.RankingSimilarity(rake_keywords, yake_keywords).rbo()
print("RBO 相似度：", round(rbo_score, 3))



import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os

# ========= 词过滤与归一设置 ==========
bad_keywords = [
    "amp", "get", "go", "say", "thing", "want", "know", "need", "still", "even", 
    "try", "use", "make", "tell", "good", "day", "see", "one", "way", "take",
    "never", "like", "new", "would", "also", "could", "first", "really", "right",
    "since", "much", "two", "via", "due", "may", "please", "u", "let", "sure", "lot", "we", "yes", "many"
]

synonym_dict = {
    "covid": ["covid19", "covid-19", "coronavirus", "corona", "corona virus", "covid pandemic", "coronavirus pandemic", "long covid", "virus"],
    "vaccine": ["vaccines", "vaccination", "vaccinate", "vaccinated", "vax", "covid vaccine", "unvaccinated"],
    "lockdown": ["quarantine"],
    "mask": ["masks", "masking", "face covering"],
    "death": ["deaths", "died", "die", "covid deaths"],
    "trump": ["realdonaldtrump"],
    "get": ["got", "getting", "going"],
    "good": ["well"],
    "children": ["kids", "child"],
    "year": ["years"],
    "work": ["working"],
    "say": ["said"],
    "go": ["going"],
    "try": ["trying"],
    "use": ["used"],
    "woman": ["women"],
    "fauci": ["dr fauci"],
    "origin": ["origins"],
    "lie": ["lied"],
    "tell": ["told"],
    "day": ["days"],
    "worker": ["workers"],
    "time": ["times"],
    "state": ["states"],
    "month": ["months"],
    "make": ["made"],
    "government": ["govt"],
    "mandate": ["mandates"],
    "test": ["tested", "testing"],
    "shot": ["shots"],
    "hancock": ["matt"]
}

def normalize_keywords(keyword_list, synonym_dict, bad_keywords):
    normalized = []
    for word in keyword_list:
        word = word.lower().strip()
        if word in bad_keywords:
            continue
        replaced = False
        for key, synonyms in synonym_dict.items():
            if word == key or word in synonyms:
                normalized.append(key)
                replaced = True
                break
        if not replaced:
            normalized.append(word)
    return normalized

# ========= 文件读取与路径准备 ==========
os.makedirs("result", exist_ok=True)
rake_df = pd.read_csv("rake/output_rake/global_top_rake.csv")
yake_df = pd.read_csv("yake/output_yake/global_top_yake.csv")
rake_keywords = rake_df['keyword'].tolist()
yake_keywords = yake_df['keyword'].tolist()

# ========= 归一 + 过滤 ==========
rake_clean = normalize_keywords(rake_keywords, synonym_dict, bad_keywords)
yake_clean = normalize_keywords(yake_keywords, synonym_dict, bad_keywords)

# ========= RAKE 词云 ==========
wordcloud_rake = WordCloud(
    background_color="white",
    width=800, height=400
).generate(" ".join(rake_clean))

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud_rake, interpolation='bilinear')
plt.axis("off")
plt.title("RAKE Top 50 Keyword WordCloud (Cleaned)")
plt.tight_layout()
plt.savefig("result/wordcloud_rake_cleaned.png", dpi=300)
plt.show()

# ========= YAKE 词云 ==========
wordcloud_yake = WordCloud(
    background_color="white",
    width=800, height=400
).generate(" ".join(yake_clean))

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud_yake, interpolation='bilinear')
plt.axis("off")
plt.title("YAKE Top 50 Keyword WordCloud (Cleaned)")
plt.tight_layout()
plt.savefig("result/wordcloud_yake_cleaned.png", dpi=300)
plt.show()
