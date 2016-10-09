from clarifai.client import ClarifaiApi
clarifai_api = ClarifaiApi("5ufSEyCVOzwUzNX5nDWPFXaTHbOTkbS3NzAGyrNa","JbqnMT_wofMV1IS-QZ0jIsYo-60tdHkQOFfqGxM7")  # assumes environment variables are set.
result = clarifai_api.tag_image_urls('https://samples.clarifai.com/metro-north.jpg')
print result
