from tweepy import OAuthHandler, API, TweepError


def auth():
    """ once you have registered for API, you can
        find 'em keys at https://apps.twitter.com while you are logged in with your account
        then click the API
        go-to "Keys and Access Tokens" tab for your keys and stuff."""
    consumer_key = 'taiVHaeP9PvO6iyYZMfhg9s2S'
    consumer_secret = 'JFDKEcTsURteiNA8qTelBsD8SmcgMnkvO5xOTb63hRVaQBBvsl'
    access_token = '939786756982849536-7qUj33koKvgAO4HXnFeqhsNXfgL7yoz'
    access_token_secret = 'vYvg2NtoqFTbXMvXS1qYF6clKa6UJ83w1efZ7IJXiNw39'
    try:
        # initialize the Oauth object for OAuthHandler class in tweepy module
        # parameters are consumer key, consumer_secret and callback(optional)
        oauth = OAuthHandler(consumer_key, consumer_secret)
        oauth.set_access_token(access_token, access_token_secret)
        username = OAuthHandler.get_username(oauth)
        api = API(oauth)
        yield api
        yield  username
    except TweepError:
        return 0
