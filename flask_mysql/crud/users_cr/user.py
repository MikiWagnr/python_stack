# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
from pprint import pprint

DATABASE = 'user_cr'
# model the class after the friend table from our database
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database

    # READ ALL
    @classmethod
    def get_all(cls,):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        pprint(results)
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            users.append( User(user) )
        return users
    
    #CREATE
    @classmethod
    def save(cls, data):
        #INSERT INTO `user_cr`.`users` (`first_name`, `last_name`, `email`, `created_at`, `updated_at`) VALUES ('miki', 'wagner', 'mwagnr@gmail.com', NOW(), NOW();INSERT INTO `user_cr`.`users` (`first_name`, `last_name`, `email`, `created_at`, `updated_at`) VALUES ('miki', 'wagner', 'mwagnr@gmail.com', NOW(), NOW();
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW() );"
        return connectToMySQL(DATABASE).query_db( query, data )


    @classmethod
    def get_one(cls,data):
        query = " SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        pprint(result[0])
        user = User(result[0])
        print(user)
        return user

    # UPDATE
    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    # DELETE
    @classmethod
    def delete(cls,data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)