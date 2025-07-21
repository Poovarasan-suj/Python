try:
   print("dcdcd")
except NameError as e:
   print("Variable 'a' is not defined.")
except Exception as e:
   print("An unexpected error occurred:", e)
finally:
   print("Execution completed.")