from pathlib import Path
import re, csv

file_path = Path.cwd()/"csv_reports"/"Cash on Hand.csv"
print(file_path.exists())

with file_path.open(mode = "r", encoding = "UTF-8") as file:
    reader = csv.reader(file)
    for line in reader:
        print(line)