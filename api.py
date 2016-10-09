import sys
from pymongo import MongoClient
from clarifai.client import ClarifaiApi

opType=sys.argv[1]
argtext=sys.argv[2]

client = MongoClient()
db = client.database

def add():
    tagHolder=[]
    i=0
    #ClarifaiApi stuff
    clarifai_api = ClarifaiApi("5ufSEyCVOzwUzNX5nDWPFXaTHbOTkbS3NzAGyrNa",
        "JbqnMT_wofMV1IS-QZ0jIsYo-60tdHkQOFfqGxM7")
    path='front/uploads/'+argtext
    result = clarifai_api.tag_images(open(path, 'rb'))
    for tag in result['results'][0]['result']['tag']['classes']:
        tag = tag.encode('ascii', 'ignore')
        tagHolder.append(tag)
    #MongoDB stuff
    ##Adding stuff
    print path
    print tagHolder
    result = db.photos.insert_one(
        {
            "path":path,
            "tags":tagHolder
        }
    )

def find():
    paths=''
    cursor = db.photos.find({"tags":argtext})
    for document in cursor:
        print document
        paths += document["path"]
        paths += '\n'
    f = open('front/out.txt', 'w')
    f.write(paths)

if __name__ == "__main__":
    if(opType=='a'):
        add()
    else:
        find()
