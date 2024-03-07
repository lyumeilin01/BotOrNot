#    pip3 install alt-profanity-check
#    pip3 install sklearn --upgrade
#    pip3 install emoji
from profanity_check import predict, predict_prob

import emoji
import unicodedata


# Profanity check
print(predict(['WHAT THE *Uck  is this self centered  SHITE  doing on the TV #LoveIsland']))

# take in a csv file and add a column called Profanity Score 


#literal use of emoji check
#first check if there is emoji present, then check if textual rep of emoji is present in sentence


def get_emoji_meaning(emoji):
  try:
    name = unicodedata.name(emoji)
    return name.lower()  # Extracting the first part of the name which usually represents the meaning
  except ValueError:
    return "Unknown"
    
def unicode_to_character(unicode_str):
    if len(unicode_str) == 1:
        return unicode_str  # Return directly if it's a single character (non-surrogate)
    else:
        # Extract the high and low surrogate code points
        high_surrogate = ord(unicode_str[0])
        low_surrogate = ord(unicode_str[1])
        # Calculate the Unicode code point using the formula for surrogate pairs
        unicode_code_point = (high_surrogate - 0xd800) * 0x400 + (low_surrogate - 0xdc00) + 0x10000
        # Convert the Unicode code point to a Unicode character
        return chr(unicode_code_point)
    
# Surrogate pair for the fire emoji
surrogate_pair_fire = '\ud83d\udd25'
# Non-surrogate representation for the star emoji
star_emoji = '\u2b50'
print(unicode_to_character(surrogate_pair_fire))  # Fire emoji: 🔥
print(unicode_to_character(star_emoji))  # Star emoji: ⭐
print(get_emoji_meaning(unicode_to_character(star_emoji)))


# now need to extract the unicodes from the tweets

# use a for loop to get \u..\u until space 

import re
sentence = 'Hi I am \ud83d\udd25!!'
print(sentence.split())
print(sentence.split()[3])