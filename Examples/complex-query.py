import pymongo
import dns

from urllib.parse import quote_plus

print("==========================================")
print("    Change Stream Listener                ")
print("Change Stream Events currently monitored: ")
print("Insert, Update, Delete, Replace           ")
print("                                          ")
print("Resume functionality is a separate thread ")
print("==========================================")

print ("Enter your username: ")
username = input()
print("Username {}".format(username))
print("Enter your password")
password = input()
print("Password {}".format(password))
print("")
username = quote_plus(username)
password = quote_plus(password)

uri = 'mongodb+srv://' + username + ':' + password + '@cluster0.wmxuklg.mongodb.net/?retryWrites=true&w=majority'
client = pymongo.MongoClient(uri)
result = client['sample_mflix']['movies'].aggregate([
    {
        '$search': {
            'compound': {
                'must': [
                    {
                        'text': {
                            'query': [
                                'Hawaii', 'Alaska'
                            ],
                            'path': 'plot'
                        }
                    }, {
                        'regex': {
                            'query': '([0-9]{4})',
                            'path': 'plot',
                            'allowAnalyzedField': True
                        }
                    }
                ],
                'mustNot': [
                    {
                        'text': {
                            'query': [
                                'Comedy', 'Romance'
                            ],
                            'path': 'genres'
                        }
                    }, {
                        'text': {
                            'query': [
                                'Beach', 'Snow'
                            ],
                            'path': 'title'
                        }
                    }
                ]
            }
        }
    }, {
        '$project': {
            'title': 1,
            'plot': 1,
            'genres': 1,
            '_id': 0
        }
    }
])

for i in result:
    print(i)
