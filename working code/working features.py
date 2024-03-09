import unicodedata
from profanity_check import predict, predict_prob
import argparse
import csv
import pandas as pd
import re
import emoji


def profanity_score(tweet):
  [score] = predict([tweet])
  return score #lol none of the tweets in tweet_text has cuss words

def extract_emojis(s):
  return [c for c in s if c in emoji.EMOJI_DATA]

def unicode_to_meaning(code):
  return [unicodedata.name(emoji) for emoji in code]

def main():

  csvfile = "mixed_tweet_unique.csv"
  df = pd.read_csv(csvfile, usecols=["text_tweet"])
  tweetlist = list(df["text_tweet"])
  print(tweetlist)
  profanityScore = []
  emojiLiteralScore = []

  for tweet in tweetlist:
    #profanityScore.append(profanity_score(tweet))
    print(unicode_to_meaning(extract_emojis(tweet)))
