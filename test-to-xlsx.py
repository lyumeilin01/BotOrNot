import pandas as pd
import json

# 读取JSON文件
with open("tweet_data.json", "r") as json_file:
    data = json.load(json_file)


