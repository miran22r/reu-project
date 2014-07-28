import csv

def csv_dict_reader(f):
    reader = csv.DictReader(f, delimiter=",")
    for line in reader:
        print(line["DATE"])
        print(line["HIGH"])
    
if __name__=="__main__":
    with open("BKW.txt") as f:
        csv_dict_reader(f)
