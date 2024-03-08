import requests
import os
import json

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = "AAAAAAAAAAAAAAAAAAAAABdasQEAAAAAn2HtkCi05NVJhJ0Q%2FB6Uippba6U%3DalRf3Fakpyw5rjHsWn9Y9CerTXJAbzAhEsA3srZwk9ErTZWlSQ"

search_url = "https://api.twitter.com/2/tweets/search/recent"

# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields

# '(from:twitterdev -is:retweet) OR #twitterdev'
#query_params = {'query': '#movie','tweet.fields': 'author_id', 'max_results':10, 'tweet.fields':'public_metrics', 'expansions':'author_id', 'user.fields':'description'}
query_params = {'query': '#movie -is:quote -is:retweet -has:links lang:en', 'tweet.fields': 'author_id', 'max_results': 100}

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    json_response = connect_to_endpoint(search_url, query_params)
    with open ("tweet_data2.json", "w") as jfile:
        json.dump(json_response, jfile, indent=4)


if __name__ == "__main__":
    main()

#source of tweet, id of tweet, no retweet, no location, langurage, user_id 