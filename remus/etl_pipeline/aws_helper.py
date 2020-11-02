""""AWS Helper"""

import boto3

class AWSHelper:


    def __init__(self):
        self.s3_connected = False
        
    def init_s3_session(self, aws_access_key_id, aws_secret_access_key):
         self.s3_connected = True
         self.s3_connection = boto3.resource('s3', 
                    aws_access_key_id=aws_access_key_id,
                    aws_secret_access_key=aws_secret_access_key
                    )
         return self

    def call_s3_data(self, bucket_name, file_name, download_name):
        if self.s3_connected:
            self.s3_connection.Object(bucket_name=bucket_name, key=file_name).download_file(download_name)
        else:
            raise ConnectionError("Open S3 Connection before trying to get data!")
            
    def load_s3_data(self, bucket, file_name):
         if self.s3_connected:
            self.s3_connection.Object(bucket_name=bucket, key=file_name).upload_file(file_name)
         else:
            raise ConnectionError("Open S3 Connection before trying to push data!")