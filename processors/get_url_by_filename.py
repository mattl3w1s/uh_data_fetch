import csv
import sys
import os

slug = sys.argv[-1]
DIR = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

urls = dict()
reader = csv.reader(open(DIR+'/program_links.csv','r'),delimiter='|')
for row in reader:
    urls[row[2]] = row[1]
    
sys.stdout.write(urls[slug])

    