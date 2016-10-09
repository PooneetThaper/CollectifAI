from pymongo import MongoClient
from clarifai.client import ClarifaiApi
import sys

#ClarifaiApi stuff

clarifai_api = ClarifaiApi("5ufSEyCVOzwUzNX5nDWPFXaTHbOTkbS3NzAGyrNa","JbqnMT_wofMV1IS-QZ0jIsYo-60tdHkQOFfqGxM7")

urls = ['https://digitalmarketing.blob.core.windows.net/6305/images/thumbs/image124265.jpg',
    'http://media.vanityfair.com/photos/56cb5d18ab73e22d6d9321f6/master/h_590,c_limit/donald-trump-short-fingered-vulgarian-fingers-bruce-handy-ss13.jpg']

tagHolder=[]

i=0

while i<len(urls):
    result = clarifai_api.tag_image_urls(urls[i])
    imageTags = []
    for tag in result['results'][0]['result']['tag']['classes']:
        tag = tag.encode('ascii', 'ignore')
        imageTags.append(tag)
    tagHolder.append(imageTags)
    i+=1

j=0
while j<i:
    #print urls[j]
    #for imageTags in tagHolder[j]:
    #    print imageTags
    j+=1

#MongoDB stuff

##Adding stuff

client = MongoClient()
db = client.database
"""
j=0
while j<i:
    result = db.photos.insert_one(
        {
            "url":urls[j],
            "tags":tagHolder[j]
        }
    )
    print result.inserted_id
    j+=1

"""
##Finding stuff

cursor = db.photos.find({"tags":"potato"})
for document in cursor:
    print(document)


###### trying to get a or f parameters
print sys.argv[1] # this is the a or f argument
print sys.argv[2] # this is the url or tag