import unicodedata
from profanity_check import predict, predict_prob
import argparse
import csv
import pandas as pd
import re
import emoji


def profanity_score(tweet):
  [score] = predict_prob([tweet])
  return score #lol none of the tweets in tweet_text has cuss words

def extract_emojis(s):
  return [c for c in s if c in emoji.EMOJI_DATA]

def unicode_to_meaning(emojiList):
  return [unicodedata.name(emoji) for emoji in emojiList]


def literal_emojis(tweet):
    literal_match = 0
    emojiList = []
    try:
      emojiList = unicode_to_meaning(extract_emojis(tweet))
    except ValueError:
      pass

    #print(emojiList)
    if len(emojiList)>0:
      for word in tweet.split():
        for emoji in emojiList:
          if word.lower() in emoji.lower().split() and word not in ["and", "with"]:
            print(word.lower(), "---", emoji.lower().split())
            literal_match +=1  

    return literal_match

def main():

  csvfile = "results.xlsx"
  df = pd.read_excel(csvfile, usecols=["Content"])
  tweetlist = list(df["Content"])
  print(tweetlist)
  profanityScore = []
  emojiLiteralScore = []

  for tweet in tweetlist:
    profanityScore.append(profanity_score(tweet))
    emojiLiteralScore.append(literal_emojis(tweet))
      
  print(emojiLiteralScore)
  print(unicodedata.name("🎶"))
  print(emoji.demojize("🎶"))
  print(profanityScore)

  #failed lol. none of the bot generated have actually the literal meaning of the emoji. ChatGPT has a more advanced way of selecting emojis. 


main()