from TweetBot import TweetBot
from TwitterTrends import TwitterTrends


def main():
    with open("tweets.txt") as file: # open tweet file
        tweets = file.readlines() # read each line of tweets and store them in a list
    bot = TweetBot(tweets) # Create TweetBot object with list of tweets
    trends = TwitterTrends(bot) # Create TwitterTrends object

    # TODO: Call and display results from getMostFrequentWord and your
    # TODO: creative method here

    print(bot.next_tweet()) # A tweet about something controversial
    print(bot.next_tweet()) # Remember to vote!
    bot.remove_tweet("Remember to vote!")
    print(bot.next_tweet()) # Look at this meme :O
    print(bot.next_tweet()) # A tweet about something controversial
    print(bot.next_tweet()) # Look at this meme :O

if __name__ == "__main__":
    main()
