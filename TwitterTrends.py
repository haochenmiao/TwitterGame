import re
class TwitterTrends:
    def __init__(self, bot):
        self.bot = bot

    def get_most_frequent_word(self):
        frequency = {}
        max_count = 0
        most_frequent_word = ""
        for i in range(self.bot.num_tweets()):
            cur_tweet = self.bot.next_tweet().lower()
            for word in cur_tweet.split():
                if word not in frequency:
                    frequency[word] = 1
                else:
                    frequency[word] += 1
                if frequency[word] > max_count:
                    max_count = frequency[word]
                    most_frequent_word = word
        return most_frequent_word

    def offensive_word(self):
        for tweet in self.bot.tweets:
            if "shit" in tweet or "f***" in tweet:
                self.bot.remove_tweet(tweet)
