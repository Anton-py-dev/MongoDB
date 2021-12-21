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

    def show_all_available(self, name):
        """
        :param name: collection name
        :return: list of dicts in collection
        """
        collection = self.db[name]
        results = collection.find({'available': True})
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
            results = collection.find({"$and": [{'available': True}, elements]})
            return [r for r in results]
        else:
            return collection.find_one({"$and": [{'available': True}, elements]})

    def insert_document(self, name, data):
        """
        :param name: collection name
        :param data: file to insert (dict type)
        :return: file id
        """
        collection = self.db[name]
        return collection.insert_one(data).inserted_id

    def update_document(self, name, query_elements, new_values):
        """
        Function update existing document
        :param name: collection name
        :param query_elements: {key: value} to find in doc ({'id_': 'car_number'})
        :param new_values: new {key: value} in this doc
        :return: updating status
        """
        collection = self.db[name]
        return collection.update_one(query_elements, {'$set': new_values}).modified_count

    def delete_document(self, name, query):
        """
        Function to delete a single document from a collection.
        :param name: collection name
        :param query: {key: value} to find in doc ({'id_': 'car_number'})
        :return: deleting status
        """
        collection = self.db[name]
        return collection.delete_one(query).deleted_count

    def find_by_interval(self, name, bottom, top):
        """
        :param name: collection name
        :param bottom: lower price
        :param top:
        :return:
        """
        collection = self.db[name]
        results = collection.find({'price': {'$gt': bottom, '$lt': top}})
        return [r for r in results]

    def inc_count(self, query_elements):
        collection = self.db['users']
        collection.update_one(query_elements, {'$inc': {'rent_count': 1}})

    def sum_inc(self, query_elements, count):
        collection = self.db['result']
        collection.update_one(query_elements, {'$inc': {'total': count}})
