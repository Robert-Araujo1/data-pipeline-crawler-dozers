import pandas as pd
from minio import Minio
from io import BytesIO

class MinIOWrapper:
    
    def __init__(self):
        self.endpoint = "localhost:9000"
        self.access_key = "admin"
        self.secret_key = "admin123"     
        
        self.client = Minio(
            endpoint=self.endpoint,
            access_key=self.access_key,
            secret_key=self.secret_key,
            secure=False
        )
    
    def bucket_exists(self, bucket):
        exists = False
        try:
            exists = self.client.bucket_exists(bucket)
        except Exception as e:
            print("❌A conexão com o MinIO não foi estabelecida com sucesso.")
            print("Verifique se o container Docker do MinIO está rodando.")
            raise e
        else:
            if not exists:
                self.client.make_bucket(bucket)
            print(f"✅Bucket {bucket} encontrado.")
        
        return exists
    
    def get_obj_minio(self, bucket, obj_name):
        try:
            response = self.client.get_object(bucket, obj_name)
            response_buffered = BytesIO(response.read())
            
            df = pd.read_csv(response_buffered, encoding="utf-8")
            return df
        except Exception as e:
            print(
                "❌Não foi possível resgatar o objeto {0} do bucket {1}".format(
                    obj_name, bucket
                )
            )
        finally:
            if 'response' in locals():
                response.close()
                response.release_conn()

    
    def fput_object(self, bucket, obj_name, file_path, content_type):
        response = None
        try:
            response = self.client.fput_object(bucket, obj_name, file_path, content_type)
            print(f"✅Objeto {obj_name} inserido no bucket {bucket}.")
        except Exception as e:
            print(
                "❌Não foi possível inserir o objeto {0} do bucket {1}".format(
                    obj_name, bucket
                )
            )

        return response

