import sqlite3

DB_FILE_PATH = 'data/data.db'


class Recipes:
    def __init__(self):
        '''Set up necessary database objects that will be reused by
        other functions of this class.'''
        self.conn = sqlite3.connect(DB_FILE_PATH)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def get_recipes(self, user_id):
        '''Get a list of dictionaries(!) representing recipes that belong
        to the given user.'''
        query = "SELECT * FROM recipe WHERE user_id = ?"
        self.cursor.execute(query, (user_id,))
        recipes = self.cursor.fetchall()
        self.conn.close()
        return recipes

    def get_recipe(self, recipe_id):
        '''Get a dictionary(!) of the data for the dictionary whose ID
        matches the given ID.'''
        query = "SELECT * FROM recipe WHERE id = ?"
        self.cursor.execute(query, (recipe_id,))
        recipe = self.cursor.fetchone()
        self.conn.close()
        return recipe

    def add_recipe(self, data, user_id):
        '''Add a recipe to the database. Use the given dictionary of data
        as well as the given user ID as data for the new row.'''
        data_unpacked = (data['name'], data['description'], data['ingredients'], data['image'], user_id)
        query = 'INSERT INTO recipe (name, description, ingredients, image, user_id) VALUES (?, ?, ?, ?, ?)'
        self.cursor.execute(query, data_unpacked)
        self.conn.commit()
        self.conn.close()
        