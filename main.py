from loguru import logger
import time

count = 0
while count < 10:
    logger.debug("This is a debug message.") 
    time.sleep(5)
    logger.info("This is an info message.")
    time.sleep(5)
    logger.warning("This is a warning message.")
    time.sleep(5)
    logger.error("This is an error message.")
    time.sleep(5)
    logger.critical("This is a critical message.")
    time.sleep(5)
    count += 1
print("exiting...")
