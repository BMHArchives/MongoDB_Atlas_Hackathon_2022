import tweepy
import pymongo
from urllib.parse import quote_plus
import Stock
import StockTweet
from datetime import datetime, timedelta
# import yaml
# from yaml.loader import SafeLoader, Loader
import os
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
import AppConfig
import logging
import sys
import warnings
from cryptography.utils import CryptographyDeprecationWarning
from dotenv import load_dotenv
warnings.filterwarnings("ignore", category=CryptographyDeprecationWarning)
def GetActiveStocksData():
    stockLists = []
    try:
        uri = 'mongodb+srv://' + AZKEYS.MongoDBUsername + ':' + AZKEYS.MongoDBPassword + '@'+ AZKEYS.MongoDBClusterName +'/?retryWrites=true&w=majority'
        client = pymongo.MongoClient(uri)
        db = client[AZKEYS.MongoDBDatabaseName]
        collection = db["Stocks"]
        
        # find all stocks where Active equals true.
        stocks = collection.find({"Active": True})
        
        
        for stock in stocks:
            stockLists.append(Stock.Stock(stock["StockName"], stock["StockSymbol"], stock["Keywords"]))

        
        client.close()
        return stockLists
    except Exception:
        print("GetActiveStocksData - An error has occured.")
        return stockLists

def RetrieveStockTweets(ActiveStocks):
    
    stockTweets = []
    try:
        # Get the current date and time
        
        toDateTime = datetime.now().strftime("%Y%m%d%H%M")
        fromDT = datetime.now() - timedelta(minutes=10)
        fromDateTime = fromDT.strftime("%Y%m%d%H%M")
        
        consumer_key = AZKEYS.TwitterConsumerKey 
        consumer_secret = AZKEYS.TwitterConsumerSecret 
        access_token = AZKEYS.TwitterAccessToken 
        access_token_secret = AZKEYS.TwitterAccessTokenSecret 
        auth = tweepy.OAuth1UserHandler(
           consumer_key, consumer_secret, access_token, access_token_secret
        )
        api = tweepy.API(auth)
        for stock in ActiveStocks:
            searchString = "({} OR #{} OR {})".format(stock.StockName, stock.StockSymbol, stock.Keywords.replace(",", " OR"))
            tweet_results = api.search_30_day(label=AZKEYS.TwitterSandboxName, query=searchString, fromDate=fromDateTime, toDate=toDateTime)
            for tweet in tweet_results:
                stockTweets.append(StockTweet.StockTweet(tweet.id, tweet.user.name, 0,0,tweet.text, tweet.lang, tweet.source, 0,0,0,stock.StockSymbol, fromDateTime, toDateTime ))
             
        return stockTweets
    except Exception as e:
           print("RetrieveStockTweets - Error: {0}".format(e))
           return stockTweets
    
def SaveStockTweetsDB(StockTweets):
    try:
        uri = 'mongodb+srv://' + AZKEYS.MongoDBUsername + ':' + AZKEYS.MongoDBPassword + '@'+ AZKEYS.MongoDBClusterName +'/?retryWrites=true&w=majority'
        client = pymongo.MongoClient(uri)
        db = client[AZKEYS.MongoDBDatabaseName]
        collection = db["StockTweets"]

        for StockTweet in StockTweets:
            collection.insert_one(StockTweet.dict())

 
    except Exception as e:
           print("SaveStockTweetsDB - Error: {0}".format(e))

def LoadAzureKeyValueSecrets():
    try:
        load_dotenv()
        TwitterAccessToken = os.environ.get("TWITTER_ACCESS_TOKEN")
        TwitterAccessTokenSecret = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")
        TwitterConsumerKey = os.environ.get("TWITTER_CONSUMER_KEY")
        TwitterConsumerSecret = os.environ.get("TWITTER_CONSUMER_SECRET")
        TwitterSandboxName = os.environ.get("TWITTER_SANDBOX_NAME")
        MongoDBUsername = os.environ.get("MONGODB_USERNAME")
        MongoDBPassword = os.environ.get("MONGODB_PASSWORD")
        MongoDBClusterName = os.environ.get("MONGODB_CLUSTER_NAME")
        MongoDBDatabaseName = os.environ.get("MONGODB_DATABASE_NAME")
        appConfig = AppConfig.AppConfig(TwitterAccessToken, TwitterAccessTokenSecret,TwitterConsumerKey, TwitterConsumerSecret,TwitterSandboxName, quote_plus(MongoDBUsername), quote_plus(MongoDBPassword),MongoDBClusterName,MongoDBDatabaseName)
        return appConfig
    except Exception as e:
            print("LoadAzureKeyValueSecrets - Error - {}".format(e))
            return ""


def main():
    print("Starting App")
    global AZKEYS
    AZKEYS = LoadAzureKeyValueSecrets()  
    print(AZKEYS)
    activeStocks = GetActiveStocksData()
    stockTweets = RetrieveStockTweets(activeStocks)
    SaveStockTweetsDB(stockTweets)
    
if __name__ == '__main__':
    main()
    