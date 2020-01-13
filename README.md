# Boto local cache
Cache S3 data locally. Mocks Boto3 get_object and put_object. 

get_object
* It will first check if the key is cached locally before going to S3.
* If the object is not saved locally, save result from S3 locally
  
  
put_object
* Will just save locally
