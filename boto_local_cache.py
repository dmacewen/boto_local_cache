import boto3
import os

pathToLocalStorage = './local'

def existsOrBuildPath(path):
    return False

def saveObjectLocally(Bucket, Key, Object):
    path = os.path.join(pathToLocalStorage, Bucket, Key)

    directory = os.path.dirname(path)

    if not os.path.isdir(directory):
        os.mkdir(path)

    with open(path, 'wb') as f:
        f.write(Object)

def client(service):
    if service == 's3':
        return s3()
    else:
        return None

class s3:
    def init(self):
        print("Creating S3 Local Cache")
        self.s3 = boto3.client('s3')

    def get_object(self, Bucket, Key):
        path = os.path.join(pathToLocalStorage, Bucket, Key)
        
        if not os.path.isfile(path):
            obj = self.s3.get_object(Bucket, Key)
            saveObjectLocally(Bucket, Key, obj)
            return obj


        with open(path, 'rb') as f:
            data = f.read()

        return data

    def put_object(self, Bucket, Key, Body):
        saveObjectLocally(Bucket, Key, obj)



