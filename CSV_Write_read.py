import csv

### Writing to CSV File.
data  = ["1,2,3,4,5,6,7,8,9".split(",")]
file = "output.csv"
with open(file,"w") as csv_file;
  writer = csv.writer(csv_file,delimiter=',')
  print("Writing CSV")
  for line in data:
    writer.writerow(line)
csv_file.close()

### Reading from CSV File.
with open(file,"r") as csv_file:
  reader = csv.reader(csv_file)
  print("Reading from the CSV file\n")
  for row in reader:
    print(" ".join(row))
csv_file.close()
