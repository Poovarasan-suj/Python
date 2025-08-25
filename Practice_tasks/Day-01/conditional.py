#Tasks for Conditional

#Task1

cloud_provider = 'AWS'

if cloud_provider == 'AWS':
    print("Deploying to AWS")
else:
   print("Other Provider")

#Task2

region = 'ap-south-1'

if region == 'ap-south-1':
    print('India Region')
else:
    print("Other Region")
#Task3

instance_type = 't2.micro'

if instance_type == 't2.micro':
    print("Free Tier Eligible")
else:
    print("Paid Tier")

#Task4

cost = 1200

if cost > 1000 :
    print("High Cost")
else:
    print("Low Cost")
