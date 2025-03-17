from src.logger import get_logger
from src.custom_exception import CustomerException
import sys

logger = get_logger(__name__)

def divide_number(a, b):
    try: 
        result = a / b 
        logger.info("dividing two numbers ")
        return result
    
    except Exception as e:
        logger.error("Error Aa gaya ")  # Log the error
        raise CustomerException("Zero se divide hota h ", sys)  # Pass `sys` for error details

if __name__ == '__main__':
    try: 
        logger.info("Starting main program")
        divide_number(10, 0)
    except CustomerException as ce:
        logger.error(str(ce))


