import json, ast

from clarifai.client import ClarifaiApi
clarifai_api = ClarifaiApi("5ufSEyCVOzwUzNX5nDWPFXaTHbOTkbS3NzAGyrNa","JbqnMT_wofMV1IS-QZ0jIsYo-60tdHkQOFfqGxM7")  
result = clarifai_api.tag_image_urls('https://samples.clarifai.com/metro-north.jpg')

tags = []

for tag in result['results'][0]['result']['tag']['classes']:
    tag = tag.encode('ascii', 'ignore')
    tags.append(tag)

print tags

'''
encoded_result = {}

for key in result:
    for value in result[key]:
        if type(value) is str:
            value = value.encode('ascii', 'ignore')
        #if type(value) is list
        encoded_result[key.encode('ascii', 'ignore')] = value # converts key from unicode to ascii


#print result
print encoded_result

'''
#ast.literal_eval(json.dumps(result))
#result = ast.literal_eval(str(result))
#print result
#url = result['url']
#tag = result['tag']
#print url
