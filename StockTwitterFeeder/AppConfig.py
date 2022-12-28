from dataclasses import dataclass

@dataclass
class AppConfig:
      TwitterAccessToken: str
      TwitterAccessTokenSecret: str
      TwitterConsumerKey: str
      TwitterConsumerSecret: str
      TwitterSandboxName: str
      MongoDBUsername: str
      MongoDBPassword: str
      MongoDBClusterName: str
      MongoDBDatabaseName: str