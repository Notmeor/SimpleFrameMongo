
import warnings

import pymongo
from gridfs import GridFS
from bson import ObjectId
from pandas.io.pickle import pkl

class SimpleFrameMongo(object):
    
    config_settings = None
    
    def __init__(self):

        db_name = self.config_settings['name'] 
        mongo_host = self.config_settings['mongo_host']
        username = self.config_settings['username']
        password = self.config_settings['password']
        
        self.db = pymongo.MongoClient(mongo_host)[db_name]
        self.db.authenticate(username, password)
        
        self.fs = GridFS(self.db)
        
    def write(self, name, df, metadata=''):
        if name in self.fs.list():
            warnings.warn(
                'filename `{}` already exists, nothing inserted'.format(name))
            return 
                            
        return self.fs.put(
            pkl.dumps(df, pkl.HIGHEST_PROTOCOL),
            filename=name,
            metadata=metadata
        )
    
    def delete(self, name):
        doc = self.db['fs.files'].find_one(
            {'filename': name})
        if doc:
            _id = doc.get('_id')
            self.fs.delete(_id)
        
    def read(self, name):
        return pkl.loads(
            self.fs.find_one({'filename': name}).read())
    
    def read_metadata(self, name):
        return self.db['fs.files'].find_one(
            {'filename': name}).get('metadata')
    
    def __enter__(self):
        return self
    
    def __exit__(self, et, ev, tb):
        self.db.client.close()
         