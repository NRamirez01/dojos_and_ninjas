from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja_model

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    
    @classmethod
    def add_dojo( cls, data ):
        query = "INSERT INTO dojos (name, created_at, updated_at ) VALUE (%(name)s, NOW(), NOW());"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)

    @classmethod
    def all_dojos(cls):
        query = "SELECT * FROM dojos;"
        current_dojos = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos_list = []
        for each_dojo in current_dojos:
            dojos_list.append( each_dojo )
        return dojos_list

    @classmethod
    def dojo_and_ninja( cls, data ):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )
        dojo = cls( results[0] )
        for row_from_db in results:
            ninja_data = {
                "id" : row_from_db['ninjas.id'],
                "first_name" : row_from_db['first_name'],
                "last_name" : row_from_db['last_name'],
                "age" : row_from_db['age'],
                "created_at" : row_from_db['ninjas.created_at'],
                "updated_at" : row_from_db['ninjas.updated_at'],
            }
            dojo.ninjas.append(ninja_model.Ninja(ninja_data))
        return dojo
