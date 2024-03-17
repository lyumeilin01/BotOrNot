import json
import pandas as pd

# Step 1: 读取 JSON 文件
def read_json_file(file_path):
    with open(file_path, "r") as file:
        return json.load(file)  # 直接返回 JSON 数据

# 读取文件中的数据
data = read_json_file("data_NHL.json")
#note: the name depends on the current directory you are in, just because you are running code in a child directory does not automatically move your pwd to the folder!

# 根据您遇到的错误，我们这里假设 data 已经是一个列表
tweets = {tweet["text"] for tweet in data}  # 使用集合去重
time = {tweet["created_at"] for tweet in data}
tweetID = {tweet["id"] for tweet in data}
userID = {tweet["author_id"] for tweet in data}

print(len(list(userID)), len(list(tweetID)), len(list(time)), len(list(tweets)))

# df = pd.DataFrame({
#     'userID': list(userID),
#     'tweetID': list(tweetID),
#     'time': list(time),
#     'tweet': list(tweets)
# })

# # Step 2: 将不重复的推文保存到 Excel 文件中
# df = pd.DataFrame(list(tweets), columns=["text"])
# df.to_excel("Canada_300_unique_tweets.xlsx", index=False)

# print(f"Total unique tweets saved: {len(tweets)}")
