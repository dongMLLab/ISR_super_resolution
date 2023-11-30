from io import BytesIO
from minio import Minio

import os

class MinioClient:
    def __init__(self, endpoint: str, access_key: str, secret_key: str):
        self.client = Minio(endpoint=endpoint, 
                            access_key=access_key,
                            secret_key=secret_key)

    def get_bucket_list(self):
        bucketList = self.client.list_buckets()

        return bucketList

    def is_bucket_exist(self, bucketName: str):
        found = self.client.bucket_exists(bucketName)

        if not found:
            self.client.make_bucket(bucketName)

            print("Bucket {} was not exist. Created Finished".format(bucketName))
        else:
            print("Bucket {} already exists".format(bucketName))

    def get_data_file(self, bucket_name: str, file_name: str, version_id: str):
        print("versionId: {}".format(version_id))

        print("FileName:{}".format(file_name))

        response = self.client.get_object(
            bucket_name = bucket_name, 
            object_name = file_name,
            version_id = version_id)

        return response

    def get_image_file(self, bucket_name: str, file_name: str, version_id: str):
        print("versionId: {}".format(version_id))

        print("FileName:{}".format(file_name))

        response = self.client.fget_object(
            bucket_name = bucket_name, 
            object_name = file_name,
            file_path="/app/results/",
            version_id = version_id
        )

        return response
       
    def upload_data_file(self, bucketName: str, fileName: str, file_path: str):
        response = self.client.fput_object(bucketName, fileName, file_path, content_type='application/csv')
        
        return response

    def upload_visualize_file(self, bucketName: str, fileName: str, image_path: str):
        response = self.client.fput_object(bucketName, fileName, image_path, content_type="image/png")
        
        return response

# client = MinioClient(
#     endpoint="file-dev.andongh.com",
#     access_key="xa0movX65zbjEoH3hrvo",
#     secret_key="Jzz7KuXZXPW7WfwID6DarmP14ppWTBvgHA4rnGS2"
# )

# data = client.get_data_file("datasets", "oneSampleTTest.xls", "5a102c3d-4f81-44ae-993e-6bf0566f9032")

