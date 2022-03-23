import datetime
from elasticsearch import Elasticsearch
import FAKE_STUDENTS
import create_mappings
es = Elasticsearch()
#es = Elasticsearch("http://localhost:2048")

#custom witing function
def wait_here(endTime):
    while True:
        if datetime.datetime.now() >= endTime:
            break
    return None

#index N data within 10 mins
def index_data(index_name, num_of_data):
    # find the endtime
    endTime = datetime.datetime.now() + datetime.timedelta(minutes=0.1)

    #check index exists or not. if not then create
    if not es.indices.exists(index_name):
        create_mappings.create_mappings(index_name)

    print('Indexing Started ..')
    for i in range(0,num_of_data):
        student_record=FAKE_STUDENTS.get_student_details()
        #print(student_record)
        doc=student_record
        try:
            res = es.index(index=index_name,id=i, body=doc)
            print(res)
            message=res['result']
        except Exception as e:
            print(e)
            pass
        print(i)
    wait_here(endTime)
if __name__ == "__main__":
    index_name='students'
    num_of_data=10
    index_data(index_name,num_of_data)