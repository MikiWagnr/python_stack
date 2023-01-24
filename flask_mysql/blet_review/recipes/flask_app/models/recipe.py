from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash
from pprint import pprint

DATABASE = 'recipes'

class Recipe:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instruction = data['instruction']
        self.date_made = data['date_made']
        self.quick_meal = data ['quick_meal']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO recipes (name, description, instruction, date_made, quick_meal, user_id) VALUE (%(name)s, %(description)s, %(instruction)s, %(date_made)s, %(quick_meal)s, %(user_id)s)'
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes JOIN users ON users.id = recipes.user_id;"
        results = connectToMySQL(DATABASE).query_db(query)
        pprint(results)
        recipes = []
        for recipe in results:
            recipes.append(cls(recipe))
        return recipes
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM recipes JOIN users ON users.id = recipes.user_id WHERE recipes.id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        pprint(result)
        return Recipe(result)
        
    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if len(recipe['name']) < 3:
            flash("Name must be three chars")
            is_valid = False
        return is_valid