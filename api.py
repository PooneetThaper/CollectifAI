import json, ast

from clarifai.client import ClarifaiApi
clarifai_api = ClarifaiApi("5ufSEyCVOzwUzNX5nDWPFXaTHbOTkbS3NzAGyrNa","JbqnMT_wofMV1IS-QZ0jIsYo-60tdHkQOFfqGxM7")  
result = clarifai_api.tag_image_urls('https://samples.clarifai.com/metro-north.jpg')

tags = []

for tag in result['results'][0]['result']['tag']['classes']:
    tag = tag.encode('ascii', 'ignore')
    tags.append(tag)

print tags
