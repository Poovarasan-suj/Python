import logging

# Configure logging
logging.basicConfig(filename='test.log' , level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Example log messages
def divide(a, b):
      if b == 0:
        logging.error("Attempted to divide by zero")
        return None
divide(5, 0)  # This will log an info message