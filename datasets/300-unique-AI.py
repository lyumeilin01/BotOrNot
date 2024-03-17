import requests
import json

# Assuming the BEARER_TOKEN is already set in your environment variables
bearer_token = "AAAAAAAAAAAAAAAAAAAAABdasQEAAAAAn2HtkCi05NVJhJ0Q%2FB6Uippba6U%3DalRf3Fakpyw5rjHsWn9Y9CerTXJAbzAhEsA3srZwk9ErTZWlSQ"

search_url = "https://api.twitter.com/2/tweets/search/recent"

query_params = {'query': '#NHL -is:quote -is:retweet -has:links -has:mentions lang:en', 'tweet.fields': 'author_id,created_at', 'max_results': 100}


def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

def main():
    total_tweets = []
    tweet_ids = set()  # Tracking the IDs of tweets we've already gathered
    tweet_texts = set()  # Tracking the content of tweets to avoid duplicates
    total_requested = 300
    next_token = None

    while len(total_tweets) < total_requested:
        if next_token:
            query_params['next_token'] = next_token
        json_response = connect_to_endpoint(search_url, query_params)
        tweets = json_response.get('data', [])
        for tweet in tweets:
            # Check if tweet ID and content are unique
            if tweet['id'] not in tweet_ids and tweet['text'] not in tweet_texts:
                total_tweets.append(tweet)
                tweet_ids.add(tweet['id'])
                tweet_texts.add(tweet['text'])
        next_token = json_response.get('meta', {}).get('next_token', None)
        if not next_token:
            break  # Exit loop if there are no more tweets to fetch

    # Truncate the list if we've got more tweets than requested (just in case)
    total_tweets = total_tweets[:total_requested]

    # Save the gathered tweets to a file
    with open("tweet_data_NHL.json", "w") as jfile:
        json.dump(total_tweets, jfile, indent=4)

    print(f"Collected {len(total_tweets)} unique tweets.")

if __name__ == "__main__":
    main()
