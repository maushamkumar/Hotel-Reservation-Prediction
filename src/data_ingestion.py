# import os 
# import pandas as pd 
# from google.cloud import storage 
# from sklearn.model_selection import train_test_split
# from src.logger import get_logger
# from src.custom_exception import CustomerException
# from config.paths_config import *
# from utlis.common_function import read_yaml

# logger = get_logger(__name__)

# class DataIngestion:
#     def __init__(self, config): # Whatever config file is we will pass here This config variable denotes to config.yaml
#         self.config = config['data_ingestion']
#         # self.bucket_name = self.config['bucket_name'] # Under data_ingestion we want buket name 
#         # self.file_name = self.config['bucket_file_name']
#         self.file_name = self.config['local_file_path']
#         self.train_test_ratio = self.config['train_ratio']
        
#         os.makedirs(RAW_DIR, exist_ok=True)
        
#         logger.info(f"Data Ingestion start with {self.file_name}")
        
#     # def download_csv_from_gcp(self):
#     #     try:
#     #         client = storage.Client()
#     #         bucket = client.bucket(self.bucket_name)
#     #         blob = bucket.blob(self.file_name)
            
#     #         blob.download_to_filename(RAW_FILE_PATH)
            
#     #         logger.info("RAW file sucessfully downloaded to raw file path")
#     #     except Exception as e:
#     #         logger.error("Error while downloading the csv file")
#     #         raise CustomerException("Failed to download csv file")
        
#     def split_data(self):
#         try:
#             logger.info("Strting the spliting process")
#             data = pd.read_csv(RAW_FILE_PATH)
#             train_data, test_data = train_test_split(data, test_size=1-self.train_test_ratio, random_state=42)
            
#             train_data.to_csv(TRAIN_FILE_PATH)
#             test_data.to_csv(TEST_FILE_PATH)
            
#             logger.info(f"Train data saved to {TRAIN_FILE_PATH}")
#             logger.info(f"Train data saved to {TEST_FILE_PATH}")
            
#         except Exception as e:
#           logger.error("Error while spliting the data ")  
#           raise CustomerException("Fail to split data into traing and test set ")
      
#     def run(self):
        
#         try: 
#             logger.info("starting data ingestion process ")
#             self.download_csv_from_gcp()
#             self.split_data()
            
#             logger.info("Data Ingestion Completed Sucessfully")
            
#         except CustomerException as ce:
#             logger.error(f'CustomerException :{str(ce)}')
            
#         finally:
#             logger.info("Data Ingestion completed")
            
            
# if __name__ == "__main__":
#     data_ingestion = DataIngestion(read_yaml(CONFIG_PATH))
#     data_ingestion.run()
    
    
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from src.logger import get_logger
from src.custom_exception import CustomerException
from config.paths_config import *
from utlis.common_function import read_yaml

logger = get_logger(__name__)

class DataIngestion:
    def __init__(self, config):
        self.config = config['data_ingestion']
        self.file_path = self.config['local_file_path']
        self.train_test_ratio = self.config['train_ratio']
        
        os.makedirs(RAW_DIR, exist_ok=True)
        logger.info(f"Data Ingestion started with file: {self.file_path}")
        
    def split_data(self):
        try:
            logger.info("Starting the data splitting process")
            
            if not os.path.exists(self.file_path):
                raise CustomerException(f"File not found: {self.file_path}")
            
            data = pd.read_csv(self.file_path)
            train_data, test_data = train_test_split(data, test_size=1-self.train_test_ratio, random_state=42)
            
            train_data.to_csv(TRAIN_FILE_PATH, index=False)
            test_data.to_csv(TEST_FILE_PATH, index=False)
            
            logger.info(f"Train data saved to {TRAIN_FILE_PATH}")
            logger.info(f"Test data saved to {TEST_FILE_PATH}")
        
        except Exception as e:
            logger.error("Error while splitting the data")  
            raise CustomerException(f"Failed to split data: {str(e)}")
      
    def run(self):
        try: 
            logger.info("Starting data ingestion process")
            self.split_data()
            logger.info("Data Ingestion Completed Successfully")
        
        except CustomerException as ce:
            logger.error(f'CustomerException: {str(ce)}')
        
        finally:
            logger.info("Data Ingestion completed")
            
if __name__ == "__main__":
    data_ingestion = DataIngestion(read_yaml(CONFIG_PATH))
    data_ingestion.run()
