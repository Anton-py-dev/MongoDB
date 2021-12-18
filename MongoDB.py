import pymongo


class CarDB:
    def __init__(self, host='localhost', port=27017):
        self.client = pymongo.MongoClient('localhost', 27017)
        self.db = self.client['CarDB']

    def show_all(self, name):
        """
        :param name: collection name
        :return: list of dicts in collection
        """
        collection = self.db[name]
        results = collection.find()
        return [r for r in results]

    def find_document(self, name, elements, multiple=False):
        """
        :param name: collection name
        :param elements: dict to find
        :param multiple: False: find first collision in doc; True: find all collisions in collection
        :return: dict or list
        """
        collection = self.db[name]
        if multiple:
            results = collection.find(elements)
            return [r for r in results]
        else:
            return collection.find_one(elements)

    def insert_document(self, name, data):
        """
        :param name: collection name
        :param data: file to insert (dict type)
        :return: file id
        """
        collection = self.db[name]
        return collection.insert_one(data).inserted_id
