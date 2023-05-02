from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.ninjas=[]
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for result in results:
            dojos.append( cls(result) )
        return dojos
    
# Create
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"

        # comes back as the new row id
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return result
    

    @classmethod
    def get_ninjas_by_dojo_id(cls, data):
        query = "SELECT * FROM ninjas WHERE dojo_id = %(id)s;"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)

    @classmethod
    def get_by_id(cls,id):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        data = {'id': id}
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        print(result)
        return(result[0])