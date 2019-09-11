import boto3
import os

pathToLocalStorage = '~/Projects/tone/local_s3_cache'

def existsOrBuildPath(path):
    return False

def saveObjectLocally(Bucket, Key, Object):
    path = os.path.expanduser(os.path.join(pathToLocalStorage, Bucket, Key))

    directory = os.path.dirname(path)

    if not os.path.isdir(directory):
        os.makedirs(directory, exist_ok=True)

    with open(path, 'wb') as f:
        f.write(Object)

def client(service):
    print('GETTING MOCK BOTO CLIENT')
    if service == 's3':
        return s3()
    else:
        return None

class s3:
    def __init__(self):
        self.aws_s3 = boto3.client('s3')

    def get_object(self, Bucket, Key):
        path = os.path.expanduser(os.path.join(pathToLocalStorage, Bucket, Key))
        
        if not os.path.isfile(path):
            obj = self.aws_s3.get_object(Bucket=Bucket, Key=Key)
            saveObjectLocally(Bucket, Key, obj['Body'].read())
        else:
            print('Found Object In Cache')

        #Leaks file... program doesnt run long enough to matter?
        mockResponse = {}
        mockResponse['Body'] = open(path, 'rb')
        return mockResponse

    def put_object(self, Bucket, Key, Body):
        saveObjectLocally(Bucket, Key, Body)



