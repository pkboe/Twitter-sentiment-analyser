
from main_gui import *
import main_gui as pd
posper = 0
negper = 0
nutper = 0
def get_Final(tweets, srch):
    pos = []
    neg = []
    nut = []

    tw_len = len(tweets)
    for a_tweet in tweets:
        if a_tweet['sentiment'] > 0:
            pos.append(a_tweet)
        elif not a_tweet['sentiment']:
            nut.append(a_tweet)
        else:
            neg.append(a_tweet)
    get_per = lambda x: (100*(len(x)))/tw_len
    print("\nSentiment Analysis for {}:".format(srch))

    print("Positive tweets: ", end=' ')
    try:
        print(get_per(pos))
        global posper
        posper=(get_per(pos))
    except ZeroDivisionError:
        print(0)

    print("Negative tweets: ", end=' ')
    try:
        print(get_per(neg))
        global negper
        negper=(get_per(neg))
    except ZeroDivisionError:
        print(0)

    print("Neutral tweets:  ", end=' ')
    try:
        print(get_per(nut))
        global  nutper
        nutper = (get_per(nut))
    except ZeroDivisionError:
        print(0)

    posper = (round(posper,2))
    negper = (round(negper, 2))
    nutper = (round(nutper, 2))

    pd.SetPerPos(str(posper))
    pd.SetPerNeg(str(negper))
    pd.SetPerNut(str(nutper))


    number = 5

    # print positive tweets
    print('\n\nPositive tweets:\n')
    out = ""
    for tweet in pos[1:]:
        print('\t> ' + tweet['tweet']+"\n")
        out = out + '\t> ' + tweet['tweet']+"\n"
        pd.SetTextPos(out)


    # print negative tweets
    out = ""
    for tweet in neg[1:]:
        print('\t> ' + tweet['tweet'] + "\n")
        out = out + '\t> ' + tweet['tweet'] + "\n"
        pd.SetTextNeg(out)

    # print neutral tweets
    print('\nNeutral tweets:\n')
    out = ""
    for tweet in nut[:number]:
        print('\t> ' + tweet['tweet'])
        out = out + '\t> ' + tweet['tweet'] + "\n"
        pd.SetTextNut(out)
