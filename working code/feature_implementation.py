#    pip3 install alt-profanity-check
#    pip3 install sklearn --upgrade
#    pip3 install emoji
from profanity_check import predict, predict_prob

import emoji
import unicodedata
import re


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
def find_third_backslash_index(text):
    count = 0
    for index, char in enumerate(text):
        if char == "\\":
            count += 1
            if count == 3:
                return index
    return -1  # Return -1 if the third backslash is not found

sentence = 'Hi I am \ud83d \u2b50!!'
s = sentence.encode('unicode-escape').decode('ascii')
print(s.split()[3])


emoji_codes = []
for word in s.split():
   if word[0:2]== "\\u":
      clean_code = re.sub(r'[!.,?;\'\":]', '', word)
      if clean_code.count("\\u")==2:
        print(clean_code) 
        emoji_codes.append(clean_code)
      elif clean_code.count("\\u")==4:
        clean_code_1 = clean_code[0:find_third_backslash_index(clean_code)]
        clean_code_2 = clean_code[find_third_backslash_index(clean_code):]       
        print(clean_code)
        emoji_codes.append(clean_code_1).append(clean_code_2)
         
print(emoji_codes)
for code in emoji_codes:    
  code = emoji_codes[0].replace("\\\\", "\\")
  print(code)
  unicode = code.encode().decode('unicode-escape')
  # print(unicode_to_character(unicode))
get_emoji_meaning("\ud83d")







