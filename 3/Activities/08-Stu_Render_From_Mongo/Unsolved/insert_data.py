import pymongo

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = client.store_inventory_db
produce = db.produce
# Drops collection if available to remove duplicates
db.produce.drop()
# Creates a collection in the database and inserts two documents
produce.insert_many(
    [
        {
            'type': 'Apples',
            'cost': .50,
            'stock':56
        },
        {
            'type': 'Bananas',
            'cost': .85,
            'stock':77
        }
    ]
)
print("its uploaded")