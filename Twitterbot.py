#Basic Imports
import tweepy
import time

#Please put your own API and API Key Secret instead from here1 and here2 respectively
API_Key = "here1"
API_Key_Secret = "here2"
#Please put your bearer Token instead of here
Bearer_Token = r"here"
#Please put your Access Token and Access Token Secret instead of here1 and here2 respectively
Access_Token = "here1"
Access_Token_Secret = "here2"

client = tweepy.Client(Bearer_Token, API_Key, API_Key_Secret, Access_Token, Access_Token_Secret)

auth = tweepy.OAuth1UserHandler(API_Key, API_Key_Secret, Access_Token, Access_Token_Secret)
api = tweepy.API(auth)


class MyStream(tweepy.StreamingClient):
#This is a function which retweets and like tweets according to the rules down and if error happend it will revert the Error
    def when_tweet(self, tweet):
       try:
            client.retweet(tweet.id)
            client.like(tweet.id)

       except Exception as error:
           print(error)    

       time.sleep(0.1)    


stream = MyStream(bearer_token=Bearer_Token)

#Here we have our rules that the bot retweets and like tweets only with the given words use OR to have multile words 
#Please use your own words instead of PUT YOUR WORDS HERE
rules = tweepy.StreamRule("(PUT YOUR WORDS HERE) (-is:retweet -is:reply)") 

stream.add_rules(rules)

#Start the stream
stream.filter()

print("Thanks so much for using my tool Credit: Ahmed Fouad")