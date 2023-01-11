class TweetBot:
    def __init__(self, tweets):
        if len(tweets) < 1:
            raise ValueError("Number of tweets must be greater than 0")
        self.count = 0
        self.tweets = tweets

    def num_tweets(self):
        return len(self.tweets)

    def add_tweet(self, tweet):
        self.tweets.append(tweet)

    def next_tweet(self):
        if self.count == len(self.tweets):
            self.count = 0
        get_word = self.tweets[self.count]
        self.count += 1
        return get_word

    def remove_tweet(self, tweet):
        if tweet in self.tweets and self.tweets.index(tweet) < self.count:
            self.count = self.count - 1
        self.tweets.remove(tweet)

    def reset(self):
        self.count = 0
