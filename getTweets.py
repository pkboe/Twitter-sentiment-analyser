def fetch_tweets(api,query):

    tweets = api.search(q=query, count=10000)  # status object returned
    print(query)
    yield query
    yield tweets

