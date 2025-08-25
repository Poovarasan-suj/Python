#Task1

def say_hello():
    print("Hello Cloud Engineer")
say_hello()

#Task2

def print_cloud_provider(provider):
    print(f"Deploying to {provider}")
print_cloud_provider('AWS')


#Task3

def instance_cost(hours, rate):
    cost = hours * rate
    print(f"The cost of hours is = {cost}")
instance_cost(1 , 1500)

#Task4

def check_region(region):
    if region == "ap-south-1":
      print("India Region")
    else:
      print("Other Region")
check_region("ap-south-1")



