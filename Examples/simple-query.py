import pymongo
import dns

from urllib.parse import quote_plus
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
#client = pymongo.MongoClient('mongodb+srv://dbAdmin:$h@rep01nt2022!@cluster0.wmxuklg.mongodb.net/?retryWrites=true&w=majority')
result = client['sample_mflix']['movies'].aggregate([
    {
        '$search': {
            'index': 'default',
            'text': {
                'query': 'baseball',
                'path': 'plot'
            }
        }
    }, {
        '$limit': 5
    }, {
        '$project': {
            '_id': 0,
            'title': 1,
            'plot': 1
        }
    }
])

for i in result:
    print(i)


