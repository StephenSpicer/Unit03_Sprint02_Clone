""" get our info from the sqlite3 rpg db """"

GET_CHAR_TABLE = """
SELECT *
FROM charactercreator_character;
"""

GET_ITEM_TABLE = """
    SELECT arm_item as item_name
    FROM (SELECT *
    FROM charactercreator_character as char_char
    INNER JOIN charactercreator_character_inventory as char_inv
    WHERE char_char.character_id = char_inv.character_id) as char_item
    INNER JOIN armory_item as arm_item
    WHERE arm_item.item_id = char_item.item_id
    AND char_item.name = {};
"""

GET_WEAPON_TABLE = """
    SELECT 
    FROM armory_weapon
    item_ptr_id
"""

# get laurence, go into DBBrowser - DMANIT>
# SELECT * FROM (SELECT * FROM charactercreator_character cc join
# charactercreator_character_inventory ci ON cc.character_id = ci.character_id) combo
# JOIN (SELECT name, item_id from armory_item) ai ON combo.item_id = ai.item_id;



# if __name__ == "__main__":
#     sl_conn = create_sl_connection()
#     sl_curs = sl_conn.cursor()
#     client = mongo_client(password, dbname)