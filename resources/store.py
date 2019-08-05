from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store not found'}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': 'Store already exists.'}, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
        except Exception:
            {'message', 'An error creating the store.'}, 500
        return store.json()

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            try:
                store.delete_from_db()
            except Exception:
                {'message': 'An error occured deleting the store.'}, 500
        return {'message': 'Store not found.'}, 404


class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}
