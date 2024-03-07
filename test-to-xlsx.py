import pandas as pd
import json

# 读取JSON文件
with open("tweet_data.json", "r") as json_file:
    data = json.load(json_file)

# 提取文本数据到列表
text_tweet = []
for i in range(0, len(data["data"])):  # 使用len(data["data"])以自动匹配数据长度
    text_tweet.append([data["data"][i]["text"]])

# 将列表转换为DataFrame
df = pd.DataFrame(text_tweet, columns=['text_tweet'])

# 替换换行符以便在Excel中正确显示
df['text_tweet'] = df['text_tweet'].str.replace('\n', '~~~', regex=False)

# 保存为XLSX文件
df.to_excel("tweet_text.xlsx", index=False, engine='openpyxl')

# 读取XLSX文件
df_xlsx = pd.read_excel("tweet_text.xlsx")

# 如果需要，将文本中的占位符恢复为换行符
df_xlsx['text_tweet'] = df_xlsx['text_tweet'].str.replace('~~~', '\n', regex=False)

print(df_xlsx)
