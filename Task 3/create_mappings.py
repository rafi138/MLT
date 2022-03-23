from elasticsearch import Elasticsearch
from fastapi import status

es=Elasticsearch()
#es = Elasticsearch("http://localhost:2048")

def create_mappings(index_name):
    status=False
    body={
            "settings":
            {
                "number_of_shards": 1
            },
            "mappings": 
            {
    
                "properties":
                { 
                    "name":     { "type": "text"  },
                    "age" :         { "type": "integer" },
                    "gender":{ "type": "keyword" },
                    "address":       { "type": "text" },
                    "contact": { "type": "text" }  
                }
  
            }
        }
    # try:
    #         es.indices.delete(index=index_name)
    #         print('Deleted the existing '+index_name+' Index')
    # except Exception as e:
    #     print(e)
    #     pass
    try:
        print(es.indices.create(index=index_name, body=body))
        print('Successfully Created ' + index_name + ' Index')
        status=True
    except Exception as e:
        print(e)
    return status

if __name__ == "__main__":
    create_mappings('test_students')