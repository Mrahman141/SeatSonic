import pymongo
from pymongo import MongoClient

client = pymongo.MongoClient('mongodb+srv://SeatSonic:BtPssgrp9@btp.rgyj8wi.mongodb.net/?retryWrites=true&w=majority')
db = client['SeatSonic']
venue = db["Venue"]
concert = db["Concert"]
user = db['User']