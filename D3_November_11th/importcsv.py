#import necessary modules
import csv

reader = csv.DictReader(open("csvpractice.csv"))
for raw in reader:
    print(raw)
    

print('other method \n')
    
    
with open('csvpractice.csv','rt')as f:
  data = csv.reader(f)
  for row in data:
        print(row)