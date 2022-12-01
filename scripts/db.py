from pymongo import MongoClient


class DB():
    def __init__(self, table):
            self.client = MongoClient('localhost',27017)
            self.db = client['sketchflow']
            self.table = table

    def get(self, query):
        self.table.find_one(query)

    def save(self, data):
        self.table.insert_one(data)

    def update(self, query, data):
        self.table.update_one(query, data)

    def delete(self, query):
        self.table.delete_one(query)

if __name__ == "__main__":

    '''
    email = "bob@gmail.com"
    password = 123
    postData = {"email": "bob@gmail.com", "password": 553}

    # Create new instance of db connected to table
    db = DB("mongodb", "users")

    # Example method calls from instance
    db.get({'email':email, 'password':password})
    db.save(postData)
    db.update({'email':email}, postData)
    db.delete({'email':email})
    '''