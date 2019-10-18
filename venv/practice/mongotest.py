from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
#client = MongoClient(<mongodb://pushpi_123:pushpi1234@cluster0-shard-00-00-ajmsa.gcp.mongodb.net:27017,cluster0-shard-00-01-ajmsa.gcp.mongodb.net:27017,cluster0-shard-00-02-ajmsa.gcp.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority>)
#client = MongoClient(mongodb://pushpi_123:pushpi1234@cluster0-shard-00-00-ajmsa.gcp.mongodb.net:27017,cluster0-shard-00-01-ajmsa.gcp.mongodb.net:27017,cluster0-shard-00-02-ajmsa.gcp.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority)
#db=client.admin

client = pymongo.MongoClient("mongodb://pushpi_123:pushpi1234@cluster0-shard-00-00-ajmsa.gcp.mongodb.net:27017,cluster0-shard-00-01-ajmsa.gcp.mongodb.net:27017,cluster0-shard-00-02-ajmsa.gcp.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

# Issue the serverStatus command and print the results
serverStatusResult=db.command("serverStatus")
pprint(serverStatusResult)
