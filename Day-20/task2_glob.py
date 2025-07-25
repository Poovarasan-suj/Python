import glob

txt = glob.glob("/home/sujith/Python/logs/*.txt")

for file in txt:
    print(f"found: {file}")
   
