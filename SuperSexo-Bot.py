import tweepy
import time
import random

auth = tweepy.OAuthHandler('MmcQFRe0Gos6xMR8wMiwIadhH', '4DGrsk4PdF1mPfUzCRFNwJvnEoedK6XiPptbANie76iSYFmg4O')
auth.set_access_token('1393293381250519045-MjfUmD8BX1up1o0RHStvBx5qlkOMuc','iEB9ITL3ruhJCxWpKK41cShrgwbPXaEGqc4XKJzMpna2Z')
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()
b = 'b*ceta dx '

for tweet in api.home_timeline():
    try:
        with open('palavras.txt') as f:
            lines = f.readlines()
            pal = random.choice(lines)
            while (len(pal) < 3 and pal != 'cu'):
                pal = random.choice(lines)
            else:
                frase = b + pal

        api.update_status(frase)
        print('Tweetou')
        time.sleep(300)

    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
