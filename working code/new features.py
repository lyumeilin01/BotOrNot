import unicodedata
from profanity_check import predict, predict_prob
import argparse
import csv
import pandas as pd


def extract_unicode(s):
  emojicodes = []
  for word in s.split():
    if word[0:2]== "\\u":
        clean_code = re.sub(r'[!.,?;\'\":]', '', word)

        emojicodes.append(clean_code)
  return emojicodes

def unicode_to_meaning(code):
  code = "\ud83e\udd0c\u2764\ufe0f"
  code = code.encode('utf-16', 'surrogatepass').decode('utf-16')
  # type(code)
  # list(code)
  return [unicodedata.name(emoji) for emoji in list(code)]


def main():

  csvfile = ""
  df = pd.read_csv(csvfile, usecols=["tweet content"])
  tweetlist = list(df["tweet content"])
  profanityScore = []
  emojiLiteralScore = []

  for tweet in tweetlist:
    profanityScore.append(predict([tweet]))
    extracted_meanings = unicode_to_meaning(extract_unicode(tweet))
    print(extracted_meanings) #['PINCHED FINGERS', 'HEAVY BLACK HEART', 'VARIATION SELECTOR-16']
    #now need to check 



main()

    

