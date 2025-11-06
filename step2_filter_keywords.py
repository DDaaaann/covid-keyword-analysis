# code/step2_filter_keywords.py

import pandas as pd

# 读取原始数据
df = pd.read_csv("result/concept_monthly.csv")

# 要过滤掉的无意义关键词
bad_keywords = [
    "amp", "get", "go", "say", "thing", "want", "know", "need", "still", "even", 
    "try", "use", "make", "tell", "good", "day", 
    #"work", 
    "see", "one",
    "way", "take"
    # , "time", "people"
    # "come", 
    #"back"
    , "never","like", "new", "would",
    "also","could", "first", "really", "right", "since", "much", "two", "via",
    "due", "may", "please", "u","let","sure","lot","we","yes","many"
]

#"work","come","back"
#词组
#"time", "people"可能有用✅

# 删除这些无意义词，保留所有其他关键词（无论出现多少月）
df_filtered = df[~df["keyword_std"].isin(bad_keywords)]


df_filtered.to_csv("result/concept_monthly_filtered.csv", index=False)
print("清洗完成，仅删除无意义词，已保存为 concept_monthly_filtered.csv")


#常青词（evergreen） → 长期活跃，出现月份多且分散
#爆发词（burst） → 短时间集中爆发，出现月份少或集中

#表2:衍生表：统计哪些月份出现
# 构建辅助函数，计算 max_consecutive_months 和 span_months
def compute_lifespan_info(month_str_list):
    months = sorted(set(month_str_list))
    months_dt = pd.to_datetime([m.replace("_", "-") + "-01" for m in months])  # 转换成日期对象

    # span_months 这个关键词从第一次出现到最后一次出现，横跨了多少个月（中间可能有空档）。
    span = (months_dt[-1] - months_dt[0]).days // 30 + 1  # 跨越几个月

    # max_consecutive_months
    diffs = [(months_dt[i+1] - months_dt[i]).days // 30 for i in range(len(months_dt)-1)]
    max_consec = 1
    current = 1
    for diff in diffs:
        if diff == 1:
            current += 1
            max_consec = max(max_consec, current)
        else:
            current = 1
    return span, max_consec



# 新生成列
def extract_info(month_str):
    month_list = month_str.split(",")
    span, max_consec = compute_lifespan_info(month_list)
    return pd.Series([len(month_list), span, max_consec])

# 构造 appear_df
appear_df = (
    df_filtered.groupby("keyword_std")["month_label"]
    .apply(lambda x: ",".join(sorted(set(x))))
    .reset_index(name="appear_in_months")
)


# appear_count是这个关键词在多少个不同的月份中实际出现过。
appear_df[["appear_count", "span_months", "max_consecutive_months"]] = (
    appear_df["appear_in_months"].apply(extract_info)
)

def label_keyword_type(row):
    if row['span_months'] >= 18 and row['max_consecutive_months'] >= 10:
        return "Evergreen"
    elif row['span_months'] <= 5 and row['max_consecutive_months'] <= 3:
        return "Burst"
    else:
        return "Other"

appear_df["keyword_type"] = appear_df.apply(label_keyword_type, axis=1)


# 保存
appear_df.to_csv("result/keyword_appear_months.csv", index=False)

#导出top50常青词爆发词
top_evergreen = appear_df[appear_df["keyword_type"] == "Evergreen"].sort_values("appear_count", ascending=False).head(50)
top_burst = appear_df[appear_df["keyword_type"] == "Burst"].sort_values("appear_count", ascending=False).head(50)

top_evergreen.to_csv("result/top50_evergreen.csv", index=False)
top_burst.to_csv("result/top50_burst.csv", index=False)


