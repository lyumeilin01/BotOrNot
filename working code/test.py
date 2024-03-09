import pandas as pd
import json
import csv
import random

random.seed(42)

with open("tweet_data.json", "r") as json_file:
    data = json.load(json_file)

with open("tweet_data2.json", "r") as json_file:
    data2 = json.load(json_file)
print(len(data["data"]))
text_tweet = []

# with open("tweet_text.tsv", "w") as tsv_file:
#     # Write each element of the list followed by a tab character
#     for i in range(0, 89):
#         tsv_file.write(data["data"][i]["text"] + "\t")  # Separate elements by tabs
#     tsv_file.write("\n")  # Add a new line at the end


for i in range(0, 98): 
    text_tweet.append(data["data"][i]["text"])
    #print([data["data"][i]["text"]])
for i in range(0, 10): 
    text_tweet.append(data2["data"][i]["text"])
    print([data2["data"][i]["text"]])


df = pd.DataFrame(text_tweet, columns=['text_tweet'])
print(len(text_tweet))

df['text_tweet'] = df['text_tweet'].str.replace('\n', '\\n').replace('\t','\\t')

print("num unique" , df['text_tweet'].nunique())
#df.to_excel("tweet_text.xlsx", index=False)

df_gen = pd.read_excel("tweet_gen2.0.xlsx", sheet_name='Sheet1', usecols='A',header=None)
df_gen = df_gen.iloc[range(0, 20, 2)]
gen_values = df_gen.iloc[:, 0].tolist()
# print(gen_values)
text_tweet+=gen_values
print(len(text_tweet))
orders = list(range(0,118))
# print(orders)
random.shuffle(orders)
labels = ["user"]*108 + ["bot"]*10
print(len(labels))

df_mixed_truth = pd.DataFrame({'Index': orders, 'Tweet Content': text_tweet, 'BON': labels})
df_mixed_truth = df_mixed_truth.sort_values(by="Index")
# print(df_mixed_truth[80:])
df_mixed_masked = df_mixed_truth[["Index", "Tweet Content"]]
# print(df_mixed_truth)
df_mixed_masked = df_mixed_masked.drop_duplicates(subset=["Tweet Content"])
df_mixed_truth = df_mixed_truth.drop_duplicates(subset = ["Tweet Content"])
print(len(df_mixed_truth))
df_mixed_truth.to_csv("mixed_tweet_answer_unique.csv", index=False)
df_mixed_masked.to_csv("mixed_tweet_unique.csv", index = False, encoding='utf-8')

print(df_mixed_masked['Tweet Content'].nunique())

