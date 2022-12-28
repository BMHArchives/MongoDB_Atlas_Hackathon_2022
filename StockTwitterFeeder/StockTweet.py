from dataclasses import dataclass, asdict

@dataclass
class StockTweet:
      TweetID: str
      Username: str
      FollowersCount: int
      FriendsCount: int
      TweetText: str
      TweetLangAbbrv: str
      TweetSource: str
      RetweetCount: int
      ReployCount: int
      QuoteCount: int
      StockSymbol: str
      FromDate:str
      ToDate:str
      
      def dict(self):
        return {k: str(v) for k, v in asdict(self).items()}