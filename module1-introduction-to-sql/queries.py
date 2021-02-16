"""
we write our sql query for this assignment
"""

### Step 3, it's called. 

# select_all = """
# SELECT *
# FROM charactercreator_creator_character;
# """

# How many total Characters are there?
TOTAL_CHARACTERS = """
SELECT COUNT(character_id)
FROM charactercreator_character; 
"""

#How many of each specific subclass?
# TOTAL_SUBCLASS = """
# SELECT (SELECT COUNT(*)
# FROM charactercreator_necromancer)
# AS count1,
# (SELECT COUNT(*)
# FROM armory_weapon)
# AS count2
# """
#How many of each specific subclass?
TOTAL_SUBCLASS = """
SELECT COUNT(model)
FROM django_content_type
WHERE app_label = 'charactercreator'
AND app_label <> 'character'
"""

#How many total Items?
TOTAL_ITEMS ="""
SELECT COUNT(*)
FROM armory_item
"""

#How many of the Items are weapons?
WEAPONS ="""
SELECT COUNT(*)
FROM armory_weapon
"""

#How many of the items are not weapons?

NON_WEAPONS ="""
SELECT COUNT(item_id)
FROM armory_item
WHERE item_id NOT IN
(SELECT item_ptr_id
FROM armory_weapon)
"""

#How many Items does each character have? (Return first 20 rows)
CHARACTER_ITEMS ="""
SELECT COUNT(item_id)
FROM charactercreator_character_inventory
GROUP BY character_id
LIMIT 20
"""

#How many Weapons does each character have? (Return first 20 rows)
CHARACTER_WEAPONS ="""
SELECT COUNT(item_id)
FROM charactercreator_character_inventory
WHERE item_id IN 
(SELECT item_ptr_id
FROM armory_weapon) 
GROUP BY character_id
LIMIT 20

"""

#On average, how many Items does each Character have?
AVG_CHARACTER_ITEMS ="""
SELECT AVG(totitems)
FROM (SELECT COUNT(item_id) AS totitems
FROM charactercreator_character_inventory
GROUP BY character_id)
""" 

#On average, how many Weapons does each character have?
AVG_CHARACTER_WEAPONS ="""
SELECT AVG(totweapons)
FROM (SELECT COUNT(item_id) as totweapons
FROM charactercreator_character_inventory
WHERE item_id IN
(SELECT item_ptr_id
FROM armory_weapon)
GROUP BY character_id)
"""


### NOW ON TO QUERIES FOR THE BUDDYMOVE db ###

