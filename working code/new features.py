import unicodedata
from profanity_check import predict, predict_prob
import argparse
import csv
import pandas as pd
import re
import emoji

def extract_unicode(s):
  emojicodes = []
  clean_code = ''
  for word in s.split():
    if word[0:2]== "\\u":
        clean_code = re.sub(r'[!.,?;\'\":\n\t]', '', word)

        emojicodes.append(clean_code)

  return clean_code #fix to return emojicodes 


#problem: extracted_unicode returns a string, but unicode_meaning works with unicode. Need to convert representation
#problem: this only works for data with emoji as unicode, not for data with emoji as photos
def unicode_to_meaning(code):
  #code = "\ud83e\udd0c\u2764\ufe0f"
  # print(len(code))
  code = code.replace("\\\\", "\\")
  code1 = code.encode('utf-16', 'surrogatepass').decode('utf-16')
  # print(code1)
  # print(len(code1))
  # print(list(code1))
  return [unicodedata.name(emoji) for emoji in list(code1)]

def profanity_score(tweet):
  [score] = predict([tweet])
  return score #lol none of the tweets in tweet_text has cuss words

def emoji_literal(tweet):
  matched_words = 0
  #print(extract_unicode(tweet))
  extracted_code = extract_unicode(tweet)
  extracted_meanings = unicode_to_meaning(extracted_code)
  #print(extracted_meanings)
  #print(extracted_meanings) #['PINCHED FINGERS', 'HEAVY BLACK HEART', 'VARIATION SELECTOR-16']
  #now need to check if any word in the tweet is in the extracted meanings list
  for word in tweet.split():
    for phrase in extracted_meanings:
      if phrase.lower().__contains__(word.lower()):
        matched_words+=1
  return matched_words

def extract_emojis(s):
  return [c for c in s if c in emoji.EMOJI_DATA]

def main():

  csvfile = "mixed_tweet_unique.csv"
  df = pd.read_csv(csvfile, usecols=["text_tweet"])
  tweetlist = list(df["text_tweet"])
  #print(tweetlist)
  profanityScore = []
  emojiLiteralScore = []

  for tweet in tweetlist[:10]:

    profanityScore.append(profanity_score(tweet))
    emojiLiteralScore.append(emoji_literal(tweet))
    emojis = extract_emojis(tweet)
    print(extract_emojis(tweet))
    if len(emojis)!=0:
      print(unicodedata.name(emojis[0]))

  #print(extract_unicode(tweet))
  #print(profanityScore)
  #print(unicode_to_meaning('\ud83c\udf1f\ud83d\ude80'))
  #print(unicode_to_meaning('\u2b50\ufe0f'))

#print(len('\ud83c\udf1f\ud83d\ude80'))

main()

    

