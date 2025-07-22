import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def divide(a, b):
      try:
          result = a / b
          logging.info(f"Divison Succesful: {result}")
          return result
      except ZeroDivisionError as e:
          logging.error("Division by zero is not allowed.")
          return None
divide(5,5)  # This will trigger an error