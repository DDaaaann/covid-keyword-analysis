# code/step1_merge_keywords.py
import pandas as pd
from pathlib import Path
import spacy
import re

#加载 spaCy 英文模型（只需首次运行时下载）
nlp = spacy.load("en_core_web_sm")

#词形还原函数
def normalize_term(term):
    term = re.sub(r"[^\w\s]", "", term.lower())  # 去除标点和大写
    doc = nlp(term)
    return " ".join([token.lemma_ for token in doc]).strip()

#同义词归一映射表（可扩展）
synonym_dict = {

    #global
    #2020_03_r:"corona virus"
    #2020_04_r:"covid pandemic", "coronavirus pandemic"
    "covid": ["covid19", "covid-19", "coronavirus", "corona", "corona virus", "covid pandemic", "coronavirus pandemic", "long covid", "virus"],
    
    #2021_04:"vaccination", "vaccinated"
    #2023_01:"vax"
    #2020_12_r:"covid vaccine"
    "vaccine": ["vaccines", "vaccination", "vaccinate", "vaccinated", "vax", "covid vaccine", "covid vaccine", "unvaccinated"],

    #2020_08:"quarantine"
    "lockdown": ["quarantine"],

    #global
    "mask": ["masks", "masking", "face covering"],
    
    #2022_11:"died"
    #2022_03_r: "die"
    "death": ["deaths", "died", "die", "covid deaths"],

    #global
    "trump": ["realdonaldtrump"],
    
    #global
    "get": ["got", "getting", "going"],
    
    #global
    "good": ["well"],
    
    #2021_09:kids
    "children": ["kids", "child"], 


    #2022_01:"years"
    "year": ["years"],

    #global_r
    "work": ["working"],

    #global_r
    "say": ["said"],

    #global_r
    "go": ["going"],

    #2023_01_r
    "try": ["trying"],
    
    #2023_01_r
    "use": ["used"],

    #2023_02_r
    "woman": ["women"],

    #2023_03_r  Anthony Fauci
    "fauci": ["dr fauci"],   

    #2023_03_r
    "origin": ["origins"],

    #2023_03_r
    "lie": ["lied"],

    #2023_03_r
    "tell": ["told"],

    #global_y
    "day": ["days"],

    #2020_05_y
    "worker": ["workers"],

    #2020_04_y
    "time": ["times"],

    #2020_06_y
    "state": ["states"],

    #2020_08_y
    "month": ["months"],

    #2021_01_y
    "make": ["made"],

    "government": ["govt"],

    #2021_09_y
    "mandate": ["mandates"],

    #2022_01_y
    "test": ["tested", "testing"],

    #2023_01_y
    "shot": ["shots"],

    "hancock": ["matt"]

}


#概念归一函数
def map_to_standard_keyword(term):
    for std, variants in synonym_dict.items():
        if term == std or term in variants:
            return std
    return term

# ---------- 输入路径 ----------
method_folders = {
    "normal": "easy_wordcount/output",
    "rake": "rake/output_rake",
    "yake": "yake/output_yake"
}

from collections import defaultdict

# 聚合用的字典
count_dict = defaultdict(int)

for method, folder in method_folders.items():
    for file in Path(folder).glob("keywords_*.csv"):
        filename = file.stem
        if "global" in filename.lower():
            continue

        parts = filename.split("_")
        month = parts[1] + "-" + parts[2]
        month_label = parts[1] + "_" + parts[2]

        df = pd.read_csv(file)
        for _, row in df.iterrows():
            raw_keyword = str(row['keyword'])
            count = int(row['count'])

            normalized = normalize_term(raw_keyword)
            keyword_std = map_to_standard_keyword(normalized)

            key = (month, method, keyword_std, month_label)
            count_dict[key] += count

# 将聚合后的结果转为列表
all_rows = [
    [month, method, keyword_std, total_count, month_label]
    for (month, method, keyword_std, month_label), total_count in count_dict.items()
]

# 输出去重后的表格
df = pd.DataFrame(all_rows, columns=["month", "method", "keyword_std", "count", "month_label"])
df.to_csv("result/concept_monthly.csv", index=False)
print("成功保存为 concept_monthly.csv，重复关键词已合并。")


