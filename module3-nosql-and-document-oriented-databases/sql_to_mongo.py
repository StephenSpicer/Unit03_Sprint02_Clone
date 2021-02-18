""" Today we go from sqlite to mongoDB 
    non-relational databases... mongo is doc based...
    we will connect using pymongo. creds in comments.
"""

# from os import getenv
import sqlite3
import pymongo
import sql_queries as q

MONGO_PASSWORD = "6ZBF7Fp1gvVolaB3"
DBNAME = "RPG JAM"
rpg_extraction = "rpg_db.sqlite3"


# Ok, first we have the SQL section. 

def sl_connection(rpg_extraction):
    """ connecting to our sqlite3 rpg db here"""
    sl_conn = sqlite3.connect(rpg_extraction)
    sl_curs = sl_conn.cursor()
    return sl_conn, sl_curs


def execute_query(curs, query):
    return curs.execute(query).fetchall()


# Now we make the Mongo Functions :

def mongo_client(password, dbname):
    """
    we are going to use F string to add in dbname and password,
    this will generate the client object
    """

    client = pymongo.MongoClient(
        "mongodb+srv://stephenspicer-windows:{}@cluster0.phcdu.mongodb.net/{}?retryWrites=true&w=majority"
        .format(password, dbname)
    )
    return client

def show_all(collection):
    all_docs = list(collection.find())
    return all_docs


def doc_creation(collection, curs, characters_list):
    docs = []
    for character in characters_list:
        doc = {
            "name":character[1],
            "level":character[2],
            "exp":character[3], 
            "hp":character[4],
            "strength":character[5],
            "intelligence":character[6],
            "dexterity":character[7], 
            "wisdom":character[8],
            "items":item_names,
            "weapons":weapon_names
        }
        db.insert_one(doc)

   # docs.append(doc)
        # collection.insert_one(doc)

    # collection.insert_many(docs)
# we know that we have to get weapon and item ID in there with the character doc "traits" (like character stats and name etc)
# Thats where I'm uncertain how to end the doc_creation, which is initially with characters

# def item_append(collection, curs, item_list):






if __name__ == "__main__":
    #drop function for testing
    #do db dot collection rpg_extraction db.drop({})

    client = mongo_client(MONGO_PASSWORD, DBNAME)
    
    db = client.test

    sl_conn, sl_curs = sl_connection(rpg_extraction=rpg_extraction)

    character_list = execute_query(sl_curs, q.GET_CHAR_TABLE, q.GET_WEAPON_TABLE, q.GET_ITEM_TABLE)



# SCRATCH CODE FOR LATER 

# doc_creation(db.test, sl_curs, character_list)

# db.collection.insertMany()
# db.collection.updateMany()
# db.inventory.find({a: X})
