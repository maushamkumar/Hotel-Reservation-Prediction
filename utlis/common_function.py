import os 
import pandas as pd 
from src.logger import get_logger
from src.custom_exception import CustomerException
import yaml 


logger = get_logger(__name__)


def read_yaml(file_path): # We give the file path from where we have to read the yaml file. and we have already specify it in config/config.yaml file
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(F"File is not in the given path")
        
        with open(file_path, 'r') as yaml_file:
            config = yaml.safe_load(yaml_file)
            logger.info("Sucessfully read the YAML File")
            return config
            
    except Exception as e:
        logger.error("Error while reading Yaml file")
        raise CustomerException("Failed to read YAML file", e)