from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint
from flask_app.models.ninja import Ninja


DATABASE = 'dojos_and_ninjas_schema'

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.ninjas = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    # ! CREATE
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    #  ! READ ALL
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        # pprint(results)
        dojos = []
        for dojo in results:
            dojos.append( Dojo(dojo) )
        # print(dojos)
        return dojos
    
    # ! READ ONE
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        pprint(result[0])
        dojo = Dojo(result[0])
        # print(dojo)
        return dojo
    
    #! READ ONE WITH MANY


    @classmethod
    def get_one_with_ninjas(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        pprint(results)
        dojo = Dojo(results[0])
        print(dojo.ninjas)
        for item in results:
            pprint(item)
            temp_ninja = {
                'id' : item['ninjas.id'],
                'first_name' : item['first_name'],
                'last_name' : item['last_name'],
                'age' : item['age'],
                'dojo_id': item['dojo_id'],
                'created_at' : item['ninjas.created_at'],
                'updated_at' : item['ninjas.updated_at']
            }
            dojo.ninjas.append(Ninja(temp_ninja))
        print(dojo)
        return dojo
        
    #  ! UPDATE
    @classmethod
    def update(cls, data):
        query = "UPDATE dojos SET name = %(name)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)
    # DELETE
    @classmethod
    def delete(cls,data):
        query = "DELETE FROM dojos WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)