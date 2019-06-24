from pymongo import MongoClient
from bson import json_util
import collections
import json

class MongoConnection:
    # Wrapper classfor handling MongoDb connection issues
    def __init__(self,host_name,port,db_name):
        # create a mongoDB connection
        try:
            self.mongo_client=MongoClient(host_name,port)
            self.db_name=db_name
            self.collection_dict=collections.defaultdict()
            for collection in self.get_collecton_list():
                self.collection_dict[collection]=self.get_fields(collection)

        except Exception:
            self.mongo_client=None
    def check_connection(self):
        # check for connection
        try:
            if self.mongo_client:
                return True
            else:
                return False
        except Exception:
            return None
    def get_client(self):
        # return the connection client
        try:
            return self.mongo_client
        except Exception:
            return False
    def close_connection(self):
        # close the connection
        try:
            self.mongo_client.close()
            return None
        except Exception:
            return False
    def get_fields(self,collection_name):
        # return all the fields that are present  to collection
        try:
            field_list=set()
            cursor=self.mongo_client[self.db_name][collection_name].find({})
            for document in cursor:
                field_list=field_list.union(set(list(document.keys())))
            return list(field_list)
        except Exception:
            return False
    def get_collecton_list(self):
        #return all the collections present in the DB
        try:
            return list(self.mongo_client[self.db_name].list_collection_names())
        except Exception:
            return False
    def get_collection_field_map(self):
        # return the collection-field map
        try:
            return self.collection_dict
        except Exception:
            return False
    def execute_query(self,collection,search_term,search_value):
        #execute the query with search term and search value
        try:
            if search_value=="null":
                current_query={search_term:{'$eq':None}}
            elif search_value in ["true","false"]:
                if search_value=="true":
                    current_query={search_term:{'$eq':True}}
                else:
                    current_query={search_term:{'$ne':True}}
            else:
                try:
                    int_value=int(search_value)
                    current_query={search_term:{'$eq':int_value}}
                except Exception:
                    current_query={search_term:{'$eq':search_value}}

                # current_query={search_term:{'$eq':search_value}}
            # print(current_query)
            collecton_object=self.mongo_client[self.db_name][collection]
            documents=collecton_object.find(current_query)
            json_documents=[]
            for document in documents:
                json_documents.append(document)
            # json_documents=json.dumps(json_documents,default=json_util.default)
            return json_documents
        except Exception:
            return False
