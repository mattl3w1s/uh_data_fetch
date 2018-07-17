import csv
import sys

slug = sys.argv[-1]

urls = dict()
reader = csv.reader(open('/Users/mattlewis/Development/python/parse_UHD/data/program_links.csv','r'),delimiter='|')
for row in reader:
    urls[row[2]] = row[1]
    
sys.stdout.write(urls[slug])

